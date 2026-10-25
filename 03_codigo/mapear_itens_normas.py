# -*- coding: utf-8 -*-
"""Gera normas_paginas.json: página (na compilação 'Consolidado Normas Aud1') de cada item de NBC TA citado nos PTs.
Uso: python mapear_itens_normas.py caminho/Consolidado_Normas_Aud1.pdf
Requer pdftotext (poppler). A compilação não é redistribuída no repositório; o JSON resultante é versionado."""
import json, os, re, subprocess, sys
import conteudo_a, conteudo_b, conteudo_c

RANGES = {"EC": (3, 28), "200": (29, 56), "210": (57, 88), "220": (89, 130), "230": (131, 145), "240": (146, 188),
          "250": (189, 202), "260": (203, 224), "265": (225, 236), "300": (237, 251), "315": (252, 366), "320": (367, 378),
          "330": (379, 403), "402": (404, 426), "450": (427, 445), "500": (446, 470), "501": (471, 482), "505": (483, 496),
          "510": (497, 520), "520": (521, 529), "530": (530, 547), "540": (548, 599), "550": (600, 624), "560": (625, 638),
          "570": (639, 659), "580": (660, 683), "600": (684, 756)}


def main(pdf):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
    out = {}
    for mod in (conteudo_a, conteudo_b, conteudo_c):
        for pt in mod.PTS:
            for norma, itens in pt["itens"]:
                a, b = RANGES[norma]
                for it in itens:
                    pat = re.compile(r"(^|\n)[ \t]*" + re.escape(it) + r"\.[ \t]+\S")
                    pat2 = re.compile(r"(^|\n|\s{3,})" + re.escape(it) + r"\.\s+[A-ZÀ-Úa-z(]")
                    pg = next((p for p in range(a, b + 1) if pat.search(txt[p - 1])), None) or \
                        next((p for p in range(a, b + 1) if pat2.search(txt[p - 1])), None)
                    out.setdefault(norma, {})[it] = pg
    out["_intervalos"] = {k: list(v) for k, v in RANGES.items()}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "normas_paginas.json"), "w"), indent=1)
    falt = [(n, i) for n, d in out.items() if n != "_intervalos" for i, p in d.items() if p is None]
    print("itens sem página localizada:", falt)


if __name__ == "__main__":
    main(sys.argv[1])
