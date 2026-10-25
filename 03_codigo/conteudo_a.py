# -*- coding: utf-8 -*-
"""Conteúdo dos papéis de trabalho: PT EC, 200, 210, 220, 230, 240, 250, 260, 265."""
from dossie_util import tabela, n0, pct, CALC, TST, R, P, S

MG, ME, TRIV = CALC["PT320"]["MG"], CALC["PT320"]["ME"], CALC["PT320"]["trivial"]

PTS = []

# =============================================================================================== PT EC
PTS.append({
    "cod": "PT EC", "titulo": "Caracterização do trabalho de asseguração",
    "norma": "NBC TA Estrutura Conceitual - Estrutura Conceitual para Trabalhos de Asseguração",
    "itens": [("EC", ["10", "11", "12", "14", "15", "19", "22", "26", "27", "34", "35", "39", "44"])],
    "objetivo": "Caracterizar o trabalho (partes, objeto, critérios, evidência, relatório e nível de asseguração) e "
                "diferenciar a auditoria das demonstrações contábeis de 2025 de outros trabalhos de asseguração.",
    "objeto": "Demonstrações financeiras individuais e consolidadas da Vivara Participações S.A. em 31/12/2025, com "
              "comparativos de 2024, notas explicativas e relatório do auditor independente (DF25 p.15-68).",
    "afirmacoes": "Não se aplica a afirmações específicas: o PT define o enquadramento do trabalho. Os riscos tratados aqui "
                  "são de enquadramento: confundir o nível de asseguração (razoável x limitada) ou o tipo de trabalho, "
                  "e apresentar conclusão sem base suficiente.",
    "populacao": "Documentos societários e regulatórios: DF25 (nota 1 p.25; nota 2.1 p.26; relatório do auditor p.15-18), "
                 "ITR1 (relatório de revisão p.3-4), FCA (p.2-4), FRE (6.5 p.164; 7.3), B3 (p.1-2).",
    "procedimentos": [
        ("Identificar as três partes do trabalho a partir das fontes públicas.", R, "Quadro 1"),
        ("Identificar objeto, informação do objeto e critérios aplicáveis.", R, "Quadro 1"),
        ("Comparar a auditoria anual (asseguração razoável) com a revisão das ITR (asseguração limitada) e com "
         "trabalhos que não são de asseguração.", R, "Quadro 2"),
    ],
    "evidencias": "DF25 p.15 (opinião da KPMG em forma positiva); DF25 p.26 (declaração de conformidade CPC/IFRS e autorização "
                  "de emissão em 18/03/2026); ITR1 p.4 (conclusão de revisão em forma negativa); FCA p.2-4 (registro na "
                  "categoria A, Novo Mercado, VIVA3); FRE p.164 (estrutura acionária). Referências: PT 210, PT 200, PT 260.",
    "anexo": "<h4>Quadro 1 - Elementos do trabalho (EC item 26)</h4>" + tabela(
        ["Elemento", "Caracterização no caso Vivara", "Fonte"],
        [["Parte responsável", "Administração da Vivara Participações S.A. (Diretoria Estatutária: Diretor Presidente, Diretor de "
          "Finanças e RI, Diretor de Operações; contador responsável), que elabora as DF individuais e consolidadas", "DF25 p.68"],
         ["Responsáveis pela governança", "Conselho de Administração; Comitê de Auditoria, Riscos e Finanças (não estatutário); "
          "Conselho Fiscal (instalado)", "FRE p.133, p.188; DF25 p.48"],
         ["Usuários previstos", "Acionistas (acionistas de referência com 47,36%; investidores do Novo Mercado), debenturistas da "
          "1ª emissão, credores (Santander - Res. 4131), CVM, B3 e demais usuários de DF de companhia aberta", "DF25 p.25, p.40; FCA p.4"],
         ["Objeto", "Posição patrimonial e financeira, desempenho e fluxos de caixa do Grupo Vivara (controladora, Tellerina, "
          "Conipa e Tellerina Panamá)", "DF25 p.25"],
         ["Informação do objeto", "DF individuais e consolidadas 2025 (BP, DRE, DRA, DMPL, DFC, DVA e notas 1 a 31)", "DF25 p.19-68"],
         ["Critérios", "Práticas contábeis adotadas no Brasil (CPC aprovados pela CVM) e IFRS (IASB) - estrutura de "
          "apresentação adequada, de propósito geral", "DF25 p.26"],
         ["Evidência", "Apropriada e suficiente para opinião (NBC TA 500). Neste dossiê: documentos públicos e dados sintéticos "
          "(ver PT 500)", "PT 500"],
         ["Relatório", "Relatório de auditoria com opinião (forma positiva). Este dossiê NÃO emite opinião", "DF25 p.15; PT CONC"]],
        larg=[20, 60, 20]) +
        "<h4>Quadro 2 - Auditoria x outros trabalhos</h4>" + tabela(
        ["Trabalho", "Nível de segurança", "Natureza dos procedimentos", "Forma da conclusão", "Exemplo no caso"],
        [["Auditoria das DF (NBC TA)", "Razoável - alto nível, não absoluto (EC 14)", "Avaliação de riscos, testes de controles e "
          "procedimentos substantivos", "Opinião em forma positiva", "Relatório KPMG 18/03/2026 (DF25 p.15)"],
         ["Revisão de informações intermediárias (NBC TR)", "Limitada (EC 15)", "Principalmente indagações e procedimentos analíticos",
          "Conclusão em forma negativa", "Revisão das ITR 1T26 (ITR1 p.4) e 2T26 (ITR2 p.4)"],
         ["Procedimentos previamente acordados (NBC TSC)", "Não é asseguração", "Procedimentos definidos com a parte contratante",
          "Relato de constatações, sem conclusão", "Não identificado nas fontes"],
         ["Consultoria / compilação", "Não é asseguração (EC 19)", "Assessoria; preparação de informações", "Sem conclusão de asseguração",
          "FRE 9.3: auditor não prestou serviços extra-auditoria em 2025 (FRE p.240)"]], larg=[18, 18, 24, 18, 22]),
    "resultados": "O trabalho é de <b>asseguração razoável</b>, do tipo <b>atestação</b>: a administração mensura o objeto "
                  "aplicando CPC/IFRS e o auditor expressa opinião sobre a informação resultante. A revisão das ITR de "
                  "2026 é trabalho distinto, de <b>asseguração limitada</b>. Não foram identificadas exceções no enquadramento.",
    "conclusao": "Trabalho de asseguração razoável sobre DF de propósito geral; as precondições estão avaliadas no PT 210. "
                 "Sem acesso a evidências diretas, este dossiê não emite opinião.",
    "limitacoes": "Sem acesso à carta de contratação real, a atas de reunião do comitê e a comunicações do auditor; "
                  "caracterização baseada em documentos públicos.",
})

