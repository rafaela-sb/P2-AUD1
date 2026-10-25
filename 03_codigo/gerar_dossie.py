# -*- coding: utf-8 -*-
"""Gera o dossiê em HTML e PDF (Chromium via Playwright): 01_dossie/Dossie_Auditoria_Vivara_241003384.pdf
Executar após: gerar_base.py, testes_auditoria.py, calculos_pts.py (e gerar_planilhas.py)."""
import os, re, subprocess, html
from dossie_util import tabela, itens_norma, CLASSE, MATRICULA, NOME, DATA_PREP, n0, n2, CALC, TST
import conteudo_a, conteudo_b, conteudo_c
from conteudo_d import IDENT, PROGS, BASE_SEC, CONC, MATRIZ, FONTES

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "..", "01_dossie")
os.makedirs(OUT, exist_ok=True)

ORDEM = ["PT EC", "PT 200", "PT 210", "PT 220", "PT 230", "PT 240", "PT 250", "PT 260", "PT 265", "PT 300", "PT 315",
         "PT 320", "PT 330", "PT 402", "PT 450", "PT 500", "PT 501", "PT 505", "PT 510", "PT 520", "PT 530", "PT 540",
         "PT 550", "PT 560", "PT 570", "PT 580", "PT 600"]
TODOS = {p["cod"]: p for m in (conteudo_a, conteudo_b, conteudo_c) for p in m.PTS}
assert set(ORDEM) == set(TODOS), set(ORDEM) ^ set(TODOS)

CSS = """
@page { size: A4; margin: 17mm 14mm 16mm 14mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 8.6pt; color: #000; line-height: 1.38; }
h1 { font-size: 18pt; color: #000; margin: 0 0 6px 0; }
h2 { font-size: 12.5pt; color: #000; border-bottom: 1.5px solid #000; padding: 2px 0 3px 0; margin: 0 0 8px 0; }
h3 { font-size: 9.6pt; color: #000; border-bottom: 0.5px solid #888; margin: 10px 0 4px 0; padding-bottom: 1px; }
h4 { font-size: 8.8pt; color: #000; margin: 8px 0 3px 0; }
p { margin: 3px 0 5px 0; text-align: justify; }
ul, ol { margin: 2px 0 6px 16px; padding-left: 8px; }
li { margin-bottom: 2px; }
table.t { border-collapse: collapse; width: 100%; margin: 4px 0 8px 0; table-layout: fixed; }
table.t th { background: #EDEDED; color: #000; font-weight: bold; text-align: left; border: 0.5px solid #777; padding: 3px 4px; font-size: 7.8pt; }
table.t td { border: 0.5px solid #999; padding: 3px 4px; vertical-align: top; font-size: 7.8pt; word-wrap: break-word; overflow-wrap: anywhere; }
table.small td, table.small th { font-size: 7.1pt; padding: 2px 3px; }
.pt { page-break-before: always; }
.head td { font-size: 8pt; }
.head td.k { background: #F3F3F3; font-weight: bold; width: 17%; }
.cl { font-size: 7.4pt; }
.ok { } .nok { font-weight: bold; }
.sign { margin-top: 10px; border: 0.5px solid #777; padding: 5px 7px; font-size: 7.6pt; }
.carta { border: 0.5px solid #777; padding: 7px 10px; margin: 6px 0; font-size: 8pt; }
.nota { font-size: 7.6pt; color: #333; }
.capa { text-align: left; padding-top: 60px; }
.capa .sub { font-size: 11.5pt; margin: 4px 0 18px 0; }
.box { border: 0.5px solid #000; padding: 8px 10px; margin: 16px 0; font-size: 8.8pt; }
.toc td { font-size: 8.4pt; padding: 2px 4px; border-bottom: 0.5px dotted #999; }
.sim { font-weight: bold; }
"""


def cl(c):
    return f'<span class="cl">[{c}] {CLASSE[c]}</span>'


