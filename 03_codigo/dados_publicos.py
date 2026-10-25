# -*- coding: utf-8 -*-
"""
Dados PÚBLICOS transcritos das demonstrações contábeis e documentos da Vivara Participações S.A.
Todos os valores em R$ mil, exceto quando indicado.
Cada grupo informa o documento e a página do PDF (numeração do arquivo PDF, não a numeração impressa).

Siglas de documentos (ver 06_fontes/relacao_fontes.md):
  DF25  = Demonstrações financeiras individuais e consolidadas 2025 (versão RI) - exercício 2025
  DFP24 = DFP 31/12/2024 (formulário CVM/ENET) - exercício 2024
  FRE   = Formulário de Referência 2026, versão 6
  ITR1  = ITR 31/03/2026 ; ITR2 = ITR 30/06/2026
  AGO   = Manual e Proposta da Administração AGO/E 27/04/2026
  FCA   = Formulário Cadastral 2026 v1 ; B3 = página "Empresas" B3 (VIVA3)
"""

# ---------------- Balanço patrimonial consolidado (DF25, p. 19) ----------------
BP = {
    "fonte": "DF25 p.19",
    "2025": {
        "caixa_equivalentes": 398644, "tvm": 0, "contas_receber": 989601, "estoques": 1478926,
        "impostos_recuperar_cp": 118227, "irpj_csll_recuperar_cp": 50247, "despesas_antecipadas_cp": 28954,
        "ativo_circulante": 3064599,
        "derivativos_lp": 0, "depositos_judiciais": 28227, "ir_cs_diferidos": 568590,
        "despesas_antecipadas_lp": 5193, "impostos_recuperar_lp": 12618, "irpj_csll_recuperar_lp": 28180,
        "realizavel_lp": 642808, "imobilizado": 955347, "intangivel": 59938,
        "ativo_nao_circulante": 1658093, "ativo_total": 4722692,
        "fornecedores": 189472, "fornecedores_convenio": 4610, "emprestimos_cp": 232973,
        "obrig_trabalhistas": 143620, "obrig_tributarias_cp": 90328, "irpj_csll_recolher": 33581,
        "arrend_variaveis": 14488, "jcp_pagar": 0, "derivativos_passivo": 22729, "dividendos_pagar": 10,
        "arrendamentos_cp": 83187, "outros_passivos_cp": 28951, "passivo_circulante": 843949,
        "emprestimos_lp": 298303, "obrig_tributarias_lp": 95, "provisoes": 26937,
        "arrendamentos_lp": 599518, "outros_passivos_lp": 4326, "passivo_nao_circulante": 929179,
        "capital_social": 2572025, "reservas_capital": -53041, "acoes_tesouraria": -26818,
        "opcoes_outorgadas": 1976, "reservas_lucros": 455500, "ora": -78, "patrimonio_liquido": 2949564,
        "passivo_pl_total": 4722692,
    },
    "2024": {
        "caixa_equivalentes": 278153, "tvm": 4530, "contas_receber": 955208, "estoques": 1332578,
        "impostos_recuperar_cp": 156755, "irpj_csll_recuperar_cp": 33149, "despesas_antecipadas_cp": 21515,
        "ativo_circulante": 2781888,
        "derivativos_lp": 1276, "depositos_judiciais": 24779, "ir_cs_diferidos": 429267,
        "despesas_antecipadas_lp": 2879, "impostos_recuperar_lp": 48438, "irpj_csll_recuperar_lp": 64705,
        "realizavel_lp": 571344, "imobilizado": 853172, "intangivel": 67326,
        "ativo_nao_circulante": 1491842, "ativo_total": 4273730,
        "fornecedores": 158736, "fornecedores_convenio": 214135, "emprestimos_cp": 113370,
        "obrig_trabalhistas": 125293, "obrig_tributarias_cp": 63727, "irpj_csll_recolher": 43254,
        "arrend_variaveis": 14933, "jcp_pagar": 2, "derivativos_passivo": 0, "dividendos_pagar": 155186,
        "arrendamentos_cp": 88069, "outros_passivos_cp": 18982, "passivo_circulante": 995687,
        "emprestimos_lp": 285191, "obrig_tributarias_lp": 150, "provisoes": 18317,
        "arrendamentos_lp": 472131, "outros_passivos_lp": 5312, "passivo_nao_circulante": 781101,
        "capital_social": 1705381, "reservas_capital": -53041, "acoes_tesouraria": -26850,
        "opcoes_outorgadas": 4346, "reservas_lucros": 866640, "ora": 466, "patrimonio_liquido": 2496942,
        "passivo_pl_total": 4273730,
    },
}

