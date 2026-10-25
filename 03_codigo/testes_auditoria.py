# -*- coding: utf-8 -*-
"""
PT 530 / PT 450 / PT 501 - PROCEDIMENTOS EXECUTADOS SOBRE A BASE SIMULADA (DADOS SINTÉTICOS)
================================================================================================
Classificação de todos os procedimentos deste programa: SIMULADO PARA FINS DIDÁTICOS.

Etapas:
  1. Conciliação da base com o saldo contábil (nota 7.2), a provisão (nota 7.3) e a base de lucro
     não realizado (nota 20.9).
  2. Testes em 100% da população (análise de dados): T1..T9.
  3. Investigação dos itens sinalizados (simula inspeção de documentos/contagem dos itens sinalizados).
  4. Amostragem estatística por unidade monetária (MUS) para existência e exatidão (contagem + vouching).
  5. Avaliação: projeção, limite superior de distorção, comparação com distorção tolerável.
  6. Comparação entre erros INSERIDOS (registro_erros_inseridos.csv) e erros IDENTIFICADOS.
     O registro de erros só é lido nesta etapa final; nenhuma etapa de detecção o utiliza.
"""
import json, os
import numpy as np
import pandas as pd
import parametros as P
from dados_publicos import ESTOQUES

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "02_base_simulada")
OUTD = os.path.join(DIR, "resultados")
os.makedirs(OUTD, exist_ok=True)
DATA_BASE = pd.Timestamp(P.DATA_BASE)


def carregar():
    b = pd.read_csv(os.path.join(DIR, "base_estoques_sintetica_31122025.csv"), sep=";", decimal=",",
                    parse_dates=["data_ultima_entrada", "data_ultima_saida", "data_ultimo_inventario_interno"])
    return b


def conciliacao(b):
    alvo = ESTOQUES["2025"]
    linhas = []
    mapa = {"PRODUTO_ACABADO": "produtos_acabados", "MATERIA_PRIMA": "materias_primas",
            "MAT_CONSUMO_EMBALAGEM": "consumo_embalagens", "EM_TRANSITO": "em_transito"}
    for cl, k in mapa.items():
        v = b.loc[b.classe_estoque == cl, "valor_liquido"].sum()
        linhas.append({"item": f"Saldo líquido - {cl}", "base_simulada_RS": round(v, 2),
                       "contabil_RS": alvo[k] * 1000.0, "diferenca_RS": round(v - alvo[k] * 1000.0, 2),
                       "fonte_contabil": "DF25 nota 7.2, p.30"})
    v = b["valor_liquido"].sum()
    linhas.append({"item": "Total estoques (líquido)", "base_simulada_RS": round(v, 2), "contabil_RS": alvo["total"] * 1000.0,
                   "diferenca_RS": round(v - alvo["total"] * 1000.0, 2), "fonte_contabil": "DF25 BP p.19 / nota 7.2 p.30"})
    v = b["provisao_perda"].sum()
    linhas.append({"item": "Provisão para perdas", "base_simulada_RS": round(v, 2), "contabil_RS": 4688000.0,
                   "diferenca_RS": round(v - 4688000.0, 2), "fonte_contabil": "DF25 nota 7.3, p.31"})
    v = b["lucro_nao_realizado_eliminado"].sum()
    linhas.append({"item": "Lucro não realizado eliminado na consolidação", "base_simulada_RS": round(v, 2),
                   "contabil_RS": 1293806000.0, "diferenca_RS": round(v - 1293806000.0, 2),
                   "fonte_contabil": "DF25 nota 20.9, p.52 (base do IR diferido)"})
    v = b["valor_contabil"].sum()
    linhas.append({"item": "Saldo bruto (antes da provisão)", "base_simulada_RS": round(v, 2),
                   "contabil_RS": 1483614000.0, "diferenca_RS": round(v - 1483614000.0, 2),
                   "fonte_contabil": "Nota 7.2 + 7.3 (premissa: composição divulgada é líquida da provisão)"})
    return pd.DataFrame(linhas)


