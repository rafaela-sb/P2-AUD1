# -*- coding: utf-8 -*-
"""Exporta anexos editáveis: dicionário de variáveis, matriz de cobertura, relação de fontes e amostra da base."""
import csv, os, re
import pandas as pd
from conteudo_d import DIC, MATRIZ, FONTES

BASE = os.path.dirname(os.path.abspath(__file__))
R = lambda *p: os.path.join(BASE, "..", *p)


def limpa(s):
    return re.sub(r"<[^>]+>", "", str(s))


def md_tabela(cab, linhas):
    out = "| " + " | ".join(cab) + " |\n|" + "---|" * len(cab) + "\n"
    for l in linhas:
        out += "| " + " | ".join(limpa(x).replace("|", "/") for x in l) + " |\n"
    return out


# Dicionário
with open(R("02_base_simulada", "dicionario_variaveis.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["variavel", "tipo", "descricao", "origem"]); w.writerows(DIC)
open(R("02_base_simulada", "dicionario_variaveis.md"), "w", encoding="utf-8").write(
    "# Dicionário de variáveis - base simulada de estoques (DADOS SINTÉTICOS)\n\n"
    "Arquivo: `base_estoques_sintetica_31122025.csv` (separador `;`, decimal `,`, datas `AAAA-MM-DD`, UTF-8).\n\n"
    + md_tabela(["Variável", "Tipo", "Descrição", "Origem"], DIC))

# Matriz de cobertura
os.makedirs(R("05_matriz_cobertura"), exist_ok=True)
with open(R("05_matriz_cobertura", "matriz_cobertura_normas.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["norma", "papel_de_trabalho", "itens_centrais", "pts_relacionados"]); w.writerows(MATRIZ)
open(R("05_matriz_cobertura", "matriz_cobertura_normas.md"), "w", encoding="utf-8").write(
    "# Matriz de cobertura das normas\n\nDossiê de auditoria - Vivara Participações S.A. - exercício 2025 - Rafaela de Sousa Barbosa, matrícula 241003384.\n\n"
    + md_tabela(["Norma (versão aplicada)", "PT principal", "Itens centrais", "PTs relacionados"], MATRIZ)
    + "\nVersões das normas e observações de vigência: PT 230, quadro 3, do dossiê.\n")

# Fontes
os.makedirs(R("06_fontes"), exist_ok=True)
with open(R("06_fontes", "relacao_fontes.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["sigla", "documento", "exercicio", "endereco_eletronico", "data_acesso", "paginas"])
    w.writerows(FONTES)
open(R("06_fontes", "relacao_fontes.md"), "w", encoding="utf-8").write(
    "# Relação das fontes utilizadas\n\nPáginas = numeração do arquivo PDF. (*) Correspondência entre os dois links de fatos relevantes "
    "e os documentos inferida pela ordem em que foram informados.\n\n"
    + md_tabela(["Sigla", "Documento", "Exercício", "Endereço eletrônico", "Data de acesso", "Páginas"], FONTES))

# Amostra da base (primeiras 2.000 linhas) para visualização no GitHub
b = pd.read_csv(R("02_base_simulada", "base_estoques_sintetica_31122025.csv"), sep=";", decimal=",", nrows=2000)
b.to_csv(R("02_base_simulada", "base_estoques_sintetica_AMOSTRA_2000_linhas.csv"), index=False, sep=";", decimal=",")
print("anexos exportados")
