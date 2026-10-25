# Dossiê de Auditoria – Vivara Participações S.A. (VIVA3) – Exercício 2025

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaela-sb/P2-AUD1/blob/main/07_colab/base_simulada_vivara_colab.ipynb)

**Universidade de Brasília (UnB)** · Auditoria 1 – CCA0024 – Turma 02 – 2026.2 · Prof. Lucas Oliveira Gomes Ferreira · P2
**Preparadora:** Rafaela de Sousa Barbosa · **Matrícula:** 241003384 · **Companhia atribuída:** Vivara Participações S.A. · **Trabalho individual**

> **Natureza do trabalho.** Este repositório contém um trabalho acadêmico. **Não é** opinião profissional independente nem relatório
> de auditoria. Nenhum contato foi feito com a companhia, seus auditores, clientes ou fornecedores. Confirmações, entrevistas,
> inspeções físicas e acessos a sistemas **não** foram realizados.
>
> **Dados sintéticos.** A base de estoques em `02_base_simulada/` é **fictícia**, gerada por programa, e não representa registros
> reais da Vivara ou de suas controladas. Todas as linhas trazem a marca `dado_sintetico = "SIM - REGISTRO FICTICIO PARA FINS DIDATICOS"`.
>
> **Uso de inteligência artificial.** O conteúdo (papéis de trabalho, código, planilhas e textos) foi produzido com uso de
> inteligência artificial, sob responsabilidade do preparador. Salvaguardas: cada dado público traz documento e página de origem,
> e todos os cálculos e a base podem ser reproduzidos pelo código. Nenhuma revisão por terceiros foi realizada ou simulada
> (os campos de revisão dos papéis de trabalho estão em branco).

## Organização do repositório

```
01_dossie/                  Dossiê em PDF (papéis de trabalho com referências cruzadas) e HTML-fonte
02_base_simulada/           Base simulada (ver link abaixo), dicionário, registro de erros inseridos, resultados dos testes
   resultados/              Conciliação, exceções, investigação, amostra MUS, comparação inseridos x identificados (CSV/JSON)
03_codigo/                  Código de geração e análise (Python) e instruções de reprodução
04_planilhas/               Planilha editável com fórmulas (materialidade, analíticos, amostragem, conciliações, mapa de distorções...)
05_matriz_cobertura/        Matriz de cobertura das normas (NBC TA x papéis de trabalho)
06_fontes/                  Relação das fontes utilizadas (endereço, data de acesso, documento, página, exercício)
07_colab/                   Notebook do Google Colab que reproduz a base simulada e os testes
```

### Papéis de trabalho (no PDF)
PT EC, 200, 210, 220, 230, 240, 250, 260, 265, 300, 315, 320, 330, 402, 450, 500, 501, 505, 510, 520, 530, 540, 550, 560,
570, 580 e 600; programas por ciclo (receitas, disponibilidades, estoques, imobilizado, passivos e estimativas); seção da base
simulada; conclusão integrada; matriz de cobertura; relação de fontes.

Classificação de cada procedimento: **[R]** realizado com evidência pública · **[P]** planejado por falta de acesso ·
**[S]** simulado para fins didáticos.

## Base simulada (≥ 500.000 linhas)

| Item | Valor |
|---|---|
| Conta | Estoques consolidados em 31/12/2025 – R$ 1.478.926 mil (DF 2025, p.19; nota 7.2) |
| Linhas | 518.271 registros (posição por SKU e local; lotes de matérias-primas/embalagens) |
| Conciliação | Diferença zero com as notas 7.2 (saldo), 7.3 (provisão de R$ 4.688 mil) e 20.9 (lucro não realizado de R$ 1.293.806 mil) |
| Arquivo | `base_estoques_sintetica_31122025.csv` (≈ 144 MB; `;` separador; `,` decimal; UTF-8) |
| SHA-256 | `4a405e474b7211503f8a6ecab1a0ff05f562693951c178b3b0fec8a90be30cbb` |
| **Download** | **[LINK EXTERNO A SER INSERIDO PELO PREPARADOR]** |