def testes_100(b):
    exc = []

    def add(mask, teste, descricao):
        for i in b.index[mask]:
            exc.append((b.at[i, "id_registro"], teste, descricao))

    # T1 - recálculo quantidade x custo unitário
    dif = (b["quantidade"] * b["custo_unitario"] - b["valor_contabil"]).abs()
    add(dif > 0.05, "T1_RECALCULO_QTDxCUSTO", "valor contábil difere de qtd x custo")
    # T2 - duplicidade de chave SKU+local+lote
    add(b.duplicated(["cod_sku", "cod_local", "lote"], keep="first"), "T2_DUPLICIDADE", "chave sku/local/lote repetida")
    # T3 - quantidades negativas
    add(b["quantidade"] < 0, "T3_QTD_NEGATIVA", "quantidade negativa")
    # T4 - corte: entrada posterior à data-base
    add(b["data_ultima_entrada"] > DATA_BASE, "T4_CORTE", "entrada posterior a 31/12/2025")
    # T5 - política de provisão (nota 7.3)
    pa = b.classe_estoque == "PRODUTO_ACABADO"
    m5a = pa & (b.passivel_derretimento == "N") & (b.dias_sem_giro > 365) & (b.provisao_perda < b.valor_contabil - 0.05)
    m5b = pa & (b.passivel_derretimento == "S") & (b.colecao_descontinuada == "S") & \
        (b.provisao_perda < b.valor_contabil * P.PERDA_DERRETIMENTO - 0.05)
    add(m5a | m5b, "T5_GIRO_LENTO_SEM_PROVISAO", "item enquadrado na política de provisão sem provisão suficiente")
    # T6 - custo x valor realizável líquido
    vrl_u = b["preco_venda_unitario"] * (1 - P.DESPESA_VENDA_VRL)
    falta = ((b["custo_unitario"] - vrl_u).clip(lower=0) * b["quantidade"].clip(lower=0)) - b["provisao_perda"]
    add(pa & (vrl_u < b["custo_unitario"]) & (falta > 0.05), "T6_CUSTO_ACIMA_VRL", "custo acima do VRL sem provisão")
    # T7 - custo unitário atípico por SKU (> 3x mediana do SKU, mínimo 3 posições)
    g = b[pa & (b.quantidade > 0)].groupby("cod_sku")["custo_unitario"]
    med = g.transform("median"); cnt = g.transform("count")
    m7 = pd.Series(False, index=b.index)
    m7.loc[med.index] = (b.loc[med.index, "custo_unitario"] > 3 * med) & (cnt >= 3)
    add(m7, "T7_CUSTO_ATIPICO", "custo unitário > 3x mediana do mesmo SKU")
    # T8 - classificação: matéria-prima fora de fábrica/filial de compras
    add((b.classe_estoque == "MATERIA_PRIMA") & ~b.tipo_local.isin(["FABRICA", "FILIAL_COMPRAS"]),
        "T8_CLASSIFICACAO_LOCAL", "matéria-prima registrada em loja")
    # T9 - integridade de campos obrigatórios
    add(b[["cod_sku", "cod_local", "classe_estoque", "custo_unitario"]].isna().any(axis=1), "T9_CAMPOS_VAZIOS",
        "campo obrigatório vazio")
    return pd.DataFrame(exc, columns=["id_registro", "teste", "descricao"])


