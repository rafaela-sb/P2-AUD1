# -*- coding: utf-8 -*-
"""Utilitários de formatação e dados compartilhados para a geração do dossiê."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "..", "02_base_simulada", "resultados")
CALC = json.load(open(os.path.join(RES, "resultados_calculos.json"), encoding="utf-8"))
TST = json.load(open(os.path.join(RES, "resultados_testes.json"), encoding="utf-8"))
try:
    NORMAS_PAG = json.load(open(os.path.join(BASE, "normas_paginas.json"), encoding="utf-8"))
except FileNotFoundError:
    NORMAS_PAG = {}

MATRICULA = "241003384"
NOME = "Rafaela de Sousa Barbosa"
DATA_PREP = "22/10/2026"
R, P, S = "R", "P", "S"
CLASSE = {"R": "Realizado com evidência pública", "P": "Planejado por falta de acesso", "S": "Simulado para fins didáticos"}


def n0(x):
    """1234567.8 -> '1.234.568'"""
    if x is None:
        return "-"
    s = f"{abs(x):,.0f}".replace(",", ".")
    return f"({s})" if x < 0 else s


def n1(x):
    s = f"{abs(x):,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"({s})" if x < 0 else s


def n2(x):
    s = f"{abs(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"-{s}" if x < 0 else s


def pct(x, d=1):
    return f"{x*100:.{d}f}%".replace(".", ",")


def tabela(cab, linhas, cls="t", larg=None):
    h = "".join(f"<th>{c}</th>" for c in cab)
    corpo = ""
    for l in linhas:
        corpo += "<tr>" + "".join(f"<td>{'' if v is None else v}</td>" for v in l) + "</tr>"
    cg = ""
    if larg:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in larg) + "</colgroup>"
    return f'<table class="{cls}">{cg}<thead><tr>{h}</tr></thead><tbody>{corpo}</tbody></table>'


def itens_norma(norma, itens):
    """Formata itens com a página da compilação de normas (Consolidado Normas Aud1)."""
    out = []
    mp = NORMAS_PAG.get(norma, {})
    for i in itens:
        p = mp.get(i)
        out.append(f"{i} (p.{p})" if p else i)
    return ", ".join(out)
