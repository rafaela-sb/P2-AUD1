# -*- coding: utf-8 -*-
"""
PT 530 / PT 500 - GERAÇÃO DA BASE SIMULADA DE ESTOQUES (DADOS SINTÉTICOS)
==========================================================================
*** TODOS OS REGISTROS GERADOS POR ESTE PROGRAMA SÃO SINTÉTICOS (FICTÍCIOS). ***
*** NÃO SÃO REGISTROS REAIS DA VIVARA PARTICIPAÇÕES S.A. NEM DE SUAS CONTROLADAS. ***

Conta escolhida: Estoques consolidados em 31/12/2025 = R$ 1.478.926 mil (DF 2025, p.19; nota 7.2, p.30).
Unidade de registro (linha): posição de estoque por item (SKU) e local (loja, CD, fábrica) para produtos
acabados; lote para matérias-primas, materiais de consumo/embalagens e estoques em trânsito.

Saídas (pasta 02_base_simulada/):
  base_estoques_sintetica_31122025.csv   -> base completa (>= 500.000 linhas)  [hospedada por link externo]
  registro_erros_inseridos.csv          -> log dos erros inseridos (gabarito; NÃO é usado na detecção)
  contagem_fisica_e_custo_documental_SIMULADOS.csv -> "verdade" simulada usada apenas para responder aos
        procedimentos de contagem e de vouching dos itens SELECIONADOS na amostra (simula a ida a campo)
  resumo_geracao.json                   -> totais, sementes e parâmetros

Reprodução: python gerar_base.py   (semente fixa = 241003384)
"""
import json, os, sys
import numpy as np
import pandas as pd
import parametros as P

SEED = 241003384
rng = np.random.default_rng(SEED)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "02_base_simulada")
os.makedirs(OUT, exist_ok=True)
DATA_BASE = np.datetime64("2025-12-31")

# ------------------------------------------------------------------------------------------------
# 1. ALVOS PÚBLICOS (R$) - nota 7.2 e 7.3 das DF 2025 (p.30-31) e nota 20.9 (p.52)
# ------------------------------------------------------------------------------------------------
ALVO = {"PRODUTO_ACABADO": 978_949_000.00, "MATERIA_PRIMA": 443_046_000.00,
        "MAT_CONSUMO_EMBALAGEM": 56_459_000.00, "EM_TRANSITO": 472_000.00}
TOTAL_ALVO = 1_478_926_000.00
PROVISAO_ALVO = 4_688_000.00          # nota 7.3 - saldo final da provisão para perdas
LNR_ALVO = 1_293_806_000.00           # nota 20.9 - base de "lucro não realizado em operações de controladas"
assert abs(sum(ALVO.values()) - TOTAL_ALVO) < 0.01

# ------------------------------------------------------------------------------------------------
# 2. PREMISSAS SINTÉTICAS (documentadas no dicionário e no PT 530)
# ------------------------------------------------------------------------------------------------
# A composição do estoque por categoria NÃO é divulgada; a distribuição resultante é sintética.
# Fração produzida em Manaus (Relatório da Administração, DF25 p.3: 86,2% Vivara; 58,3% Life).
# Relógios e acessórios: premissa sintética (40% e 0%).
FRAC_PROPRIA = {"JOIAS": 0.862, "LIFE": 0.583, "RELOGIOS": 0.40, "ACESSORIOS": 0.0}
# Custo unitário sintético (mediana R$, sigma lognormal)
CUSTO_PA = {"JOIAS": (650, 1.05), "LIFE": (85, 0.55), "RELOGIOS": (420, 0.80), "ACESSORIOS": (70, 0.60)}
MARKUP = {"JOIAS": 3.4, "LIFE": 3.2, "RELOGIOS": 2.6, "ACESSORIOS": 2.8}   # preço de venda / custo (sintético)

# Locais (quantidades públicas: nota 1, DF25 p.25; 3 CDs: FRE p.26; fábrica em Manaus: nota 1)
N_VIVARA, N_LIFE, N_QUIOSQUE = 267, 219, 11
LOCAIS = []
for i in range(1, N_VIVARA + 1):
    LOCAIS.append((f"LJV{i:03d}", "LOJA_VIVARA", "TELLERINA"))
for i in range(1, N_LIFE + 1):
    LOCAIS.append((f"LJL{i:03d}", "LOJA_LIFE", "TELLERINA"))
for i in range(1, N_QUIOSQUE + 1):
    LOCAIS.append((f"QSQ{i:03d}", "QUIOSQUE", "TELLERINA"))
