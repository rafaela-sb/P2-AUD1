# -*- coding: utf-8 -*-
"""Reproduz todo o trabalho na ordem correta.
Uso: python executar_tudo.py            (gera base, testes, cálculos, planilhas e dossiê)
     python executar_tudo.py --sem-pdf  (não gera o PDF; útil sem Chromium/Playwright)"""
import subprocess, sys

etapas = ["gerar_base.py", "testes_auditoria.py", "calculos_pts.py", "gerar_planilhas.py", "exportar_anexos.py"]
if "--sem-pdf" not in sys.argv:
    etapas.append("gerar_dossie.py")
for e in etapas:
    print(f"==> {e}", flush=True)
    subprocess.run([sys.executable, e], check=True)
print("Concluído.")
