# -*- coding: utf-8 -*-
"""Conteúdo dos papéis de trabalho: PT 300, 315, 320, 330, 402, 450."""
from dossie_util import tabela, n0, n1, n2, pct, CALC, TST, R, P, S
from distorcoes import PUBLICAS

MG, ME, TRIV = CALC["PT320"]["MG"], CALC["PT320"]["ME"], CALC["PT320"]["trivial"]
MUS = TST["mus"]
PTS = []

# =============================================================================================== PT 300
PTS.append({
    "cod": "PT 300", "titulo": "Planejamento: estratégia global, plano, cronograma e programas",
    "norma": "NBC TA 300 (R1) - Planejamento da Auditoria de Demonstrações Contábeis",
    "itens": [("300", ["5", "6", "7", "8", "9", "10", "11", "12", "13", "A8", "A20"])],
    "objetivo": "Elaborar estratégia global, plano de auditoria, cronograma e programas por ciclo; justificar prioridades e alterações.",
    "objeto": "Auditoria das DF individuais e consolidadas de 2025 (auditoria inicial didática).",
    "afirmacoes": "Todas; prioridades definidas pelos riscos significativos do PT 315.",
    "populacao": "PT 315 (riscos), PT 320 (materialidade), PT 600 (componentes), FRE 5.2 (calendário de inventários - FRE p.137-138).",
    "procedimentos": [
        ("Definir estratégia global (alcance, época, direção) - item 7.", R, "Quadro 1"),
        ("Elaborar plano de auditoria (natureza, época, extensão) - item 9.", R, "PT 330 e programas PROG-01 a PROG-06"),
        ("Elaborar cronograma (didático e de referência para auditoria real).", R, "Quadro 2"),
        ("Atividades preliminares de auditoria inicial: comunicação com o auditor antecessor e leitura das DF 2024 (item 13).", R,
         "PT 510 (leitura realizada; comunicação planejada)"),
        ("Registrar alterações relevantes no planejamento (item 10).", R, "Quadro 3"),
    ],
    "evidencias": "Ver quadros. Referências cruzadas: PT 315, PT 320, PT 330, PT 600, PROG-01 a PROG-06.",
    "anexo": "<h4>Quadro 1 - Estratégia global</h4>" + tabela(
        ["Elemento", "Definição"],
        [["Alcance", "DF individuais e consolidadas (CPC/IFRS); componentes: controladora, Tellerina, Conipa (significativos) e Tellerina Panamá (PT 600)"],
         ["Época", "Exercício encerrado em 31/12/2025; DF autorizadas em 18/03/2026 (DF25 p.26); corte de eventos subsequentes em 18/03/2026 (PT 560)"],
         ["Direção", "Prioridade aos riscos significativos R01-R06 (PT 315); abordagem predominantemente substantiva (risco de controle no máximo)"],
         ["Materialidade", f"MG R$ {n0(MG)} mil; ME R$ {n0(ME)} mil; trivial R$ {n0(TRIV)} mil (PT 320)"],
         ["Recursos", "Especialistas: tributário (subvenções/créditos), TI (Capta/SAP), avaliação de metais/gemas; uso de análise de dados (Python)"],
         ["Auditoria inicial", "Saldos de abertura a partir das DF 2024 auditadas pela KPMG (relatório sem modificação de 18/03/2025 - DFP24 p.101-103)"]],
        larg=[20, 80]) + "<h4>Quadro 2 - Cronograma</h4>" + tabela(
        ["Fase", "Referência (auditoria real)", "Este dossiê"],
        [["Aceitação, carta e comunicação com antecessor", "Set/2025", "22/10/2026 (PT 210, 510)"],
         ["Entendimento, riscos e materialidade", "Out-Nov/2025", "22/10/2026 (PT 315, 320)"],
         ["Testes de controles e procedimentos interinos", "Nov/2025 (com ITR 3T25)", "Planejados (PT 330)"],
         ["Acompanhamento de inventários físicos (lojas, CDs, fábrica)", "Dez/2025 - 31/12/2025", "Simulado (PT 501, 530)"],
         ["Procedimentos finais e confirmações", "Jan-Fev/2026", "Planejados (PT 505)"],
         ["Eventos subsequentes, representações e relatório", "Até 18/03/2026", "PT 560, 580; conclusão integrada"],
         ["Montagem do arquivo", "Até 60 dias após o relatório", "Repositório GitHub (PT 230)"]], larg=[40, 30, 30]) +
        "<h4>Quadro 3 - Prioridades e alterações</h4>" + tabela(
        ["Item", "Justificativa"],
        [["Estoques como foco da base simulada e dos testes de detalhe", "Maior saldo do ativo consolidado (31,3%) e 537 dias de estoque ex-GGF (DF25 p.3)"],
         ["Inclusão de R05 (lucro não realizado) como risco significativo", "Base de R$ 1.293.806 mil (DF25 p.52) e retificação de 2023 (DFP24 p.59)"],
         ["Inclusão de R06 (créditos extemporâneos)", "Principal assunto de auditoria no relatório de 2025 e 2024 (DF25 p.16; DFP24 p.101)"],
         ["Alteração: data de corte do PT 560", "Fixada em 18/03/2026 (data das DF e do relatório); documentos posteriores tratados como fatos conhecidos após a emissão"],
         ["Alteração: versão de normas", "NBC TA 240 (R2) e 570 (R1) publicadas em 25/09/2026 não aplicadas a 2025 (PT 230)"]], larg=[45, 55]),
    "resultados": "Estratégia e plano definidos; programas por ciclo apresentados após o PT 600.",
    "conclusao": "Planejamento adequado aos riscos identificados; execução limitada às evidências públicas e à simulação.",
    "limitacoes": "Cronograma de referência é ilustrativo; não há equipe real.",
})