def render_pt(p, pagina=None):
    itens = "; ".join(f"NBC TA {n if n != 'EC' else 'Estrutura Conceitual'}: itens {itens_norma(n, i)}" for n, i in p["itens"])
    head = tabela(["", ""], [], cls="t head")  # placeholder
    head = ('<table class="t head"><tbody>'
            f'<tr><td class="k">Código</td><td><b>{p["cod"]}</b></td><td class="k">Data de preparação</td><td>{DATA_PREP}</td></tr>'
            f'<tr><td class="k">Título</td><td colspan="3">{p["titulo"]}</td></tr>'
            f'<tr><td class="k">Norma</td><td colspan="3">{p["norma"]}</td></tr>'
            f'<tr><td class="k">Itens utilizados (página na compilação)</td><td colspan="3">{itens}</td></tr>'
            f'<tr><td class="k">Preparador</td><td>{NOME} - matrícula {MATRICULA}</td><td class="k">Revisão</td><td>Campo de revisão: ______________ (não preenchido)</td></tr>'
            '</tbody></table>')
    procs = tabela(["#", "Procedimento", "Classificação", "Referência / evidência"],
                   [[f"{p['cod'].replace('PT ', '')}.{i:02d}", t, cl(c), r] for i, (t, c, r) in enumerate(p["procedimentos"], 1)],
                   larg=[7, 55, 18, 20])
    return f"""<section class="pt" id="{p['cod'].replace(' ', '-')}">
<h2>{p['cod']} - {p['titulo']}</h2>{head}
<h3>1. Objetivo e conta, processo ou divulgação examinada</h3><p><b>Objetivo:</b> {p['objetivo']}</p><p><b>Objeto examinado:</b> {p['objeto']}</p>
<h3>2. Afirmações relevantes e riscos identificados</h3><p>{p['afirmacoes']}</p>
<h3>3. População, fontes e critérios de seleção</h3><p>{p['populacao']}</p>
<h3>4. Procedimentos planejados ou executados</h3>{procs}
<h3>5. Evidências e referências cruzadas</h3><p>{p['evidencias']}</p>
<h3>6. Resultados e exceções</h3><p>{p['resultados']}</p>{p.get('anexo', '')}
<h3>7. Conclusão</h3><p>{p['conclusao']}</p>
<h3>8. Limitações</h3><p>{p['limitacoes']}</p>
<div class="sign"><b>Preparado por:</b> {NOME}, matrícula {MATRICULA}, em {DATA_PREP}. Conteúdo elaborado com uso de inteligência artificial, sob
responsabilidade do preparador. &nbsp;|&nbsp; <b>Revisado por:</b> ____________________ &nbsp; <b>Data:</b> ___/___/______
<br><i>Campo de revisão não preenchido: nenhuma revisão por terceiros foi realizada nem simulada.</i></div>
</section>"""


def render_prog(g):
    return f"""<h3>{g['cod']} - {g['titulo']}</h3><p><b>Riscos cobertos:</b> {g['riscos']}</p>{g['tabela']}"""