O arquivo completo excede o limite de 100 MB do GitHub e está disponível pelo link acima. O repositório contém o código que o
reproduz de forma idêntica (semente fixa 241003384; confira pelo SHA-256), uma amostra de 2.000 linhas
(`base_estoques_sintetica_AMOSTRA_2000_linhas.csv`), o dicionário de variáveis e o registro dos erros inseridos.

Arquivos de apoio:
- `registro_erros_inseridos.csv` – gabarito com 3.705 erros inseridos (9 tipos); lido apenas na comparação final.
- `contagem_fisica_e_custo_documental_SIMULADOS.zip` (CSV compactado; também recriado por `gerar_base.py`) – "verdade simulada" consultada somente para itens selecionados
  (simula contagem física e inspeção de documentos).
- `resultados/` – saídas dos testes (PT 450, 500, 530).

## Como reproduzir

**Google Colab:** abra `07_colab/base_simulada_vivara_colab.ipynb` no Colab (Arquivo → Abrir notebook → GitHub), ou use o botão "Abrir no Colab" acima e execute todas as células (Ambiente de execução → Executar tudo).

**Localmente:**

Requisitos: Python 3.10+.

```bash
cd 03_codigo
pip install -r requirements.txt
python -m playwright install chromium     # apenas para gerar o PDF
python executar_tudo.py                    # base -> testes -> cálculos -> planilha -> anexos -> PDF
# ou, sem gerar o PDF:
python executar_tudo.py --sem-pdf
```

Etapas individuais:

| Script | Saída |
|---|---|
| `gerar_base.py` | base simulada, registro de erros, verdade simulada, resumo |
| `testes_auditoria.py` | conciliação da base, testes de 100% (T1–T9), investigação, amostra MUS, avaliação, comparação inseridos x identificados |
| `calculos_pts.py` | materialidade, 44 conciliações, saldos iniciais, analíticos, sensibilidade, liquidez, componentes (dados públicos em `dados_publicos.py`) |
| `gerar_planilhas.py` | `04_planilhas/PT_calculos_Vivara_241003384.xlsx` (com fórmulas) |
| `exportar_anexos.py` | dicionário, matriz de cobertura, relação de fontes, amostra da base |
| `gerar_dossie.py` | `01_dossie/Dossie_Auditoria_Vivara_241003384.pdf` |
| `mapear_itens_normas.py` | `normas_paginas.json` (página de cada item das NBC TA na compilação da disciplina; requer o PDF da compilação) |

## Parâmetros principais

- Materialidade global: R$ 29.000 mil (5% do LAIR consolidado de 2025, arredondado); materialidade para execução: R$ 17.400 mil (60%);
  limite trivial: R$ 1.450 mil (PT 320).
- Data de corte dos eventos subsequentes: 18/03/2026 (data de autorização das DF e do relatório do auditor) (PT 560).
- Normas: versões aplicáveis ao exercício de 2025 conforme a compilação "Consolidado Normas Aud1"; registro de versões no PT 230.

## Identificação da companhia

Vivara Participações S.A. – CNPJ 33.839.910/0001-11 – Código CVM 2480-5 – ações ordinárias **VIVA3** (Novo Mercado, desde
10/10/2019). Nome empresarial anterior: L.I.R.S.P.E. Empreendimentos e Participações Ltda. (até 15/06/2019). Nenhuma alteração
de código de negociação identificada (FCA 2026, p.2 e p.4; B3, p.2).

## Fontes

Documentos públicos da CVM (FRE 2026 v6, DFP 2024, FCA 2026), da B3 (página da companhia) e da área de RI da Vivara (DF 2025,
ITR 1T26 e 2T26, fatos relevantes, proposta e ata da AGO/E 2026, aviso ao mercado da 2ª emissão de debêntures). Lista completa com endereços, datas de acesso e páginas em
`06_fontes/relacao_fontes.md`.