# =============================================================================================== PT 200
PTS.append({
    "cod": "PT 200", "titulo": "Objetivos gerais: ética, independência, ceticismo, julgamento e risco de auditoria",
    "norma": "NBC TA 200 (R1) - Objetivos Gerais do Auditor Independente e a Condução da Auditoria",
    "itens": [("200", ["11", "13", "14", "15", "16", "17", "A20", "A23", "A25", "A32", "A34", "A40", "A47", "A49"])],
    "objetivo": "Documentar como os requisitos de ética, independência, ceticismo profissional, julgamento profissional, "
                "risco de auditoria e as condições para segurança razoável foram aplicados (ou não puderam ser aplicados) "
                "neste trabalho.",
    "objeto": "Trabalho de auditoria como um todo (DF 2025 da Vivara).",
    "afirmacoes": "Todas as afirmações, no nível das demonstrações. Risco geral: concluir sem evidência suficiente ou sem "
                  "postura cética diante de informações inconsistentes.",
    "populacao": "Todas as fontes listadas em 06_fontes; inconsistências registradas no PT 450 (D01 a D08).",
    "procedimentos": [
        ("Declarar a independência do preparador e a inexistência de vínculos com a Vivara, a KPMG e partes relacionadas "
         "(campo de declaração no rodapé).", R, "Quadro 1"),
        ("Registrar ameaças à independência e salvaguardas aplicáveis ao trabalho didático.", R, "Quadro 1"),
        ("Aplicar ceticismo: confrontar informações entre documentos (DF x FRE x FCA x ITR x AGO) em vez de aceitar uma única fonte.",
         R, "PT 500; PT 450"),
        ("Registrar os julgamentos relevantes (referencial de materialidade, riscos significativos, premissas da simulação).",
         R, "Quadro 2"),
        ("Decompor o risco de auditoria (RA = RI x RC x RD) e fixar o risco de detecção aceitável por área.", R, "Quadro 3; PT 315"),
        ("Avaliar se as condições para obter segurança razoável estão presentes.", R, "Conclusão"),
    ],
    "evidencias": "Inconsistências que exigiram ceticismo: FRE 9.1 x FCA (início da KPMG); FRE 6.4 x nota 1 (Tellerina "
                  "Panamá); nota 31 x nota 18.1 (data do aumento de capital - D01); nota 9.2 (somatório - D04); "
                  "DFP24 formulário x nota 3 (retificação de 2023). Referências: PT 450, PT 500, PT 510.",
    "anexo": "<h4>Quadro 1 - Ética e independência</h4>" + tabela(
        ["Requisito", "Aplicação neste trabalho", "Status"],
        [["Princípios éticos (integridade, objetividade, competência, sigilo, comportamento) - NBC PG 100 (EC item 6)",
          "Uso exclusivo de documentos públicos; nenhum contato com a companhia, auditores, clientes ou fornecedores; "
          "fontes citadas com página; dados sintéticos identificados", "Atendido"],
         ["Independência de pensamento e aparência (NBC TA 200 item 14)", "Declaração do preparador: não possui participação "
          "acionária, vínculo de emprego, relação familiar ou comercial com a Vivara, a KPMG ou seus administradores "
          "[declaração a ser confirmada pelo preparador no campo de revisão]", "Pendente de confirmação"],
         ["Ameaça de autorrevisão", "Não há: o preparador não elaborou registros da entidade", "N/A"],
         ["Ameaça de familiaridade / defesa de interesse", "Não identificadas", "N/A"],
         ["Uso de IA na elaboração", "Risco de conteúdo sem suporte: mitigado por referência de página em cada dado e por "
          "código reproduzível (03_codigo)", "Salvaguarda aplicada"]], larg=[34, 50, 16]) +
        "<h4>Quadro 2 - Julgamentos profissionais relevantes</h4>" + tabela(
        ["Julgamento", "Decisão", "Referência"],
        [["Referencial de materialidade", f"5% do LAIR consolidado 2025 (R$ {n0(CALC['PT320']['MG_calculada'])} mil), arredondado para R$ {n0(MG)} mil", "PT 320"],
         ["Materialidade para execução", f"60% da MG (R$ {n0(ME)} mil) - auditoria inicial e inconsistências observadas", "PT 320"],
         ["Riscos significativos", "Receita (fraude presumida), burla de controles, estoques (existência e valorização), "
          "lucro não realizado na consolidação, créditos tributários extemporâneos", "PT 315"],
         ["Conta da base simulada", "Estoques (maior saldo do ativo consolidado)", "PT 530"],
         ["Estimativa para PT 540", "Passivo de arrendamento (taxa de desconto) e provisão para perdas de estoques", "PT 540"]],
        larg=[30, 52, 18]) +
        "<h4>Quadro 3 - Modelo de risco de auditoria (avaliação qualitativa)</h4>" + tabela(
        ["Área", "Risco inerente", "Risco de controle", "RDM combinado", "Risco de detecção aceitável"],
        [["Receita (ocorrência/corte)", "Alto (presunção de fraude)", "Não testado - máximo", "Alto (significativo)", "Baixo"],
         ["Estoques (existência/valorização)", "Alto", "Não testado - máximo", "Alto (significativo)", "Baixo"],
         ["Consolidação (LNR/IR diferido)", "Alto", "Não testado - máximo", "Alto (significativo)", "Baixo"],
         ["Créditos tributários extemporâneos", "Alto", "Não testado - máximo", "Alto (significativo)", "Baixo"],
         ["Arrendamentos", "Moderado/alto", "Não testado - máximo", "Moderado/alto", "Baixo/moderado"],
         ["Caixa e equivalentes", "Baixo", "Não testado - máximo", "Baixo/moderado", "Moderado"]],
        larg=[28, 18, 18, 18, 18]),
    "resultados": "Ceticismo aplicado resultou em 8 inconsistências nas DF 2025 (PT 450) e 4 em outros documentos (PTs 265, 510 e 600). Nenhuma ameaça à independência "
                  "identificada; a declaração formal do preparador permanece como campo a confirmar.",
    "conclusao": "As condições para segurança razoável (evidência apropriada e suficiente, acesso irrestrito, representações "
                 "formais, comunicação com a governança) <b>não estão presentes</b> neste trabalho didático. Por isso não se "
                 "emite opinião; o dossiê documenta riscos, procedimentos e evidências públicas disponíveis.",
    "limitacoes": "Risco de controle mantido no máximo por ausência de testes de controles; avaliação de independência "
                  "baseada em declaração do preparador.",
})

