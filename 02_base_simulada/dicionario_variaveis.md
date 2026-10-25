# Dicionário de variáveis - base simulada de estoques (DADOS SINTÉTICOS)

Arquivo: `base_estoques_sintetica_31122025.csv` (separador `;`, decimal `,`, datas `AAAA-MM-DD`, UTF-8).

| Variável | Tipo | Descrição | Origem |
|---|---|---|---|
| id_registro | texto | Identificador único do registro sintético (SIM-EST-nnnnnnn) | Sintético |
| dado_sintetico | texto | Marca obrigatória: 'SIM - REGISTRO FICTICIO PARA FINS DIDATICOS' | Sintético |
| data_base | data | 31/12/2025 | Público (data das DF) |
| entidade | texto | TELLERINA, CONIPA ou TELLERINA_PANAMA | Estrutura pública (nota 1); alocação sintética |
| cod_local / tipo_local | texto | Código e tipo do local: LOJA_VIVARA (267), LOJA_LIFE (219), QUIOSQUE (11), LOJA_PANAMA (1), CENTRO_DISTRIBUICAO (3), FABRICA, FILIAL_COMPRAS, EM_TRANSITO | Quantidades públicas (nota 1; FRE p.28); códigos sintéticos |
| classe_estoque | texto | PRODUTO_ACABADO, MATERIA_PRIMA, MAT_CONSUMO_EMBALAGEM, EM_TRANSITO | Público (nota 7.2) |
| conta_contabil_sintetica | texto | 1.1.04.01 a 1.1.04.05 | Sintético |
| categoria / subcategoria | texto | JOIAS, LIFE, RELOGIOS, ACESSORIOS; OURO, PRATA, DIAMANTES etc. | Categorias públicas (nota 23); subcategorias sintéticas |
| cod_sku / lote | texto | Código do item e do lote | Sintético |
| origem | texto | FABRICACAO_PROPRIA_MANAUS, REVENDA_IMPORTADA, REVENDA_NACIONAL, COMPRA_NACIONAL, COMPRA_IMPORTADA, TRANSFERENCIA_INTERNA | Proporção de produção própria pública (DF25 p.3); demais sintéticas |
| unidade | texto | UN, G (gramas), CT (quilates) | Sintético |
| quantidade | número | Quantidade registrada | Sintético |
| custo_unitario | R$ | Custo médio ponderado unitário (consolidado) | Sintético, calibrado ao saldo |
| valor_contabil | R$ | Valor bruto registrado (= quantidade x custo, salvo erro inserido E7) | Sintético |
| provisao_perda | R$ | Provisão para perdas (giro lento/derretimento) | Total = R$ 4.688.000 (nota 7.3) |
| valor_liquido | R$ | valor_contabil - provisao_perda | Total = R$ 1.478.926.000 (BP) |
| ggf_alocado | R$ | Parcela informativa de GGF (7% do valor de itens fabricados) | Sintético |
| custo_transferencia_unitario | R$ | Custo na Tellerina a preço de transferência intragrupo | Sintético |
| margem_intragrupo | número | Margem calibrada para o LNR (1,878905) | Calibrada a dado público |
| lucro_nao_realizado_eliminado | R$ | LNR eliminado na consolidação | Total = R$ 1.293.806.000 (nota 20.9) |
| preco_venda_unitario | R$ | Preço de venda (para teste de VRL) | Sintético |
| colecao_descontinuada / passivel_derretimento | S/N | Atributos para a política de provisão | Política pública (nota 7.3); atribuição sintética |
| data_ultima_entrada / data_ultima_saida / dias_sem_giro | data / número | Movimentação e aging | Sintético |
| data_ultimo_inventario_interno | data | Última contagem interna | Sintético (frequências do FRE p.137-138) |
