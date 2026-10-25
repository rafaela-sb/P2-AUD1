# -*- coding: utf-8 -*-
"""Programas por ciclo, base simulada, conclusão integrada, matriz de cobertura, fontes e identificação."""
import json, os
from dossie_util import tabela, n0, n2, pct, CALC, TST

MG, ME = CALC["PT320"]["MG"], CALC["PT320"]["ME"]
RESUMO = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "02_base_simulada", "resumo_geracao.json"), encoding="utf-8"))
MUS = TST["mus"]

# ------------------------------------------------------------------------------------------- Identificação
IDENT = tabela(["Item", "Informação", "Fonte"], [
    ["Companhia atribuída (matrícula 241003384)", "Vivara Participações S.A.", "Instruções P2"],
    ["Nome empresarial atual", "Vivara Participações S.A. - desde 15/06/2019", "FCA p.2"],
    ["Nome empresarial anterior", "L.I.R.S.P.E. Empreendimentos e Participações Ltda. (constituída em 23/05/2019 como sociedade limitada; "
     "transformada em S.A. na reorganização de 15/06/2019)", "FCA p.2; FRE p.17"],
    ["Nomes históricos do negócio", "'Confecção de Joias Vivara' (1977) refere-se à operação original, hoje nas controladas; Conipa constituída "
     "em 31/08/2016 por cisão parcial da Tellerina", "FRE p.17"],
    ["Nome de pregão", "VIVARA S.A. (segmento Novo Mercado - 'VIVA-NM')", "B3 p.2"],
    ["Código de negociação", "VIVA3 (ações ordinárias). 'Outros códigos de negociação': nenhum. Início de negociação: 10/10/2019 (IPO). "
     "Nenhuma alteração de código identificada", "B3 p.2; FCA p.4; FRE p.17"],
    ["CNPJ / Código CVM", "33.839.910/0001-11 / 2480-5 (registro em 08/10/2019, categoria A)", "FCA p.2"],
    ["Auditor do exercício 2025", "KPMG Auditores Independentes Ltda. (CVM 418-9); relatório de 18/03/2026 sem modificação", "FCA p.5; DF25 p.15-18"],
    ["Exercício examinado", "01/01/2025 a 31/12/2025, com comparativos de 2024", "DF25 p.19"],
], larg=[24, 58, 18])

# ------------------------------------------------------------------------------------------- Programas
def prog(cod, titulo, riscos, linhas):
    return {"cod": cod, "titulo": titulo, "riscos": riscos,
            "tabela": tabela(["#", "Afirmação", "Procedimento", "Classificação", "Referência"], linhas, larg=[5, 14, 55, 11, 15])}