# =============================================================================================== PT 210
carta = """
<div class="carta">
<p><b>MINUTA DIDÁTICA - CARTA DE CONTRATAÇÃO</b> (não enviada; sem assinaturas)</p>
<p>Ao Conselho de Administração e à Diretoria da Vivara Participações S.A.<br>Rua Verbo Divino, 1207, São Paulo - SP (FCA p.3)</p>
<p><b>1. Objetivo e alcance.</b> Os senhores solicitaram a auditoria das demonstrações financeiras individuais e consolidadas da
Vivara Participações S.A. e controladas, que compreendem o balanço patrimonial em 31 de dezembro de 2025 e as demonstrações do
resultado, do resultado abrangente, das mutações do patrimônio líquido, dos fluxos de caixa e do valor adicionado do exercício,
e as notas explicativas. A auditoria tem por objetivo expressar opinião sobre se as demonstrações apresentam adequadamente, em
todos os aspectos relevantes, a posição patrimonial e financeira, o desempenho e os fluxos de caixa, de acordo com as práticas
contábeis adotadas no Brasil e as IFRS.</p>
<p><b>2. Responsabilidades do auditor.</b> Conduzir a auditoria de acordo com as normas brasileiras e internacionais de auditoria,
cumprir exigências éticas, planejar e executar a auditoria para obter segurança razoável de que as demonstrações estão livres de
distorção relevante, causada por fraude ou erro. Em razão das limitações inerentes, existe risco inevitável de que algumas
distorções relevantes não sejam detectadas. O auditor comunicará deficiências significativas de controle interno identificadas
(NBC TA 265) e os principais assuntos de auditoria (NBC TA 701).</p>
<p><b>3. Responsabilidades da administração.</b> A administração reconhece sua responsabilidade: (a) pela elaboração das
demonstrações de acordo com CPC/IFRS, incluindo a DVA (CPC 09); (b) pelos controles internos necessários para permitir a
elaboração de demonstrações livres de distorção relevante; (c) por fornecer acesso irrestrito a todas as informações, registros,
pessoas e locais (lojas, centros de distribuição e fábrica de Manaus), inclusive para acompanhamento de inventários físicos;
(d) pelas representações formais ao final do trabalho (NBC TA 580); (e) pela identificação e divulgação de partes relacionadas
e eventos subsequentes.</p>
<p><b>4. Estrutura do relatório.</b> Relatório conforme NBC TA 700, 701, 705, 706 e 720: opinião; base para opinião; principais
assuntos de auditoria; outras informações (relatório da administração); responsabilidades da administração e da governança;
responsabilidades do auditor. O formato poderá ser alterado se as constatações o exigirem.</p>
<p><b>5. Outros termos.</b> Cronograma (PT 300), equipe e honorários: [a definir]. Auditoria inicial: será necessário acesso aos
papéis de trabalho do auditor antecessor (KPMG - DF 2024) para os saldos iniciais (NBC TA 510).</p>
<p>De acordo: ______________________ (Vivara - não assinado) &nbsp;&nbsp; Auditor: Rafaela de Sousa Barbosa, matrícula 241003384 (trabalho didático)</p>
</div>"""
PTS.append({
    "cod": "PT 210", "titulo": "Termos do trabalho e precondições para a auditoria",
    "norma": "NBC TA 210 (R1) - Concordância com os Termos do Trabalho de Auditoria",
    "itens": [("210", ["6", "7", "8", "9", "10", "13", "A2", "A3", "A23"])],
    "objetivo": "Avaliar as precondições para a auditoria e preparar carta de contratação didática com objetivo, alcance, "
                "responsabilidades e estrutura do relatório.",
    "objeto": "Termos do trabalho de auditoria das DF 2025 (individuais e consolidadas).",
    "afirmacoes": "Nível das demonstrações. Riscos: estrutura de relatório financeiro inaceitável; administração não reconhecer "
                  "responsabilidades; restrição de alcance imposta.",
    "populacao": "DF25 nota 2.1 (p.26); declaração dos diretores (DF25 p.14); relatório do auditor (DF25 p.15-18); FRE 9.1-9.3 "
                 "(p.239-240); FCA item 4 (p.5).",
    "procedimentos": [
        ("Determinar se a estrutura de relatório financeiro é aceitável (item 6(a)).", R, "Quadro 1"),
        ("Obter evidência pública de que a administração reconhece suas responsabilidades (item 6(b)).", R, "Quadro 1"),
        ("Preparar minuta de carta de contratação (item 10).", R, "Minuta abaixo"),
        ("Obter concordância formal da administração e assinatura da carta.", P, "Depende de contato com a companhia - vedado"),
        ("Verificar existência de restrição de alcance imposta pela administração (item 7).", P, "Sem acesso"),
    ],
    "evidencias": "Nota 2.1 declara conformidade com CPC e IFRS e autorização de emissão em 18/03/2026 (DF25 p.26). A Diretoria "
                  "declarou ter revisado as DF e o relatório do auditor (DF25 p.14). O relatório do auditor descreve as "
                  "responsabilidades da administração (DF25 p.17). FRE p.239: KPMG contratada em 04/12/2024.",
    "anexo": "<h4>Quadro 1 - Precondições (item 6)</h4>" + tabela(
        ["Precondição", "Evidência pública", "Conclusão"],
        [["(a) Estrutura de relatório aceitável", "CPC/IFRS de propósito geral, exigidos pela CVM para companhia aberta (DF25 p.26)", "Aceitável"],
         ["(b)(i) Responsabilidade pela elaboração das DF", "Declaração dos diretores (DF25 p.14); seção de responsabilidades no relatório (DF25 p.17)", "Reconhecida (evidência indireta)"],
         ["(b)(ii) Controle interno", "FRE 5.2: controles para DF confiáveis (FRE p.137-139)", "Reconhecida (evidência indireta)"],
         ["(b)(iii) Acesso irrestrito", "Não verificável publicamente", "Planejado - carta (PT 580)"]], larg=[28, 52, 20]) + carta,
    "resultados": "Estrutura aceitável; reconhecimento das responsabilidades evidenciado de forma indireta. Nenhuma restrição "
                  "de alcance pública identificada.",
    "conclusao": "As precondições (item 6) estariam atendidas com base nas evidências públicas; a aceitação formal depende de "
                 "carta assinada, procedimento planejado e não executado.",
    "limitacoes": "A carta é minuta didática; não houve contato com a companhia.",
})

