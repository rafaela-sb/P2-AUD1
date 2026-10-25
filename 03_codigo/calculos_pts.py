# -*- coding: utf-8 -*-
"""
Cálculos reproduzíveis dos papéis de trabalho com DADOS PÚBLICOS (classificação: REALIZADO COM EVIDÊNCIA PÚBLICA,
exceto quando indicado). Valores em R$ mil. Saída: 02_base_simulada/resultados/resultados_calculos.json
PT 320 materialidade | PT 500 conciliações | PT 510 saldos iniciais | PT 520 analíticos |
PT 540 sensibilidade (arrendamentos e provisão de estoques) | PT 570 liquidez | PT 600 componentes
"""
import json, os
import numpy as np
import dados_publicos as D
import parametros as P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "02_base_simulada", "resultados")
os.makedirs(OUT, exist_ok=True)
R = {}
B25, B24 = D.BP["2025"], D.BP["2024"]
R25, R24 = D.DRE["2025"], D.DRE["2024"]


def chk(desc, calculado, divulgado, fonte, tol=1):
    dif = round(calculado - divulgado, 2)
    return {"verificacao": desc, "calculado": round(calculado, 2), "divulgado": round(divulgado, 2), "diferenca": dif,
            "status": "OK" if abs(dif) <= tol else "DIVERGENCIA", "fonte": fonte}


# ------------------------------------------------------------------ PT 320
alternativas = [
    ("LAIR 2025", R25["lair"], 0.05), ("LAIR médio 2023-2025", (R25["lair"] + R24["lair"] + D.DRE["2023"]["lair"]) / 3, 0.05),
    ("Receita líquida 2025", R25["receita_liquida"], 0.01), ("Receita líquida 2025 (0,5%)", R25["receita_liquida"], 0.005),
    ("Ativo total 2025", B25["ativo_total"], 0.01), ("Patrimônio líquido 2025", B25["patrimonio_liquido"], 0.01),
    ("Lucro bruto 2025", R25["lucro_bruto"], 0.01)]
R["PT320"] = {"alternativas": [{"referencial": a, "base": round(b, 1), "percentual": p, "materialidade": round(b * p, 1)}
                               for a, b, p in alternativas],
              "referencial_escolhido": P.REFERENCIAL, "MG_calculada": round(P.MG_CALCULADA, 1), "MG": P.MG,
              "ME": P.ME, "perc_ME": P.PERC_ME, "trivial": P.LIMITE_TRIVIAL,
              "MG_sobre_receita": round(P.MG / R25["receita_liquida"], 4), "MG_sobre_ativo": round(P.MG / B25["ativo_total"], 4),
              "MG_sobre_PL": round(P.MG / B25["patrimonio_liquido"], 4), "MG_sobre_LL": round(P.MG / R25["lucro_liquido"], 4),
              "especificas": [{"item": "Remuneração dos administradores (nota 19.3)", "materialidade": 1200,
                               "base": "≈10% do total de R$ 12.020 mil; sensibilidade dos usuários e limite aprovado em AGO"},
                              {"item": "Transações e saldos com partes relacionadas (nota 19)", "materialidade": 1450,
                               "base": "limite trivial - natureza qualitativa (NBC TA 550)"}]}

# ------------------------------------------------------------------ PT 500 conciliações
C = []
f = "DF25 p.19"
C.append(chk("Ativo circulante = soma dos itens", sum(B25[k] for k in ["caixa_equivalentes", "tvm", "contas_receber", "estoques",
             "impostos_recuperar_cp", "irpj_csll_recuperar_cp", "despesas_antecipadas_cp"]), B25["ativo_circulante"], f))
C.append(chk("Realizável a LP = soma dos itens", sum(B25[k] for k in ["derivativos_lp", "depositos_judiciais", "ir_cs_diferidos",
             "despesas_antecipadas_lp", "impostos_recuperar_lp", "irpj_csll_recuperar_lp"]), B25["realizavel_lp"], f))