LOCAIS.append(("PAN001", "LOJA_PANAMA", "TELLERINA_PANAMA"))
for i in range(1, 4):
    LOCAIS.append((f"CD{i:02d}", "CENTRO_DISTRIBUICAO", "TELLERINA"))
LOCAIS.append(("FAB-MAO", "FABRICA", "CONIPA"))
LOCAIS.append(("FIL-SP", "FILIAL_COMPRAS", "CONIPA"))

# Nº de SKUs por posição e quantidades (sintético)
SKU_POR_LOCAL = {"LOJA_VIVARA": (1090, 120), "LOJA_LIFE": (810, 90), "QUIOSQUE": (300, 40),
                 "LOJA_PANAMA": (420, 0), "CENTRO_DISTRIBUICAO": (8200, 300), "FABRICA": (3800, 200)}
CATS_LOCAL = {"LOJA_VIVARA": {"JOIAS": .60, "LIFE": .12, "RELOGIOS": .23, "ACESSORIOS": .05},
              "LOJA_LIFE": {"LIFE": .93, "ACESSORIOS": .07},
              "QUIOSQUE": {"LIFE": .70, "JOIAS": .20, "ACESSORIOS": .10},
              "LOJA_PANAMA": {"JOIAS": .60, "LIFE": .20, "RELOGIOS": .15, "ACESSORIOS": .05},
              "CENTRO_DISTRIBUICAO": {"JOIAS": .45, "LIFE": .33, "RELOGIOS": .17, "ACESSORIOS": .05},
              "FABRICA": {"JOIAS": .70, "LIFE": .25, "RELOGIOS": .05}}
# Peso de valor por tipo de local (premissa sintética: lojas 70%, CDs 25%, fábrica 5%)
PESO_LOCAL = {"LOJA_VIVARA": 1.0, "LOJA_LIFE": 1.0, "QUIOSQUE": 1.0, "LOJA_PANAMA": 1.0,
              "CENTRO_DISTRIBUICAO": 1.0, "FABRICA": 1.0}

# Catálogo sintético de SKUs
N_SKU = {"JOIAS": 12000, "LIFE": 7000, "RELOGIOS": 4000, "ACESSORIOS": 2000}
SUBCAT = {"JOIAS": ["OURO_18K", "OURO_DIAMANTE", "PRATA_VIVARA", "DUO_PRATA_OURO", "DIAMANTE_LAB", "PEROLAS"],
          "LIFE": ["BERLOQUE", "PULSEIRA", "COLAR", "ANEL", "BRINCO"],
          "RELOGIOS": ["RELOGIO_MARCA_PROPRIA", "RELOGIO_REVENDA"],
          "ACESSORIOS": ["BOLSA", "OCULOS", "FRAGRANCIA", "CARTEIRA"]}


def catalogo():
    rows = []
    for cat, n in N_SKU.items():
        med, sig = CUSTO_PA[cat]
        custos = np.round(med * np.exp(rng.normal(0, sig, n)), 2)
        custos = np.clip(custos, 5, 250_000)
        sub = rng.choice(SUBCAT[cat], n)
        propria = rng.random(n) < FRAC_PROPRIA[cat]
        descont = np.zeros(n, dtype=bool)      # status de coleção definido por posição (seção 5)
        derretivel = np.isin(sub, ["OURO_18K", "OURO_DIAMANTE", "PRATA_VIVARA", "DUO_PRATA_OURO"]) | \
            ((cat == "LIFE") & (rng.random(n) < 0.6))
        for j in range(n):
            rows.append((f"{cat[:3]}-{j+1:05d}", cat, sub[j], custos[j], bool(propria[j]), bool(descont[j]),
                         bool(derretivel[j])))
    return pd.DataFrame(rows, columns=["cod_sku", "categoria", "subcategoria", "custo_base", "fabricacao_propria",
                                       "colecao_descontinuada", "passivel_derretimento"])