# =============================================================================================== PT 220
PTS.append({
    "cod": "PT 220", "titulo": "Gestão de qualidade do trabalho",
    "norma": "NBC TA 220 (R3) - Gestão de Qualidade da Auditoria de Demonstrações Contábeis",
    "itens": [("220", ["13", "14", "16", "17", "25", "26", "29", "30", "31", "35", "36", "37"])],
    "objetivo": "Planejar direção, supervisão, revisão, consultas e recursos; documentar conflitos e riscos à qualidade.",
    "objeto": "Trabalho de auditoria das DF 2025 (dossiê).",
    "afirmacoes": "Nível do trabalho. Riscos à qualidade: equipe sem competência setorial (joalheria, Zona Franca), "
                  "uso de IA sem verificação, ausência de revisão independente, conclusões sem suporte.",
    "populacao": "Recursos do trabalho, cronograma (PT 300), fontes (06_fontes).",
    "procedimentos": [
        ("Definir responsabilidades de direção, supervisão e revisão.", R, "Quadro 1"),
        ("Identificar riscos à qualidade e respostas.", R, "Quadro 2"),
        ("Planejar consultas sobre assuntos difíceis (incentivos SUDAM/ICMS, CPC 32 sobre lucro não realizado).", P, "Quadro 1"),
        ("Planejar revisão de qualidade do trabalho (EQR), exigida para entidade listada (NBC PA 02).", P, "Quadro 1"),
        ("Executar revisão pelo responsável e pelo revisor de qualidade antes da data do relatório.", P, "Campo de revisão em branco"),
    ],
    "evidencias": "Cronograma no PT 300; registro de versões no PT 230; reprodutibilidade em 03_codigo.",
    "anexo": "<h4>Quadro 1 - Direção, supervisão, revisão, consultas e recursos</h4>" + tabela(
        ["Elemento", "Planejamento", "Status"],
        [["Sócio responsável / direção", "Preparadora (Rafaela de Sousa Barbosa, matrícula 241003384) assume a direção do trabalho didático", "Definido"],
         ["Supervisão", "Não há equipe a supervisionar; trabalho individual", "Não aplicável no ambiente didático"],
         ["Revisão", "Campo de revisão em cada PT; nenhuma revisão de terceiros foi realizada ou simulada", "Pendente"],
         ["Revisor de qualidade (EQR)", "Exigido para companhia listada; revisor independente da equipe", "Planejado - não executado"],
         ["Consultas", "Especialistas tributários (subvenções ICMS, SUDAM, PIS/COFINS), especialista em TI (Capta/SAP), "
          "gemólogo para inventário de joias", "Planejado - não executado"],
         ["Recursos tecnológicos", "Python (geração e testes da base), planilha com fórmulas, Git para versões", "Utilizados"],
         ["Recursos de IA", "Elaboração assistida por IA; salvaguardas: citação de página, código reproduzível, "
          "dados sintéticos identificados", "Utilizados e declarados"]], larg=[24, 56, 20]) +
        "<h4>Quadro 2 - Riscos à qualidade, conflitos e respostas</h4>" + tabela(
        ["Risco / conflito", "Resposta"],
        [["Conteúdo gerado sem suporte em fonte", "Toda informação factual referenciada a documento e página; verificação cruzada no PT 500"],
         ["Confusão entre dado real e sintético", "Campo 'dado_sintetico' em todas as linhas; células laranja na planilha; títulos 'SIMULADO'"],
         ["Falta de competência setorial (metais preciosos, gemas)", "Consulta a especialista planejada (PT 501)"],
         ["Prazo curto (entrega 25/10/2026)", "Priorização dos riscos significativos (PT 300)"],
         ["Conflito de interesse", "Nenhum conflito conhecido; declaração no PT 200"],
         ["Norma posterior não aplicável (NBC TA 240 (R2) e 570 (R1), DOU 25/09/2026)", "Aplicadas as versões vigentes para 2025 (PT 230, registro de versões)"]],
        larg=[40, 60]),
    "resultados": "Plano de qualidade definido; revisão e EQR não executadas.",
    "conclusao": "A ausência de revisão independente é limitação relevante e está registrada; nenhuma revisão foi simulada.",
    "limitacoes": "Trabalho individual; sem sistema de gestão de qualidade de firma (NBC PA 01).",
})