# =============================================================================================== PT 315
B25 = {"rec": 989601, "est": 1478926, "imob": 955347, "caixa": 398644}
matriz = [
    ["R01", "Receita líquida 3.026.582", "Ocorrência, corte", "Fraude presumida; 4T = ~35% da receita (FRE p.95); e-commerce reconhecido na entrega; Giftback", "Alto", "Sim"],
    ["R02", "Todas (lançamentos e consolidação)", "Todas", "Burla de controles; troca de CEO/COO em 11/12/2025", "Alto", "Sim"],
    ["R03", "Estoques 1.478.926", "Existência, direitos", "Itens de alto valor e pequeno porte; 498 lojas + 3 CDs + fábrica; furtos/perdas", "Alto", "Sim"],
    ["R04", "Estoques / CMV 921.472", "Valorização, exatidão", "Custo médio; alteração de método de GGF (2024); provisão de giro lento e derretimento; VRL", "Alto", "Sim"],
    ["R05", "Estoques consolidados / IR diferido", "Valorização, exatidão (consolidação)", "LNR de R$ 1.293.806 mil; erro corrigido em 2023 (CPC 32)", "Alto", "Sim"],
    ["R06", "Impostos a recuperar 130.845 / outras receitas", "Ocorrência, valorização", "Créditos extemporâneos PIS/COFINS (PAA); subvenções ICMS R$ 334.056 mil; SUDAM", "Alto", "Sim"],
    ["R07", "IR/CS diferidos 568.590", "Valorização", "Realização depende de lucro tributável futuro; mudança de alíquota no cálculo", "Alto", "Não"],
    ["R08", "Arrendamentos 682.705 / direito de uso 593.023", "Valorização, completude", "Taxa de desconto (12,92%); remensuração R$ 156.768 mil; 420 contratos", "Moderado/alto", "Não"],
    ["R09", "Provisões 26.937; possíveis 382.523", "Completude, valorização, divulgação", "Auto de infração R$ 79.896 mil; Tema 985; IPI", "Moderado/alto", "Não"],
    ["R10", "Contas a receber 989.601", "Existência, valorização, direitos", "Recebíveis de cartão; antecipação sem regresso de R$ 164.985 mil em 26/12/2025", "Moderado", "Não"],
    ["R11", "Empréstimos 531.276; derivativos 22.729", "Completude, classificação, valorização", "Debêntures (set/2025); 4131 com swap (nível 2) vence em dez/2026", "Moderado", "Não"],
    ["R12", "Partes relacionadas / remuneração 12.020", "Completude, divulgação", "Acionistas de referência; Presidente do Conselho é acionista; empresa imobiliária acionista", "Moderado", "Não"],
    ["R13", "Notas explicativas", "Exatidão, apresentação", "Inconsistências observadas D01-D08", "Moderado", "Não"],
    ["R14", "TI - Capta x SAP x SAP CAR x PDV/OMS", "Exatidão, completude (receita e estoques)", "Integrações entre sistemas; dependência de data center (FRE p.94)", "Moderado", "Não (controle)"],
    ["R15", "Imobilizado 955.347", "Existência, valorização", "Benfeitorias em lojas; UGC = lojas; sem impairment registrado", "Baixo/moderado", "Não"],
    ["R16", "Continuidade operacional", "Apresentação (base contábil)", "Liquidez corrente 3,63; dívida líquida/LAJIDA 0,17", "Baixo", "Não"],
]
PTS.append({
    "cod": "PT 315", "titulo": "Entendimento da entidade, TI, controles e matriz de riscos",
    "norma": "NBC TA 315 (R2) - Identificação e Avaliação dos Riscos de Distorção Relevante",
    "itens": [("315", ["13", "14", "19", "20", "21", "22", "25", "26", "28", "31", "32", "A229"])],
    "objetivo": "Compreender a entidade, seu ambiente, a estrutura contábil, a TI e os controles; elaborar matriz de riscos por "
                "conta e afirmação e identificar riscos significativos.",
    "objeto": "Grupo Vivara e DF consolidadas 2025.",
    "afirmacoes": "Por conta - ver matriz.",
    "populacao": "DF25 (notas 1, 2, 4, 7, 9, 21, 23, relatório da administração); FRE seções 1, 4, 5; DFP24; ITR 2026.",
    "procedimentos": [
        ("Obter entendimento do negócio, do setor e do modelo de receita a partir de fontes públicas.", R, "Quadro 1"),
        ("Obter entendimento da estrutura de relatório financeiro e das políticas contábeis.", R, "Quadro 2"),
        ("Obter entendimento do ambiente de TI e dos componentes de controle interno (COSO).", R, "Quadro 3"),
        ("Procedimentos analíticos preliminares (margens, giros, prazos).", R, "PT 520"),
        ("Walkthrough dos processos de vendas, estoques, compras e fechamento; avaliação de desenho e implementação.", P, "Sem acesso"),
        ("Discussão da equipe sobre suscetibilidade a fraude e erro (item 17).", P, "Trabalho individual - registrado no PT 240"),
        ("Avaliar riscos inerentes por afirmação e identificar riscos significativos.", R, "Matriz de riscos"),
    ],
    "evidencias": "Fontes indicadas em cada quadro. Referências: PT 240 (fraude), PT 330 (respostas), PT 520 (analíticos), PT 600.",
    "anexo": "<h4>Quadro 1 - Entidade e ambiente</h4>" + tabela(
        ["Aspecto", "Entendimento", "Fonte"],
        [["Estrutura", "Holding (Vivara Participações) com 100% de Tellerina (varejo, marcas Vivara e Life, CDs), Conipa (fábrica em Manaus; "
          "filial de compras em SP) e Tellerina Panamá (1 loja)", "DF25 p.25"],
         ["Rede", "498 pontos de venda em 31/12/2025 (268 Vivara, 219 Life, 11 quiosques); 41 aberturas líquidas em 2025", "DF25 p.25, p.4"],
         ["Receita", "Bruta (líquida de devoluções) R$ 3.801.302 mil: Joias 48,8%, Life 35,6%, Relógios 14,1%; lojas 84,8%, digital 14,8%", "DF25 p.55"],
         ["Sazonalidade", "Quarto trimestre ≈ 35% da receita líquida (Black Friday e Natal); 2º trimestre (Dia das Mães/Namorados)", "FRE p.33, p.95"],
         ["Produção", "Produção em Manaus: 86,2% (Vivara) e 58,3% (Life) do mix; ciclo operacional > 12 meses", "DF25 p.3, p.30"],
         ["Incentivos", "Subvenções de ICMS (AM, MG, ES, PE); SUDAM até 2033; CD no ES inaugurado em jun/2025", "DF25 p.49; p.7"],
         ["Financiamento", "Debêntures R$ 300.000 mil (set/2025); 4131 Santander com swap; sem covenants financeiros", "DF25 p.40-41"],
         ["Indicadores de desempenho", "SSS 11,8%; margem bruta 69,6%; EBITDA ajustado (medida não contábil); dias de estoque ex-GGF 537", "DF25 p.3-4"],
         ["Governança", "Novo Mercado; acionistas de referência 47,36%; Comitê de Auditoria não estatutário; Conselho Fiscal instalado", "FCA p.4; DF25 p.25; FRE p.188"]],
        larg=[16, 66, 18]) + "<h4>Quadro 2 - Estrutura contábil e políticas relevantes</h4>" + tabela(
        ["Política", "Descrição", "Fonte", "Risco"],
        [["Estoques", "Custo médio ponderado, inclui GGF; provisão para giro lento (> 12 meses, não derretível) e perdas no derretimento", "DF25 p.30", "R04"],
         ["GGF", "Metodologia alterada no fechamento de 2024: GGF compõe o custo do produto acabado (CPC 16)", "DF25 p.9", "R04"],
         ["Receita", "Reconhecida na transferência do controle (loja: imediata; e-commerce: entrega); líquida de impostos e devoluções; Giftback", "DF25 p.52-53", "R01"],
         ["Consolidação", "Eliminação integral de saldos e lucros não realizados, líquidos de IR/CS", "DF25 p.28", "R05"],
         ["Arrendamentos", "CPC 06 (R2); taxa DI x pré + spread; fluxos nominais", "DF25 p.58", "R08"],
         ["Tributos diferidos", "Reconhecidos quando provável lucro tributável; incentivos de ICMS e lucro da exploração", "DF25 p.47-52", "R07"],
         ["Segmento", "Segmento único (varejo)", "DF25 p.54-55", "R13"]], larg=[14, 58, 14, 14]) +
        "<h4>Quadro 3 - TI e componentes do controle interno</h4>" + tabela(
        ["Componente", "Entendimento (fonte pública)", "Fonte"],
        [["Sistemas", "ERP Capta (vendas, produção, armazenagem, distribuição); ERP SAP (compras, fiscal, contabilidade) desde 2022; SAP CAR "
          "(conciliação de contas a receber); código de barras individual por joia e relógio", "FRE p.137"],
         ["Ambiente de controle", "Código de Conduta (revisado em 11/09/2024); comitês de assessoramento; Canal Aberto independente", "FRE p.141-145"],
         ["Avaliação de riscos", "Política de Gerenciamento de Riscos (aprovada 15/08/2019, revisada 11/11/2025), metodologia COSO", "FRE p.130"],
         ["Atividades de controle", "Fechamento mensal de PDV, conciliações de integrações, revisão analítica; inventários: anual nos CDs, "
          "semestral na fábrica, diário/semanal nas lojas, geral anual", "FRE p.137-138"],
         ["Monitoramento", "Auditoria interna (plano anual aprovado pelo Conselho); Controles Internos; FP&A", "FRE p.131, p.138"],
         ["Deficiências reportadas", "Administração informa ausência de deficiências significativas reportadas pela KPMG em 2025", "FRE p.139"]],
        larg=[18, 64, 18]) + "<h4>Matriz de riscos por conta e afirmação (R$ mil)</h4>" + tabela(
        ["Risco", "Conta / saldo", "Afirmações", "Fatores de risco inerente", "RDM", "Signif.?"], matriz,
        larg=[6, 19, 16, 37, 11, 11]),
    "resultados": "16 riscos mapeados; 6 riscos significativos (R01 a R06).",
    "conclusao": "A matriz é a base das respostas do PT 330 e dos programas por ciclo.",
    "limitacoes": "Entendimento de controles limitado ao FRE; desenho e implementação não avaliados.",
})

