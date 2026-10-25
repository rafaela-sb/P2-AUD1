# -*- coding: utf-8 -*-
"""PT 450 - Mapa de distorções e inconsistências. Valores em R$ mil.
Origem: P = evidência pública (observada nos documentos); S = simulada (base sintética de estoques)."""

PUBLICAS = [
    # código, descrição, documento/página, natureza, valor (R$ mil), afeta DF 2025?, tratamento
    ("D01", "Nota 31 data o aumento de capital de R$ 866.644 mil em '15 de dezembro de 2015'; a nota 18.1 informa "
            "deliberação do Conselho em 15/12/2025", "DF25 p.68 x p.45", "Divulgação (exatidão)", 0, "Sim",
     "Não corrigida (DF já emitidas). Qualitativamente irrelevante para decisões; comunicar à governança (PT 260)"),
    ("D02", "Nota 31 remete à 'Nota Explicativa nº 15.3' para juros e encargos; a 15.3 trata de covenants e a "
            "movimentação está na 15.5", "DF25 p.68 x p.41", "Divulgação (referência cruzada)", 0, "Sim",
     "Não corrigida; irrelevante; comunicar"),
    ("D03", "Sumário das DF anuais refere-se a 'informações financeiras intermediárias' e a 'relatório sobre informações "
            "financeiras intermediárias'", "DF25 p.2", "Apresentação (título)", 0, "Sim",
     "Não corrigida; o relatório do auditor (p.15) e as demonstrações identificam o exercício corretamente"),
    ("D04", "Nota 9.2: 'Total do passivo e PL' das controladas não iguala o 'Total do ativo'; a diferença é igual ao "
            "resultado do exercício de cada controlada (Tellerina 67.090; Conipa 874.926; Panamá 1.484) - 2025 e 2024",
     "DF25 p.32", "Divulgação (somatório)", 0, "Sim",
     "Não corrigida; não afeta saldos consolidados nem a equivalência (nota 9.3/9.4 concilia); comunicar"),
    ("D05", "Base de IR diferido 'provisão para perdas dos estoques' 2024 = 5.401 (nota 20.9) x saldo da provisão "
            "em 31/12/2024 = 5.217 (nota 7.3)", "DF25 p.52 x p.31", "Divulgação/mensuração (comparativo)", 184, "Sim",
     "Diferença de 184 x alíquota 34% = 63 de IR diferido; claramente trivial (< 1.450)"),
    ("D06", "Nota 29.3: comparativo 2024 de 'Fornecedores e outras contas a pagar' = 93.654 (só fornecedores) x BP "
            "2024 = 158.736; dividendos a pagar consolidados 2025 apresentados como '-' x BP = 10",
     "DF25 p.63 x p.19", "Divulgação (consistência de comparativos)", 65082, "Sim",
     "Classificação dentro da nota de instrumentos financeiros; não afeta o BP; qualitativamente irrelevante"),
    ("D07", "Nota 20.8: IR/CS diferidos de 139.324 x DRE 139.322 (diferença 2)", "DF25 p.51 x p.20",
     "Arredondamento", 2, "Sim", "Trivial"),
    ("D08", "Nota 22 (despesas por natureza): depreciação e amortização no resultado = 152.836 x DFC/notas 10.6 e 11.2 = "
            "162.855 (diferença 10.019)", "DF25 p.53-54 x p.23, p.36-37", "Item de reconciliação (a explicar)", 10019, "Sim",
     "Hipótese: parcela de depreciação incorporada ao custo dos estoques (GGF). Confirmar com a administração (planejado)"),
]