def gerar_produtos_acabados(cat_df):
    blocos = []
    by_cat = {c: cat_df[cat_df.categoria == c].reset_index(drop=True) for c in N_SKU}
    for cod, tipo, ent in LOCAIS:
        if tipo == "FILIAL_COMPRAS":
            continue
        n_med, n_sd = SKU_POR_LOCAL[tipo]
        n_pos = max(50, int(rng.normal(n_med, n_sd))) if n_sd else n_med
        mix = CATS_LOCAL[tipo]
        cats = rng.choice(list(mix.keys()), n_pos, p=np.array(list(mix.values())) / sum(mix.values()))
        for c in np.unique(cats):
            k = int((cats == c).sum())
            pool = by_cat[c]
            idx = rng.choice(len(pool), size=min(k, len(pool)), replace=False)
            sel = pool.iloc[idx].copy()
            if tipo in ("CENTRO_DISTRIBUICAO", "FABRICA"):
                q = rng.negative_binomial(2, 0.06, len(sel)) + 1
            else:
                q = rng.poisson(1.6, len(sel)) + 1
            sel["quantidade"] = q
            sel["cod_local"], sel["tipo_local"], sel["entidade"] = cod, tipo, ent
            blocos.append(sel)
    pa = pd.concat(blocos, ignore_index=True)
    # variação do custo médio ponderado por posição (+-3%) - custo médio difere por local/lote
    pa["custo_unitario"] = np.round(pa["custo_base"] * rng.normal(1.0, 0.015, len(pa)).clip(0.95, 1.05), 2)
    pa["classe_estoque"] = "PRODUTO_ACABADO"
    pa["unidade"] = "UN"
    pa["origem"] = np.where(pa["fabricacao_propria"], "FABRICACAO_PROPRIA_MANAUS",
                            np.where(rng.random(len(pa)) < 0.5, "REVENDA_IMPORTADA", "REVENDA_NACIONAL"))
    return pa


def gerar_materias_primas():
    tipos = {"OURO": ("G", .45, 900), "PRATA": ("G", .15, 900), "DIAMANTES": ("CT", .20, 2600),
             "PEDRAS_CORADAS": ("CT", .08, 1500), "PEROLAS": ("UN", .02, 500),
             "COMPONENTES_RELOGIO": ("UN", .07, 2300), "LIGAS_E_INSUMOS": ("G", .03, 500)}
    blocos = []
    for t, (un, w, n) in tipos.items():
        valor_lote = ALVO["MATERIA_PRIMA"] * w / n * np.exp(rng.normal(0, 0.9, n))
        if un == "G":
            custo = {"OURO": 520, "PRATA": 7.5, "LIGAS_E_INSUMOS": 3.0}[t] * rng.normal(1, .02, n)
        elif un == "CT":
            custo = {"DIAMANTES": 3800, "PEDRAS_CORADAS": 650}[t] * np.exp(rng.normal(0, .5, n))
        else:
            custo = {"PEROLAS": 45, "COMPONENTES_RELOGIO": 95}[t] * np.exp(rng.normal(0, .4, n))
        q = np.maximum(1, np.round(valor_lote / custo, 2 if un != "UN" else 0))
        local = np.where(rng.random(n) < 0.7, "FAB-MAO", "FIL-SP")
        df = pd.DataFrame({"categoria": t, "subcategoria": t, "unidade": un, "quantidade": q,
                           "custo_unitario": np.round(custo, 2), "cod_local": local})
        df["cod_sku"] = [f"MP-{t[:3]}-{k:05d}" for k in range(1, n + 1)]
        blocos.append(df)
    mp = pd.concat(blocos, ignore_index=True)
    mp["tipo_local"] = np.where(mp.cod_local == "FAB-MAO", "FABRICA", "FILIAL_COMPRAS")
    mp["entidade"] = "CONIPA"
    mp["classe_estoque"] = "MATERIA_PRIMA"
    mp["origem"] = np.where(rng.random(len(mp)) < 0.55, "COMPRA_NACIONAL", "COMPRA_IMPORTADA")
    mp["fabricacao_propria"] = False
    mp["colecao_descontinuada"] = False
    mp["passivel_derretimento"] = mp["categoria"].isin(["OURO", "PRATA", "LIGAS_E_INSUMOS"])
    return mp


def gerar_embalagens():
    n = 6000
    locs = [l for l in LOCAIS if l[1] != "FILIAL_COMPRAS"]
    pick = rng.integers(0, len(locs), n)
    df = pd.DataFrame({"cod_local": [locs[i][0] for i in pick], "tipo_local": [locs[i][1] for i in pick],
                       "entidade": [locs[i][2] for i in pick]})
    # concentra valor em CDs e fábrica
    peso = np.where(df.tipo_local.isin(["CENTRO_DISTRIBUICAO", "FABRICA"]), 25.0, 1.0)
    df["categoria"] = np.where(rng.random(n) < 0.7, "EMBALAGEM", "MATERIAL_CONSUMO")
    df["subcategoria"] = df["categoria"]
    df["unidade"] = "UN"
    df["custo_unitario"] = np.round(np.exp(rng.normal(np.log(9), 0.7, n)), 2)
    q = np.maximum(1, np.round(peso * np.exp(rng.normal(np.log(160), 0.8, n))))
    df["quantidade"] = q
    df["cod_sku"] = [f"EMB-{k:05d}" for k in rng.integers(1, 1500, n)]
    df["classe_estoque"] = "MAT_CONSUMO_EMBALAGEM"
    df["origem"] = "COMPRA_NACIONAL"
    df["fabricacao_propria"] = False
    df["colecao_descontinuada"] = False
    df["passivel_derretimento"] = False
    return df