# ---------------- DRE consolidada (DF25, p. 20) ----------------
DRE = {
    "fonte": "DF25 p.20",
    "2025": {"receita_liquida": 3026582, "cmv": -921472, "lucro_bruto": 2105110, "desp_vendas": -1086276,
             "desp_gerais_adm": -282216, "outras_receitas_despesas": -10296, "lucro_antes_res_fin": 726322,
             "receitas_financeiras": 69737, "despesas_financeiras": -208261, "lair": 587798,
             "ir_cs_correntes": -107618, "ir_cs_diferidos": 139322, "lucro_liquido": 619502},
    "2024": {"receita_liquida": 2577113, "cmv": -767087, "lucro_bruto": 1810026, "desp_vendas": -946097,
             "desp_gerais_adm": -257972, "outras_receitas_despesas": 77628, "lucro_antes_res_fin": 683585,
             "receitas_financeiras": 56935, "despesas_financeiras": -114282, "lair": 626238,
             "ir_cs_correntes": -108150, "ir_cs_diferidos": 135306, "lucro_liquido": 653394},
    # 2023 (DFP24 p.19, formulário padronizado, valores em R$ convertidos para R$ mil)
    "2023": {"receita_liquida": 2186975, "cmv": -670864, "lucro_bruto": 1516111, "desp_vendas": -817845,
             "desp_gerais_adm": -266574, "lair": 400843, "lucro_liquido": 369245},
}

# ---------------- DFC consolidada (DF25, p. 23) - principais linhas ----------------
DFC = {
    "fonte": "DF25 p.23",
    "2025": {"depreciacao_amortizacao": 162855, "var_estoques": -145819, "var_contas_receber": -39848,
             "caixa_operacional_liquido": 468870, "caixa_investimento": -78439, "caixa_financiamento": -269940,
             "aumento_caixa": 120491, "caixa_inicial": 278153, "caixa_final": 398644,
             "dividendos_pagos": -319175, "aquisicao_imobilizado": -69906, "aquisicao_intangivel": -10534,
             "provisao_perdas_estoque_ajuste": -529},
    "2024": {"depreciacao_amortizacao": 154530, "var_estoques": -550632, "var_contas_receber": -124143,
             "caixa_operacional_liquido": 150682, "caixa_investimento": -52127, "caixa_financiamento": -41897,
             "aumento_caixa": 56658, "caixa_inicial": 221495, "caixa_final": 278153},
}

# ---------------- Nota 7 - Estoques (DF25, p. 30-31) ----------------
ESTOQUES = {
    "fonte": "DF25 p.30-31 (nota 7.2 e 7.3)",
    "2025": {"produtos_acabados": 978949, "materias_primas": 443046, "consumo_embalagens": 56459,
             "adiantamentos_importacoes": 0, "em_transito": 472, "total": 1478926},
    "2024": {"produtos_acabados": 866841, "materias_primas": 353107, "consumo_embalagens": 48252,
             "adiantamentos_importacoes": 62262, "em_transito": 2116, "total": 1332578},
    "estoques_no_cmv_2025": 877247, "estoques_no_cmv_2024": 593764,
    "ggf_alocado_2025": 68145, "ggf_alocado_2024": 43911,
    "provisao": {"2025": {"inicio": -5217, "provisoes": -5271, "reversoes": 5800, "fim": -4688},
                 "2024": {"inicio": -4457, "provisoes": -5469, "reversoes": 4709, "fim": -5217}},
    # base do IR diferido (DF25 p.52, nota 20.9)
    "provisao_perdas_base_ir_diferido": {"2025": 4688, "2024": 5401},
    "lucro_nao_realizado_base_ir_diferido": {"2025": 1293806, "2024": 1029612},
    # Provisão para perdas no ITR (ITR1 p.14; ITR2 p.14)
    "provisao_itr": {"1T26": {"complementos": -1421, "reversoes": 2392, "fim": -3717},
                     "2T26": {"complementos": -2243, "reversoes": 4472, "fim": -2459}},
    "dias_estoque_ex_ggf_RA": 537,   # DF25 p.3
}