# =============================================================================================== PT 230
PTS.append({
    "cod": "PT 230", "titulo": "Documentação: índice, códigos, referências, versões e arquivo",
    "norma": "NBC TA 230 (R1) - Documentação de Auditoria",
    "itens": [("230", ["7", "8", "9", "14", "15", "16", "A21", "A22", "A23"])],
    "objetivo": "Criar índice, convenção de códigos, referências cruzadas, controle de versões e procedimentos de montagem e "
                "guarda do arquivo.",
    "objeto": "Dossiê, base simulada, código, planilhas e fontes (repositório GitHub).",
    "afirmacoes": "Nível do trabalho. Risco: documentação insuficiente para um auditor experiente entender o trabalho (item 8).",
    "populacao": "Todos os arquivos do repositório.",
    "procedimentos": [
        ("Definir índice e convenção de códigos.", R, "Quadros 1 e 2"),
        ("Definir convenção de referências cruzadas e de fontes.", R, "Quadro 2"),
        ("Controlar versões por Git (histórico de commits) e registrar a versão das normas.", R, "Quadro 3"),
        ("Definir montagem (até 60 dias após o relatório - A21) e guarda (mínimo 5 anos - A23).", R, "Quadro 2"),
    ],
    "evidencias": "Estrutura de pastas no README; matriz de cobertura (05_matriz_cobertura); relação de fontes (06_fontes).",
    "anexo": "<h4>Quadro 1 - Índice do arquivo</h4>" + tabela(
        ["Seção", "Conteúdo", "Arquivo"],
        [["A - Planejamento e aceitação", "PT EC, 200, 210, 220, 230, 300, 320", "01_dossie (PDF)"],
         ["B - Riscos", "PT 240, 250, 315, 402, 550, 600", "01_dossie"],
         ["C - Respostas e evidência", "PT 330, 500, 501, 505, 510, 520, 530, 540, programas por ciclo", "01_dossie; 04_planilhas"],
         ["D - Conclusão e comunicação", "PT 260, 265, 450, 560, 570, 580, conclusão integrada", "01_dossie"],
         ["E - Base simulada", "Base de 518.271 linhas, dicionário, registro de erros, resultados", "02_base_simulada (base completa por link externo)"],
         ["F - Código", "gerar_base.py, testes_auditoria.py, calculos_pts.py, gerar_planilhas.py, gerar_dossie.py", "03_codigo"],
         ["G - Matriz e fontes", "Matriz de cobertura; relação de fontes", "05, 06"]], larg=[28, 47, 25]) +
        "<h4>Quadro 2 - Convenções</h4>" + tabela(
        ["Item", "Convenção"],
        [["Código do PT", "'PT' + número da NBC TA (ex.: PT 315); PT EC = Estrutura Conceitual; PROG-xx = programas; PT CONC = conclusão"],
         ["Riscos", "R01 a R16 (definidos no PT 315 e usados nos PTs 240, 330, 260, 265)"],
         ["Procedimentos", "Código do PT + nº sequencial (ex.: 330.07); classificação [R], [P] ou [S]"],
         ["Distorções", "D01-D08 (públicas) e S-xx (simuladas) - PT 450"],
         ["Fontes", "Sigla do documento + página do PDF (ex.: DF25 p.30). Siglas no 06_fontes"],
         ["Normas", "Item da NBC TA + página da compilação 'Consolidado Normas Aud1' (ex.: 320 item 10, p.371)"],
         ["Montagem do arquivo", "Até 60 dias após a data do relatório (A21); sem novos procedimentos nessa fase (A22)"],
         ["Guarda", "Mínimo de 5 anos a partir da data do relatório (A23); repositório público + cópia local"],
         ["Alterações após montagem", "Somente com registro de motivo, autor e data (item 16) - via commit Git"]], larg=[25, 75]) +
        "<h4>Quadro 3 - Registro de versões das normas consultadas</h4>" + tabela(
        ["Norma", "Versão aplicada ao exercício 2025", "Observação"],
        [["Estrutura Conceitual", "NBC TA Estrutura Conceitual (DOU 25/11/2015)", "Vigente"],
         ["200, 210, 230, 300, 320, 330, 450, 500, 510, 560, 580", "Versões (R1) de 2016 conforme compilação", "Vigentes"],
         ["220", "NBC TA 220 (R3), de 18/11/2021", "Vigente; alterada pela Revisão NBC 20 (2023)"],
         ["240", "NBC TA 240 (R1)", "NBC TA 240 (R2) publicada em 25/09/2026 aplica-se a períodos iniciados a partir de 01/01/2027 - não aplicável"],
         ["250", "NBC TA 250, de 07/02/2019", "Vigente"],
         ["260", "NBC TA 260 (R2)", "Revisão NBC 27 (dez/2024) incluiu o item 16A, aplicável a exercícios iniciados em 2025; não consta da compilação utilizada"],
         ["315", "NBC TA 315 (R2), de 19/08/2021", "Vigente"],
         ["540", "NBC TA 540 (R2), de 17/10/2019", "Vigente"],
         ["570", "NBC TA 570", "NBC TA 570 (R1) publicada em 25/09/2026 - aplicável a partir de 2027"],
         ["600", "NBC TA 600 (R2), de 25/10/2023", "Aplicável a períodos iniciados a partir de 01/01/2024"],
         ["265, 402, 501, 505, 520, 530, 550", "Versões originais (Resoluções CFC 2009)", "Vigentes"]], larg=[30, 32, 38]),
    "resultados": "Índice e convenções definidos; histórico de versões mantido no Git.",
    "conclusao": "A documentação permite reexecução dos cálculos e da base simulada (README, seção de reprodução).",
    "limitacoes": "A base completa (> 100 MB) fica fora do repositório (link externo), mas é reproduzível pelo código com semente fixa.",
})