C.append(chk("Ativo não circulante = RLP + imobilizado + intangível", B25["realizavel_lp"] + B25["imobilizado"] + B25["intangivel"],
             B25["ativo_nao_circulante"], f))
C.append(chk("Ativo total = AC + ANC", B25["ativo_circulante"] + B25["ativo_nao_circulante"], B25["ativo_total"], f))
C.append(chk("Passivo circulante = soma dos itens", sum(B25[k] for k in ["fornecedores", "fornecedores_convenio", "emprestimos_cp",
             "obrig_trabalhistas", "obrig_tributarias_cp", "irpj_csll_recolher", "arrend_variaveis", "jcp_pagar", "derivativos_passivo",
             "dividendos_pagar", "arrendamentos_cp", "outros_passivos_cp"]), B25["passivo_circulante"], f))
C.append(chk("Passivo não circulante = soma dos itens", sum(B25[k] for k in ["emprestimos_lp", "obrig_tributarias_lp", "provisoes",
             "arrendamentos_lp", "outros_passivos_lp"]), B25["passivo_nao_circulante"], f))
C.append(chk("PL = soma dos itens", sum(B25[k] for k in ["capital_social", "reservas_capital", "acoes_tesouraria", "opcoes_outorgadas",
             "reservas_lucros", "ora"]), B25["patrimonio_liquido"], f))
C.append(chk("Passivo + PL = Ativo total", B25["passivo_circulante"] + B25["passivo_nao_circulante"] + B25["patrimonio_liquido"],
             B25["ativo_total"], f))
C.append(chk("DRE: lucro líquido = LAIR + IR/CS", R25["lair"] + R25["ir_cs_correntes"] + R25["ir_cs_diferidos"], R25["lucro_liquido"], "DF25 p.20"))
C.append(chk("DRE: LAIR = EBIT + resultado financeiro", R25["lucro_antes_res_fin"] + R25["receitas_financeiras"] + R25["despesas_financeiras"],
             R25["lair"], "DF25 p.20"))
F25 = D.DFC["2025"]
C.append(chk("DFC: variação de caixa = operacional + investimento + financiamento", F25["caixa_operacional_liquido"] +
             F25["caixa_investimento"] + F25["caixa_financiamento"], F25["aumento_caixa"], "DF25 p.23"))
C.append(chk("DFC: caixa final = BP", F25["caixa_inicial"] + F25["aumento_caixa"], B25["caixa_equivalentes"], "DF25 p.23 x p.19"))
E = D.ESTOQUES
C.append(chk("Nota 7.2: composição = estoques no BP", sum(v for k, v in E["2025"].items() if k != "total"), B25["estoques"], "DF25 p.30 x p.19"))
C.append(chk("Nota 7.3: provisão (fim) = base do IR diferido 2025 (nota 20.9)", -E["provisao"]["2025"]["fim"],
             E["provisao_perdas_base_ir_diferido"]["2025"], "DF25 p.31 x p.52"))
C.append(chk("Nota 7.3: provisão (fim) 2024 = base do IR diferido 2024 (nota 20.9)", -E["provisao"]["2024"]["fim"],
             E["provisao_perdas_base_ir_diferido"]["2024"], "DF25 p.31 x p.52"))
C.append(chk("Nota 7.3: movimentação da provisão", E["provisao"]["2025"]["inicio"] + E["provisao"]["2025"]["provisoes"] +
             E["provisao"]["2025"]["reversoes"], E["provisao"]["2025"]["fim"], "DF25 p.31"))
C.append(chk("DFC: ajuste 'provisão para perdas de estoque' = -(provisões + reversões) (nota 7.3)", -(E["provisao"]["2025"]["provisoes"] +
             E["provisao"]["2025"]["reversoes"]), F25["provisao_perdas_estoque_ajuste"], "DF25 p.23 x p.31"))