PROGS = [
    prog("PROG-01", "Receitas (R$ 3.026.582 mil)", "R01, R02, R14", [
        ["1", "Ocorrência", "Analítico de receita das lojas físicas com SSS e expansão de lojas", "[R]", "PT 520"],
        ["2", "Exatidão", "Conciliar composição da receita (nota 21.2) e categorias/canais (nota 23)", "[R]", "PT 500"],
        ["3", "Ocorrência", "Conciliar vendas do Capta com recebimentos dos adquirentes e com o SAP (amostra mensal)", "[P]", "PT 402"],
        ["4", "Corte", "Testar vendas dos últimos/primeiros 10 dias do exercício (entrega do e-commerce; devoluções de jan/2026)", "[P]", "PT 240"],
        ["5", "Exatidão", "Recalcular provisão do Giftback (taxa histórica de resgate e expiração)", "[P]", "PT 540"],
        ["6", "Ocorrência", "Conciliar receita de subvenção de ICMS com apurações estaduais e atos concessivos", "[P]", "PT 250"],
        ["7", "Apresentação", "Avaliar divulgação de receita por categoria/canal e segmento único", "[R]", "PT 501"]]),
    prog("PROG-02", "Disponibilidades (R$ 398.644 mil)", "R10, R11", [
        ["1", "Exatidão", "Conciliar nota 5 com BP e DFC (caixa inicial + variação = final)", "[R]", "PT 500"],
        ["2", "Existência", "Confirmar saldos bancários e aplicações (compromissadas R$ 333.013 mil; letras financeiras R$ 33.212 mil)", "[P]", "PT 505"],
        ["3", "Existência", "Inspecionar conciliações bancárias de dezembro/2025 e itens pendentes", "[P]", "-"],
        ["4", "Classificação", "Avaliar classificação como equivalente de caixa (liquidez diária, risco insignificante)", "[R]", "Nota 5.1 p.28"],
        ["5", "Apresentação", "Avaliar efeito da antecipação de recebíveis de 26/12/2025 na DFC (operacional)", "[R]", "PT 570"]]),
    prog("PROG-03", "Estoques (R$ 1.478.926 mil)", "R03, R04, R05", [
        ["1", "Exatidão", "Conciliar composição (nota 7.2), provisão (7.3) e base do IR diferido (20.9)", "[R]", "PT 500"],
        ["2", "Existência", "Acompanhar inventários em lojas, CDs e fábrica; contagens-teste nos dois sentidos", "[P]", "PT 501"],
        ["3", "Existência/Exatidão", "MUS com contagem e vouching de custo", "[S]", "PT 530"],
        ["4", "Integridade", "Testes de 100%: recálculo, duplicidade, negativos, campos vazios", "[S]", "PT 530"],
        ["5", "Corte", "Entradas posteriores à data-base; mercadorias em trânsito", "[S]", "PT 530"],
        ["6", "Valorização", "Aging x política de provisão; custo x VRL; custo unitário atípico", "[S]", "PT 530; PT 540"],
        ["7", "Valorização", "Recalcular custo médio e alocação de GGF (R$ 68.145 mil em 2025)", "[P]", "PT 520"],
        ["8", "Valorização (consolidação)", "Recalcular lucro não realizado e IR diferido; conciliar variação da base com a eliminação", "[R]/[S]", "PT 600"],
        ["9", "Direitos", "Verificar estoques de terceiros/consignação e em poder de terceiros", "[P]", "PT 505"]]),
    prog("PROG-04", "Imobilizado e direito de uso (R$ 955.347 mil)", "R08, R15", [
        ["1", "Exatidão", "Conciliar movimentação (nota 10.6) e saldo do BP", "[R]", "PT 500"],
        ["2", "Exatidão", "Analítico de depreciação por classe com vida útil divulgada", "[R]", "PT 520"],
        ["3", "Existência", "Vouching de adições (R$ 252.011 mil, incluindo direito de uso) e inspeção física em lojas novas", "[P]", "-"],
        ["4", "Valorização", "Avaliar indicadores de impairment das lojas (UGC) e o teste da administração", "[P]", "Nota 10.5"],
        ["5", "Valorização", "Recalcular amostra de contratos de arrendamento; sensibilidade de taxa", "[P]/[R]", "PT 540"]]),
    prog("PROG-05", "Passivos (fornecedores, empréstimos, arrendamentos, provisões, tributos)", "R09, R11, R12", [
        ["1", "Exatidão", "Conciliar notas 12, 13, 14, 15, 16, 17 e 28 com o BP", "[R]", "PT 500"],
        ["2", "Completude", "Confirmar empréstimos, debêntures e swap; recalcular juros", "[P]/[R]", "PT 505; PT 520"],
        ["3", "Completude", "Busca de passivos não registrados: pagamentos de jan-fev/2026 e notas fiscais", "[P]", "-"],
        ["4", "Classificação", "Fornecedores convênio: avaliar natureza operacional x financeira (CPC 03)", "[R]", "Nota 12.2 p.38"],
        ["5", "Completude/Avaliação", "Cartas a advogados; conciliação nota 17 x FRE 4.4; análise de passivos possíveis", "[P]/[R]", "PT 501"],
        ["6", "Exatidão", "Recalcular dividendo mínimo e destinação do lucro", "[R]", "PT 500"]]),
    prog("PROG-06", "Estimativas contábeis", "R04, R06, R07, R08, R09", [
        ["1", "Valorização", "Passivo de arrendamento: método, taxa e sensibilidade", "[R]", "PT 540"],
        ["2", "Valorização", "Provisão de estoques: revisão retrospectiva com ITR 2026 e cenários", "[R]", "PT 540"],
        ["3", "Valorização", "IR diferido ativo: projeções de lucro tributável e realização (nota 20.6)", "[P]", "PT 315"],
        ["4", "Ocorrência/Valorização", "Créditos extemporâneos PIS/COFINS: pareceres e recálculo com especialista", "[P]", "PT 250"],
        ["5", "Valorização", "Provisões para riscos: prognósticos de advogados", "[P]", "PT 501"],
        ["6", "Valorização", "Derivativos (swap nível 2): recalcular MTM com curvas de mercado", "[P]", "Nota 29.6"],
        ["7", "Viés", "Avaliar indicadores de viés da administração no conjunto das estimativas", "[R]", "PT 540"]]),
]