# =============================================================================================== PT 320
alt = CALC["PT320"]["alternativas"]
PTS.append({
    "cod": "PT 320", "titulo": "Materialidade",
    "norma": "NBC TA 320 (R1) - Materialidade no Planejamento e na Execução da Auditoria",
    "itens": [("320", ["10", "11", "12", "13", "14", "A3", "A4", "A7", "A10", "A12", "A13"])],
    "objetivo": "Calcular e justificar a materialidade global, a materialidade para execução e materialidades específicas; "
                "fundamentar bases, percentuais e revisões.",
    "objeto": "DF consolidadas 2025.",
    "afirmacoes": "Todas.",
    "populacao": "DRE e BP consolidados 2023-2025 (DF25 p.19-20; DFP24 p.19).",
    "procedimentos": [
        ("Calcular alternativas de referencial (resultado, receita, ativo, PL, lucro bruto).", R, "Planilha PT320"),
        ("Selecionar referencial e percentual com justificativa.", R, "Abaixo"),
        ("Definir materialidade para execução e limite de distorções claramente triviais.", R, "Planilha PT320"),
        ("Definir materialidades específicas para itens sensíveis.", R, "Quadro"),
        ("Revisar a materialidade com base nas DF finais (item 12).", R, "Abaixo"),
    ],
    "evidencias": "Planilha 04_planilhas/PT_calculos (aba PT320, com fórmulas). Referências: PT 450, PT 530, PT 600.",
    "anexo": tabela(["Referencial", "Base (R$ mil)", "%", "Materialidade (R$ mil)"],
                    [[a["referencial"], n0(a["base"]), pct(a["percentual"], 1), n0(a["materialidade"])] for a in alt], larg=[40, 20, 10, 30]) +
        tabela(["Parâmetro", "Valor (R$ mil)", "Justificativa"],
               [["Materialidade global (MG)", n0(MG), f"5% do LAIR 2025 (R$ {n0(CALC['PT320']['MG_calculada'])} mil), arredondado para baixo. "
                 "Usuários (acionistas do Novo Mercado) focam lucro; o LAIR de 2025 é estável frente a 2024 (626.238)"],
                ["MG como % de", "-", f"receita {pct(CALC['PT320']['MG_sobre_receita'], 2)}; ativo {pct(CALC['PT320']['MG_sobre_ativo'], 2)}; "
                 f"PL {pct(CALC['PT320']['MG_sobre_PL'], 2)}; lucro líquido {pct(CALC['PT320']['MG_sobre_LL'], 2)}"],
                ["Materialidade para execução (ME)", n0(ME), "60% da MG: auditoria inicial, ausência de histórico de distorções, "
                 "inconsistências de divulgação observadas (PT 450) e alto volume de itens de estoque"],
                ["Limite claramente trivial", n0(TRIV), "5% da MG"],
                ["Específica - remuneração dos administradores", "1.200", "≈10% do total de R$ 12.020 mil (DF25 p.48); interesse dos usuários e limite aprovado em AGO"],
                ["Específica - partes relacionadas", "1.450", "Natureza qualitativa (NBC TA 550)"],
                ["Distorção tolerável para a base de estoques (PT 530)", n0(ME), "Igual à ME"]], larg=[30, 14, 56]),
    "resultados": f"MG R$ {n0(MG)} mil; ME R$ {n0(ME)} mil; trivial R$ {n0(TRIV)} mil.",
    "conclusao": "Revisão: o LAIR de referência é o valor final auditado de 2025; não há fato que exija revisão. "
                 "Teste de sensibilidade: o LAIR ajustado pelos itens que a administração classifica como não recorrentes "
                 "(587.798 + 42.900 IPI - 38.400 créditos PIS/COFINS + 17.200 reestruturação/êxito + 15.492 juros do IPI - 11.206 "
                 "Selic dos créditos = 613.784 - DF25 p.12, p.32, p.56) resultaria em MG calculada de cerca de R$ 30.689 mil; a MG adotada "
                 "(R$ 29.000 mil) permanece conservadora e é mantida.",
    "limitacoes": "Em auditoria real a MG seria fixada no planejamento com base em dados anualizados (ex.: ITR 3T25), não "
                  "disponíveis nas fontes fornecidas.",
})