RC = D.RECEBER["2025"]
C.append(chk("Nota 6.2: contas a receber líquido = BP", RC["bruto"] + RC["pecld"], B25["contas_receber"], "DF25 p.29 x p.19"))
C.append(chk("Nota 10.4: imobilizado líquido = BP", D.IMOB["liquido_2025"], B25["imobilizado"], "DF25 p.35 x p.19"))
EP = D.EMPREST["2025"]
C.append(chk("Nota 15.1: empréstimos CP + LP = BP", EP["cp"] + EP["lp"], B25["emprestimos_cp"] + B25["emprestimos_lp"], "DF25 p.40 x p.19"))
C.append(chk("Nota 15.1: total líquido de derivativos", EP["total"] + EP["swap_passivo"], EP["total_liq_deriv"], "DF25 p.40"))
PV = D.PROVISOES["2025"]
C.append(chk("Nota 17.1: provisões = BP", PV["total"], B25["provisoes"], "DF25 p.41 x p.19"))
C.append(chk("FRE item 4.4: provisões (R$) x nota 17.1", sum(D.PROVISOES_FRE_REAIS.values()) / 1000, PV["total"], "FRE p.116 x DF25 p.41"))
A = D.ARREND
C.append(chk("Nota 28: passivo de arrendamento CP + LP = BP", B25["arrendamentos_cp"] + B25["arrendamentos_lp"], A["passivo_2025"], "DF25 p.58 x p.19"))
C.append(chk("Nota 28: fluxos não descontados - juros embutidos = passivo", A["fluxos_nao_descontados_2025"]["total"] +
             A["fluxos_nao_descontados_2025"]["juros_embutidos"], A["passivo_2025"], "DF25 p.60"))
mv = A["movimento_2025"]
C.append(chk("Nota 28: movimentação do passivo", sum(v for k, v in mv.items() if k != "fim"), mv["fim"], "DF25 p.59"))
IRD = D.IR_DIFERIDO
C.append(chk("Nota 20.9: IR/CS diferidos líquidos = BP", IRD["ativo_2025"] + IRD["passivo_2025"], B25["ir_cs_diferidos"], "DF25 p.52 x p.19"))
RE = D.RECEITA["2025"]
C.append(chk("Nota 21.2: composição = receita líquida", sum(v for k, v in RE.items() if k != "liquida"), R25["receita_liquida"], "DF25 p.53 x p.20"))
C.append(chk("Nota 23: receita por categoria = bruta - devoluções (nota 21.2)", D.RECEITA["categorias_2025"]["total"],
             RE["bruta_mercadorias"] + RE["bruta_servicos"] + RE["devolucoes"], "DF25 p.55 x p.53"))
C.append(chk("Nota 18.4: dividendo mínimo = 25% x (LL - reserva legal)", round((R25["lucro_liquido"] - 30975) * 0.25), 147132, "DF25 p.46"))
C.append(chk("AGO: lucro líquido (R$) x DRE", D.OUTROS["lucro_liquido_ago_reais"] / 1000, R25["lucro_liquido"], "AGO p.14 x DF25 p.20"))
C.append(chk("AGO: reserva estatutária (R$) = lucro ajustado - dividendos", 588527183.98 - 164000000.00,
             D.OUTROS["reserva_estatutaria_ago_reais"], "AGO p.15", tol=0.01))
C.append(chk("Nota 20.8: IR/CS diferidos na conciliação x DRE", 139324, R25["ir_cs_diferidos"], "DF25 p.51 x p.20", tol=0))
C.append(chk("Nota 9.4: investimentos (controladora) = soma das controladas", 713539 + 2513919 + 3010, D.CONTROLADAS["investimento_2025"], "DF25 p.33"))
for nome, c in D.CONTROLADAS["2025"].items():
    C.append(chk(f"Nota 9.2: {nome} - total do passivo e PL divulgado x total do ativo", c["total_passivo_pl_divulgado"], c["ativo_total"], "DF25 p.32"))