def investigar(b, exc, verdade):
    """Simula a investigação dos itens sinalizados (inspeção de documentos e recontagem).
    Retorna a distorção quantificada por item (R$, + = superavaliação do estoque líquido)."""
    ids = exc["id_registro"].unique()
    bb = b.set_index("id_registro").loc[ids]
    vv = verdade.set_index("id_registro").loc[ids]
    res = []
    for idr in ids:
        r = bb.loc[idr]; t = vv.loc[idr]
        testes = sorted(exc.loc[exc.id_registro == idr, "teste"].unique())
        qf = max(t["quantidade_contada_simulada"], 0.0); cd = t["custo_unitario_documental_simulado"]
        auditado_bruto = round(qf * cd, 2)
        prov_req = r["provisao_perda"]
        if r["classe_estoque"] == "PRODUTO_ACABADO" and qf > 0:
            if r["passivel_derretimento"] == "N" and r["dias_sem_giro"] > 365:
                prov_req = auditado_bruto
            elif r["passivel_derretimento"] == "S" and r["colecao_descontinuada"] == "S":
                prov_req = max(prov_req, round(auditado_bruto * P.PERDA_DERRETIMENTO, 2))
            vrl = r["preco_venda_unitario"] * (1 - P.DESPESA_VENDA_VRL)
            if pd.notna(vrl) and vrl < cd:
                prov_req = max(prov_req, round((cd - vrl) * qf, 2))
        if qf == 0:
            prov_req = 0.0
        auditado_liq = round(auditado_bruto - prov_req, 2)
        dist = round(r["valor_liquido"] - auditado_liq, 2)
        res.append({"id_registro": idr, "testes": "+".join(testes), "valor_liquido_registrado": r["valor_liquido"],
                    "valor_liquido_auditado_simulado": auditado_liq, "distorcao_RS": dist,
                    "status": "CONFIRMADA" if abs(dist) > 0.05 or "T8_CLASSIFICACAO_LOCAL" in testes else "NAO_CONFIRMADA"})
    return pd.DataFrame(res)


def amostra_mus(b, verdade, ids_excecao):
    pop = b[b["valor_liquido"] > 0].sort_values("id_registro").reset_index(drop=True)
    BV = pop["valor_liquido"].sum()
    TM, EM = P.DISTORCAO_TOLERAVEL_RS, P.DISTORCAO_ESPERADA_RS
    n = int(np.ceil(BV * P.FATOR_CONFIABILIDADE / (TM - EM * P.FATOR_EXPANSAO)))
    J = BV / n
    rng = np.random.default_rng(P.SEMENTE)
    inicio = rng.uniform(0, J)
    pontos = inicio + J * np.arange(n)
    cum = pop["valor_liquido"].cumsum().to_numpy()
    pos = np.searchsorted(cum, pontos, side="left")
    sel = pop.iloc[pos].copy()
    sel["ponto_selecao_RS"] = np.round(pontos, 2)
    sel["acertos"] = 1
    sel = sel.groupby("id_registro", as_index=False).agg({**{c: "first" for c in sel.columns if c not in ("id_registro", "acertos")},
                                                          "acertos": "sum"})
    v = verdade.set_index("id_registro")
    sel["quantidade_contada_simulada"] = sel["id_registro"].map(v["quantidade_contada_simulada"])
    sel["custo_documental_simulado"] = sel["id_registro"].map(v["custo_unitario_documental_simulado"])
    sel["valor_auditado_RS"] = (sel["quantidade_contada_simulada"].clip(lower=0) * sel["custo_documental_simulado"]
                                - sel["provisao_perda"]).round(2)
    sel.loc[sel["quantidade_contada_simulada"] <= 0, "valor_auditado_RS"] = 0.0
    sel["distorcao_RS"] = (sel["valor_liquido"] - sel["valor_auditado_RS"]).round(2)
    sel["ja_identificado_teste_100pct"] = sel["id_registro"].isin(ids_excecao)
    sel["taint"] = (sel["distorcao_RS"] / sel["valor_liquido"]).clip(upper=1.0).round(6)
    # Avaliação (Stringer) - apenas distorções não identificadas nos testes de 100% são projetadas
    proj = sel[(sel.distorcao_RS.abs() > 0.05) & (~sel.ja_identificado_teste_100pct)].copy()
    proj["distorcao_projetada_RS"] = np.where(proj["valor_liquido"] >= J, proj["distorcao_RS"], proj["taint"] * J)
    sobre = proj[proj.distorcao_RS > 0].sort_values("taint", ascending=False)
    PB = J * P.FATORES_POISSON_95[0]
    incr = 0.0
    for k, (_, r) in enumerate(sobre.iterrows(), start=1):
        if r["valor_liquido"] >= J:
            continue
        f = P.FATORES_POISSON_95[min(k, 10)] - P.FATORES_POISSON_95[min(k - 1, 10)]
        incr += (f - 1) * r["taint"] * J
    projetada = float(sobre["distorcao_projetada_RS"].sum())
    UML = PB + projetada + incr
    aval = {"populacao_itens": int(len(pop)), "valor_populacao_RS": round(BV, 2), "distorcao_toleravel_RS": TM,
            "distorcao_esperada_RS": EM, "fator_confiabilidade": P.FATOR_CONFIABILIDADE, "fator_expansao": P.FATOR_EXPANSAO,
            "tamanho_amostra_unidades": n, "itens_distintos_selecionados": int(len(sel)), "intervalo_amostral_RS": round(J, 2),
            "inicio_aleatorio_RS": round(float(inicio), 2), "semente": P.SEMENTE,
            "itens_com_distorcao_total": int((sel.distorcao_RS.abs() > 0.05).sum()),
            "itens_com_distorcao_ja_identificada_100pct": int(((sel.distorcao_RS.abs() > 0.05) & sel.ja_identificado_teste_100pct).sum()),
            "itens_com_distorcao_projetada": int(len(proj)), "distorcao_amostra_projetavel_RS": round(float(proj.distorcao_RS.sum()), 2),
            "precisao_basica_RS": round(PB, 2), "distorcao_projetada_RS": round(projetada, 2),
            "provisao_incremental_RS": round(incr, 2), "limite_superior_distorcao_RS": round(UML, 2),
            "conclusao": "UML <= distorção tolerável: população aceita" if UML <= TM else
            "UML > distorção tolerável: população NÃO aceita sem procedimentos adicionais/ajuste"}
    return sel, proj, aval