# ------------------------------------------------------------------------------------------- Base simulada
DIC = [
    ["id_registro", "texto", "Identificador único do registro sintético (SIM-EST-nnnnnnn)", "Sintético"],
    ["dado_sintetico", "texto", "Marca obrigatória: 'SIM - REGISTRO FICTICIO PARA FINS DIDATICOS'", "Sintético"],
    ["data_base", "data", "31/12/2025", "Público (data das DF)"],
    ["entidade", "texto", "TELLERINA, CONIPA ou TELLERINA_PANAMA", "Estrutura pública (nota 1); alocação sintética"],
    ["cod_local / tipo_local", "texto", "Código e tipo do local: LOJA_VIVARA (267), LOJA_LIFE (219), QUIOSQUE (11), LOJA_PANAMA (1), "
     "CENTRO_DISTRIBUICAO (3), FABRICA, FILIAL_COMPRAS, EM_TRANSITO", "Quantidades públicas (nota 1; FRE p.28); códigos sintéticos"],
    ["classe_estoque", "texto", "PRODUTO_ACABADO, MATERIA_PRIMA, MAT_CONSUMO_EMBALAGEM, EM_TRANSITO", "Público (nota 7.2)"],
    ["conta_contabil_sintetica", "texto", "1.1.04.01 a 1.1.04.05", "Sintético"],
    ["categoria / subcategoria", "texto", "JOIAS, LIFE, RELOGIOS, ACESSORIOS; OURO, PRATA, DIAMANTES etc.", "Categorias públicas (nota 23); subcategorias sintéticas"],
    ["cod_sku / lote", "texto", "Código do item e do lote", "Sintético"],
    ["origem", "texto", "FABRICACAO_PROPRIA_MANAUS, REVENDA_IMPORTADA, REVENDA_NACIONAL, COMPRA_NACIONAL, COMPRA_IMPORTADA, TRANSFERENCIA_INTERNA",
     "Proporção de produção própria pública (DF25 p.3); demais sintéticas"],
    ["unidade", "texto", "UN, G (gramas), CT (quilates)", "Sintético"],
    ["quantidade", "número", "Quantidade registrada", "Sintético"],
    ["custo_unitario", "R$", "Custo médio ponderado unitário (consolidado)", "Sintético, calibrado ao saldo"],
    ["valor_contabil", "R$", "Valor bruto registrado (= quantidade x custo, salvo erro inserido E7)", "Sintético"],
    ["provisao_perda", "R$", "Provisão para perdas (giro lento/derretimento)", "Total = R$ 4.688.000 (nota 7.3)"],
    ["valor_liquido", "R$", "valor_contabil - provisao_perda", "Total = R$ 1.478.926.000 (BP)"],
    ["ggf_alocado", "R$", "Parcela informativa de GGF (7% do valor de itens fabricados)", "Sintético"],
    ["custo_transferencia_unitario", "R$", "Custo na Tellerina a preço de transferência intragrupo", "Sintético"],
    ["margem_intragrupo", "número", f"Margem calibrada para o LNR ({str(RESUMO['margem_intragrupo_calibrada']).replace('.', ',')})", "Calibrada a dado público"],
    ["lucro_nao_realizado_eliminado", "R$", "LNR eliminado na consolidação", "Total = R$ 1.293.806.000 (nota 20.9)"],
    ["preco_venda_unitario", "R$", "Preço de venda (para teste de VRL)", "Sintético"],
    ["colecao_descontinuada / passivel_derretimento", "S/N", "Atributos para a política de provisão", "Política pública (nota 7.3); atribuição sintética"],
    ["data_ultima_entrada / data_ultima_saida / dias_sem_giro", "data / número", "Movimentação e aging", "Sintético"],
    ["data_ultimo_inventario_interno", "data", "Última contagem interna", "Sintético (frequências do FRE p.137-138)"],
]
gen = TST["comparacao"]
BASE_SEC = {
    "justificativa": f"<p><b>Conta escolhida: Estoques consolidados</b> - R$ 1.478.926 mil em 31/12/2025, o maior saldo do ativo "
                     f"consolidado (31,3% do ativo total de R$ 4.722.692 mil), à frente de contas a receber (21,0%) e imobilizado "
                     f"(20,2%) (DF25 p.19). O saldo equivale a {str(round(1478926/MG,1)).replace('.',',')} vezes a materialidade global, "
                     "cresceu 11,0% no ano e corresponde a 537 dias de estoque ex-GGF (DF25 p.3). No balanço individual o maior ativo "
                     "é o investimento em controladas (R$ 3.230.468 mil), eliminado na consolidação; por isso a escolha considera as DF "
                     "consolidadas, que representam a realidade econômica do grupo.</p>",
    "premissas": "<ul><li>Unidade de registro: posição de estoque por SKU e local (produtos acabados - rastreados por código de barras "
                 "individual, FRE p.137) e lote (matérias-primas, embalagens, trânsito). Nenhuma linha é cópia de outra, exceto as 60 "
                 "duplicidades inseridas propositalmente como erro E4.</li>"
                 "<li>Totais por classe, provisão e lucro não realizado reproduzem exatamente as notas 7.2, 7.3 e 20.9. Premissa: a "
                 "composição da nota 7.2 é líquida da provisão (a nota não apresenta linha de provisão).</li>"
                 "<li>Locais: quantidades de lojas da nota 1; 3 CDs (FRE p.28); fábrica em Manaus e filial de compras em SP (notas 1 e 8.2).</li>"
                 "<li>Fração de produção própria por categoria a partir do relatório da administração (86,2% Vivara; 58,3% Life); "
                 "relógios (40%) e acessórios (0%) são premissas sintéticas.</li>"
                 "<li>Custos, quantidades, preços, datas, giro e atributos de coleção são sintéticos (distribuições lognormal, Poisson, "
                 "binomial negativa e exponencial) e calibrados apenas para reproduzir os saldos. A distribuição por categoria resultante "
                 "não é divulgada pela companhia e não deve ser lida como informação real.</li>"
                 "<li>Política de provisão aplicada aos dados limpos: 100% do custo para itens não derretíveis com giro > 365 dias; 8% "
                 "(perda de derretimento, sintético) para derretíveis de coleção descontinuada.</li>"
                 "<li>Semente fixa 241003384: reexecutar o código gera a mesma base.</li></ul>",
    "metodo": "<ol><li>Catálogo sintético de 25.000 SKUs; posições por local; matérias-primas e embalagens por lote.</li>"
              "<li>Pré-calibração do custo por classe; inserção de erros controlados com registro (gabarito).</li>"
              "<li>Calibração final dos itens sem erro para fechar cada classe ao centavo; provisão atribuída até R$ 4.688.000,00.</li>"
              "<li>Inserção de duplicidades com compensação em itens limpos (mantém a conciliação).</li>"
              "<li>Cálculo do lucro não realizado por item (margem intragrupo calibrada) até R$ 1.293.806.000,00.</li>"
              "<li>Exportação: base (CSV, separador ';', decimal ','), registro de erros e arquivo de 'verdade simulada' para "
              "contagem/vouching, consultado apenas para itens selecionados.</li></ol>",
    "erros": tabela(["Erro inserido", "Natureza", "Qtd.", "Efeito (R$ mil)", "Teste que deveria detectar"],
                    [[c["tipo_erro"], {"E1": "Valorização/exatidão", "E2": "Existência", "E3": "Valorização", "E4": "Existência",
                                       "E5": "Corte", "E6": "Valorização (VRL)", "E7": "Exatidão", "E8": "Integridade",
                                       "E9": "Classificação"}[c["tipo_erro"][:2]], c["inseridos"], n2(c["efeito_inserido_RS"] / 1000),
                      {"E1": "T7 (e T6)", "E2": "Contagem (MUS)", "E3": "T5", "E4": "T2", "E5": "T4", "E6": "T6", "E7": "T1",
                       "E8": "T3", "E9": "T8"}[c["tipo_erro"][:2]]] for c in gen], larg=[36, 18, 8, 14, 24]),
    "dicionario": tabela(["Variável", "Tipo", "Descrição", "Origem"], DIC, cls="t small", larg=[24, 9, 45, 22]),
}