# =============================================================================================== PT 240
PTS.append({
    "cod": "PT 240", "titulo": "Fraude: fatores de risco, receita e burla de controles",
    "norma": "NBC TA 240 (R1) - Responsabilidade do Auditor em Relação a Fraude",
    "itens": [("240", ["11", "15", "16", "17", "24", "25", "26", "27", "28", "31", "32", "33", "A24", "A30"])],
    "objetivo": "Avaliar fatores de risco de fraude, inclusive no reconhecimento de receitas e na burla de controles pela "
                "administração, e planejar testes de lançamentos e respostas.",
    "objeto": "Receita líquida (R$ 3.026.582 mil - DF25 p.20), estoques, lançamentos manuais e ajustes de consolidação, estimativas.",
    "afirmacoes": "Ocorrência e corte (receita); existência (estoques); valorização (estimativas); apresentação (medidas não contábeis).",
    "populacao": "DF25; FRE seções 4, 5, 7 e 8; fatos relevantes de 2026; proposta da AGO; nota 30 (incentivos).",
    "procedimentos": [
        ("Identificar fatores de risco de fraude (incentivos/pressões, oportunidades, atitudes).", R, "Quadro 1"),
        ("Reconhecer a presunção de risco de fraude na receita e definir a natureza (item 26-27).", R, "Quadro 2; R01"),
        ("Tratar a burla de controles como risco significativo (item 31) e definir testes de lançamentos (item 33(a)).", R, "Quadro 3; R02"),
        ("Executar testes de lançamentos manuais e ajustes de consolidação no razão geral.", P, "Sem acesso ao razão"),
        ("Revisão retrospectiva de estimativas (item 33(b)): provisão de estoques revertida no 1S26.", R, "PT 540"),
        ("Avaliar transações significativas fora do curso normal (item 33(c)): antecipação de recebíveis de 26/12/2025 "
         "para pagamento de dividendos intercalares.", R, "Quadro 1; PT 570"),
        ("Indagar administração, auditoria interna, comitê e canal de denúncias (itens 17-21).", P, "Sem acesso"),
        ("Testar furtos/perdas de joias em lojas por análise de dados e contagem (apropriação indébita).", S, "PT 530 (T3, contagens MUS)"),
    ],
    "evidencias": "Ver quadro 1 (fonte em cada linha). Referências: PT 315 (R01, R02, R03), PT 330, PT 520, PT 540.",
    "anexo": "<h4>Quadro 1 - Fatores de risco de fraude identificados em fontes públicas</h4>" + tabela(
        ["Categoria", "Fator", "Fonte", "Risco"],
        [["Incentivo/pressão", "Remuneração variável da Diretoria de R$ 6.422 mil em R$ 10.224 mil (63%) e ILP com metas de ROIC e TSR",
          "DF25 p.48; p.66", "R01, R02"],
         ["Incentivo/pressão", "Projeção pública de 55 a 65 aberturas em 2026 divulgada no dia da emissão das DF", "FR guidance 18/03/2026", "R01"],
         ["Incentivo/pressão", "Indicadores divulgados (SSS 11,8%; EBITDA ajustado; dias de estoque ex-GGF) e ajustes 'não recorrentes'",
          "DF25 p.3, p.11-12", "R01, R04"],
         ["Incentivo/pressão", "Lucro líquido caiu 29,8% no 1T26 vs 1T25 (80.795 x 115.038) - pressão sobre resultados de 2026",
          "ITR1 p.6", "R01 (corte de dez/25)"],
         ["Oportunidade", "Itens de alto valor e pequeno porte (joias, gemas, ouro) em 498 lojas, 3 CDs e fábrica", "DF25 p.25; FRE p.28", "R03"],
         ["Oportunidade", "Recebimentos em espécie (verificação diária prevista na política de PLD)", "FRE p.140", "R03, R10"],
         ["Oportunidade", "Operações intragrupo relevantes (vendas Conipa-Tellerina R$ 2.552.081 mil; royalties R$ 352.769 mil) e "
          "lucro não realizado de R$ 1.293.806 mil", "DF25 p.47, p.52", "R05"],
         ["Oportunidade", "Estimativas com julgamento: créditos extemporâneos, IR diferido, arrendamentos, provisões", "DF25 p.27", "R06-R09"],
         ["Oportunidade", "Antecipação de R$ 164.985 mil de recebíveis em 26/12/2025 para pagamento de dividendos em 29/12/2025",
          "DF25 p.29; p.4; p.46", "R10"],
         ["Atitude/ambiente", "Troca do Diretor Presidente e do Diretor de Operações em 11/12/2025; DRI desde 16/02/2025",
          "FRE p.180, p.187; FCA p.7", "R02"],
         ["Atitude/ambiente (mitigante)", "Canal Aberto independente, programa de integridade, auditoria interna; nenhum caso confirmado "
          "contra a administração pública em 3 anos", "FRE p.132, p.145-146", "-"]], larg=[16, 52, 18, 14]) +
        "<h4>Quadro 2 - Receita: presunção não refutada</h4>"
        "<p>A presunção do item 26 <b>não foi refutada</b>. Natureza do risco: (i) antecipação de vendas no 4T25 (R$ 1,4 bi de "
        "receita bruta no trimestre, Black Friday e Natal - DF25 p.3); (ii) corte do e-commerce, cuja receita é reconhecida na "
        "entrega ao consumidor (nota 21.1, DF25 p.52); (iii) provisão do Giftback (10% da compra) reduz a receita e depende de "
        "estimativa de resgate (DF25 p.52-53); (iv) devoluções (R$ 9.601 mil - DF25 p.53).</p>"
        "<h4>Quadro 3 - Critérios para teste de lançamentos (planejado - item 33(a))</h4>" + tabela(
        ["Critério de seleção", "Justificativa"],
        [["Lançamentos manuais em receita, estoques, CMV e provisões após o fechamento de dezembro/2025", "Ajustes de fechamento"],
         ["Lançamentos de consolidação (eliminação de LNR, IR diferido)", "Retificação de 2023 decorreu desse cálculo (DFP24 p.59)"],
         ["Débito em estoque com crédito em resultado (ou inverso) sem documento de origem", "Manipulação de margem e GGF"],
         ["Valores redondos, lançados em fins de semana/feriados, por usuários não usuais ou pela alta administração", "Indicadores clássicos"],
         ["Reversões de provisões em janeiro/fevereiro de 2026", "Viés de estimativa"],
         ["Lançamentos com descrição vaga em 'outras receitas (despesas)'", "Créditos tributários (nota 24.1)"]], larg=[60, 40]),
    "resultados": "Nenhuma evidência pública de fraude. Fatores de risco presentes geram riscos significativos R01 (receita) e "
                  "R02 (burla de controles). Na simulação, o teste de quantidade negativa (T3) e as contagens identificaram "
                  "diferenças compatíveis com perdas não baixadas (PT 530).",
    "conclusao": "Riscos de fraude avaliados e respondidos no PT 330; testes de lançamentos e indagações permanecem planejados.",
    "limitacoes": "Sem acesso ao razão geral, a atas do Comitê e aos relatos do Canal Aberto; nenhuma entrevista realizada.",
})

# =============================================================================================== PT 250
PTS.append({
    "cod": "PT 250", "titulo": "Leis e regulamentos",
    "norma": "NBC TA 250 - Consideração de Leis e Regulamentos na Auditoria de Demonstrações Contábeis",
    "itens": [("250", ["13", "14", "15", "16", "17", "18", "19", "22", "23", "A6", "A8"])],
    "objetivo": "Mapear obrigações legais relevantes, riscos de descumprimento e definir procedimentos e comunicações diante de indícios.",
    "objeto": "Ambiente legal e regulatório da Vivara e controladas.",
    "afirmacoes": "Completude e avaliação de passivos e provisões; ocorrência de receitas de subvenção; divulgação de contingências.",
    "populacao": "Notas 17, 20, 21, 24 e 28 (DF25 p.41-60); FRE seções 4 e 5; FCA; DF25 p.13.",
    "procedimentos": [
        ("Mapear leis com efeito direto nas DF (categoria do item 6(a)).", R, "Quadro 1"),
        ("Mapear leis com efeito indireto/operacional (item 6(b)).", R, "Quadro 1"),
        ("Ler notas de contingências e FRE 4.4 e conciliar provisões.", R, "PT 500 (FRE x nota 17: diferença de R$ 0,4 mil, arredondamento)"),
        ("Indagar administração e assessores jurídicos sobre descumprimentos (item 14).", P, "Carta a advogados - PT 505"),
        ("Inspecionar correspondências com SEFAZ, RFB, SUDAM e CVM (item 15).", P, "Sem acesso"),
        ("Definir comunicação à governança e ao órgão regulador diante de indícios (itens 22-29).", R, "Quadro 2"),
    ],
    "evidencias": "Ver quadro 1. Referências: PT 501 (litígios), PT 260, PT 265.",
    "anexo": "<h4>Quadro 1 - Mapa de obrigações e riscos</h4>" + tabela(
        ["Obrigação / norma", "Evidência pública", "Risco de descumprimento / efeito nas DF", "Tipo"],
        [["Lei 6.404/76 (reserva legal, dividendo mínimo, art. 133 §6º com redação da Lei 15.177/2025)", "DF25 p.13, p.46; AGO p.14-15",
          "Destinação do lucro; divulgação de equidade salarial", "Direto"],
         ["CVM - Res. 44 (fato relevante), 77 (recompra), 80 (FRE), 81 (assembleias); Regulamento do Novo Mercado",
          "FR recompra e guidance; FCA p.4", "Divulgação tempestiva; limites de recompra (10% das ações em circulação)", "Direto/indireto"],
         ["ICMS: subvenções/crédito presumido (AM, MG, ES, PE) e DIFAL/fundo de pobreza", "DF25 p.49, p.53; p.42",
          "Receita de subvenção R$ 334.056 mil; perda do benefício; provisões tributárias", "Direto"],
         ["SUDAM - redução de 75% do IRPJ (lucro da exploração) até 2033, com obrigações (reserva, não distribuição)",
          "DF25 p.48-49", "Perda do incentivo e cobrança do imposto se condições não cumpridas", "Direto"],
         ["PIS/COFINS - créditos extemporâneos (insumos) e IPI (regularização de R$ 42.841 mil + R$ 15.492 mil de juros)",
          "DF25 p.31-32, p.56", "Glosa de créditos; risco possível de R$ 50.361 mil divulgado (p.45)", "Direto"],
         ["IRPJ/CSLL - auto de infração Conipa 2021-2023 (FTI/UEA)", "DF25 p.44", "R$ 79.896 mil classificado como perda possível", "Direto"],
         ["Tema 985 STF - contribuição sobre 1/3 de férias", "DF25 p.42", "Provisão integral (perda provável)", "Direto"],
         ["Reforma tributária (EC 132/2023) - fim de PIS/COFINS em 2026 e CBS", "DF25 p.60", "Mensuração de arrendamentos líquida de créditos", "Direto"],
         ["CLT e convenções coletivas", "DF25 p.43; FRE p.244 (rotatividade 49,8%)", "Provisões trabalhistas R$ 16.318 mil; possíveis R$ 59.531 mil", "Indireto"],
         ["Código de Defesa do Consumidor", "DF25 p.43, p.44", "Ações cíveis de consumidores", "Indireto"],
         ["Lei 9.613/1998 (PLD) - comércio de joias e metais preciosos; comunicações ao COAF", "FRE p.140", "Sanções administrativas", "Indireto"],
         ["Lei 12.846/2013 (Anticorrupção)", "FRE p.140-141", "Multas; reputação", "Indireto"],
         ["LGPD (dados de clientes do varejo e e-commerce)", "FRE p.39, p.96-97", "Multas; reputação", "Indireto"],
         ["Lei 4.131 (empréstimo em moeda estrangeira) e escritura de debêntures", "DF25 p.40-41", "Vencimento antecipado (protesto > R$ 100.000 mil)", "Direto"]],
        larg=[30, 18, 38, 14]) +
        "<h4>Quadro 2 - Resposta a indícios de descumprimento</h4><p>Diante de indício: (1) obter entendimento da natureza e "
        "circunstâncias (item 19); (2) discutir com a administração e, se aplicável, com a governança (item 20); (3) obter "
        "parecer jurídico se a administração não fornecer informação suficiente; (4) avaliar efeito na opinião e nas "
        "representações formais; (5) comunicar à governança (item 22); (6) avaliar dever legal de comunicar à CVM "
        "(item 28-29). Nenhum indício foi identificado nas fontes públicas além das contingências já divulgadas.</p>",
    "resultados": "Obrigações relevantes mapeadas; contingências divulgadas são consistentes entre nota 17 e FRE 4.4.",
    "conclusao": "Não há indício público de descumprimento não divulgado. A regularização espontânea de IPI de 2021-2024 "
                 "(DF25 p.56) indica histórico de exposição tributária e reforça o risco R06/R09.",
    "limitacoes": "Sem acesso a correspondências com órgãos reguladores, cartas de advogados e livros fiscais.",
})