C.append(chk("Depreciação e amortização: DFC x notas 10.6 + 11.2", D.IMOB["deprec_2025"]["total"] + 17834, F25["depreciacao_amortizacao"], "DF25 p.23 x p.36-37"))
C.append(chk("Depreciação e amortização: DFC x nota 22 (custo + vendas + G&A)", 1636 + 85796 + 65404, F25["depreciacao_amortizacao"], "DF25 p.23 x p.53-54"))
C.append(chk("Nota 29.3: 'fornecedores e outras contas a pagar' 2024 x BP 2024", 93654, B24["fornecedores"], "DF25 p.63 x p.19"))
C.append(chk("Nota 29.3: dividendos a pagar consolidado 2025 x BP", 0, B25["dividendos_pagar"], "DF25 p.63 x p.19", tol=0))
I1 = D.ITR["1T26"]
C.append(chk("ITR 1T26: comparativo 31/12/2025 - ativo total x DF 2025", I1["comparativo_12_2025_ativo_total"], B25["ativo_total"], "ITR1 p.5 x DF25 p.19", tol=0))
C.append(chk("ITR 1T26: comparativo 31/12/2025 - PL x DF 2025", I1["comparativo_12_2025_pl"], B25["patrimonio_liquido"], "ITR1 p.5 x DF25 p.19", tol=0))
C.append(chk("ITR 1T26: comparativo 31/12/2025 - reservas de lucros x DF 2025", I1["comparativo_12_2025_reservas_lucros"], B25["reservas_lucros"], "ITR1 p.5 x DF25 p.19", tol=0))
R["PT500"] = C

# ------------------------------------------------------------------ PT 510 saldos iniciais
F = D.DFP24_FORM["2024"]
pares = [("Caixa e equivalentes", F["caixa"], B24["caixa_equivalentes"]), ("Aplicações financeiras/TVM", F["aplicacoes"], B24["tvm"]),
         ("Contas a receber", F["contas_receber"], B24["contas_receber"]), ("Estoques", F["estoques"], B24["estoques"]),
         ("Tributos a recuperar (CP)", F["tributos_recuperar"], B24["impostos_recuperar_cp"] + B24["irpj_csll_recuperar_cp"]),
         ("Ativo circulante", F["ativo_circulante"], B24["ativo_circulante"]),
         ("Ativo não circulante", F["ativo_nao_circulante"], B24["ativo_nao_circulante"]),
         ("Imobilizado", F["imobilizado"], B24["imobilizado"]), ("Intangível", F["intangivel"], B24["intangivel"]),
         ("Passivo circulante", F["passivo_circulante"], B24["passivo_circulante"]),
         ("Fornecedores (DFP: inclui convênio)", F["fornecedores"], B24["fornecedores"] + B24["fornecedores_convenio"]),
         ("Empréstimos CP", F["emprestimos_cp"], B24["emprestimos_cp"]), ("Empréstimos LP", F["emprestimos_lp"], B24["emprestimos_lp"]),
         ("Passivo não circulante", F["passivo_nao_circulante"], B24["passivo_nao_circulante"]),
         ("Provisões", F["provisoes"], B24["provisoes"]),
         ("Receita líquida 2024", F["receita_liquida"], R24["receita_liquida"]), ("CMV 2024", F["cmv"], R24["cmv"]),
         ("LAIR 2024", F["lair"], R24["lair"]), ("Lucro líquido 2024", F["lucro_liquido"], R24["lucro_liquido"])]
R["PT510"] = [{"linha": a, "DFP2024_RS_mil": round(x / 1000, 1), "comparativo_DF2025_RS_mil": y,
               "diferenca": round(x / 1000 - y, 1), "status": "OK (arredondamento)" if abs(x / 1000 - y) <= 1.5 else "DIVERGENCIA"} for a, x, y in pares]
N3 = D.DFP24_FORM["nota3_2023"]
R["PT510_retificacao_2023"] = {"lucro_2023_formulario_DFP24": D.DFP24_FORM["2023"]["lucro_liquido"] / 1000,
                               "lucro_2023_retificado_nota3": N3["lucro_retificado"], "diferenca": round(N3["lucro_retificado"] - D.DFP24_FORM["2023"]["lucro_liquido"] / 1000, 1)}