# ------------------------------------------------------------------------------------------- Conclusão
CONC = f"""
<p>Este dossiê é um exercício acadêmico e <b>não constitui opinião profissional independente</b> sobre as demonstrações contábeis
da Vivara Participações S.A.</p>
<p><b>Riscos.</b> Seis riscos significativos (PT 315): receita (R01), burla de controles (R02), existência (R03) e valorização (R04)
de estoques, eliminação do lucro não realizado na consolidação (R05) e créditos tributários extemporâneos (R06).</p>
<p><b>Procedimentos e evidências.</b> Com evidência pública: materialidade, conciliações, saldos iniciais, analíticos,
sensibilidade de estimativas, liquidez, eventos subsequentes e mapeamentos de partes relacionadas, leis, prestadores e componentes.
Os saldos primários são consistentes com as notas; as inconsistências encontradas são de divulgação (PT 450); não há indício de
incerteza sobre continuidade (PT 570) nem evento subsequente que exija ajuste (PT 560). Na base simulada, as distorções estimadas
(R$ {n2((TST['distorcao_conhecida_testes_100pct_RS'] + MUS['distorcao_projetada_RS'])/1000)} mil) ficaram abaixo da materialidade
global (PT 450 e PT 530).</p>
<p><b>Limitações.</b> Sem acesso a registros, contratos, sistemas, pessoas e locais; confirmações, entrevistas, inspeções físicas,
testes de controles e teste de lançamentos permanecem planejados. Os dados simulados não representam a companhia.</p>
<p><b>Conclusão.</b> Com as evidências públicas disponíveis, não se identificou indício de distorção relevante nos saldos de 2025.
Essa constatação tem alcance limitado e <b>não equivale a segurança razoável</b>, pois os riscos significativos dependem dos
procedimentos planejados.</p>
"""