def montar(paginas=None):
    pg = paginas or {}
    secoes = [("CAPA", "Capa e identificação")] + \
             [(c, f"{c} - {TODOS[c]['titulo']}") for c in ORDEM] + \
             [("PROG", "Programas de auditoria por ciclo (PROG-01 a PROG-06)"), ("BASE", "Base de dados simulada - estoques"),
              ("CONC", "Conclusão integrada"), ("MATRIZ", "Matriz de cobertura das normas"), ("FONTES", "Relação das fontes utilizadas")]
    toc = "<table class='t toc'><tbody>" + "".join(
        f"<tr><td>{t}</td><td style='width:12%;text-align:right'>{pg.get(c, '')}</td></tr>" for c, t in secoes) + "</tbody></table>"
    capa = f"""<div class="capa">
<p style="font-size:10pt;color:#555">UNIVERSIDADE DE BRASÍLIA - UnB · Auditoria 1 - CCA0024 - Turma 02 - 2026.2 · P2</p>
<h1>Dossiê de Auditoria</h1>
<div class="sub">Vivara Participações S.A. (VIVA3) · Demonstrações contábeis individuais e consolidadas de 31/12/2025</div>
<p><b>Preparadora:</b> {NOME} - matrícula {MATRICULA} &nbsp;·&nbsp; <b>Data:</b> {DATA_PREP} &nbsp;·&nbsp; <b>Trabalho individual</b></p>
<div class="box"><b>Natureza do documento.</b> Trabalho acadêmico. Não constitui opinião profissional independente nem relatório de
auditoria. Nenhum contato foi feito com a companhia, seus auditores, clientes ou fornecedores. Confirmações, entrevistas, inspeções
físicas e acessos a sistemas <b>não</b> foram realizados. Dados identificados como <span class="sim">SIMULADO</span> são sintéticos
e não representam registros reais da Vivara. Conteúdo elaborado com uso de inteligência artificial (ver README).</div>
<h3>Identificação da companhia, nome empresarial e código de negociação</h3>{IDENT}
<h3>Sumário</h3>{toc}</div>"""
    siglas = tabela(["Sigla", "Documento"], [[f[0], f[1]] for f in FONTES], larg=[12, 88])
    leg = f"""<section class="pt" id="LEG"><h2>Legenda, siglas e convenções</h2>
<h3>Classificação dos procedimentos</h3>{tabela(["Marca", "Significado"], [[cl("R"), "Executado com documentos e informações efetivamente disponíveis ao público"],
    [cl("P"), "Detalhado, mas não executado por depender de informações internas ou de contato vedado"],
    [cl("S"), "Executado com dados sintéticos, identificados e separados dos dados reais"]], larg=[30, 70])}
<h3>Siglas das fontes (páginas = numeração do arquivo PDF)</h3>{siglas}
<h3>Convenções</h3><ul><li>Valores em R$ mil, salvo indicação (a base simulada usa R$).</li>
<li>Referência a normas: item da NBC TA e página na compilação "Consolidado Normas Aud1" (fonte NORMAS).</li>
<li>Riscos R01-R16 definidos no PT 315; distorções D01-D08 e S-xx no PT 450; procedimentos numerados por PT (ex.: 330.03).</li>
<li>Materialidade: MG R$ {n0(CALC['PT320']['MG'])} mil; ME R$ {n0(CALC['PT320']['ME'])} mil; limite trivial R$ {n0(CALC['PT320']['trivial'])} mil.</li>
<li>Data de corte dos eventos subsequentes: 18/03/2026.</li><li>Arquivos de apoio: 02_base_simulada, 03_codigo, 04_planilhas, 05_matriz_cobertura, 06_fontes.</li></ul></section>"""
    pts = "".join(render_pt(TODOS[c]) for c in ORDEM)
    prog = '<section class="pt" id="PROG"><h2>Programas de auditoria por ciclo</h2><p>Programas para receitas, disponibilidades, ' \
           'estoques, imobilizado, passivos e estimativas, vinculados aos riscos do PT 315 e às respostas do PT 330. ' \
           'Classificação: [R] realizado com evidência pública; [P] planejado; [S] simulado.</p>' + \
           "".join(render_prog(g) for g in PROGS) + '<div class="sign"><b>Preparado por:</b> ' + NOME + ', matrícula ' + MATRICULA + \
           f', em {DATA_PREP} (com uso de IA). | <b>Revisado por:</b> ____________ (não preenchido)</div></section>'
    base = f"""<section class="pt" id="BASE"><h2>Base de dados simulada - Estoques (DADOS SINTÉTICOS)</h2>
<p><b>Aviso:</b> todos os registros descritos nesta seção são fictícios, gerados por programa (03_codigo/gerar_base.py) para fins
didáticos, e não são registros reais da Vivara Participações S.A. ou de suas controladas.</p>
<h3>1. Justificativa da conta e materialidade</h3>{BASE_SEC['justificativa']}
<h3>2. Premissas</h3>{BASE_SEC['premissas']}<h3>3. Método de geração</h3>{BASE_SEC['metodo']}
<h3>4. Tamanho e conciliação</h3><p>{n0(TST['linhas_base'])} linhas (registros individuais). Conciliação com o saldo contábil: diferença
de R$ 0,00 por classe, no total, na provisão e no lucro não realizado (PT 500, quadro 3). A base completa (≈ 150 MB) é disponibilizada
por link externo indicado no README e pode ser reproduzida pelo código.</p>
<h3>5. Erros inseridos (registro em 02_base_simulada/registro_erros_inseridos.csv)</h3>{BASE_SEC['erros']}
<p class="nota">O registro de erros é o gabarito: não é lido por nenhuma etapa de detecção, apenas na comparação final (PT 450, quadro 3).</p>
<h3>6. Dicionário de variáveis</h3>{BASE_SEC['dicionario']}
<h3>7. Uso nos procedimentos</h3><p>Seleção de amostra MUS, testes de 100%, identificação e investigação de exceções, projeção de erros e
avaliação de resultados: PT 530; acumulação e comparação inseridos x identificados: PT 450; conciliação: PT 500; eliminação de lucro
não realizado: PT 600.</p></section>"""
    conc = f'<section class="pt" id="CONC"><h2>Conclusão integrada</h2>{CONC}<div class="sign"><b>Preparado por:</b> {NOME}, matrícula ' \
           f'{MATRICULA}, em {DATA_PREP} (com uso de IA). | <b>Revisado por:</b> ____________ (não preenchido)</div></section>'
    matriz = '<section class="pt" id="MATRIZ"><h2>Matriz de cobertura das normas</h2>' + tabela(
        ["Norma (versão aplicada)", "Papel de trabalho principal", "Itens centrais", "PTs relacionados"], MATRIZ, larg=[26, 24, 24, 26]) + \
        "<p class='nota'>Versões: ver PT 230, quadro 3. Matriz também em 05_matriz_cobertura.</p></section>"
    fontes = '<section class="pt" id="FONTES"><h2>Relação das fontes utilizadas</h2>' + tabela(
        ["Sigla", "Documento", "Exercício", "Endereço eletrônico", "Data de acesso", "Páginas utilizadas"],
        [[f[0], f[1], f[2], f'<span style="font-size:6.6pt">{html.escape(f[3])}</span>', f[4], f[5]] for f in FONTES],
        cls="t small", larg=[7, 24, 9, 35, 10, 15]) + \
        "<p class='nota'>(*) Correspondência entre os dois links de fatos relevantes e os documentos inferida pela ordem em que foram " \
        "informados; conferir. Datas de acesso informadas pelo preparador no momento do download. Páginas referem-se à numeração " \
        "do arquivo PDF.</p></section>"
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Dossiê de Auditoria - Vivara 2025</title>" \
           f"<style>{CSS}</style></head><body>{capa}{pts}{prog}{base}{conc}{matriz}{fontes}</body></html>", secoes