def gerar_transito(cat_df):
    n = 140
    sel = cat_df.sample(n, random_state=SEED).copy()
    sel["quantidade"] = rng.integers(1, 6, n)
    sel["custo_unitario"] = sel["custo_base"]
    sel["cod_local"] = "TRANSITO"
    sel["tipo_local"] = "EM_TRANSITO_ENTRE_LOCAIS"
    sel["entidade"] = "TELLERINA"
    sel["classe_estoque"] = "EM_TRANSITO"
    sel["unidade"] = "UN"
    sel["origem"] = "TRANSFERENCIA_INTERNA"
    return sel


def main():
    cat_df = catalogo()
    pa = gerar_produtos_acabados(cat_df)
    mp = gerar_materias_primas()
    emb = gerar_embalagens()
    tr = gerar_transito(cat_df)
    base = pd.concat([pa, mp, emb, tr], ignore_index=True)
    base = base.sample(frac=1.0, random_state=SEED).reset_index(drop=True)
    n = len(base)
    base["id_registro"] = [f"SIM-EST-{i:07d}" for i in range(1, n + 1)]
    base["lote"] = [f"L{v:08d}" for v in rng.integers(1, 99_999_999, n)]
    base["quantidade"] = base["quantidade"].astype(float)
    # pré-calibração: aproxima cada classe do saldo-alvo antes da inserção de erros
    _alvo_pre = dict(ALVO); _alvo_pre["PRODUTO_ACABADO"] += PROVISAO_ALVO
    for cl, alvo in _alvo_pre.items():
        mc = base.classe_estoque == cl
        f0 = alvo / float((base.loc[mc, "quantidade"] * base.loc[mc, "custo_unitario"]).sum())
        base.loc[mc, "custo_unitario"] = np.round(base.loc[mc, "custo_unitario"] * f0, 2).clip(lower=0.01)

    # Datas sintéticas de movimentação e giro
    dias = np.minimum(np.round(rng.exponential(110, n)).astype(int), 365)   # giro lento atribuído na seção 5
    base["dias_sem_giro"] = dias
    base["data_ultima_saida"] = (DATA_BASE - dias.astype("timedelta64[D]")).astype("datetime64[D]")
    entrada = dias + rng.integers(0, 200, n)
    base["data_ultima_entrada"] = (DATA_BASE - entrada.astype("timedelta64[D]")).astype("datetime64[D]")
    inv_dias = rng.integers(0, 360, n)
    base["data_ultimo_inventario_interno"] = (DATA_BASE - inv_dias.astype("timedelta64[D]")).astype("datetime64[D]")

    # ---------------------------------------------------------------- 3. INSERÇÃO DE ERROS (gabarito)
    log = []
    base["qtd_fisica_sim"] = base["quantidade"].copy()          # verdade simulada
    base["custo_documental_sim"] = base["custo_unitario"].copy()  # verdade simulada
    base["valor_override"] = np.nan                              # valor registrado sem suporte (E7)
    base["provisao_correta_extra"] = 0.0                         # provisão faltante (E3/E6)
    usados = set()

    def escolher(mask, k):
        cand = base.index[mask & ~base.index.isin(list(usados))]
        esc = rng.choice(cand, size=min(k, len(cand)), replace=False)
        usados.update(esc.tolist())
        return esc

    pa_mask = base.classe_estoque == "PRODUTO_ACABADO"
    loja_mask = base.tipo_local.isin(["LOJA_VIVARA", "LOJA_LIFE", "QUIOSQUE"])
    # E2 - quantidade registrada maior que a existente (perda/furto não baixado)
    for i in escolher(pa_mask & loja_mask & (base.custo_unitario > 150), 3000):
        d = int(rng.integers(1, 3))
        base.at[i, "quantidade"] += d
        log.append((base.at[i, "id_registro"], "E2_QTD_SEM_EXISTENCIA_FISICA", "quantidade", "Existência",
                    base.at[i, "qtd_fisica_sim"], base.at[i, "quantidade"]))
    # E1 - custo unitário com deslocamento decimal (x10)
    for i in escolher(pa_mask & (base.custo_unitario.between(80, 2500)), 40):
        c = base.at[i, "custo_unitario"]
        base.at[i, "custo_unitario"] = round(c * 10, 2)
        log.append((base.at[i, "id_registro"], "E1_CUSTO_UNITARIO_DIGITADO_X10", "custo_unitario",
                    "Valorização/Exatidão", c, base.at[i, "custo_unitario"]))
    # E3 - item obsoleto (giro > 540 dias, coleção descontinuada, não derretível) sem provisão
    m3 = pa_mask & (~base.passivel_derretimento) & (base.custo_unitario > 60)
    for i in escolher(m3, 300):
        base.at[i, "colecao_descontinuada"] = True
        d = int(rng.integers(541, 1000))
        base.at[i, "dias_sem_giro"] = d
        base.at[i, "data_ultima_saida"] = DATA_BASE - np.timedelta64(d, "D")
        base.at[i, "data_ultima_entrada"] = DATA_BASE - np.timedelta64(d + 30, "D")
        base.at[i, "provisao_correta_extra"] = -1.0   # marcador: provisão correta = 100% do custo
        log.append((base.at[i, "id_registro"], "E3_OBSOLETO_SEM_PROVISAO", "provisao_perda", "Valorização",
                    "100% do custo", 0.0))
    # E5 - corte: lote com entrada em jan/2026 incluído no estoque de 31/12/2025
    m5 = base.classe_estoque.isin(["MATERIA_PRIMA", "PRODUTO_ACABADO"]) & base.tipo_local.isin(
        ["FABRICA", "FILIAL_COMPRAS", "CENTRO_DISTRIBUICAO"])
    for i in escolher(m5, 80):
        d = int(rng.integers(2, 20))
        base.at[i, "data_ultima_entrada"] = np.datetime64("2026-01-01") + np.timedelta64(d, "D")
        base.at[i, "dias_sem_giro"] = 0
        base.at[i, "data_ultima_saida"] = pd.NaT
        base.at[i, "qtd_fisica_sim"] = 0.0
        log.append((base.at[i, "id_registro"], "E5_CORTE_ENTRADA_POSTERIOR_A_DATA_BASE", "data_ultima_entrada",
                    "Corte/Existência", "não pertence a 31/12/2025", str(base.at[i, "data_ultima_entrada"])[:10]))
    # E8 - quantidade negativa (saída sem entrada)
    for i in escolher(pa_mask & loja_mask, 30):
        q = base.at[i, "quantidade"]
        base.at[i, "quantidade"] = -q
        base.at[i, "qtd_fisica_sim"] = 0.0
        log.append((base.at[i, "id_registro"], "E8_QUANTIDADE_NEGATIVA", "quantidade", "Exatidão/Integridade", 0, -q))
    # E9 - classificação: matéria-prima registrada em loja
    for i in escolher(base.classe_estoque == "MATERIA_PRIMA", 25):
        j = int(rng.integers(0, N_VIVARA))
        base.at[i, "cod_local"], base.at[i, "tipo_local"], base.at[i, "entidade"] = LOCAIS[j][0], LOCAIS[j][1], LOCAIS[j][2]
        log.append((base.at[i, "id_registro"], "E9_CLASSIFICACAO_LOCAL_INCOMPATIVEL", "cod_local",
                    "Classificação/Apresentação", "FAB-MAO ou FIL-SP", base.at[i, "cod_local"]))
    # E7 - valor contábil sem suporte (difere de qtd x custo)
    for i in escolher(pa_mask & (base.custo_unitario > 300), 50):
        v = base.at[i, "quantidade"] * base.at[i, "custo_unitario"]
        base.at[i, "valor_override"] = round(v + float(rng.integers(2_000, 18_000)), 2)
        log.append((base.at[i, "id_registro"], "E7_VALOR_DIFERENTE_DE_QTDxCUSTO", "valor_contabil",
                    "Exatidão", round(v, 2), base.at[i, "valor_override"]))
    # E6 - custo acima do valor realizável líquido sem provisão (preço de venda rebaixado)
    e6 = escolher(pa_mask & (base.custo_unitario > 200) & (~base.colecao_descontinuada), 120)

    # ---------------------------------------------------------------- 4. CALIBRAÇÃO AO SALDO CONTÁBIL
    base["valor_contabil"] = np.round(base["quantidade"] * base["custo_unitario"], 2)
    m7 = base["valor_override"].notna()
    base.loc[m7, "valor_contabil"] = base.loc[m7, "valor_override"]
    erro_idx = set(usados)
    limpos = ~base.index.isin(list(erro_idx))
    alvo_bruto = dict(ALVO)
    alvo_bruto["PRODUTO_ACABADO"] += PROVISAO_ALVO       # premissa: composição da nota 7.2 é líquida da provisão
    for cl, alvo in alvo_bruto.items():
        mc = base.classe_estoque == cl
        fixo = base.loc[mc & ~limpos, "valor_contabil"].sum()
        var = base.loc[mc & limpos, "valor_contabil"].sum()
        f = (alvo - fixo) / var
        base.loc[mc & limpos, "custo_unitario"] = np.round(base.loc[mc & limpos, "custo_unitario"] * f, 2)
        base.loc[mc & limpos, "custo_documental_sim"] = base.loc[mc & limpos, "custo_unitario"]
        base.loc[mc & limpos, "valor_contabil"] = np.round(base.loc[mc & limpos, "quantidade"] *
                                                           base.loc[mc & limpos, "custo_unitario"], 2)
        # resíduo de centavos: ajusta custo de um item limpo com quantidade 1
        res = round(alvo - base.loc[mc, "valor_contabil"].sum(), 2)
        cand_k = base.index[mc & limpos & (base.quantidade == 1)]
        if len(cand_k) == 0:   # sem item unitário: converte o lote de menor quantidade em 1 unidade (kit/lote fechado)
            sub = base.loc[mc & limpos & (base.unidade == "UN")]
            k = sub.quantidade.idxmin()
            base.at[k, "custo_unitario"] = base.at[k, "valor_contabil"]
            base.at[k, "quantidade"] = 1.0
            base.at[k, "qtd_fisica_sim"] = 1.0
        else:
            k = cand_k[0]
        base.at[k, "custo_unitario"] = round(base.at[k, "custo_unitario"] + res, 2)
        base.at[k, "custo_documental_sim"] = base.at[k, "custo_unitario"]
        base.at[k, "valor_contabil"] = base.at[k, "custo_unitario"]
        assert abs(base.loc[mc, "valor_contabil"].sum() - alvo) < 0.005, cl

    # Preço de venda sintético e VRL
    mk = base["categoria"].map(MARKUP).fillna(1.0)
    base["preco_venda_unitario"] = np.where(base.classe_estoque.isin(["PRODUTO_ACABADO", "EM_TRANSITO"]),
                                            np.round(base["custo_documental_sim"] * mk * rng.normal(1, .05, n), 2), np.nan)
    for i in e6:
        c = base.at[i, "custo_unitario"]
        base.at[i, "preco_venda_unitario"] = round(c * float(rng.uniform(0.55, 0.9)), 2)
        vrl = round(base.at[i, "preco_venda_unitario"] * (1 - P.DESPESA_VENDA_VRL), 2)   # premissa sintética
        falta = round((c - vrl) * base.at[i, "quantidade"], 2)
        base.at[i, "provisao_correta_extra"] = falta
        log.append((base.at[i, "id_registro"], "E6_CUSTO_ACIMA_DO_VRL_SEM_PROVISAO", "provisao_perda", "Valorização",
                    falta, 0.0))

    # ---------------------------------------------------------------- 5. PROVISÃO REGISTRADA (R$ 4.688 mil)
    base["provisao_perda"] = 0.0
    # Política (nota 7.3): (a) produto acabado não derretível com giro > 12 meses -> provisão pelo custo;
    # (b) joias derretíveis de coleções descontinuadas -> perda estimada no derretimento (8%, premissa sintética).
    elegivel = pa_mask & limpos & (base.quantidade > 0) & (base.valor_contabil < 60000)
    cand = base.index[elegivel].to_numpy().copy()
    rng.shuffle(cand)
    acum = 0.0
    for i in cand:
        v = base.at[i, "valor_contabil"]
        if base.at[i, "passivel_derretimento"]:
            p = round(v * P.PERDA_DERRETIMENTO, 2)
            base.at[i, "colecao_descontinuada"] = True
        else:
            p = v
            d = int(rng.integers(366, 900))
            base.at[i, "dias_sem_giro"] = d
            base.at[i, "data_ultima_saida"] = DATA_BASE - np.timedelta64(d, "D")
            base.at[i, "data_ultima_entrada"] = DATA_BASE - np.timedelta64(d + int(rng.integers(0, 120)), "D")
        if acum + p >= PROVISAO_ALVO:
            # fechamento exato: usa um item derretível cuja perda (>= 8% do custo) absorve o resíduo
            if not base.at[i, "passivel_derretimento"]:
                base.at[i, "dias_sem_giro"] = int(rng.integers(30, 300))
                base.at[i, "data_ultima_saida"] = DATA_BASE - np.timedelta64(int(base.at[i, "dias_sem_giro"]), "D")
            else:
                base.at[i, "colecao_descontinuada"] = False
            rem = round(PROVISAO_ALVO - acum, 2)
            ok = base.index[elegivel & base.passivel_derretimento & (base.provisao_perda == 0) &
                            (base.valor_contabil * P.PERDA_DERRETIMENTO <= rem) & (base.valor_contabil >= rem)]
            j = ok[0]
            base.at[j, "colecao_descontinuada"] = True
            base.at[j, "provisao_perda"] = rem
            acum += rem
            break
        base.at[i, "provisao_perda"] = p
        acum += p
    assert abs(acum - PROVISAO_ALVO) < 0.01
    base["valor_liquido"] = np.round(base["valor_contabil"] - base["provisao_perda"], 2)

    # Conta contábil sintética
    conta = {"PRODUTO_ACABADO": "1.1.04.01", "MATERIA_PRIMA": "1.1.04.02", "MAT_CONSUMO_EMBALAGEM": "1.1.04.03",
             "EM_TRANSITO": "1.1.04.05"}
    base["conta_contabil_sintetica"] = base["classe_estoque"].map(conta)
    base["dado_sintetico"] = "SIM - REGISTRO FICTICIO PARA FINS DIDATICOS"
    base["data_base"] = "2025-12-31"
    base["ggf_alocado"] = np.where(base.origem == "FABRICACAO_PROPRIA_MANAUS",
                                   np.round(base["valor_contabil"] * 0.07, 2), 0.0)  # informativo (sintético)

    # ---------------------------------------------------------------- 7. DUPLICIDADES (E4) após calibração
    # Inserimos duplicidades e retiramos o mesmo valor de itens limpos (mantendo a conciliação)
    dup_idx = rng.choice(base.index[pa_mask & limpos & (base.provisao_perda == 0) & (base.quantidade > 0)], 60, replace=False)
    dups = base.loc[dup_idx].copy()
    dups["id_registro"] = [f"SIM-EST-{n + i + 1:07d}" for i in range(len(dups))]
    dups["qtd_fisica_sim"] = 0.0
    valor_dup = dups["valor_contabil"].sum()
    for _, r in dups.iterrows():
        log.append((r["id_registro"], "E4_REGISTRO_DUPLICADO", "linha inteira", "Existência", 0.0, r["valor_contabil"]))
    # compensação: reduz proporcionalmente custos de itens limpos de PA de baixo valor (não duplicados)
    comp = pa_mask & limpos & (base.provisao_perda == 0) & ~base.index.isin(dup_idx) & (base.quantidade == 1)
    comp_idx = base.index[comp][:20000]
    f = 1 - valor_dup / base.loc[comp_idx, "valor_contabil"].sum()
    base.loc[comp_idx, "custo_unitario"] = np.round(base.loc[comp_idx, "custo_unitario"] * f, 2)
    base.loc[comp_idx, "custo_documental_sim"] = base.loc[comp_idx, "custo_unitario"]
    base.loc[comp_idx, "valor_contabil"] = base.loc[comp_idx, "custo_unitario"]
    base.loc[comp_idx, "valor_liquido"] = base.loc[comp_idx, "valor_contabil"]
    base = pd.concat([base, dups], ignore_index=True)
    res = round(ALVO["PRODUTO_ACABADO"] - base.loc[base.classe_estoque == "PRODUTO_ACABADO", "valor_liquido"].sum(), 2)
    k = comp_idx[-1]
    base.at[k, "custo_unitario"] += res; base.at[k, "custo_documental_sim"] += res
    base.at[k, "valor_contabil"] += res; base.at[k, "valor_liquido"] += res
    base["custo_unitario"] = base["custo_unitario"].round(2)

    # ---------------------------------------------------------------- 6. LUCRO NÃO REALIZADO (consolidação)
    pa_mask = base.classe_estoque == "PRODUTO_ACABADO"
    m_lnr = pa_mask & (base.origem == "FABRICACAO_PROPRIA_MANAUS") & (base.entidade == "TELLERINA") & (base.quantidade > 0)
    base_lnr = base.loc[m_lnr, "valor_contabil"].sum()
    margem = LNR_ALVO / base_lnr
    base["margem_intragrupo"] = np.where(m_lnr, round(margem, 6), 0.0)
    base["custo_transferencia_unitario"] = np.where(m_lnr, np.round(base["custo_unitario"] * (1 + margem), 2),
                                                    base["custo_unitario"])
    base["lucro_nao_realizado_eliminado"] = np.where(m_lnr, np.round(base["valor_contabil"] * margem, 2), 0.0)
    res = round(LNR_ALVO - base["lucro_nao_realizado_eliminado"].sum(), 2)
    k = base.index[m_lnr][0]
    base.at[k, "lucro_nao_realizado_eliminado"] += res

    # ---------------------------------------------------------------- 8. GABARITO DE VALORES CORRETOS
    logdf = pd.DataFrame(log, columns=["id_registro", "tipo_erro", "campo_afetado", "afirmacao", "valor_correto",
                                       "valor_registrado"])
    b = base.set_index("id_registro")
    # valor correto por registro = qtd_fisica x custo documental - provisão correta
    correto = np.round(b["qtd_fisica_sim"].clip(lower=0) * b["custo_documental_sim"], 2)
    prov_corr = b["provisao_perda"].copy()
    m3c = b["provisao_correta_extra"] == -1.0
    prov_corr[m3c] = correto[m3c]
    m6c = b["provisao_correta_extra"] > 0
    prov_corr[m6c] = prov_corr[m6c] + b.loc[m6c, "provisao_correta_extra"]
    liquido_correto = (correto - prov_corr).round(2)
    efeito = (b["valor_liquido"] - liquido_correto).round(2)
    logdf["efeito_superavaliacao_RS"] = logdf["id_registro"].map(efeito)
    logdf["classe_estoque"] = logdf["id_registro"].map(b["classe_estoque"])
    logdf.to_csv(os.path.join(OUT, "registro_erros_inseridos.csv"), index=False, sep=";", decimal=",")

    # arquivo de "verdade simulada" (só consultado para itens selecionados - simula contagem e vouching)
    verdade = base[["id_registro", "qtd_fisica_sim", "custo_documental_sim"]].rename(
        columns={"qtd_fisica_sim": "quantidade_contada_simulada", "custo_documental_sim": "custo_unitario_documental_simulado"})
    verdade.to_csv(os.path.join(OUT, "contagem_fisica_e_custo_documental_SIMULADOS.csv"), index=False, sep=";", decimal=",")

    cols = ["id_registro", "dado_sintetico", "data_base", "entidade", "cod_local", "tipo_local", "classe_estoque",
            "conta_contabil_sintetica", "categoria", "subcategoria", "cod_sku", "lote", "origem", "unidade",
            "quantidade", "custo_unitario", "valor_contabil", "provisao_perda", "valor_liquido", "ggf_alocado",
            "custo_transferencia_unitario", "margem_intragrupo", "lucro_nao_realizado_eliminado",
            "preco_venda_unitario", "colecao_descontinuada", "passivel_derretimento", "data_ultima_entrada",
            "data_ultima_saida", "dias_sem_giro", "data_ultimo_inventario_interno"]
    base = base[cols]
    base["colecao_descontinuada"] = np.where(base.colecao_descontinuada.astype(bool), "S", "N")
    base["passivel_derretimento"] = np.where(base.passivel_derretimento.astype(bool), "S", "N")
    base.to_csv(os.path.join(OUT, "base_estoques_sintetica_31122025.csv"), index=False, sep=";", decimal=",",
                date_format="%Y-%m-%d")

    resumo = {"semente": SEED, "linhas": int(len(base)),
              "total_valor_liquido": round(float(base.valor_liquido.sum()), 2),
              "por_classe_liquido": {k: round(float(v), 2) for k, v in base.groupby("classe_estoque").valor_liquido.sum().items()},
              "provisao_total": round(float(base.provisao_perda.sum()), 2),
              "lucro_nao_realizado_total": round(float(base.lucro_nao_realizado_eliminado.sum()), 2),
              "margem_intragrupo_calibrada": round(float(margem), 6),
              "erros_inseridos": logdf.groupby("tipo_erro").agg(qtd=("id_registro", "count"),
                                                                 efeito=("efeito_superavaliacao_RS", "sum")).round(2).reset_index().to_dict("records"),
              "efeito_total_erros": round(float(logdf.efeito_superavaliacao_RS.sum()), 2)}
    json.dump(resumo, open(os.path.join(OUT, "resumo_geracao.json"), "w"), ensure_ascii=False, indent=2)
    print(json.dumps(resumo, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