# ------------------------------------------------------------------------------------------- Matriz de cobertura
MATRIZ = [
    ["NBC TA Estrutura Conceitual", "PT EC", "Itens 10-15, 19, 22, 26-44", "PT 210, PT CONC"],
    ["NBC TA 200 (R1)", "PT 200", "11, 13-17, A20-A49", "Todos"],
    ["NBC TA 210 (R1)", "PT 210", "6-10, 13, A23", "PT EC, PT 580"],
    ["NBC TA 220 (R3)", "PT 220", "13-17, 25-37", "PT 230, PT 300"],
    ["NBC TA 230 (R1)", "PT 230", "7-9, 14-16, A21-A23", "Estrutura do repositório"],
    ["NBC TA 240 (R1)", "PT 240", "11, 15-17, 24-33", "PT 315 (R01, R02), PT 330, PT 540"],
    ["NBC TA 250", "PT 250", "13-23", "PT 501, PT 260"],
    ["NBC TA 260 (R2)", "PT 260", "11, 13-19, 21, A29", "PT 265, PT 450"],
    ["NBC TA 265", "PT 265", "6-11, A5-A7", "PT 450, PT 260"],
    ["NBC TA 300 (R1)", "PT 300", "5-13", "PROG-01 a 06"],
    ["NBC TA 315 (R2)", "PT 315", "13-32", "PT 240, PT 330"],
    ["NBC TA 320 (R1)", "PT 320", "10-14, A3-A13", "PT 450, PT 530, PT 600"],
    ["NBC TA 330 (R1)", "PT 330", "5-8, 18-26", "PROG-01 a 06"],
    ["NBC TA 402", "PT 402", "9-16", "PT 505"],
    ["NBC TA 450 (R1)", "PT 450", "5-12", "PT 530, PT 260, PT 580"],
    ["NBC TA 500 (R1)", "PT 500", "6-11, A26-A33", "Todos"],
    ["NBC TA 501", "PT 501", "4-13", "PT 530, PT 505"],
    ["NBC TA 505", "PT 505", "7-16", "PT 402, PT 501"],
    ["NBC TA 510 (R1)", "PT 510", "5-9", "PT 300"],
    ["NBC TA 520", "PT 520", "5-7, A4-A16", "PT 315, PT 540"],
    ["NBC TA 530", "PT 530 + Base simulada", "6-15, A10-A23", "PT 450, PT 500"],
    ["NBC TA 540 (R2)", "PT 540", "13-32", "PT 240, PROG-06"],
    ["NBC TA 550", "PT 550", "11-25", "PT 580"],
    ["NBC TA 560 (R1)", "PT 560", "5-10, 14-15", "PT 570, PT 580"],
    ["NBC TA 570", "PT 570", "10-18", "PT 560"],
    ["NBC TA 580 (R1)", "PT 580", "4, 9-20", "PT 210"],
    ["NBC TA 600 (R2)", "PT 600", "11-45", "PT 320, PT 530"],
]