def pdf(html_path, pdf_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(html_path))
        pg.pdf(path=pdf_path, format="A4", print_background=True, display_header_footer=True,
               margin={"top": "17mm", "bottom": "16mm", "left": "14mm", "right": "14mm"},
               header_template="<div style='font-size:7px;width:100%;padding:0 14mm;color:#000;display:flex;justify-content:space-between'>"
                               "<span>Dossiê de Auditoria · Vivara Participações S.A. · Exercício 2025</span><span>Rafaela de Sousa Barbosa · Matrícula 241003384 · Trabalho acadêmico</span></div>",
               footer_template="<div style='font-size:7px;width:100%;padding:0 14mm;color:#000;display:flex;justify-content:space-between'>"
                               "<span>Vivara Participações S.A. · 31/12/2025</span>"
                               "<span>Página <span class='pageNumber'></span> de <span class='totalPages'></span></span></div>")
        b.close()


def localizar_paginas(pdf_path, secoes):
    txt = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True).stdout.split("\f")
    unicos = {"LEG": "Classificação dos procedimentos", "PROG": "Riscos cobertos", "BASE": "Justificativa da conta e materialidade",
              "CONC": "Riscos. Seis riscos significativos", "MATRIZ": "Norma (versão aplicada)", "FONTES": "Endereço eletrônico"}
    res = {"CAPA": 1}
    for cod, titulo in secoes:
        if cod == "CAPA":
            continue
        for i, t in enumerate(txt, start=1):
            if i <= 2:
                continue
            if cod in unicos:
                if unicos[cod] in t:
                    res[cod] = i; break
            elif re.sub(r"\s+", " ", f"{cod} - {TODOS[cod]['titulo'][:30]}") in re.sub(r"\s+", " ", t):
                res[cod] = i; break
    return res


def main():
    h, secoes = montar()
    hp = os.path.join(OUT, "dossie.html"); pp = os.path.join(OUT, "Dossie_Auditoria_Vivara_241003384.pdf")
    open(hp, "w", encoding="utf-8").write(h)
    pdf(hp, pp)
    pags = localizar_paginas(pp, secoes)
    for _ in range(3):   # repete até o sumário refletir as páginas reais
        h, _ = montar(pags)
        open(hp, "w", encoding="utf-8").write(h)
        pdf(hp, pp)
        novas = localizar_paginas(pp, secoes)
        if novas == pags:
            break
        pags = novas
    print("páginas:", pags)


if __name__ == "__main__":
    main()
