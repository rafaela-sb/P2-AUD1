# -*- coding: utf-8 -*-
"""Conteúdo dos papéis de trabalho: PT 500, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580, 600."""
from dossie_util import tabela, n0, n1, n2, pct, CALC, TST, R, P, S

MG, ME, TRIV = CALC["PT320"]["MG"], CALC["PT320"]["ME"], CALC["PT320"]["trivial"]
MUS = TST["mus"]
PTS = []


def stt(s):
    return f'<span class="{"ok" if s.startswith("OK") else "nok"}">{s}</span>'


# =============================================================================================== PT 500
def nf(x):
    return n0(x) if abs(x - round(x)) < 1e-9 else n2(x)


conc = [[c["verificacao"], nf(c["calculado"]), nf(c["divulgado"]), nf(c["diferenca"]),
         stt("OK" if c["status"] == "OK" else "DIVERG."), c["fonte"]] for c in CALC["PT500"] if c["status"] != "OK"]
ndiv = sum(1 for c in CALC["PT500"] if c["status"] != "OK")
PTS.append({
    "cod": "PT 500", "titulo": "Evidência: relevância, confiabilidade, suficiência e conciliações",
    "norma": "NBC TA 500 (R1) - Evidência de Auditoria",
    "itens": [("500", ["6", "7", "8", "9", "10", "11", "A1", "A5", "A26", "A31", "A33"])],
    "objetivo": "Avaliar relevância, confiabilidade e suficiência das evidências; reconciliar saldos com as demonstrações; "
                "explicitar limitações das fontes públicas e dos dados simulados.",
    "objeto": "Todas as fontes do dossiê; demonstrações e notas de 2025; base simulada de estoques.",
    "afirmacoes": "Exatidão, classificação e apresentação (conciliações); todas (avaliação de suficiência).",
    "populacao": f"{len(CALC['PT500'])} verificações aritméticas e cruzadas entre BP, DRE, DFC, notas, FRE, AGO e ITR (calculos_pts.py); "
                 "conciliação da base simulada (testes_auditoria.py).",
    "procedimentos": [
        ("Avaliar cada tipo de fonte quanto a relevância e confiabilidade (itens 7 e A26-A33).", R, "Quadro 1"),
        ("Recalcular somatórios e conciliar demonstrações e notas (recálculo - A21).", R, "Quadro 2"),
        ("Conciliar documentos entre si (DF x FRE x AGO x ITR).", R, "Quadro 2"),
        ("Conciliar a base simulada com o saldo contábil de estoques, a provisão e o lucro não realizado.", S, "Quadro 3"),
        ("Obter evidências diretas (inspeção, observação, confirmação, indagação) junto à entidade.", P, "Sem acesso"),
    ],
    "evidencias": "Planilha PT500; resultados_calculos.json; PT500_conciliacao_base_x_contabil.csv.",
    "anexo": "<h4>Quadro 1 - Avaliação das fontes</h4>" + tabela(
        ["Fonte", "Relevância", "Confiabilidade", "Limitações"],
        [["DF 2025 (versão do RI, auditada)", "Alta - objeto do trabalho", "Alta - documento auditado, divulgado ao mercado",
          "Versão do RI, não o formulário ENET; sem 'Pareceres e Declarações' (comitê de auditoria, conselho fiscal)"],
         ["DFP 2024 (formulário CVM)", "Alta - saldos iniciais", "Alta - auditada", "Formulário apresenta 2023 sem a retificação (PT 510)"],
         ["FRE 2026 v6", "Média/alta - governança, riscos, controles", "Média - declarações da administração, não auditadas", "Versão posterior (dados até 30/09/2026); divergências com o FCA e a nota 1 (PTs 265 e 600)"],
         ["FCA 2026; página da B3", "Média - identificação", "Alta - registros oficiais", "Informação cadastral"],
         ["ITR 1T26 e 2T26", "Média - eventos subsequentes e continuidade", "Média/alta - revisão limitada", "Posteriores à data de corte"],
         ["Fatos relevantes; proposta e ata da AGO/E; aviso ao mercado da 2ª emissão", "Média", "Alta (documentos oficiais)", "Posteriores à data de corte; escritura da 2ª emissão não obtida"],
         ["Notícias", "Baixa", "Baixa", "Não usadas como evidência"],
         ["Base simulada", "Didática", "Nenhuma sobre a realidade", "Dados sintéticos; não representam registros reais"]],
        larg=[20, 20, 24, 36]) + f"<h4>Quadro 2 - Verificações com divergência ({ndiv} de {len(CALC['PT500'])}; lista completa na planilha, aba PT500)</h4>" + tabela(
        ["Verificação", "Calculado", "Divulgado", "Diferença", "Status", "Fonte"], conc, cls="t small", larg=[38, 12, 12, 8, 9, 21]) +
        "<h4>Quadro 3 - Conciliação da base simulada (R$) - SIMULADO</h4>" + tabela(
        ["Item", "Base simulada", "Contábil", "Diferença", "Fonte"],
        [[c["item"], n2(c["base_simulada_RS"]), n2(c["contabil_RS"]), n2(c["diferenca_RS"]), c["fonte_contabil"]] for c in TST["conciliacao"]],
        larg=[30, 17, 17, 10, 26]),
    "resultados": f"{len(CALC['PT500']) - ndiv} verificações conferem. As {ndiv} divergências são: arredondamentos (≤ 3), "
                  "inconsistências de divulgação (nota 9.2, nota 29.3, base de IR diferido 2024), diferença de D&A entre DFC e nota "
                  "22 (10.019 - a explicar) e comparativos do ITR 1T26 (arredondamento, fora das DF 2025). As de divulgação estão no PT 450. A base simulada concilia "
                  "exatamente com as notas 7.2, 7.3 e 20.9.",
    "conclusao": "Os saldos das demonstrações primárias são aritmeticamente consistentes entre si e com as notas. As evidências "
                 "públicas são relevantes e confiáveis para análise, mas <b>insuficientes</b> para opinião: não há evidência "
                 "direta sobre existência, direitos e valorização dos ativos.",
    "limitacoes": "Sem acesso a razão, subsidiários, contratos e pessoas; dados simulados não fornecem evidência sobre a Vivara.",
})