# ------------------------------------------------------------------ PT 520 analíticos
A520 = []
ME = P.ME


def anal(nome, esperado, real, limite, premissas, fonte):
    dif = real - esperado
    return {"conta": nome, "esperado": round(esperado, 1), "real": round(real, 1), "diferenca": round(dif, 1),
            "diferenca_pct": round(dif / esperado, 4) if esperado else None, "limite_investigacao": round(limite, 1),
            "investigar": abs(dif) > limite, "premissas": premissas, "fonte": fonte}


lojas24 = D.RECEITA["canais_2024"]["Lojas"]; lojas25 = D.RECEITA["canais_2025"]["Lojas"]
esp = lojas24 * (1 + D.OUTROS["sss_2025"]) + D.OUTROS["aberturas_liquidas_2025"] * D.OUTROS["receita_media_life_madura"] * 0.5
A520.append(anal("Receita bruta - lojas físicas", esp, lojas25, ME,
                 "Lojas 2024 x (1 + SSS 11,8%) + 41 aberturas líquidas x R$ 5.600 mil (receita média anual de loja Life madura) x 50% do ano",
                 "DF25 p.55; p.3; p.4; p.7"))
mg24 = R24["lucro_bruto"] / R24["receita_liquida"]
A520.append(anal("Custo das mercadorias vendidas", R25["receita_liquida"] * (1 - mg24), -R25["cmv"], ME,
                 f"Receita líquida 2025 x (1 - margem bruta 2024 de {mg24:.2%})", "DF25 p.20"))
dv24 = -R24["desp_vendas"] / R24["receita_liquida"]
A520.append(anal("Despesas com vendas", R25["receita_liquida"] * dv24, -R25["desp_vendas"], ME,
                 f"Receita líquida 2025 x (despesas com vendas/receita 2024 = {dv24:.2%})", "DF25 p.20"))
ga24 = -R24["desp_gerais_adm"] / R24["receita_liquida"]
A520.append(anal("Despesas gerais e administrativas", R25["receita_liquida"] * ga24, -R25["desp_gerais_adm"], ME,
                 f"Receita líquida 2025 x (G&A/receita 2024 = {ga24:.2%})", "DF25 p.20"))
c24, c25 = D.IMOB["custo_2024"], D.IMOB["custo_2025"]; vu = D.IMOB["vida_util_anos"]
esp_dep = sum((c24[k] + c25[k]) / 2 / (sum(vu[k]) / 2) for k in ["benfeitorias", "moveis", "maquinas", "veiculos", "informatica", "rou_imoveis"])
real_dep = sum(D.IMOB["deprec_2025"][k] for k in ["benfeitorias", "moveis", "maquinas", "veiculos", "informatica", "rou_imoveis"])
A520.append(anal("Depreciação (imobilizado e direito de uso de imóveis)", esp_dep, real_dep, ME,
                 "Custo médio (2024/2025) por classe / ponto médio da vida útil divulgada (nota 10.3)", "DF25 p.34-36"))
esp_arr = (A["passivo_2024"] + A["passivo_2025"]) / 2 * A["taxa_media"]
A520.append(anal("Encargos financeiros de arrendamento", esp_arr, A["encargos_2025"], ME,
                 "Passivo médio de arrendamento x taxa média ponderada de 12,92% a.a. (nota 28)", "DF25 p.58-59"))
cdi = 0.1432
esp_deb = 300000 * (((1 + cdi) * 1.007) ** (117 / 365) - 1)
A520.append(anal("Juros das debêntures (05/09 a 31/12/2025)", esp_deb, D.EMPREST["debentures"]["juros_incorridos_2025"], ME,
                 "R$ 300.000 mil x [(1+CDI 14,32%)x(1,007)]^(117/365) - 1; CDI 14,32% = taxa do cenário I da nota 29.7 (proxy)",
                 "DF25 p.40-41 e p.66"))