# ------------------------------------------------------------------------------------------- Fontes
MZ = "https://api.mziq.com/mzfilemanager/v2/d/61a4df2d-a461-44d6-9128-da74058019db/"
FONTES = [
    ["DF25", "Demonstrações financeiras individuais e consolidadas 2025 (versão RI, com relatório do auditor)", "2025 (comp. 2024)",
     MZ + "16b7bfcb-6e5f-48d9-5a73-9302caef63a9?origin=2", "21/10/2026 12:15", "p.2-68"],
    ["DFP24", "DFP 31/12/2024 - formulário CVM (com relatório do auditor e nota 3)", "2024 (comp. 2023)",
     MZ + "4f58b50f-3ba9-e3f2-2f32-9e30d751466c?origin=2", "21/10/2026 16:58", "p.14-20, 30, 43, 59-60, 101-104"],
    ["FRE", "Formulário de Referência 2026 - versão 6 (CVM)", "2025/2026",
     "https://www.rad.cvm.gov.br/ENETWEB/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=161775&CodigoTipoInstituicao=1",
     "21/10/2026 16:45", "p.17, 26, 28, 33, 39, 50, 94-97, 113-116, 127-164, 179-193, 239-244, 258-263"],
    ["ITR1", "ITR 31/03/2026 (com relatório de revisão)", "1T26", MZ + "c68d2a78-1699-a728-f91c-e06357853bae?origin=2",
     "21/10/2026 16:51", "p.3-6, 14, 47"],
    ["ITR2", "ITR 30/06/2026 (com relatório de revisão)", "2T26", MZ + "0ef9b209-fd78-4a0a-073a-3560e1d38766?origin=2",
     "22/10/2026 09:41", "p.3-6, 14"],
    ["FRR", "Fato relevante - Aprovação de programa de recompra (06/05/2026)", "2026",
     MZ + "4ec6743c-18fc-8ec7-9090-2c4b7ba6dd3f?origin=2 (*)", "22/10/2026 09:47", "p.1-2"],
    ["FRG", "Fato relevante - Guidance de abertura de lojas para 2026 (18/03/2026)", "2026",
     MZ + "b796f175-b7c1-6746-fb25-1742ab5f1247?origin=2 (*)", "22/10/2026 09:47", "p.1"],
    ["AGO", "Manual para participação e proposta da administração - AGO/E de 27/04/2026", "2025",
     MZ + "dd5880f9-e3e2-5105-ee6a-c81c3300beec?origin=2", "22/10/2026 09:48", "p.2-5, 14-15, 44, 51-56"],
    ["ATA", "Ata da AGO/E realizada em 27/04/2026", "2025", MZ + "cb9fb923-bbd6-4775-7e9a-b4fb101db415?origin=2",
     "22/10/2026 10:51", "p.1-4"],
    ["DEB2", "Aviso ao mercado - 2ª emissão de debêntures (13/10/2026)", "2026",
     "https://filemanager-cdn.mziq.com/published/61a4df2d-a461-44d6-9128-da74058019db/4ff30f96-81ce-4f79-bd22-071deb015218",
     "22/10/2026 10:52", "p.1-4"],
    ["FCA", "Formulário Cadastral 2026 - versão 1", "2026", MZ + "33df8f9f-6e7d-2d5c-09c6-176d8e3bf436?origin=2",
     "22/10/2026 09:53", "p.2-7"],
    ["B3", "B3 - Empresas listadas: Vivara (VIVA3) - página impressa em PDF", "2026",
     "https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas.htm", "22/10/2026 09:50", "p.2"],
    ["NORMAS", "Consolidado Normas Aud1 (compilação das NBC TA - disciplina)", "Vigentes para 2025",
     "https://unbbr.sharepoint.com/sites/AUD1_2026_2/Documentos%20Compartilhados/General/Consolidado%20Normas%20Aud1.pdf",
     "21/10/2026 11:49", "Páginas indicadas em cada PT"],
    ["CFC", "CFC - relação das NBC TA de auditoria independente (verificação de versões)", "-",
     "https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/", "22/10/2026", "-"],
    ["CFC27", "Revisão NBC 27 - minuta em audiência pública (vigência proposta: exercícios iniciados a partir de 01/01/2025)", "-",
     "https://www.gov.br/participamaisbrasil/revisaonbc27", "22/10/2026", "-"],
]