# =============================================================================================== PT 260
comunic = f"""
<div class="carta">
<p><b>MINUTA DIDÁTICA - COMUNICAÇÃO COM OS RESPONSÁVEIS PELA GOVERNANÇA</b> (não enviada)</p>
<p>Ao Conselho de Administração e ao Comitê de Auditoria, Riscos e Finanças da Vivara Participações S.A.</p>
<p><b>1. Responsabilidades do auditor e alcance.</b> A auditoria visa opinião sobre as DF individuais e consolidadas de 2025 elaboradas
de acordo com CPC/IFRS; não exime a administração nem a governança de suas responsabilidades. Alcance: controladora, Tellerina,
Conipa e Tellerina Panamá (PT 600). Materialidade global de R$ {n0(MG)} mil (PT 320).</p>
<p><b>2. Época.</b> Planejamento e avaliação de riscos no 3º/4º trimestre; inventários físicos em dezembro/2025 (lojas, CDs e
fábrica); trabalhos finais até a emissão em março/2026 (PT 300).</p>
<p><b>3. Riscos significativos identificados.</b> R01 receita (ocorrência/corte - fraude presumida); R02 burla de controles;
R03/R04 estoques (existência e valorização); R05 eliminação do lucro não realizado e IR diferido; R06 créditos tributários
extemporâneos e incentivos fiscais (PT 315).</p>
<p><b>4. Independência.</b> O auditor declara cumprir as exigências éticas relevantes, incluindo as de independência
aplicáveis a entidades de interesse público, e comunica relacionamentos e serviços que possam afetá-la (não identificados).</p>
<p><b>5. Assuntos qualitativos e dificuldades.</b> Inconsistências de divulgação observadas (D01 a D07 - PT 450) e em documentos
regulatórios (FRE x FCA sobre o início da KPMG; FRE 6.4 sem a Tellerina Panamá). Dificuldade principal deste trabalho: ausência de acesso a registros, pessoas e locais.</p>
<p><b>6. Distorções.</b> Distorções simuladas não corrigidas e seus efeitos (PT 450); solicitação de correção das divulgações.</p>
<p>São Paulo, [data]. Auditor (didático) - Rafaela de Sousa Barbosa, matrícula 241003384.</p>
</div>"""
PTS.append({
    "cod": "PT 260", "titulo": "Comunicação com os responsáveis pela governança",
    "norma": "NBC TA 260 (R2) - Comunicação com os Responsáveis pela Governança",
    "itens": [("260", ["11", "13", "14", "15", "16", "17", "18", "19", "21", "A29"])],
    "objetivo": "Preparar a comunicação sobre alcance, época, riscos significativos, independência e principais dificuldades.",
    "objeto": "Comunicação ao Conselho de Administração e ao Comitê de Auditoria, Riscos e Finanças.",
    "afirmacoes": "Nível das demonstrações e do trabalho.",
    "populacao": "Estrutura de governança (FRE 5.1 p.133; 7.4 p.188-189; proposta AGO p.15); PT 315; PT 450.",
    "procedimentos": [
        ("Identificar os responsáveis pela governança e o canal adequado (item 11).", R, "Quadro 1"),
        ("Preparar minuta da comunicação (itens 14-17).", R, "Minuta abaixo"),
        ("Realizar reuniões com o Comitê e obter retorno sobre riscos de fraude e leis.", P, "Sem acesso"),
        ("Avaliar adequação do processo de comunicação bidirecional (item 21).", P, "Sem acesso"),
    ],
    "evidencias": "Comitê de Auditoria, Riscos e Finanças (não estatutário), acompanha auditoria interna, riscos e controles "
                  "(FRE p.133). Presidente do Conselho é acionista de referência (FRE p.193). Conselho Fiscal instalado "
                  "(remuneração de R$ 374 mil em 2025 - DF25 p.48). Na AGO/E de 27/04/2026 estiveram presentes representantes da KPMG, do Conselho Fiscal "
                  "e do Comitê de Auditoria; as contas foram aprovadas com 37.153.987 abstenções e o limite de remuneração de 2026 teve "
                  "39.159.594 votos contrários (ATA p.1-4).",
    "anexo": "<h4>Quadro 1 - Responsáveis pela governança</h4>" + tabela(
        ["Órgão", "Papel na comunicação", "Fonte"],
        [["Conselho de Administração", "Destinatário final; aprova DF (autorização em 18/03/2026)", "DF25 p.26; FRE p.133"],
         ["Comitê de Auditoria, Riscos e Finanças", "Interlocutor técnico: riscos, controles, auditoria interna", "FRE p.133, p.188"],
         ["Conselho Fiscal", "Parecer sobre as DF à AGO", "AGO p.14; DF25 p.48"],
         ["Comitê de Pessoas, Sustentabilidade e Governança", "Casos relevantes do Canal Aberto (fraude)", "FRE p.142"]], larg=[30, 50, 20]) + comunic,
    "resultados": "Comunicação preparada com os elementos dos itens 14 a 17.",
    "conclusao": "Comunicação pronta para uso; nenhuma reunião ocorreu. A compilação de normas utilizada não contém o item 16A "
                 "(Revisão NBC 27); a minuta já menciona os requisitos de independência aplicáveis.",
    "limitacoes": "Sem retorno da governança; não é possível avaliar a comunicação bidirecional.",
})