# =============================================================================================== PT 330
resp = [
    ["R01", "Receita", "Entender e testar controles de PDV/e-commerce e integração Capta-SAP [P]",
     "Analítico de receita por canal (PT 520) [R]; corte de vendas/entregas de dez/2025 e devoluções de jan/2026 [P]; "
     "conciliação recebimentos de adquirentes x vendas [P]; recálculo do Giftback [P]", "Final (31/12) e subsequente", "Amostras ampliadas no 4T"],
    ["R02", "Burla de controles", "-", "Teste de lançamentos (critérios no PT 240) [P]; revisão retrospectiva de estimativas (PT 540) [R]; "
     "análise de transações incomuns (antecipação de recebíveis) [R]", "Final", "100% dos lançamentos que atendam aos critérios"],
    ["R03", "Estoques - existência", "Controle de contagens cíclicas (FRE p.137) [P]",
     "Acompanhamento de inventários em lojas/CDs/fábrica [P]; MUS com contagem e vouching [S]; testes de 100% (duplicidades, negativos, corte) [S]",
     "31/12/2025", f"n = {MUS['tamanho_amostra_unidades']} unidades monetárias; 100% para análise de dados"],
    ["R04", "Estoques - valorização", "Aprovação de custos e de GGF [P]", "Recálculo do custo médio e GGF [P]; aging x provisão (T5) [S]; VRL (T6) [S]; "
     "análise de custo unitário atípico (T7) [S]; revisão retrospectiva da provisão (PT 540) [R]", "Final", "100% (análise de dados)"],
    ["R05", "Lucro não realizado", "Controle de cálculo da eliminação [P]", "Recálculo da eliminação com margens intragrupo (nota 9.3) [P]; "
     "reconciliação da variação da base de LNR com a eliminação do exercício (PT 600) [R]; simulação da eliminação por item [S]", "Final", "Integral"],
    ["R06", "Créditos tributários / incentivos", "-", "Leitura de pareceres jurídicos e recálculo amostral com especialista [P]; "
     "leitura da nota 8.3 e do PAA [R]; conciliação da receita de subvenção [P]", "Final", "Amostral com especialista"],
    ["R07", "IR diferido", "-", "Avaliar projeções de lucro tributável [P]; conciliar nota 20.9 com BP [R]", "Final", "Integral"],
    ["R08", "Arrendamentos", "-", "Recalcular amostra de contratos [P]; sensibilidade de taxa (PT 540) [R]", "Final", "Amostral"],
    ["R09", "Provisões", "-", "Cartas a advogados [P]; conciliação nota 17 x FRE 4.4 [R]", "Final e subsequente", "Integral"],
    ["R10", "Contas a receber", "-", "Confirmação/relatórios de adquirentes [P]; prazo médio (PT 520) [R]; contrato da antecipação [P]", "Final", "Integral por adquirente"],
    ["R11", "Empréstimos/derivativos", "-", "Confirmação (PT 505) [P]; recálculo de juros (PT 520) [R]; MTM do swap [P]", "Final", "Integral"],
    ["R12", "Partes relacionadas", "-", "Procedimentos do PT 550 [R/P]", "Final", "Integral"],
    ["R13", "Divulgações", "-", "Conciliação notas x demonstrações (PT 500) [R]", "Final", "Integral"],
    ["R14", "TI", "Controles gerais de TI e de interfaces [P]", "Reconciliação de interfaces [P]", "Interino", "-"],
    ["R15", "Imobilizado", "-", "Analítico de depreciação (PT 520) [R]; vouching de adições [P]; impairment de lojas [P]", "Final", "Amostral"],
    ["R16", "Continuidade", "-", "Análise de liquidez (PT 570) [R]", "Final", "-"],
]
PTS.append({
    "cod": "PT 330", "titulo": "Respostas aos riscos avaliados",
    "norma": "NBC TA 330 (R1) - Resposta do Auditor aos Riscos Avaliados",
    "itens": [("330", ["5", "6", "7", "8", "18", "20", "21", "25", "26", "A4", "A42"])],
    "objetivo": "Relacionar cada risco a testes de controles e procedimentos substantivos, definindo natureza, época e extensão "
                "e distinguindo testes executados de planejados.",
    "objeto": "Riscos R01-R16 do PT 315.",
    "afirmacoes": "Conforme matriz do PT 315.",
    "populacao": "Matriz de riscos (PT 315); materialidade (PT 320).",
    "procedimentos": [
        ("Respostas gerais: ceticismo reforçado, imprevisibilidade (lojas não usuais), supervisão (item 5).", R, "Abaixo"),
        ("Respostas específicas por risco - tabela.", R, "Tabela"),
        ("Procedimentos substantivos para cada risco significativo (item 21).", R, "R01-R06 com procedimentos [R]/[P]/[S]"),
        ("Testes de controles para riscos significativos quando houver confiança (item 15).", P, "Sem acesso: risco de controle no máximo"),
        ("Avaliar se as evidências são suficientes (item 26).", R, "PT 500"),
    ],
    "evidencias": "Tabela abaixo; classificação [R] realizado com evidência pública, [P] planejado por falta de acesso, [S] simulado.",
    "anexo": tabela(["Risco", "Área", "Testes de controles", "Procedimentos substantivos", "Época", "Extensão"], resp,
                    larg=[6, 14, 20, 38, 11, 11]),
    "resultados": "Todos os riscos significativos têm procedimento substantivo definido; parte executada com evidência pública, parte simulada.",
    "conclusao": "Abordagem predominantemente substantiva. A ausência de testes de controles e de procedimentos de campo é a "
                 "principal limitação do dossiê.",
    "limitacoes": "Procedimentos [P] dependem de acesso a registros, pessoas e locais; procedimentos [S] usam dados sintéticos.",
})