pes25 = sum(D.DESPESAS["pessoal_2025"].values()); pes24 = sum(D.DESPESAS["pessoal_2024"].values())
hc25, hc24 = D.OUTROS["headcount_2025"], D.OUTROS["headcount_2024"]
A520.append(anal("Despesas de pessoal (custo + vendas + G&A)", pes24 / hc24 * hc25, pes25, ME,
                 "Custo de pessoal por colaborador 2024 x quadro de 2025 (quadro de fim de exercício, nota de pessoas)", "DF25 p.14 e p.53-54"))
# Investigação das diferenças acima do limite (corroboração com o Relatório da Administração - DF25 p.8-12)
cmv24_sem_ggf = -R24["cmv"] + 43900          # 2024: R$ 43,9 mi de GGF alocados ao estoque (DF25 p.8)
mg24_aj = 1 - cmv24_sem_ggf / R24["receita_liquida"]
esp_cmv_aj = R25["receita_liquida"] * (1 - mg24_aj) - 24400   # 2025: R$ 24,4 mi alocados ao estoque (DF25 p.8)
for a in A520:
    if a["conta"] == "Custo das mercadorias vendidas":
        a["investigacao"] = {"explicacao": "Mudança de metodologia de GGF no fechamento de 2024 (alocação de R$ 43,9 mi ao estoque em 2024 e R$ 24,4 mi em 2025) - DF25 p.8-9",
                             "esperado_ajustado": round(esp_cmv_aj, 1), "diferenca_residual": round(-R25["cmv"] - esp_cmv_aj, 1),
                             "residual_dentro_do_limite": abs(-R25["cmv"] - esp_cmv_aj) <= ME}
    if a["conta"] == "Despesas com vendas":
        a["investigacao"] = {"explicacao": "Menor número de aberturas em 2025 (41) que em 2024 (71) reduziu despesas de pessoal de lojas novas; aumentos em fretes, CRM e marketing (DF25 p.10)",
                             "diferenca_residual": None, "residual_dentro_do_limite": None,
                             "conclusao": "Explicação qualitativa corroborada parcialmente; sem dados internos para quantificar - procedimento substantivo de detalhe planejado (PT 330)"}
    if a["conta"] == "Despesas gerais e administrativas":
        a["investigacao"] = {"explicacao": "Alavancagem operacional; G&A (ex-D&A) cresceu 8,6% vs receita líquida +17,4%; reversão one-off de ICP no 4T24 (DF25 p.10)",
                             "diferenca_residual": None, "residual_dentro_do_limite": None,
                             "conclusao": "Explicação qualitativa consistente com a nota 22.3; teste de detalhes de serviços profissionais planejado (PT 330)"}
R["PT520_analiticos"] = A520
avg_est25 = (B24["estoques"] + B25["estoques"]) / 2
avg_est24 = (D.DFP24_FORM["2023"]["estoques"] / 1000 + B24["estoques"]) / 2
R["PT520_indices"] = {
    "margem_bruta": {"2025": round(R25["lucro_bruto"] / R25["receita_liquida"], 4), "2024": round(mg24, 4)},
    "margem_liquida": {"2025": round(R25["lucro_liquido"] / R25["receita_liquida"], 4), "2024": round(R24["lucro_liquido"] / R24["receita_liquida"], 4)},
    "dias_estoque_CMV": {"2025": round(avg_est25 / -R25["cmv"] * 365, 1), "2024": round(avg_est24 / -R24["cmv"] * 365, 1),
                         "RA_ex_GGF_2025": D.ESTOQUES["dias_estoque_ex_ggf_RA"]},
    "giro_estoque": {"2025": round(-R25["cmv"] / avg_est25, 3), "2024": round(-R24["cmv"] / avg_est24, 3)},
    "dias_recebimento_receita_bruta": {"2025": round(D.RECEBER["2025"]["bruto"] / (RE["bruta_mercadorias"] + RE["bruta_servicos"]) * 365, 1),
                                       "divulgado_nota6": D.RECEBER["prazo_medio_dias_2025"]},
    "provisao_sobre_estoque": {"2025": round(4688 / (B25["estoques"] + 4688), 5), "2024": round(5217 / (B24["estoques"] + 5217), 5)},
    "crescimento_receita_liquida": round(R25["receita_liquida"] / R24["receita_liquida"] - 1, 4),
    "crescimento_estoques": round(B25["estoques"] / B24["estoques"] - 1, 4),
    "aliquota_efetiva": {"2025": round(-(R25["ir_cs_correntes"] + R25["ir_cs_diferidos"]) / R25["lair"], 4)}}