def comparar(b, inv, sel):
    log = pd.read_csv(os.path.join(DIR, "registro_erros_inseridos.csv"), sep=";", decimal=",")
    confirmados = inv[inv.status == "CONFIRMADA"].set_index("id_registro")
    amostra_erro = sel[(sel.distorcao_RS.abs() > 0.05)].set_index("id_registro")
    log["detectado_teste_100pct"] = log["id_registro"].isin(confirmados.index)
    log["testes_que_detectaram"] = log["id_registro"].map(confirmados["testes"]).fillna("")
    log["detectado_na_amostra_MUS"] = log["id_registro"].isin(amostra_erro.index)
    log["detectado"] = log["detectado_teste_100pct"] | log["detectado_na_amostra_MUS"]
    log["distorcao_quantificada_RS"] = log["id_registro"].map(confirmados["distorcao_RS"]).fillna(
        log["id_registro"].map(amostra_erro["distorcao_RS"])).fillna(0.0)
    resumo = log.groupby("tipo_erro").agg(inseridos=("id_registro", "count"), detectados=("detectado", "sum"),
                                          detectados_100pct=("detectado_teste_100pct", "sum"),
                                          detectados_amostra=("detectado_na_amostra_MUS", "sum"),
                                          efeito_inserido_RS=("efeito_superavaliacao_RS", "sum"),
                                          distorcao_quantificada_RS=("distorcao_quantificada_RS", "sum")).reset_index()
    resumo["taxa_deteccao"] = (resumo["detectados"] / resumo["inseridos"]).round(4)
    fp = inv[(inv.status == "NAO_CONFIRMADA")]
    fp_extra = inv[(inv.status == "CONFIRMADA") & (~inv.id_registro.isin(log.id_registro))]
    return log, resumo, fp, fp_extra