# ---------------- Nota 1 - Pontos de venda (DF25 p.25) ----------------
LOJAS = {"fonte": "DF25 p.25",
         "2025": {"vivara_br": 267, "life": 219, "quiosques": 11, "panama": 1, "total": 498},
         "2024": {"vivara_br": 265, "life": 180, "quiosques": 11, "panama": 1, "total": 457}}

# ---------------- Nota 6 - Contas a receber (DF25 p.29-30) ----------------
RECEBER = {"fonte": "DF25 p.29-30", "2025": {"cartoes": 986130, "boletos": 3663, "cheques": 163,
           "bruto": 989956, "pecld": -355, "liquido": 989601, "vencidos": 325, "a_vencer": 989631},
           "2024": {"cartoes": 952984, "boletos": 2209, "cheques": 256, "bruto": 955449, "pecld": -241,
                    "liquido": 955208}, "antecipacao_26dez2025_bruto": 164985, "prazo_medio_dias_2025": 95,
           "prazo_medio_dias_2024": 106}

# ---------------- Nota 10 - Imobilizado (DF25 p.35-36) ----------------
IMOB = {"fonte": "DF25 p.35-36",
        "custo_2025": {"benfeitorias": 369615, "moveis": 115968, "maquinas": 114614, "veiculos": 386,
                       "informatica": 32735, "terrenos": 350, "rou_imoveis": 1008024, "rou_cloud": 12380,
                       "andamento": 2706, "total": 1656778},
        "custo_2024": {"benfeitorias": 337860, "moveis": 107813, "maquinas": 90168, "veiculos": 302,
                       "informatica": 28570, "terrenos": 350, "rou_imoveis": 832197, "rou_cloud": 12380,
                       "andamento": 3233, "total": 1412873},
        "deprec_2025": {"benfeitorias": 29307, "moveis": 12460, "maquinas": 11132, "veiculos": 62,
                        "informatica": 4611, "rou_imoveis": 87416, "rou_cloud": 33, "total": 145021},
        "vida_util_anos": {"benfeitorias": (10, 15), "moveis": (5, 10), "maquinas": (5, 10), "veiculos": (5, 5),
                           "informatica": (3, 10), "rou_imoveis": (5, 15), "rou_cloud": (3, 3)},
        "liquido_2025": 955347, "liquido_2024": 853172}

# ---------------- Nota 15 - Empréstimos (DF25 p.40-41) ----------------
EMPREST = {"fonte": "DF25 p.40-41",
           "2025": {"debentures_1a": 312704, "santander_4131": 218572, "itau_cg": 0, "convenio": 0,
                    "total": 531276, "cp": 232973, "lp": 298303, "swap_passivo": 22729, "total_liq_deriv": 554005},
           "2024": {"debentures_1a": 0, "santander_4131": 245977, "itau_cg": 104402, "convenio": 48182,
                    "total": 398561, "cp": 113370, "lp": 285191, "swap_ativo": 1276, "total_liq_deriv": 397285},
           "debentures": {"valor": 300000, "emissao": "05/09/2025", "taxa": "CDI + 0,70% a.a.",
                          "vencimentos": "ago/2029 e ago/2030", "juros_incorridos_2025": 14401},
           "covenants": "Sem cláusulas financeiras restritivas; liquidação antecipada por protesto > R$10.000 mil "
                        "(capital de giro) e > R$100.000 mil (debêntures) - nota 15.3"}

# ---------------- Nota 17 - Provisões (DF25 p.41-45) ----------------
PROVISOES = {"fonte": "DF25 p.41-45",
             "2025": {"civeis": 3874, "trabalhistas": 16318, "tributarios": 6745, "total": 26937},
             "2024": {"civeis": 4791, "trabalhistas": 8772, "tributarios": 4754, "total": 18317},
             "possiveis_2025": {"trabalhistas": 59531, "civeis": 2813, "tributarios": 320179, "total": 382523},
             "possiveis_2024": {"trabalhistas": 48419, "civeis": 12975, "tributarios": 142512, "total": 203906},
             "auto_infracao_conipa_irpj_csll": 79896}
# FRE item 4.4 (FRE p.116) - valores provisionados em R$
PROVISOES_FRE_REAIS = {"trabalhistas": 16317946.53, "tributarias": 6744667.67, "civeis": 3873972.39}