# ------------------------------------------------------------------ PT 540 sensibilidade - arrendamentos
fl = A["fluxos_nao_descontados_2025"]
cf = [(0.5, fl["ate_1"]), (1.5, fl["1_2"]), (2.5, fl["2_3"]), (3.5, fl["3_5"] / 2), (4.5, fl["3_5"] / 2)] + \
     [(5.5 + i, fl["mais_5"] / 5) for i in range(5)]


def pv(r):
    return sum(v / (1 + r) ** t for t, v in cf)


lo, hi = 0.0, 0.5
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if pv(mid) > A["passivo_2025"] else (lo, mid)
taxa_impl = (lo + hi) / 2
sens = [{"taxa": round(r, 4), "valor_presente": round(pv(r), 1), "variacao_vs_12_92": round(pv(r) - pv(A["taxa_media"]), 1)}
        for r in [0.1092, 0.1192, 0.1292, 0.1392, 0.1492]]
R["PT540_arrendamento"] = {"premissa_distribuicao_fluxos": "pontos médios das faixas; faixa 3-5 anos dividida em 2 anos; > 5 anos distribuída em 5 anos (contratos majoritariamente de 10 anos - nota 28)",
                           "vp_a_12_92": round(pv(A["taxa_media"]), 1), "passivo_divulgado": A["passivo_2025"],
                           "diferenca_modelo": round(pv(A["taxa_media"]) - A["passivo_2025"], 1),
                           "taxa_implicita_modelo": round(taxa_impl, 4), "sensibilidade": sens,
                           "efeito_1pp": round(pv(0.1192) - pv(0.1292), 1)}
# provisão para perdas de estoque - revisão retrospectiva (ITR 2026)
pv25 = -E["provisao"]["2025"]["fim"]
R["PT540_provisao_estoque"] = {"saldo_31_12_2025": pv25, "reversoes_1T26": E["provisao_itr"]["1T26"]["reversoes"],
                               "reversoes_1S26": E["provisao_itr"]["2T26"]["reversoes"],
                               "complementos_1S26": -E["provisao_itr"]["2T26"]["complementos"],
                               "pct_revertido_1S26": round(E["provisao_itr"]["2T26"]["reversoes"] / pv25, 4),
                               "saldo_30_06_2026": -E["provisao_itr"]["2T26"]["fim"],
                               "provisao_sobre_estoque_bruto": round(pv25 / (B25["estoques"] + pv25), 5),
                               "cenarios": [{"cenario": f"Provisão de {p:.1%} do estoque bruto", "provisao": round((B25["estoques"] + pv25) * p, 1),
                                             "efeito_resultado": round(-(B25["estoques"] + pv25) * p + pv25, 1)} for p in [0.005, 0.01, 0.02]]}

# ------------------------------------------------------------------ PT 570 liquidez
def ind(b, caixa_extra=0):
    return {"liquidez_corrente": round(b["ativo_circulante"] / b["passivo_circulante"], 2),
            "liquidez_seca": round((b["ativo_circulante"] - b["estoques"]) / b["passivo_circulante"], 2),
            "liquidez_imediata": round((b["caixa_equivalentes"] + b.get("tvm", 0)) / b["passivo_circulante"], 2),
            "endividamento_geral": round((b["passivo_circulante"] + b["passivo_nao_circulante"]) / b["ativo_total"], 4),
            "PL_sobre_ativo": round(b["patrimonio_liquido"] / b["ativo_total"], 4)}