def main():
    b = carregar()
    verdade = pd.read_csv(os.path.join(DIR, "contagem_fisica_e_custo_documental_SIMULADOS.csv"), sep=";", decimal=",")
    conc = conciliacao(b)
    exc = testes_100(b)
    inv = investigar(b, exc, verdade)
    ids_conf = set(inv.loc[inv.status == "CONFIRMADA", "id_registro"])
    sel, proj, aval = amostra_mus(b, verdade, ids_conf)
    log, resumo, fp, fp_extra = comparar(b, inv, sel)

    conc.to_csv(os.path.join(OUTD, "PT500_conciliacao_base_x_contabil.csv"), index=False, sep=";", decimal=",")
    exc.to_csv(os.path.join(OUTD, "PT530_excecoes_testes_100pct.csv"), index=False, sep=";", decimal=",")
    inv.to_csv(os.path.join(OUTD, "PT530_investigacao_itens_sinalizados.csv"), index=False, sep=";", decimal=",")
    sel.to_csv(os.path.join(OUTD, "PT530_amostra_MUS_selecionada.csv"), index=False, sep=";", decimal=",", date_format="%Y-%m-%d")
    log.to_csv(os.path.join(OUTD, "PT450_comparacao_inseridos_x_identificados_detalhe.csv"), index=False, sep=";", decimal=",")
    resumo.to_csv(os.path.join(OUTD, "PT450_comparacao_inseridos_x_identificados_resumo.csv"), index=False, sep=";", decimal=",")

    por_teste = exc.groupby("teste").id_registro.nunique().to_dict()
    conf_por_teste = {}
    for t in exc.teste.unique():
        ids = exc.loc[exc.teste == t, "id_registro"].unique()
        sub = inv[inv.id_registro.isin(ids)]
        conf_por_teste[t] = {"sinalizados": int(len(ids)), "confirmados": int((sub.status == "CONFIRMADA").sum()),
                             "distorcao_confirmada_RS": round(float(sub.loc[sub.status == "CONFIRMADA", "distorcao_RS"].sum()), 2)}
    conhecidas = float(inv.loc[inv.status == "CONFIRMADA", "distorcao_RS"].sum())
    prioridade = ["T2_DUPLICIDADE", "T3_QTD_NEGATIVA", "T4_CORTE", "T1_RECALCULO_QTDxCUSTO", "T7_CUSTO_ATIPICO",
                  "T5_GIRO_LENTO_SEM_PROVISAO", "T6_CUSTO_ACIMA_VRL", "T8_CLASSIFICACAO_LOCAL", "T9_CAMPOS_VAZIOS"]
    inv["teste_principal"] = inv["testes"].apply(lambda t: next(x for x in prioridade if x in t.split("+")))
    por_principal = inv[inv.status == "CONFIRMADA"].groupby("teste_principal").agg(
        itens=("id_registro", "count"), distorcao_RS=("distorcao_RS", "sum")).round(2).reset_index().to_dict("records")
    inv.to_csv(os.path.join(OUTD, "PT530_investigacao_itens_sinalizados.csv"), index=False, sep=";", decimal=",")
    out = {"linhas_base": int(len(b)), "conciliacao": conc.to_dict("records"), "testes_100pct": conf_por_teste,
           "itens_sinalizados_distintos": int(exc.id_registro.nunique()),
           "itens_confirmados": int((inv.status == "CONFIRMADA").sum()),
           "falsos_positivos": int(len(fp)), "confirmados_fora_do_registro_de_erros": int(len(fp_extra)),
           "distorcao_conhecida_testes_100pct_RS": round(conhecidas, 2), "distorcao_por_teste_principal": por_principal,
           "mus": aval, "comparacao": resumo.to_dict("records"),
           "efeito_total_inserido_RS": round(float(log.efeito_superavaliacao_RS.sum()), 2),
           "distorcao_total_estimada_RS": round(conhecidas + aval["distorcao_projetada_RS"], 2)}
    json.dump(out, open(os.path.join(OUTD, "resultados_testes.json"), "w"), ensure_ascii=False, indent=2, default=float)
    print(json.dumps({k: v for k, v in out.items() if k not in ("conciliacao",)}, ensure_ascii=False, indent=1, default=float))


if __name__ == "__main__":
    main()