# =============================================================================================== PT 402
PTS.append({
    "cod": "PT 402", "titulo": "Organizações prestadoras de serviços",
    "norma": "NBC TA 402 - Considerações de Auditoria para a Entidade que Utiliza Organização Prestadora de Serviços",
    "itens": [("402", ["9", "10", "11", "12", "13", "14", "15", "16", "A1", "A20"])],
    "objetivo": "Identificar serviços terceirizados relevantes e controles complementares; planejar análise de relatórios tipo 1 "
                "ou tipo 2 e procedimentos alternativos.",
    "objeto": "Serviços prestados por terceiros que afetam informações das DF.",
    "afirmacoes": "Existência e valorização de recebíveis; ocorrência de receita; existência de estoques; exatidão de dados de ações e debêntures.",
    "populacao": "Notas 6, 12, 15, 18 (DF25); FCA itens 5 e 6; FRE p.26, p.28, p.132, p.138.",
    "procedimentos": [
        ("Identificar prestadores relevantes e o efeito no controle interno (item 9).", R, "Quadro"),
        ("Identificar controles complementares da entidade usuária (CUEC).", R, "Quadro"),
        ("Obter relatórios tipo 2 (NBC TO 3402/ISAE 3402 ou SOC 1) dos prestadores e avaliar período, exceções e CUEC (itens 13-16).", P, "Sem acesso"),
        ("Procedimentos alternativos: confirmação externa, reconciliação de extratos de adquirentes, visita ao prestador (item 12).", P, "PT 505"),
    ],
    "evidencias": "Ver quadro.",
    "anexo": tabela(["Prestador / serviço", "Informação afetada", "Fonte", "CUEC esperado na Vivara", "Resposta planejada"],
        [["Adquirentes/operadoras de cartão - captura, liquidação e antecipação", "Contas a receber R$ 986.130 mil; receita",
          "DF25 p.29-30; FRE p.138", "Conciliação SAP CAR x extratos; contratos de antecipação", "Relatório tipo 2 ou confirmação + recálculo"],
         ["Itaú Corretora - escrituração de ações", "Ações em tesouraria (1.125.955), capital, base acionária", "FCA p.6; DF25 p.45",
          "Conciliação mensal das posições", "Confirmação (PT 505)"],
         ["Vórtx DTVM - agente fiduciário das debêntures", "Saldo e condições da 1ª emissão (R$ 312.704 mil)", "DF25 p.40",
          "Controle de pagamentos e covenants", "Confirmação"],
         ["Instituições financeiras - convênio com fornecedores (risco sacado)", "Fornecedores convênio R$ 4.610 mil", "DF25 p.38",
          "Conciliação de títulos antecipados", "Confirmação"],
         ["Transportadoras terceirizadas (lojas e e-commerce)", "Corte de receita do e-commerce; estoques em trânsito", "FRE p.28",
          "Comprovante de entrega x faturamento", "Teste de corte com comprovantes de entrega"],
         ["Laboratório terceirizado de gemologia", "Qualidade/valor de diamantes e pedras (matérias-primas)", "FRE p.26",
          "Laudos por lote recebido", "Especialista do auditor (PT 501)"],
         ["Empresa do Canal Aberto (denúncias)", "Informações sobre fraude", "FRE p.132", "Encaminhamento à Comissão de Conduta", "Indagação (PT 240)"],
         ["Equipe especializada no inventário geral anual", "Existência de estoques", "FRE p.138 (não informa se é terceirizada)",
          "Supervisão e conciliação das contagens", "Acompanhamento das contagens (PT 501)"]],
        larg=[22, 20, 14, 22, 22]),
    "resultados": "8 serviços terceirizados com potencial efeito nas DF; os mais relevantes são adquirentes de cartão (recebíveis) e escriturador.",
    "conclusao": "Sem relatórios tipo 1/2 disponíveis publicamente, a resposta seria por procedimentos alternativos (confirmação "
                 "e reconciliação), todos planejados.",
    "limitacoes": "Nomes dos adquirentes não divulgados; existência de relatórios de asseguração dos prestadores desconhecida.",
})