div25 = EP["total_liq_deriv"]; div24 = D.EMPREST["2024"]["total_liq_deriv"]
ebitda25 = R25["lucro_antes_res_fin"] + F25["depreciacao_amortizacao"]; ebitda24 = R24["lucro_antes_res_fin"] + D.DFC["2024"]["depreciacao_amortizacao"]
R["PT570"] = {"2025": ind(B25), "2024": ind(B24),
              "divida_bruta_liq_derivativos": {"2025": div25, "2024": div24},
              "divida_liquida": {"2025": div25 - B25["caixa_equivalentes"], "2024": div24 - B24["caixa_equivalentes"] - B24["tvm"]},
              "lajida_calculado": {"2025": ebitda25, "2024": ebitda24},
              "divida_liquida_sobre_lajida": {"2025": round((div25 - B25["caixa_equivalentes"]) / ebitda25, 3),
                                              "2024": round((div24 - B24["caixa_equivalentes"] - B24["tvm"]) / ebitda24, 3)},
              "fco": {"2025": F25["caixa_operacional_liquido"], "2024": D.DFC["2024"]["caixa_operacional_liquido"]},
              "vencimentos_12m_emprestimos": 268108, "vencimentos_12m_arrendamento": 139829,
              "santander_4131_vencimento_dez_2026": EP["santander_4131"],
              "ITR_1T26": {"liquidez_corrente": round(I1["ativo_circulante"] / I1["passivo_circulante"], 2), "caixa": I1["caixa"], "pl": I1["pl"]},
              "ITR_2T26": {"liquidez_corrente": round(D.ITR["2T26"]["ativo_circulante"] / D.ITR["2T26"]["passivo_circulante"], 2),
                           "caixa": D.ITR["2T26"]["caixa"], "pl": D.ITR["2T26"]["pl"], "lucro_6m": D.ITR["2T26"]["lucro_6m"]}}

# ------------------------------------------------------------------ PT 600 componentes
comp = []
tot_at = sum(c["ativo_total"] for c in D.CONTROLADAS["2025"].values())
for nome, c in D.CONTROLADAS["2025"].items():
    comp.append({"componente": nome, "ativo_total": c["ativo_total"], "pct_soma_ativos_componentes": round(c["ativo_total"] / tot_at, 4),
                 "lucro_prejuizo": c["lucro"], "pct_lucro_abs": round(abs(c["lucro"]) / sum(abs(x["lucro"]) for x in D.CONTROLADAS["2025"].values()), 4)})
R["PT600"] = {"componentes": comp, "MG_grupo": P.MG, "ME_grupo": P.ME,
              "ME_componentes": {"Tellerina": 12000, "Conipa": 12000, "Tellerina Panama": 3000, "Vivara Participacoes (controladora)": 6000},
              "eliminacoes_2025": D.CONTROLADAS["equivalencia_2025"],
              "lnr_base_ir_diferido": D.ESTOQUES["lucro_nao_realizado_base_ir_diferido"],
              "variacao_lnr": D.ESTOQUES["lucro_nao_realizado_base_ir_diferido"]["2025"] - D.ESTOQUES["lucro_nao_realizado_base_ir_diferido"]["2024"]}

json.dump(R, open(os.path.join(OUT, "resultados_calculos.json"), "w"), ensure_ascii=False, indent=2)
div = [c for c in C if c["status"] != "OK"]
print("Conciliações:", len(C), "divergências:", len(div))
for c in div:
    print("  ", c["verificacao"], c["calculado"], c["divulgado"], c["diferenca"])
for a in A520:
    print(a["conta"], a["esperado"], a["real"], a["diferenca"], a["investigar"])
print(R["PT540_arrendamento"]); print(R["PT570"]["2025"], R["PT570"]["divida_liquida_sobre_lajida"]); print(R["PT520_indices"])
print(R["PT510"]); print(R["PT510_retificacao_2023"])