# ---------------- Nota 28 - Arrendamentos (DF25 p.58-61) ----------------
ARREND = {"fonte": "DF25 p.58-61",
          "contratos_total": 500, "contratos_isentos": 80, "contratos_cpc06": 420, "taxa_media": 0.1292,
          "taxa_media_2024": 0.1219,
          "passivo_2025": 682705, "passivo_2024": 560200, "encargos_2025": 80179,
          "fluxos_nao_descontados_2025": {"ate_1": 139829, "1_2": 139666, "2_3": 139350, "3_5": 273517,
                                          "mais_5": 360342, "total": 1052704, "juros_embutidos": -369999},
          "movimento_2025": {"inicio": 560200, "adicoes": 25337, "remensuracao": 156768, "baixas": -4903,
                             "encargos": 80179, "pag_juros": -33391, "pag_principal": -101166,
                             "conversao": -319, "fim": 682705}}

# ---------------- Nota 20.9 - IR/CS diferidos (DF25 p.52) ----------------
IR_DIFERIDO = {"fonte": "DF25 p.52", "ativo_2025": 775771, "passivo_2025": -207181, "liquido_2025": 568590,
               "ativo_2024": 595388, "passivo_2024": -166121, "liquido_2024": 429267}

# ---------------- Nota 21 / 23 - Receita (DF25 p.53, 55) ----------------
RECEITA = {"fonte": "DF25 p.53 e p.55",
           "2025": {"bruta_mercadorias": 3802631, "bruta_servicos": 8272, "icms": -750042, "icms_subvencao": 334056,
                    "cofins": -255923, "pis": -55290, "fti_uea": -47267, "iss": -254, "devolucoes": -9601,
                    "liquida": 3026582},
           "2024": {"bruta_mercadorias": 3277471, "bruta_servicos": 9858, "icms": -644174, "icms_subvencao": 272011,
                    "cofins": -224772, "pis": -48806, "fti_uea": -48052, "iss": -340, "devolucoes": -16083,
                    "liquida": 2577113},
           "categorias_2025": {"Joias": 1853378, "Life": 1354460, "Relogios": 536167, "Acessorios": 49024,
                               "Servicos": 8272, "total": 3801302},
           "categorias_2024": {"Joias": 1582845, "Life": 1176407, "Relogios": 443554, "Acessorios": 58582,
                               "Servicos": 9858, "total": 3271246},
           "canais_2025": {"Lojas": 3223909, "Digital": 561584, "Outros": 7537, "Servicos": 8272, "total": 3801302},
           "canais_2024": {"Lojas": 2788197, "Digital": 469827, "Outros": 3363, "Servicos": 9858, "total": 3271245}}

# ---------------- Nota 22 - Despesas por natureza (DF25 p.53-54) ----------------
DESPESAS = {"fonte": "DF25 p.53-54",
            "pessoal_2025": {"cmv": 18387, "vendas": 520730, "ga": 96622},
            "pessoal_2024": {"cmv": 52123, "vendas": 476641, "ga": 84947},
            "fin_encargos_arrend_2025": 80179, "fin_encargos_arrend_2024": 60051}

# ---------------- Nota 9 - Controladas (DF25 p.32-33) ----------------
CONTROLADAS = {"fonte": "DF25 p.32-33 (nota 9.2)",
               "2025": {"Tellerina": {"ativo_total": 5360640, "pc": 3954213, "pnc": 616702, "pl": 856815,
                                      "total_passivo_pl_divulgado": 5427730, "lucro": -67090},
                        "Conipa": {"ativo_total": 4114502, "pc": 900770, "pnc": 11646, "pl": 2327160,
                                   "total_passivo_pl_divulgado": 3239576, "lucro": 874926},
                        "Tellerina Panama": {"ativo_total": 17650, "pc": 12838, "pnc": 1802, "pl": 4494,
                                             "total_passivo_pl_divulgado": 19134, "lucro": -1484}},
               "2024": {"Tellerina": {"ativo_total": 4353349, "pc": 2887752, "pnc": 765520, "pl": 704075,
                                      "total_passivo_pl_divulgado": 4357347, "lucro": -3998},
                        "Conipa": {"ativo_total": 3024255, "pc": 480517, "pnc": 12401, "pl": 1648632,
                                   "total_passivo_pl_divulgado": 2141550, "lucro": 882705},
                        "Tellerina Panama": {"ativo_total": 18472, "pc": 10922, "pnc": 2512, "pl": 6667,
                                             "total_passivo_pl_divulgado": 20101, "lucro": -1629}},
               "equivalencia_2025": {"lucro_controladas": 806352, "lucro_nao_realizado_estoques": -264234,
                                     "ir_cs_lnr": 89871, "avp": -6071, "ir_avp": 2064, "resultado": 627983},
               "investimento_2025": 3230468}