# =============================================================================================== PT 265
PTS.append({
    "cod": "PT 265", "titulo": "Deficiências de controle interno",
    "norma": "NBC TA 265 - Comunicação de Deficiências de Controle Interno",
    "itens": [("265", ["6", "7", "8", "9", "10", "11", "A5", "A6", "A7"])],
    "objetivo": "Preparar matriz com condição, critério, causa, efeito e recomendação, distinguindo hipóteses de constatações "
                "sustentadas por evidências.",
    "objeto": "Controles sobre elaboração das DF, estoques, divulgações e documentos regulatórios.",
    "afirmacoes": "Exatidão e apresentação das divulgações; existência e valorização de estoques; consolidação.",
    "populacao": "Inconsistências públicas (PT 450, D01-D08; FRE/FCA) e exceções da base simulada (PT 530).",
    "procedimentos": [
        ("Avaliar se inconsistências públicas indicam deficiência de controle (item 7).", R, "Matriz (C1-C4)"),
        ("Avaliar exceções da base simulada como deficiências hipotéticas.", S, "Matriz (C5-C7)"),
        ("Classificar severidade (significativa ou não) - item 8 e A5-A7.", R, "Matriz"),
        ("Testar desenho e efetividade dos controles (walkthrough, reexecução).", P, "Sem acesso"),
        ("Comunicar por escrito à governança as deficiências significativas (item 9).", P, "PT 260"),
    ],
    "evidencias": "FRE 5.2.d: a administração informa que não foram reportadas deficiências significativas pela KPMG em 2025 "
                  "(FRE p.139). Retificação de 2023 por erro no IR diferido do LNR (DFP24 p.59).",
    "anexo": "<h4>Matriz de deficiências</h4>" + tabela(
        ["#", "Tipo", "Condição", "Critério", "Causa", "Efeito", "Recomendação", "Severidade"],
        [["C1", "Constatação (evidência pública)", "Erros de data, referência cruzada e somatório nas notas 9.2 e 31 e no sumário (D01-D04)",
          "CPC 26 / Res. CVM; revisão de notas antes da emissão", "Hipótese: revisão final das notas insuficiente",
          "Divulgação inexata; não altera saldos", "Checklist de revisão e conferência de somas e referências", "Não significativa"],
         ["C2", "Constatação (evidência pública)", "Comparativos e bases divergentes: provisão 2024 (D05), nota 29.3 (D06), D&A (D08)",
          "Consistência entre notas", "Hipótese: notas preparadas por áreas diferentes sem conciliação final",
          "Comparabilidade prejudicada", "Matriz de conciliação nota x BP", "Não significativa"],
         ["C3", "Constatação (evidência pública)", "FRE x FCA divergem sobre início da KPMG; FRE 6.4 omite Tellerina Panamá; "
          "conselho fiscal 'permanente'", "Res. CVM 80 (FRE/FCA)", "Hipótese: atualização parcial dos formulários",
          "Informação regulatória inconsistente", "Revisão cruzada FRE/FCA/DF pelo jurídico/RI", "Não significativa"],
         ["C4", "Constatação (evidência pública)", "Correção de erro no IR diferido do LNR (2023) e regularização de IPI 2021-2024",
          "CPC 32; legislação do IPI", "Metodologia de cálculo inadequada em exercícios anteriores",
          "Ajustes de exercícios anteriores e despesas não recorrentes", "Monitorar controles de tributos e consolidação", "A avaliar (histórico)"],
         ["C5", "Hipótese (simulação)", "Posições de estoque com quantidade negativa e duplicidades (T2/T3)", "Integridade do cadastro/ERP",
          "Ausência de bloqueio sistêmico (hipótese)", "Superavaliação/subavaliação", "Travas no ERP Capta; conciliação diária", "Não significativa (simulada)"],
         ["C6", "Hipótese (simulação)", "Itens de giro lento sem provisão e custo acima do VRL (T5/T6)", "Política da nota 7.3; CPC 16",
          "Rotina de aging sem integração com a provisão (hipótese)", "Superavaliação", "Relatório automático de aging x provisão", "A avaliar"],
         ["C7", "Hipótese (simulação)", "Entradas de janeiro/2026 no estoque de 31/12/2025 (T4) e custos unitários digitados (T7)",
          "Corte e aprovação de custos", "Falta de controle de corte e de limites de variação de custo", "Superavaliação",
          "Corte por data do documento; alerta de variação > 3x", "Significativa se confirmada (efeito de R$ 3,1 mi simulado)"]],
        larg=[4, 11, 19, 12, 13, 12, 17, 12]),
    "resultados": "4 constatações sustentadas por evidência pública (divulgação/relato) e 3 hipóteses originadas da simulação. "
                  "Nenhuma das constatações públicas, isoladamente, indica deficiência significativa sobre saldos.",
    "conclusao": "As constatações C1 a C3 são deficiências de controle sobre divulgação, de severidade não significativa. C5 a "
                 "C7 são hipóteses que exigiriam teste de controles antes de qualquer comunicação.",
    "limitacoes": "Sem walkthrough ou testes de efetividade; causas são hipóteses.",
})