# =============================================================================================== PT 450
pub = [[d[0], d[1], d[2], d[3], (n0(d[4]) if d[4] else "-"), d[5], d[6]] for d in PUBLICAS]
sim = [[f"S-{v['teste_principal'][:2]}", v["teste_principal"], v["itens"], n2(v["distorcao_RS"] / 1000)] for v in TST["distorcao_por_teste_principal"]]
sim.append(["S-PJ", "Projeção MUS (diferenças de contagem)", MUS["itens_com_distorcao_projetada"], n2(MUS["distorcao_projetada_RS"] / 1000)])
tot_sim = (TST["distorcao_conhecida_testes_100pct_RS"] + MUS["distorcao_projetada_RS"]) / 1000
sim.append(["", "<b>Total simulado (factual + projetado)</b>", "", f"<b>{n2(tot_sim)}</b>"])
PTS.append({
    "cod": "PT 450", "titulo": "Mapa de distorções identificadas e simuladas",
    "norma": "NBC TA 450 (R1) - Avaliação das Distorções Identificadas durante a Auditoria",
    "itens": [("450", ["5", "6", "7", "8", "10", "11", "12", "A3", "A16", "A21"])],
    "objetivo": "Elaborar mapa de distorções identificadas ou simuladas, corrigidas e não corrigidas, e avaliar efeitos "
                "quantitativos e qualitativos.",
    "objeto": "DF 2025 (divulgações) e estoques (base simulada).",
    "afirmacoes": "Exatidão e apresentação (divulgações); existência, valorização e corte (estoques).",
    "populacao": "PT 500 (conciliações), PT 510, PT 530.",
    "procedimentos": [
        ("Acumular distorções acima do limite trivial (R$ 1.450 mil) e todas as qualitativas relevantes (item 5).", R, "Quadros 1 e 2"),
        ("Classificar distorções em factuais, de julgamento e projetadas (A3).", R, "Quadro 2"),
        ("Solicitar correção à administração (item 8).", P, "Sem acesso"),
        ("Avaliar o efeito das não corrigidas, individualmente e em conjunto (item 11).", R, "Avaliação"),
        ("Comparar distorções simuladas identificadas com os erros inseridos.", S, "Quadro 3"),
    ],
    "evidencias": "Planilha PT450; arquivos PT450_comparacao_inseridos_x_identificados_*.csv.",
    "anexo": "<h4>Quadro 1 - Distorções e inconsistências com evidência pública (R$ mil)</h4>" + tabela(
        ["Cód.", "Descrição", "Fonte", "Natureza", "Valor", "Afeta DF 2025?", "Tratamento"], pub, larg=[5, 33, 12, 12, 7, 7, 24]) +
        "<h4>Quadro 2 - Distorções simuladas na base de estoques (R$ mil) - SIMULADO</h4>" + tabela(
        ["Cód.", "Origem (teste principal)", "Itens", "Distorção (+ superavaliação)"], sim, larg=[8, 52, 10, 30]) +
        "<h4>Quadro 3 - Erros inseridos x identificados - SIMULADO</h4>" + tabela(
        ["Tipo de erro inserido", "Inseridos", "Detectados", "Taxa", "Efeito inserido (R$ mil)", "Quantificado (R$ mil)"],
        [[c["tipo_erro"], c["inseridos"], c["detectados"], pct(c["taxa_deteccao"], 1), n2(c["efeito_inserido_RS"] / 1000),
          n2(c["distorcao_quantificada_RS"] / 1000)] for c in TST["comparacao"]], larg=[38, 10, 10, 10, 16, 16]),
    "resultados": f"Públicas: 8 inconsistências nas DF 2025, nenhuma afeta saldos das demonstrações primárias; as quantitativas são "
                  f"triviais ou de classificação dentro de notas. Simuladas: distorção factual de R$ {n2(TST['distorcao_conhecida_testes_100pct_RS']/1000)} mil "
                  f"+ projetada de R$ {n2(MUS['distorcao_projetada_RS']/1000)} mil = R$ {n2(tot_sim)} mil "
                  f"({pct(tot_sim/MG, 1)} da MG; {pct(tot_sim/ME, 1)} da ME). Incluído o risco de amostragem (UML da amostra), o total "
                  f"chega a R$ {n2((TST['distorcao_conhecida_testes_100pct_RS'] + MUS['limite_superior_distorcao_RS'])/1000)} mil, acima da ME e abaixo da MG. "
                  f"O efeito real dos erros inseridos é R$ {n2(TST['efeito_total_inserido_RS']/1000)} mil: a projeção subestimou os erros de "
                  "contagem (E2: 1 de 3.000 itens detectado), que só a contagem física revela.",
    "conclusao": "Quantitativamente, as distorções simuladas não corrigidas são inferiores à MG; porém o limite superior com risco de "
                 "amostragem excede a ME, o que exigiria ampliar as contagens nas lojas ou solicitar ajuste. Qualitativamente, "
                 "as inconsistências de divulgação (D01-D07) não alteram decisões dos usuários, mas devem ser comunicadas (PT 260).",
    "limitacoes": "Distorções simuladas não representam distorções reais da Vivara. Sem resposta da administração sobre correções.",
})