# ---------------- Remuneração e partes relacionadas (DF25 p.47-48) ----------------
PARTES_REL = {"fonte": "DF25 p.47-48",
              "controladores_pct": 47.36, "saldo_controladora_tellerina_2025": 3307, "saldo_2024": 1646,
              "intragrupo_2025": {"mercadorias_conipa_para_tellerina": 2552081, "materia_prima_tellerina_para_conipa": 298951,
                                  "direitos_autorais_conipa_receita": 352769, "csc": 13147},
              "remuneracao_2025": {"conselho": 1423, "conselho_fiscal": 374, "diretoria": 10224, "total": 12020},
              "remuneracao_2024": {"conselho": 2476, "conselho_fiscal": 0, "diretoria": 11375, "total": 13851},
              "limite_global_2025": 13877}

# ---------------- ITRs 2026 (ITR1 p.5-6; ITR2 p.5-6) ----------------
ITR = {"1T26": {"caixa": 308474, "estoques": 1550286, "contas_receber": 899085, "ativo_total": 4675668,
                "passivo_circulante": 715120, "ativo_circulante": 2962975, "emprestimos_cp": 214776,
                "emprestimos_lp": 298394, "pl": 3030290, "receita_liquida_tri": 595512, "lucro_tri": 80795,
                "comparativo_12_2025_ativo_total": 4722693, "comparativo_12_2025_pl": 2949567,
                "comparativo_12_2025_reservas_lucros": 455502, "relatorio_revisao": "07/05/2026"},
       "2T26": {"caixa": 416659, "estoques": 1537963, "contas_receber": 1015525, "ativo_total": 4880314,
                "passivo_circulante": 752176, "ativo_circulante": 3150810, "emprestimos_cp": 219847,
                "emprestimos_lp": 298484, "pl": 3184285, "receita_liquida_6m": 1428643, "lucro_6m": 232460,
                "relatorio_revisao": "05/08/2026"}}

# ---------------- DFP 2024 (formulário CVM) - saldos consolidados em R$ (DFP24 p.15-20) ----------------
DFP24_FORM = {"fonte": "DFP24 p.14-18 (BP) e p.19 (DRE)",
              "2024": {"ativo_circulante": 2781887721, "caixa": 278153431, "aplicacoes": 4529633,
                       "contas_receber": 955208115, "estoques": 1332577733, "tributos_recuperar": 189903972,
                       "ativo_nao_circulante": 1491842589, "imobilizado": 853171562, "intangivel": 67326039,
                       "passivo_circulante": 995685874, "fornecedores": 372870705, "emprestimos_cp": 113369653,
                       "passivo_nao_circulante": 781101449, "emprestimos_lp": 285191051, "provisoes": 18317611,
                       "receita_liquida": 2577113417, "cmv": -767087486, "lair": 626238141, "lucro_liquido": 653393946},
              "2023": {"estoques": 782706418, "contas_receber": 830832349, "caixa": 221495208,
                       "ir_cs_diferido_dre": 22999026, "lucro_liquido": 369244553},
              # Nota 3 da DFP24 (p.59-60; relatório do auditor p.101-103): retificação 2023
              "nota3_2023": {"lucro_apresentado": 369245, "ajuste": 11875, "lucro_retificado": 381120,
                             "ir_diferido_ativo_apresentado": 222152, "ajuste_bp": 71809, "ir_diferido_retificado": 293961}}

# ---------------- Outras informações ----------------
OUTROS = {"headcount_2025": 4986, "headcount_2024": 4802,  # DF25 p.14
          "sss_2025": 0.118, "receita_media_life_madura": 5600,  # DF25 p.3 e p.7 (R$ mil por loja/ano)
          "aberturas_liquidas_2025": 41,  # DF25 p.4
          "dividendos_intercalares_2025": 164000, "data_rca_dividendos": "15/12/2025",  # DF25 p.46
          "capital_aumento_2025": 866644,
          "honorarios_auditoria_2025_reais": 1586005.83,  # FRE p.239
          "lucro_liquido_ago_reais": 619502298.93, "reserva_legal_ago_reais": 30975114.95,
          "dividendo_obrigatorio_ago_reais": 147131796.00, "reserva_estatutaria_ago_reais": 424527183.92}  # AGO p.14-15