# =============================================================================================== PT 501
PTS.append({
    "cod": "PT 501", "titulo": "Itens específicos: estoques, litígios e informações por segmento",
    "norma": "NBC TA 501 - Evidência de Auditoria - Considerações Específicas para Itens Selecionados",
    "itens": [("501", ["4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "A4", "A9"])],
    "objetivo": "Planejar procedimentos sobre estoques, litígios e informações por segmento; executar os procedimentos permitidos "
                "pelas fontes disponíveis.",
    "objeto": "Estoques R$ 1.478.926 mil; provisões R$ 26.937 mil e passivos contingentes possíveis R$ 382.523 mil; nota 23 (segmento único).",
    "afirmacoes": "Existência e condição (estoques); completude e avaliação (litígios); apresentação (segmentos).",
    "populacao": "DF25 notas 7, 17 e 23 (p.30-31, p.41-45, p.54-55); FRE 4.4 (p.116) e 5.2 (p.137-138); base simulada.",
    "procedimentos": [
        ("Estoques: avaliar instruções e calendário de inventário da administração (FRE p.137-138).", R, "Quadro 1"),
        ("Estoques: acompanhar contagens em lojas, CDs e fábrica, fazer contagens-teste nos dois sentidos (item 4).", P, "Sem acesso"),
        ("Estoques: contagem-teste nos itens selecionados por MUS (sentido registro → físico).", S, f"PT 530 - {MUS['itens_distintos_selecionados']} itens"),
        ("Estoques: testes de corte e de condição (obsolescência) em 100% da base.", S, "PT 530 (T4, T5, T6)"),
        ("Estoques: avaliar o uso de especialista para teor de ouro e qualidade de gemas.", P, "PT 220"),
        ("Litígios: conciliar provisões da nota 17 com FRE 4.4.", R, "PT 500 (diferença R$ 0,4 mil)"),
        ("Litígios: analisar movimentação e passivos possíveis.", R, "Quadro 2"),
        ("Litígios: carta de circularização aos advogados (item 10).", P, "Modelo no PT 505"),
        ("Segmentos: avaliar a conclusão de segmento único frente às informações gerenciais divulgadas (item 13).", R, "Quadro 3"),
    ],
    "evidencias": "Ver quadros; referências PT 505, PT 530, PT 315.",
    "anexo": "<h4>Quadro 1 - Estoques: entendimento das contagens (FRE p.137-138)</h4>" + tabela(
        ["Local", "Frequência informada", "Implicação para a auditoria"],
        [["Centros de distribuição", "Inventário anual", "Acompanhar na data-base ou próximo; testar roll-forward"],
         ["Fábrica (Manaus)", "Duas vezes por ano", "Acompanhar; atenção a perdas de metal por fase produtiva"],
         ["Lojas", "Contagens diárias (joias, relógios, acessórios) e semanais (Life); inventário geral anual por equipe especializada",
          "Selecionar lojas por valor e de forma imprevisível; avaliar diferenças das contagens cíclicas"],
         ["Rastreabilidade", "Código de barras individual por joia e relógio (Capta)", "Permite seleção registro → físico e físico → registro"]],
        larg=[20, 40, 40]) + "<h4>Quadro 2 - Litígios (R$ mil)</h4>" + tabela(
        ["Natureza", "Provisão 2025", "Provisão 2024", "Possível 2025", "Possível 2024", "Comentário"],
        [["Trabalhistas", "16.318", "8.772", "59.531", "48.419", "Adições de 28.183 (Tema 985 / 1/3 de férias)"],
         ["Cíveis", "3.874", "4.791", "2.813", "12.975", "Renovatórias de aluguel e consumidores"],
         ["Tributários", "6.745", "4.754", "320.179", "142.512", "Aumento de 177.667 no possível: auto de infração Conipa (79.896) e créditos PIS/COFINS (50.361)"],
         ["Total", "26.937", "18.317", "382.523", "203.906", "DF25 p.41-45"]], larg=[14, 12, 12, 12, 12, 38]) +
        "<h4>Quadro 3 - Segmento</h4><p>A nota 23 afirma segmento único (varejo) e informa receita por categoria e canal (DF25 p.54-55). "
        "O relatório da administração apresenta desempenho por bandeira de loja (Vivara x Life, SSS por bandeira - DF25 p.6-7). "
        "Pelo CPC 22, a identificação depende das informações revisadas regularmente pelo principal tomador de decisões (CEO). "
        "Procedimento planejado: inspecionar os relatórios gerenciais do CEO para confirmar se resultados operacionais por bandeira "
        "são avaliados para alocação de recursos. Com as fontes públicas, a conclusão da administração é plausível (custos "
        "compartilhados, divulgado na nota 23), mas não pôde ser corroborada.</p>",
    "resultados": "Provisões conciliam com o FRE; passivos possíveis tributários aumentaram 124,7%; procedimentos de campo de "
                  "estoques simulados (PT 530).",
    "conclusao": "Não há evidência pública de omissão em litígios; o crescimento dos passivos possíveis é fator de atenção para "
                 "divulgação (R09). Contagem física e carta a advogados são indispensáveis e estão planejadas.",
    "limitacoes": "Sem acompanhamento físico, sem respostas de advogados, sem relatórios gerenciais por segmento.",
})

# =============================================================================================== PT 505
mod_banco = """<div class="carta"><p><b>MODELO 1 - Confirmação de instituição financeira (positiva)</b> - NÃO ENVIADA</p>
<p>[Papel timbrado da Vivara Participações S.A.] - Ao Banco [nome], [agência]. Prezados senhores: nossos auditores, [nome do auditor],
estão examinando nossas demonstrações financeiras em 31/12/2025. Solicitamos informar diretamente a eles, no endereço abaixo, os saldos
e condições em 31/12/2025 de: contas correntes e aplicações; empréstimos e financiamentos (inclusive Res. 4131), com taxas, vencimentos
e garantias; instrumentos derivativos (swaps) com valor de mercado; garantias e avais prestados; convênios de antecipação a fornecedores;
outras operações. Esta solicitação não é pedido de pagamento. Assinatura: [administração - não assinado]</p></div>"""
mod_adv = """<div class="carta"><p><b>MODELO 2 - Carta aos assessores jurídicos</b> - NÃO ENVIADA</p>
<p>Solicitamos que informem diretamente aos auditores, até [data próxima à data do relatório], a relação de processos sob seu
patrocínio envolvendo a Vivara e controladas em 31/12/2025 e até a data da resposta: natureza, valor envolvido, estágio,
avaliação de perda (provável, possível, remota) e estimativa de valor; e processos encerrados após 31/12/2025.</p></div>"""
mod_adq = """<div class="carta"><p><b>MODELO 3 - Confirmação de adquirente/operadora de cartão</b> - NÃO ENVIADA</p>
<p>Solicitamos confirmar aos auditores a agenda de recebíveis da Tellerina em 31/12/2025 (valores a liquidar por data), recebíveis
cedidos/antecipados em dezembro/2025 (inclusive a operação de 26/12/2025), existência de direito de regresso, chargebacks em aberto
e garantias.</p></div>"""
PTS.append({
    "cod": "PT 505", "titulo": "Confirmações externas",
    "norma": "NBC TA 505 - Confirmações Externas",
    "itens": [("505", ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "A1", "A6"])],
    "objetivo": "Preparar modelos, controle de circularização, tratamento de diferenças e procedimentos alternativos, sem envio de solicitações reais.",
    "objeto": "Empréstimos, debêntures, derivativos, caixa e aplicações, recebíveis de cartão, fornecedores, litígios, ações em tesouraria.",
    "afirmacoes": "Existência, direitos e obrigações, completude, valorização.",
    "populacao": "Notas 5, 6, 12, 15, 17, 18 (DF25) e FCA item 5.",
    "procedimentos": [
        ("Selecionar as partes a confirmar e o tipo de confirmação (itens 7, 15).", R, "Planilha PT505"),
        ("Preparar modelos de solicitação.", R, "Modelos 1 a 3"),
        ("Manter controle do processo pelo auditor - envio, respostas, segundas vias (item 7).", P, "Planilha PT505 (status 'não enviado')"),
        ("Avaliar confiabilidade das respostas e tratar divergências (itens 10, 14).", P, "Abaixo"),
        ("Aplicar procedimentos alternativos para não respostas (item 12).", P, "Abaixo"),
    ],
    "evidencias": "Planilha PT505 (10 confirmações planejadas).",
    "anexo": mod_banco + mod_adv + mod_adq + "<h4>Tratamento de diferenças e procedimentos alternativos</h4>" + tabela(
        ["Situação", "Tratamento"],
        [["Diferença na resposta", "Investigar se é distorção ou diferença temporal (ex.: liquidação em trânsito); documentar; acumular no PT 450 se distorção"],
         ["Não resposta - bancos/debêntures", "Extratos e contratos originais; cálculo de juros; pagamentos subsequentes; consulta ao SCR (com autorização)"],
         ["Não resposta - adquirentes", "Relatórios de liquidação; recebimentos subsequentes em jan-fev/2026; conciliação SAP CAR"],
         ["Não resposta - fornecedores", "Pagamentos subsequentes, notas fiscais e comprovantes de entrega"],
         ["Não resposta - advogados", "Reunião com jurídico interno; análise de despesas jurídicas; consulta a tribunais"],
         ["Recusa da administração em permitir envio", "Avaliar razões e efeito na avaliação de risco de fraude; comunicar à governança (item 8-9)"]],
        larg=[30, 70]),
    "resultados": "Programa de confirmação preparado; nenhuma solicitação enviada (vedação do comando).",
    "conclusao": "As confirmações seriam a principal evidência externa para R10 e R11; sem elas, essas áreas ficam sem evidência direta.",
    "limitacoes": "Nomes de bancos (caixa), adquirentes e advogados não divulgados; nenhum envio realizado.",
})

# =============================================================================================== PT 510
p510 = [[c["linha"], n1(c["DFP2024_RS_mil"]), n0(c["comparativo_DF2025_RS_mil"]), n1(c["diferenca"]), stt(c["status"])] for c in CALC["PT510"]]
PTS.append({
    "cod": "PT 510", "titulo": "Saldos iniciais (auditoria inicial didática)",
    "norma": "NBC TA 510 (R1) - Trabalhos Iniciais - Saldos Iniciais",
    "itens": [("510", ["5", "6", "7", "8", "9", "A1", "A2", "A4", "A7"])],
    "objetivo": "Tratar o caso como auditoria inicial: examinar saldos de abertura, políticas contábeis e efeitos de modificações na "
                "opinião do auditor anterior.",
    "objeto": "Saldos em 01/01/2025 (= 31/12/2024) e políticas contábeis aplicadas.",
    "afirmacoes": "Existência, completude e valorização dos saldos iniciais; consistência das políticas.",
    "populacao": "DFP 2024 (formulário CVM, relatório KPMG p.101-103, nota 3 p.59-60) x comparativos das DF 2025.",
    "procedimentos": [
        ("Ler as DF 2024 e o relatório do auditor antecessor (item 5).", R, "Quadro 1"),
        ("Verificar se os saldos finais de 2024 foram corretamente transportados (item 6(a)).", R, "Quadro 2"),
        ("Verificar consistência de políticas contábeis (item 7).", R, "Quadro 1"),
        ("Avaliar efeito de modificação na opinião anterior (item 9).", R, "Sem modificação - não aplicável, com fundamento"),
        ("Revisar papéis de trabalho do auditor antecessor (item 6(c)(i)).", P, "Sem acesso"),
        ("Procedimentos sobre estoques iniciais: roll-back e análise de margem; observação de contagens de 2025 (A7).", P, "Sem acesso"),
    ],
    "evidencias": "DFP24 p.101-103 (opinião sem ressalva, PAA crédito extemporâneo, 2023 auditado por outros auditores com relatório "
                  "de 20/03/2024 sem modificação); DFP24 p.59-60 (retificação de 2023); DF25 p.9 (mudança de metodologia de GGF no fechamento de 2024).",
    "anexo": "<h4>Quadro 1 - Leitura do relatório anterior e políticas</h4>" + tabela(
        ["Aspecto", "Constatação", "Efeito em 2025"],
        [["Opinião 2024 (KPMG, 18/03/2025)", "Sem modificação; PAA: crédito extemporâneo PIS/COFINS", "Sem modificação a avaliar (item 9 não se aplica, pois a opinião não contém ressalva, adverso ou abstenção)"],
         ["Auditor de 2023", "Outros auditores; relatório de 20/03/2024 sem modificação", "Primeiro ano da KPMG foi 2024; na simulação, auditor de 2025 é novo"],
         ["Retificação de 2023", "IR diferido sobre LNR passou a usar alíquota nominal de 34%; +71.809 no PL de 2023 e +11.875 no lucro", "Afeta saldo inicial de IR diferido e PL; política aplicada de forma consistente em 2024-2025"],
         ["Formulário DFP 2024", "Coluna 2023 da DRE não retificada (lucro 369.245 x 381.120 na nota 3)", "Sem efeito em 2025"],
         ["Política de GGF", "Alterada no fechamento de 2024 (custos de fábrica no estoque)", "Consistente entre 2024 e 2025; afeta comparabilidade do CMV (PT 520)"],
         ["Apresentação de fornecedores", "DFP 2024 agrupa fornecedores convênio em fornecedores; DF 2025 separa (158.736 + 214.135 = 372.871)", "Reclassificação de apresentação sem efeito em saldos"]],
        larg=[22, 44, 34]) + "<h4>Quadro 2 - Transporte dos saldos (R$ mil)</h4>" + tabela(
        ["Linha", "DFP 2024", "Comparativo DF 2025", "Diferença", "Status"], p510, larg=[40, 16, 18, 12, 14]),
    "resultados": "19 linhas comparadas: todas iguais, com diferenças de arredondamento (≤ 1,1). Políticas consistentes; mudança de GGF ocorrida em 2024.",
    "conclusao": "Os saldos iniciais estão corretamente transportados e não há modificação na opinião anterior. A retificação de "
                 "2023 evidencia risco histórico na consolidação/IR diferido (R05). Evidência sobre a existência dos estoques iniciais "
                 "dependeria de papéis do antecessor - planejado.",
    "limitacoes": "Sem acesso aos papéis da KPMG nem a contagens de 31/12/2024.",
})

# =============================================================================================== PT 520
an = [[a["conta"], n0(a["esperado"]), n0(a["real"]), n0(a["diferenca"]), pct(a["diferenca_pct"], 1), "SIM" if a["investigar"] else "não",
       a["premissas"]] for a in CALC["PT520_analiticos"]]
inv = "".join(f"<li><b>{a['conta']}:</b> {a['investigacao']['explicacao']}. "
              + (f"Expectativa ajustada {n0(a['investigacao']['esperado_ajustado'])}; diferença residual {n0(a['investigacao']['diferenca_residual'])} "
                 f"({'dentro' if a['investigacao']['residual_dentro_do_limite'] else 'fora'} do limite)." if a['investigacao'].get('esperado_ajustado') else a['investigacao'].get('conclusao', ''))
              + "</li>" for a in CALC["PT520_analiticos"] if a.get("investigacao"))
I = CALC["PT520_indices"]
PTS.append({
    "cod": "PT 520", "titulo": "Procedimentos analíticos",
    "norma": "NBC TA 520 - Procedimentos Analíticos",
    "itens": [("520", ["5", "6", "7", "A4", "A6", "A12", "A14", "A16"])],
    "objetivo": "Construir expectativas, definir precisão e limites de investigação, calcular relações e variações e investigar diferenças, "
                "com cálculos reproduzíveis.",
    "objeto": "Receita, CMV, despesas operacionais, depreciação, encargos financeiros e indicadores de estoques e recebíveis.",
    "afirmacoes": "Ocorrência, completude e exatidão (resultado); valorização (estoques).",
    "populacao": "DRE, notas 10, 15, 21-23, 28 e relatório da administração (DF25); DFP24.",
    "procedimentos": [
        ("Avaliar confiabilidade dos dados usados nas expectativas (item 5(b)): dados auditados e divulgados.", R, "PT 500"),
        ("Desenvolver expectativas independentes (item 5(c)).", R, "Quadro 1"),
        (f"Fixar limite de investigação = ME (R$ {n0(ME)} mil) (item 5(c), A16).", R, "Quadro 1"),
        ("Investigar diferenças acima do limite com corroboração (item 7).", R, "Investigação"),
        ("Obter explicações da administração e evidência corroborativa adicional.", P, "Sem acesso"),
    ],
    "evidencias": "Planilha PT520 (fórmulas); calculos_pts.py.",
    "anexo": "<h4>Quadro 1 - Expectativas (R$ mil)</h4>" + tabela(
        ["Conta", "Esperado", "Real", "Diferença", "%", "Investigar?", "Modelo"], an, cls="t small", larg=[16, 10, 10, 10, 7, 8, 39]) +
        f"<h4>Investigação</h4><ul>{inv}</ul><h4>Quadro 2 - Índices</h4>" + tabela(
        ["Indicador", "2025", "2024", "Comentário"],
        [["Margem bruta", pct(I["margem_bruta"]["2025"]), pct(I["margem_bruta"]["2024"]), "Queda de 0,7 p.p.; GGF e subvenção (DF25 p.8)"],
         ["Margem líquida", pct(I["margem_liquida"]["2025"]), pct(I["margem_liquida"]["2024"]), "2024 incluiu créditos extemporâneos de R$ 87.298 mil"],
         ["Dias de estoque (estoque médio / CMV)", n1(I["dias_estoque_CMV"]["2025"]), n1(I["dias_estoque_CMV"]["2024"]),
          f"Administração divulga {I['dias_estoque_CMV']['RA_ex_GGF_2025']} dias ex-GGF (DF25 p.3); método diferente"],
         ["Giro do estoque", n2(I["giro_estoque"]["2025"]), n2(I["giro_estoque"]["2024"]), "Estoques +10,98% x receita líquida +17,44%"],
         ["Prazo de recebimento (dias, receita bruta)", n1(I["dias_recebimento_receita_bruta"]["2025"]), "-",
          f"Nota 6 informa {I['dias_recebimento_receita_bruta']['divulgado_nota6']} dias - consistente"],
         ["Provisão / estoque bruto", pct(I["provisao_sobre_estoque"]["2025"], 2), pct(I["provisao_sobre_estoque"]["2024"], 2), "Baixa frente a 537 dias de estoque - ver PT 540"],
         ["Alíquota efetiva (IR/CS sobre LAIR)", pct(I["aliquota_efetiva"]["2025"], 1), "-", "Benefício líquido: incentivos ICMS e lucro da exploração (nota 20.8)"]],
        larg=[30, 12, 12, 46]),
    "resultados": "3 de 8 expectativas excederam o limite (CMV, despesas com vendas e G&A). O CMV fica dentro do limite após "
                  "ajuste pelo efeito do GGF; despesas com vendas e G&A têm explicações qualitativas consistentes, sem quantificação "
                  "possível com dados públicos.",
    "conclusao": "Os procedimentos analíticos não indicam distorção relevante não explicada nas contas de resultado testadas; "
                 "para despesas com vendas e G&A, testes de detalhe permanecem planejados. O baixo índice de provisão frente aos dias "
                 "de estoque reforça o risco R04.",
    "limitacoes": "Expectativas com dados agregados anuais (precisão limitada); CDI do período aproximado pela taxa do cenário I da nota 29.7.",
})

# =============================================================================================== PT 530
tst100 = [[t, v["sinalizados"], v["confirmados"], n2(v["distorcao_confirmada_RS"])] for t, v in sorted(TST["testes_100pct"].items())]
PTS.append({
    "cod": "PT 530", "titulo": "Amostragem e testes sobre a base simulada de estoques",
    "norma": "NBC TA 530 - Amostragem em Auditoria",
    "itens": [("530", ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "A10", "A13", "A17", "A21", "A22"])],
    "objetivo": "Aplicar amostragem à base simulada obrigatória: população, unidade amostral, método, tamanho, seleção, risco "
                "amostral, tratamento e projeção de erros.",
    "objeto": "Base SINTÉTICA de estoques em 31/12/2025 (518.271 registros; saldo líquido R$ 1.478.926.000,00).",
    "afirmacoes": "Existência e exatidão (amostra MUS); valorização, corte, classificação e integridade (testes de 100%).",
    "populacao": f"População da MUS: {n0(MUS['populacao_itens'])} registros com valor líquido positivo, R$ {n2(MUS['valor_populacao_RS'])} "
                 "(registros negativos testados em 100% pelo T3). Unidade amostral: real (R$ 1,00) do valor líquido; o item físico "
                 "é a posição de estoque que contém a unidade selecionada.",
    "procedimentos": [
        ("Justificar a conta e sua materialidade; documentar premissas e método de geração da base.", S, "Seção 'Base simulada' e dicionário"),
        ("Conciliar o total da base com o saldo contábil (nota 7.2), a provisão (7.3) e o LNR (20.9).", S, "PT 500 - Quadro 3 (diferença zero)"),
        ("Testes de 100% (análise de dados) T1 a T9 e investigação dos itens sinalizados.", S, "Quadro 2"),
        ("Definir parâmetros da MUS (confiança 95%, distorção tolerável = ME, distorção esperada 10% da tolerável).", S, "Quadro 1"),
        ("Selecionar a amostra por seleção sistemática por unidade monetária com início aleatório (semente 241003384).", S, "PT530_amostra_MUS_selecionada.csv"),
        ("Executar contagem e vouching (simulados) dos itens selecionados.", S, "Arquivo de verdade simulada"),
        ("Projetar distorções e calcular o limite superior (Stringer/Poisson).", S, "Quadro 1"),
        ("Comparar erros inseridos x identificados.", S, "PT 450 - Quadro 3"),
    ],
    "evidencias": "02_base_simulada/resultados/*.csv; planilhas PT530_MUS, PT530_Amostra, PT530_Testes100.",
    "anexo": "<h4>Quadro 1 - Amostragem por unidade monetária (R$) - SIMULADO</h4>" + tabela(
        ["Parâmetro", "Valor", "Fórmula / critério"],
        [["Valor da população (BV)", n2(MUS["valor_populacao_RS"]), "Soma dos valores líquidos > 0"],
         ["Distorção tolerável (TM)", n2(MUS["distorcao_toleravel_RS"]), "= materialidade para execução"],
         ["Distorção esperada (EM)", n2(MUS["distorcao_esperada_RS"]), "10% da TM (auditoria inicial)"],
         ["Fator de confiabilidade / expansão", f"{MUS['fator_confiabilidade']} / {MUS['fator_expansao']}", "Poisson 95%, 0 erros / risco 5%"],
         ["Tamanho da amostra (n)", n0(MUS["tamanho_amostra_unidades"]), "n = BV x RF / (TM - EM x EF)"],
         ["Intervalo amostral (J)", n2(MUS["intervalo_amostral_RS"]), "J = BV / n; itens > J seriam 100% (nenhum)"],
         ["Início aleatório", n2(MUS["inicio_aleatorio_RS"]), "Uniforme(0, J), semente 241003384"],
         ["Itens com distorção na amostra", f"{MUS['itens_com_distorcao_total']} ({MUS['itens_com_distorcao_ja_identificada_100pct']} já identificado(s) nos testes de 100%)", "Contagem e custo documental simulados"],
         ["Distorção projetada", n2(MUS["distorcao_projetada_RS"]), "Σ taint x J (itens não identificados em 100%)"],
         ["Precisão básica", n2(MUS["precisao_basica_RS"]), "J x 3,0"],
         ["Provisão incremental", n2(MUS["provisao_incremental_RS"]), "Σ (ΔRF - 1) x taint x J"],
         ["Limite superior de distorção (UML)", n2(MUS["limite_superior_distorcao_RS"]), "Precisão básica + projetada + incremental"],
         ["Conclusão estatística", MUS["conclusao"], "UML x TM"]], larg=[30, 30, 40]) +
        "<h4>Quadro 2 - Testes de 100% (R$) - SIMULADO</h4>" + tabela(
        ["Teste", "Sinalizados", "Confirmados", "Distorção confirmada (R$)"], tst100, larg=[40, 15, 15, 30]) +
        "<p class='nota'>Um mesmo item pode ser sinalizado por mais de um teste (ex.: custo digitado x10 é sinalizado por T7 e T6); "
        "no PT 450 cada item é contado uma única vez pelo teste principal. Falsos positivos: "
        f"{TST['falsos_positivos']}.</p>",
    "resultados": f"Testes de 100% identificaram {TST['itens_confirmados']} itens com distorção confirmada (R$ "
                  f"{n2(TST['distorcao_conhecida_testes_100pct_RS'])}). A MUS ({MUS['itens_distintos_selecionados']} itens) "
                  f"encontrou {MUS['itens_com_distorcao_total']} itens com diferença; projetada R$ {n2(MUS['distorcao_projetada_RS'])}; "
                  f"UML R$ {n2(MUS['limite_superior_distorcao_RS'])} ≤ TM R$ {n2(MUS['distorcao_toleravel_RS'])}. "
                  "Na comparação com o gabarito, todos os erros detectáveis por análise de dados (E1, E3-E9) foram identificados "
                  "(100%), mas apenas 1 de 3.000 diferenças de contagem (E2) apareceu na amostra.",
    "conclusao": "Estatisticamente a população é aceita para existência/exatidão com 95% de confiança (UML < TM), mas a margem é "
                 "estreita e o gabarito mostra subestimação dos erros de contagem. Em auditoria real, a resposta seria ampliar as "
                 "contagens em lojas (estratificação por loja e categoria) e exigir correção das distorções factuais.",
    "limitacoes": "Base, contagens e documentos são SINTÉTICOS; conclusões não se aplicam aos estoques reais da Vivara.",
})

# =============================================================================================== PT 540
A = CALC["PT540_arrendamento"]; PE = CALC["PT540_provisao_estoque"]
PTS.append({
    "cod": "PT 540", "titulo": "Estimativas contábeis: passivo de arrendamento e provisão de estoques",
    "norma": "NBC TA 540 (R2) - Auditoria de Estimativas Contábeis e Divulgações Relacionadas",
    "itens": [("540", ["13", "14", "16", "18", "19", "21", "22", "23", "26", "29", "32", "A95"])],
    "objetivo": "Selecionar estimativa relevante e avaliar método, premissas, dados, incerteza e possível viés da administração; "
                "executar análise de sensibilidade.",
    "objeto": "(1) Passivo de arrendamento R$ 682.705 mil (nota 28) - taxa de desconto e prazos; (2) provisão para perdas de "
              "estoques R$ 4.688 mil (nota 7.3).",
    "afirmacoes": "Valorização e divulgação.",
    "populacao": "DF25 p.58-61 (nota 28); p.30-31 (nota 7.3); ITR1/ITR2 nota 5.2 (p.14).",
    "procedimentos": [
        ("Entender método, premissas e dados da administração (item 13).", R, "Quadro 1"),
        ("Desenvolver estimativa pontual/intervalo independente para o passivo a partir dos fluxos não descontados (item 29).", R, "Quadro 2"),
        ("Análise de sensibilidade da taxa de desconto (±1 e ±2 p.p.).", R, "Quadro 2; planilha PT540_Arrend"),
        ("Revisão retrospectiva da provisão de estoques com os ITR de 2026 (item 14).", R, "Quadro 3"),
        ("Cenários de provisão de estoques (0,5%, 1% e 2% do estoque bruto).", R, "Quadro 3"),
        ("Testar dados de entrada (contratos, aging real) e controles sobre a estimativa.", P, "Sem acesso"),
        ("Avaliar indicadores de viés (item 32).", R, "Conclusão"),
    ],
    "evidencias": "Notas 28 e 7.3; ITR 1T26/2T26; planilhas PT540.",
    "anexo": "<h4>Quadro 1 - Método e premissas</h4>" + tabela(
        ["Elemento", "Arrendamentos", "Provisão de estoques"],
        [["Método", "Fluxo de caixa descontado nominal, sem inflação projetada (CPC 06 R2); fluxos líquidos de PIS/COFINS/CBS", "Custo de itens de giro lento (> 12 meses, não derretíveis) e perda de derretimento"],
         ["Premissas-chave", f"Taxa média ponderada 12,92% (2024: 12,19%); 420 contratos (367 de 10 anos); remensuração R$ 156.768 mil", "Prazo de 12 meses; percentuais de perda no derretimento (não divulgados)"],
         ["Dados", "Contratos de locação, reajustes, créditos tributários", "Aging do ERP Capta; coleções descontinuadas"],
         ["Incerteza", "Alta sensibilidade à taxa e ao prazo; reforma tributária (CBS)", "Baixa em valor; alta em julgamento (537 dias de estoque)"]],
        larg=[16, 46, 38]) + "<h4>Quadro 2 - Sensibilidade do passivo de arrendamento (R$ mil)</h4>" + tabela(
        ["Taxa", "Valor presente (modelo)", "Variação vs 12,92%", "Variação / ME"],
        [[pct(s["taxa"], 2), n0(s["valor_presente"]), n0(s["variacao_vs_12_92"]), pct(s["variacao_vs_12_92"] / ME, 0)] for s in A["sensibilidade"]],
        larg=[20, 30, 25, 25]) +
        f"<p class='nota'>O modelo simplificado (fluxos nas faixas da nota 28, pontos médios) gera R$ {n0(A['vp_a_12_92'])} mil a 12,92% "
        f"(diferença de {n0(A['diferenca_modelo'])} = {pct(A['diferenca_modelo']/A['passivo_divulgado'],1)} do saldo; taxa implícita do modelo "
        f"{pct(A['taxa_implicita_modelo'],2)}), aproximação aceitável para sensibilidade. Variação de 1 p.p. na taxa ≈ R$ {n0(A['efeito_1pp'])} mil, "
        "acima da ME.</p><h4>Quadro 3 - Provisão de estoques: retrospectiva e cenários (R$ mil)</h4>" + tabela(
        ["Item", "Valor"],
        [["Saldo em 31/12/2025", n0(PE["saldo_31_12_2025"])], ["Reversões no 1º semestre de 2026", n0(PE["reversoes_1S26"])],
         ["Complementos no 1º semestre de 2026", n0(PE["complementos_1S26"])], ["Saldo em 30/06/2026", n0(PE["saldo_30_06_2026"])],
         ["% do saldo de 2025 revertido no 1S26", pct(PE["pct_revertido_1S26"], 1)],
         ["Provisão / estoque bruto", pct(PE["provisao_sobre_estoque_bruto"], 2)]] +
        [[c["cenario"], f"{n0(c['provisao'])} (efeito no resultado {n0(c['efeito_resultado'])})"] for c in PE["cenarios"]], larg=[60, 40]),
    "resultados": f"Arrendamentos: estimativa sensível - ±1 p.p. altera o passivo em ≈ R$ {n0(A['efeito_1pp'])} mil (> ME). "
                  f"Provisão de estoques: {pct(PE['pct_revertido_1S26'],0)} do saldo foi revertido no 1S26, indicando que a provisão "
                  "foi utilizada/realizada ou superestimada; o saldo é imaterial (0,32% do estoque bruto), mas uma provisão de 1% "
                  "do estoque bruto reduziria o resultado em ≈ R$ 10 milhões.",
    "conclusao": "Passivo de arrendamento: risco de estimativa alto (R08); taxa divulgada e método são consistentes com a norma; "
                 "requer teste de contratos e da curva de juros. Provisão de estoques: sem indicador de viés para subestimar o "
                 "resultado; o baixo índice frente ao giro de estoque exige teste do aging real (simulado no PT 530: T5/T6).",
    "limitacoes": "Sem acesso a contratos, aging e curvas de juros; modelo de fluxo aproximado.",
})

# =============================================================================================== PT 550
PTS.append({
    "cod": "PT 550", "titulo": "Partes relacionadas",
    "norma": "NBC TA 550 - Partes Relacionadas",
    "itens": [("550", ["11", "12", "13", "14", "15", "16", "18", "19", "20", "22", "25", "A11", "A22"])],
    "objetivo": "Mapear vínculos, saldos e transações; avaliar completude e divulgações; planejar a identificação de operações não informadas.",
    "objeto": "Nota 19 (DF25 p.47-48); FRE seções 6, 7.5 e 11.",
    "afirmacoes": "Completude, ocorrência, apresentação e divulgação.",
    "populacao": "Estrutura acionária (FRE p.149-153), acordo de acionistas (FRE p.50), relações familiares (FRE p.193), "
                 "operações intragrupo (DF25 p.47), remuneração (DF25 p.48).",
    "procedimentos": [
        ("Mapear partes relacionadas e vínculos.", R, "Quadro 1"),
        ("Conciliar saldos e transações divulgados com BP e DRE.", R, "Quadro 2"),
        ("Comparar remuneração paga com o limite aprovado em AGO.", R, "Quadro 2"),
        ("Ler política de transações com partes relacionadas e FRE 11.2.", R, "Quadro 3"),
        ("Identificar operações não informadas: atas do Conselho, contratos de locação de lojas/escritórios x lista de partes "
         "relacionadas (inclusive NKaufman Empreendimentos Imobiliários), pagamentos a CPFs/CNPJs vinculados no contas a pagar, "
         "declarações de interesse dos administradores.", P, "Sem acesso"),
        ("Indagar administração e governança (itens 13-14).", P, "Sem acesso"),
    ],
    "evidencias": "Ver quadros.",
    "anexo": "<h4>Quadro 1 - Mapa de vínculos</h4>" + tabela(
        ["Parte", "Vínculo", "Fonte"],
        [["Nelson Kaufman", "Acionista de referência (27,414%); parte do acordo de acionistas; controla integralmente a NK", "FRE p.50, p.153"],
         ["Marina Kaufman Bueno Netto", "Acionista de referência (13,918%); Presidente do Conselho de Administração; filha de Nelson Kaufman", "FRE p.152, p.193"],
         ["NKaufman Empreendimentos Imobiliários Ltda.", "Acionista (5,726%); parte do acordo; quotas de Nelson Kaufman e Penrich Consultants Corp.", "FRE p.149-151"],
         ["Penrich Consultants Corp.", "79,231% da NK; 100% de Nelson Kaufman", "FRE p.150-151"],
         ["Tellerina, Conipa, Tellerina Panamá", "Controladas integrais (eliminadas na consolidação)", "DF25 p.25"],
         ["Administradores e conselheiros", "Pessoal-chave (remuneração R$ 12.020 mil)", "DF25 p.48"]], larg=[28, 52, 20]) +
        "<h4>Quadro 2 - Saldos e transações (R$ mil)</h4>" + tabela(
        ["Item", "2025", "2024", "Verificação"],
        [["Passivo da controladora com Tellerina (CSC)", "3.307", "1.646", "Igual ao BP individual (DF25 p.19) - OK"],
         ["Vendas Conipa → Tellerina", "2.552.081", "2.461.329", "Eliminadas; base do LNR (PT 600)"],
         ["Vendas de matéria-prima Tellerina → Conipa", "298.951", "70.063", "Aumento de 327% - entender motivo (planejado)"],
         ["Direitos autorais (Conipa recebe)", "352.769", "360.948", "Eliminados"],
         ["Remuneração total da administração", "12.020", "13.851", "≤ limite AGO 2025 de R$ 13.877 mil - OK"]], larg=[38, 14, 14, 34]) +
        "<h4>Quadro 3 - Política e divulgação</h4><p>A política exige aprovação prévia do Conselho para qualquer transação com parte "
        "relacionada e veda empréstimos a administradores e acionistas (FRE p.258-259). O FRE 11.2 declara não haver transações "
        "além das dispensadas (FRE p.260-261). A nota 19 divulga apenas operações intragrupo e remuneração.</p>",
    "resultados": "Saldos divulgados conferem; nenhuma transação com acionistas divulgada. Remuneração dentro do limite.",
    "conclusao": "Completude não pode ser confirmada com fontes públicas. Como a NK é empresa imobiliária controlada pelo acionista de "
                 "referência e a Vivara possui 500 contratos de locação (nota 28), o cruzamento de locadores com partes relacionadas "
                 "é o procedimento prioritário planejado. Não há evidência de que tais transações existam.",
    "limitacoes": "Sem acesso a atas, contratos e cadastro de fornecedores/locadores.",
})

# =============================================================================================== PT 560
ev = [["12/02/2026", "Tellerina recebeu notificação da RFB homologando compensação (CSLL 2015)", "DF25 p.49",
       "Evidencia condição existente em 31/12/2025 (crédito) - tipo que exige ajuste se necessário; já refletido/divulgado", "Antes do corte"],
      ["06/02/2026", "Premissas do relatório Focus de 06/02/2026 usadas na análise de sensibilidade", "DF25 p.65-66", "Informação usada na divulgação - não é evento", "Antes do corte"],
      ["18/03/2026", "Fato relevante: projeção de 55 a 65 aberturas em 2026", "FR guidance", "Não exige ajuste nem divulgação nas DF (projeção)", "Na data de corte"],
      ["18/03/2026", "Autorização de emissão das DF pelo Conselho; relatório do auditor", "DF25 p.26, p.18", "Data-limite da avaliação", "Data de corte"],
      ["27/03/2026", "Proposta da administração para AGO/E: destinação do lucro; declara não haver eventos subsequentes (item 2.6)", "AGO p.14-15, p.44",
       "Consistente com as DF; sem efeito", "Após o corte"],
      ["27/04/2026", "AGO/E aprovou sem ressalvas as contas e as DF 2025 (135.552.562 votos a favor; 37.153.987 abstenções), a destinação do lucro (R$ 30.975 mil reserva legal; R$ 164.000 mil dividendos intercalares; R$ 424.527 mil reserva estatutária), o Conselho Fiscal e o limite de remuneração 2026 de R$ 30.734 mil (39.159.594 votos contra); KPMG, Conselho Fiscal e Comitê de Auditoria presentes", "ATA p.1-4", "Confirma a destinação divulgada na nota 18.4; DF publicadas no Valor Econômico em 19/03/2026; sem efeito nas DF", "Após o corte"],
      ["06/05/2026", "Fato relevante: novo programa de recompra (até 12.369.833 ações, até 06/05/2027)", "FR recompra; ITR1 p.47", "Não exige ajuste", "Após o corte"],
      ["28/05/2026", "3º aditivo ao acordo de acionistas", "FRE p.50", "Não exige ajuste", "Após o corte"],
      ["05/08/2026", "ITR 2T26: lucro de R$ 232.460 mil no semestre; provisão de estoques reduzida a R$ 2.459 mil", "ITR2 p.6, p.14", "Corrobora valorização (PT 540)", "Após o corte"],
      ["12-16/10/2026", "2ª emissão de debêntures: escritura celebrada em 12/10/2026; registro automático requerido na CVM em 13/10/2026; "
       "300.000 debêntures de R$ 1.000 (R$ 300.000 mil), série única, quirografárias, com fiança de Tellerina e Conipa; data de emissão "
       "15/10/2026; liquidação prevista para 16/10/2026; rating pela Fitch; coordenadores Itaú BBA e Santander; agente fiduciário Vórtx",
       "DEB2 p.1-3", "Transação posterior; não exige ajuste nem reemissão das DF 2025", "Após o corte"],
      ["15-19/10/2026", "B3 registra anúncios de início (15/10) e de encerramento (19/10) da distribuição pública", "B3 p.2",
       "Anúncios não obtidos; corroboram a conclusão da oferta", "Após o corte"]]
PTS.append({
    "cod": "PT 560", "titulo": "Eventos subsequentes",
    "norma": "NBC TA 560 (R1) - Eventos Subsequentes",
    "itens": [("560", ["5", "6", "7", "8", "9", "10", "14", "15", "A6", "A8"])],
    "objetivo": "Fixar a data de corte da pesquisa, examinar publicações posteriores ao encerramento e distinguir eventos que exigem "
                "ajuste dos que exigem divulgação.",
    "objeto": "Período de 01/01/2026 a 18/03/2026 (data de corte = data de autorização das DF e do relatório do auditor); "
              "fatos conhecidos após essa data avaliados à luz dos itens 14-17.",
    "afirmacoes": "Todas (ajustes e divulgações).",
    "populacao": "DF25; fato relevante de 18/03/2026; proposta e ata da AGO/E; ITR 1T26 e 2T26; fato relevante de 06/05/2026; FRE v6; aviso ao mercado da 2ª emissão de debêntures; página da B3.",
    "procedimentos": [
        ("Fixar data de corte (18/03/2026) e documentar a fundamentação (item 6).", R, "Objeto"),
        ("Ler documentos públicos do período e posteriores; classificar eventos.", R, "Quadro 1"),
        ("Ler a nota de eventos subsequentes das DF: não há nota específica; verificar se algum evento exigiria divulgação.", R, "Conclusão"),
        ("Indagar administração, ler atas de reuniões e ITR internos até a data do relatório (item 7).", P, "Sem acesso"),
        ("Obter representação formal sobre eventos subsequentes (item 9).", P, "PT 580"),
    ],
    "evidencias": "Quadro 1 (fonte em cada linha).",
    "anexo": "<h4>Quadro 1 - Eventos e classificação</h4>" + tabela(["Data", "Evento", "Fonte", "Classificação / efeito", "Período"], ev,
                                                                  larg=[10, 36, 12, 32, 10]),
    "resultados": "Nenhum evento entre 01/01/2026 e 18/03/2026 exige ajuste adicional; a homologação da compensação de CSLL "
                  "(12/02/2026) refere-se a condição existente em 31/12/2025 e está mencionada na nota 20.4. Eventos após a data de "
                  "corte (AGO/E que aprovou as DF sem ressalvas, recompra, aditivo do acordo, 2ª emissão de debêntures de R$ 300.000 mil) não teriam levado à "
                  "modificação do relatório nem à reemissão das DF.",
    "conclusao": "Sem eventos subsequentes que exijam ajuste ou divulgação adicional nas DF 2025, com base nas fontes públicas. A "
                 "ausência de nota de eventos subsequentes é consistente com a declaração da administração (AGO p.44).",
    "limitacoes": "Sem atas do Conselho e sem indagação; escritura da 2ª emissão e anúncios de início/encerramento não obtidos; o aviso ao mercado não informa a destinação dos recursos.",
})

# =============================================================================================== PT 570
L = CALC["PT570"]
PTS.append({
    "cod": "PT 570", "titulo": "Continuidade operacional",
    "norma": "NBC TA 570 - Continuidade Operacional",
    "itens": [("570", ["10", "11", "12", "13", "16", "17", "18", "A3", "A8"])],
    "objetivo": "Analisar liquidez, endividamento, cláusulas contratuais, fluxos de caixa e eventos adversos; avaliar incertezas relevantes e divulgações.",
    "objeto": "Capacidade de continuidade operacional por pelo menos 12 meses a partir de 31/12/2025.",
    "afirmacoes": "Apresentação (base contábil) e divulgação.",
    "populacao": "BP, DRE, DFC (DF25 p.19-23); notas 15 e 29.9 (p.40-41, p.65); ITR 1T26 e 2T26; FRE 2.1.",
    "procedimentos": [
        ("Calcular indicadores de liquidez e endividamento (2024-2025 e 2026).", R, "Quadro 1; planilha PT570"),
        ("Analisar cláusulas contratuais (covenants e vencimento antecipado).", R, "Quadro 2"),
        ("Analisar fluxos de caixa e vencimentos de 12 meses.", R, "Quadro 2"),
        ("Identificar eventos adversos (item A3) em fontes públicas.", R, "Quadro 2"),
        ("Obter avaliação da administração e projeções de caixa; representações (item 16).", P, "Sem acesso"),
    ],
    "evidencias": "Planilha PT570; DF25 p.40-41 (covenants), p.65 (vencimentos), ITR1 p.5, ITR2 p.5; aviso ao mercado da 2ª emissão (DEB2 p.1-3).",
    "anexo": "<h4>Quadro 1 - Indicadores</h4>" + tabela(
        ["Indicador", "31/12/2025", "31/12/2024", "30/06/2026"],
        [["Liquidez corrente", n2(L["2025"]["liquidez_corrente"]), n2(L["2024"]["liquidez_corrente"]), n2(L["ITR_2T26"]["liquidez_corrente"])],
         ["Liquidez seca", n2(L["2025"]["liquidez_seca"]), n2(L["2024"]["liquidez_seca"]), "-"],
         ["Liquidez imediata", n2(L["2025"]["liquidez_imediata"]), n2(L["2024"]["liquidez_imediata"]), "-"],
         ["Endividamento geral (PC+PNC)/AT", pct(L["2025"]["endividamento_geral"]), pct(L["2024"]["endividamento_geral"]), "-"],
         ["Dívida líquida (R$ mil)", n0(L["divida_liquida"]["2025"]), n0(L["divida_liquida"]["2024"]), "-"],
         ["LAJIDA calculado (R$ mil)", n0(L["lajida_calculado"]["2025"]), n0(L["lajida_calculado"]["2024"]), "-"],
         ["Dívida líquida / LAJIDA", n2(L["divida_liquida_sobre_lajida"]["2025"]), n2(L["divida_liquida_sobre_lajida"]["2024"]), "-"],
         ["Caixa operacional líquido (R$ mil)", n0(L["fco"]["2025"]), n0(L["fco"]["2024"]), "-"],
         ["Caixa e equivalentes (R$ mil)", "398.644", "278.153", n0(L["ITR_2T26"]["caixa"])],
         ["Patrimônio líquido (R$ mil)", "2.949.564", "2.496.942", n0(L["ITR_2T26"]["pl"])]], larg=[40, 20, 20, 20]) +
        "<h4>Quadro 2 - Cláusulas, vencimentos e eventos</h4>" + tabela(
        ["Fator", "Evidência", "Avaliação"],
        [["Covenants financeiros", "Inexistentes; vencimento antecipado por protesto > R$ 10.000 mil (capital de giro) ou R$ 100.000 mil (debêntures)", "Risco baixo"],
         ["Vencimentos em 12 meses", f"Empréstimos R$ {n0(L['vencimentos_12m_emprestimos'])} mil (fluxo); arrendamentos R$ {n0(L['vencimentos_12m_arrendamento'])} mil; "
          f"Santander 4131 R$ {n0(L['santander_4131_vencimento_dez_2026'])} mil vence em dez/2026", "Cobertos por caixa (398.644) + FCO (468.870)"],
         ["Dividendos", "R$ 164.000 mil pagos em 29/12/2025, financiados por antecipação de recebíveis de R$ 163.800 mil líquidos", "Gestão de caixa; não indica dificuldade"],
         ["Resultados", "Lucro de R$ 619.502 mil (2025) e R$ 232.460 mil no 1S26", "Positivo"],
         ["Acesso a crédito após a data-base", "2ª emissão de debêntures de R$ 300.000 mil, data de emissão 15/10/2026, com fiança das controladas (DEB2 p.1-2)",
          "Evidencia acesso a financiamento; destinação não informada no aviso"],
         ["Eventos adversos públicos", "Nenhum identificado (perda de clientes-chave, litígio relevante provável, falta de crédito)", "-"],
         ["Relatório do auditor 2025", "Sem parágrafo de incerteza relevante (DF25 p.15-18)", "Consistente"]], larg=[22, 54, 24]),
    "resultados": "Indicadores sólidos e melhores que 2024; não há covenants financeiros; vencimento do 4131 em dez/2026 coberto pela posição de caixa.",
    "conclusao": "Não foram identificados eventos ou condições que levantem dúvida significativa; a base contábil de continuidade "
                 "é apropriada e não há incerteza relevante a divulgar, com base nas evidências públicas.",
    "limitacoes": "Sem acesso a orçamento e projeções de caixa da administração.",
})

# =============================================================================================== PT 580
carta580 = """<div class="carta"><p><b>MINUTA DIDÁTICA - CARTA DE REPRESENTAÇÃO DA ADMINISTRAÇÃO</b> (não assinada; nenhuma assinatura simulada)</p>
<p>[Papel timbrado da Vivara Participações S.A.] São Paulo, 18 de março de 2026. Ao Auditor Independente.</p>
<p>Esta carta é fornecida em conexão com a auditoria das demonstrações financeiras individuais e consolidadas da Vivara Participações S.A.
de 31 de dezembro de 2025. Confirmamos, com base em nosso conhecimento e após indagações apropriadas:</p>
<ol>
<li>Cumprimos nossa responsabilidade pela elaboração das DF de acordo com CPC/IFRS, conforme a carta de contratação, e elas
apresentam adequadamente a posição patrimonial e financeira, o desempenho e os fluxos de caixa.</li>
<li>As premissas significativas das estimativas (arrendamentos, provisão para perdas de estoques, provisões para riscos, IR diferido,
créditos tributários extemporâneos) são razoáveis.</li>
<li>Relações e transações com partes relacionadas foram registradas e divulgadas; não há transações com acionistas de referência,
NKaufman Empreendimentos Imobiliários Ltda. ou administradores além das divulgadas na nota 19.</li>
<li>Todos os eventos subsequentes a 31/12/2025 que exigem ajuste ou divulgação foram ajustados ou divulgados.</li>
<li>Os efeitos das distorções não corrigidas listadas em anexo (PT 450) são, individualmente e em conjunto, irrelevantes.</li>
<li>Fornecemos acesso a todas as informações, registros e pessoas, inclusive atas, contratos e inventários físicos.</li>
<li>Divulgamos todos os casos conhecidos de fraude ou suspeita envolvendo administração, empregados com papéis relevantes no controle
interno ou outros, com efeito relevante, e as alegações comunicadas por empregados, ex-empregados, reguladores ou outros.</li>
<li>Divulgamos todos os casos conhecidos de não conformidade com leis e regulamentos, e todos os litígios e reivindicações.</li>
<li>Os estoques existem, são de propriedade das controladas e estão registrados ao menor entre custo e valor realizável líquido;
os lucros não realizados em operações intragrupo foram eliminados.</li>
<li>As condições dos incentivos fiscais (SUDAM, ICMS) foram cumpridas e os créditos de PIS/COFINS reconhecidos têm fundamento legal.</li>
</ol>
<p>Diretor Presidente: ____________ &nbsp; Diretor de Finanças e RI: ____________ &nbsp; Contador: ____________</p></div>"""
PTS.append({
    "cod": "PT 580", "titulo": "Representações formais",
    "norma": "NBC TA 580 (R1) - Representações Formais",
    "itens": [("580", ["4", "9", "10", "11", "13", "14", "15", "16", "19", "20", "A1", "A8"])],
    "objetivo": "Preparar minuta didática da carta de representações da administração e explicar por que ela não substitui outras evidências.",
    "objeto": "Representações da Diretoria (Diretor Presidente, Diretor de Finanças e RI) e do contador (DF25 p.68).",
    "afirmacoes": "Todas.",
    "populacao": "Riscos do PT 315; distorções do PT 450; eventos do PT 560.",
    "procedimentos": [
        ("Identificar os signatários adequados (item 9).", R, "DF25 p.68; FRE p.180, p.187"),
        ("Preparar minuta com representações gerais (itens 10-11) e específicas (item 13).", R, "Minuta"),
        ("Datar a carta o mais próximo possível da data do relatório (item 14).", R, "18/03/2026"),
        ("Obter a carta assinada e avaliar consistência com outras evidências (itens 15-16).", P, "Sem acesso"),
    ],
    "evidencias": "Os diretores declararam ter revisado as DF e o relatório do auditor (DF25 p.14) - declaração pública, não substitui a carta.",
    "anexo": carta580 + "<h4>Por que a carta não substitui outras evidências</h4><p>As representações formais são evidência "
             "necessária, mas, sozinhas, não são suficientes para nenhum assunto (NBC TA 580, item 4 e A1). Elas vêm da própria "
             "parte responsável e não verificam, por exemplo, a existência física das joias ou o valor do passivo de arrendamento. "
             "No caso, o Diretor Presidente e o Diretor de Operações assumiram em 11/12/2025 (FRE p.180, p.187), o que exige "
             "cuidado adicional: representações sobre fatos anteriores dependem de indagações a ex-administradores e de evidência "
             "documental. Se houver dúvida sobre a integridade da administração ou recusa de representações, o auditor deve avaliar "
             "efeitos na opinião (itens 19-20).</p>",
    "resultados": "Minuta preparada com representações gerais e específicas para os riscos significativos.",
    "conclusao": "A carta complementa, mas não substitui, os procedimentos dos PTs 330, 501, 505, 530 e 540.",
    "limitacoes": "Carta não obtida; nenhuma assinatura simulada.",
})

# =============================================================================================== PT 600
C6 = CALC["PT600"]
PTS.append({
    "cod": "PT 600", "titulo": "Auditoria de grupo: componentes, consolidação e materialidade",
    "norma": "NBC TA 600 (R2) - Considerações Especiais - Auditorias de Demonstrações Contábeis de Grupos",
    "itens": [("600", ["11", "12", "14", "19", "21", "22", "23", "26", "29", "31", "33", "35", "37", "45"])],
    "objetivo": "Mapear o grupo, componentes e processo de consolidação; avaliar riscos, materialidade dos componentes, envolvimento "
                "de auditores de componentes e suficiência das evidências.",
    "objeto": "Grupo Vivara: controladora + Tellerina + Conipa + Tellerina Panamá; eliminações e lucro não realizado.",
    "afirmacoes": "Completude do perímetro; exatidão e valorização das eliminações; apresentação das divulgações de controladas.",
    "populacao": "Notas 1, 4.2, 9 e 20.9 (DF25 p.25, p.28, p.32-33, p.52); FRE 6.4-6.5 (p.163-164).",
    "procedimentos": [
        ("Mapear componentes e atividades.", R, "Quadro 1"),
        ("Avaliar perímetro: nota 1 x FRE 6.4/6.5.", R, "FRE 6.4 omite Tellerina Panamá"),
        ("Definir materialidade para execução dos componentes (abaixo da ME do grupo).", R, "Quadro 1; planilha PT600"),
        ("Reconciliar a variação da base de LNR com a eliminação do exercício.", R, "Quadro 2"),
        ("Verificar somatório da nota 9.2.", R, "D04"),
        ("Recalcular eliminações de estoques por margem intragrupo (simulação item a item).", S, "Base simulada: campo lucro_nao_realizado_eliminado = R$ 1.293.806.000,00"),
        ("Comunicar instruções a auditores de componentes (se houver) e avaliar seu trabalho (itens 37-45).", P, "Auditor da Tellerina Panamá não identificado"),
    ],
    "evidencias": "Nota 9.3 (eliminações de LNR de R$ 264.234 mil e IR de R$ 89.871 mil); nota 20.9 (bases de LNR).",
    "anexo": "<h4>Quadro 1 - Componentes</h4>" + tabela(
        ["Componente", "Atividade", "Ativo total (R$ mil)", "Lucro (R$ mil)", "ME componente", "Abordagem"],
        [["Vivara Participações", "Holding; debêntures (R$ 312.704 mil)", "3.272.296 (individual)", "619.502", "6.000", "Equipe do grupo"],
         ["Tellerina", "Varejo (lojas, CDs, e-commerce)", n0(C6["componentes"][0]["ativo_total"]), n0(C6["componentes"][0]["lucro_prejuizo"]), "12.000",
          "Significativo - auditoria completa; estoques a preço de transferência"],
         ["Conipa", "Fábrica (Manaus), compras (SP), royalties", n0(C6["componentes"][1]["ativo_total"]), n0(C6["componentes"][1]["lucro_prejuizo"]), "12.000",
          "Significativo - incentivos fiscais e margens intragrupo"],
         ["Tellerina Panamá", "1 loja (moeda funcional US$)", n0(C6["componentes"][2]["ativo_total"]), n0(C6["componentes"][2]["lucro_prejuizo"]), "3.000",
          "Não significativo - analíticos no grupo; conversão (CPC 02)"]], larg=[16, 24, 16, 12, 10, 22]) +
        "<h4>Quadro 2 - Lucro não realizado (R$ mil)</h4>" + tabela(
        ["Item", "Valor", "Fonte"],
        [["Base de LNR em 31/12/2024", n0(C6["lnr_base_ir_diferido"]["2024"]), "DF25 p.52"],
         ["Base de LNR em 31/12/2025", n0(C6["lnr_base_ir_diferido"]["2025"]), "DF25 p.52"],
         ["Variação da base", n0(C6["variacao_lnr"]), "Cálculo"],
         ["Eliminação de LNR no resultado de 2025 (equivalência)", "264.234", "DF25 p.33"],
         ["Diferença", n0(C6["variacao_lnr"] - 264234), "Pequena (R$ 40 mil), abaixo do limite trivial; não explicável com dados públicos"],
         ["IR/CS diferido sobre LNR do exercício", "89.871 (34%)", "DF25 p.33"]], larg=[50, 25, 25]),
    "resultados": "Conipa gera 92,7% do lucro absoluto dos componentes e Tellerina detém o estoque a preço de transferência; a "
                  "variação da base de LNR (264.194) concilia com a eliminação do exercício (264.234) com diferença de 40. "
                  "Registradas a inconsistência D04 (PT 450) e a omissão da Tellerina Panamá no FRE 6.4.",
    "conclusao": "A consolidação concentra o principal risco do grupo (R05). As evidências públicas confirmam a coerência entre "
                 "notas, mas não substituem o recálculo das eliminações com dados de margem por produto (planejado; simulado na base).",
    "limitacoes": "Sem acesso a pacotes de consolidação, a auditores de componentes e às DF individuais das controladas.",
})
