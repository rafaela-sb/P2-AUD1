# -*- coding: utf-8 -*-
"""Parâmetros de auditoria (PT 320 / PT 530). Valores em R$ mil, exceto quando indicado."""
from dados_publicos import DRE

# ---------------- PT 320 - Materialidade ----------------
REFERENCIAL = "Lucro antes do IR e CS consolidado 2025 (DF25 p.20)"
LAIR_2025 = DRE["2025"]["lair"]            # 587.798
PERC_MG = 0.05
MG_CALCULADA = LAIR_2025 * PERC_MG         # 29.389,9
MG = 29_000                                # arredondamento para baixo (julgamento - PT 320)
PERC_ME = 0.60                             # auditoria inicial + inconsistências de divulgação observadas
ME = MG * PERC_ME                          # 17.400 (materialidade para execução)
PERC_TRIVIAL = 0.05
LIMITE_TRIVIAL = MG * PERC_TRIVIAL         # 1.450 (distorções claramente triviais)

# ---------------- PT 530 - Amostragem estatística por unidade monetária (MUS) ----------------
CONFIANCA = 0.95
FATOR_CONFIABILIDADE = 3.0                 # Poisson, 0 erros, 95%
FATOR_EXPANSAO = 1.6                       # para risco de aceitação incorreta de 5%
PERC_DISTORCAO_ESPERADA = 0.10             # 10% da distorção tolerável (auditoria inicial)
DISTORCAO_TOLERAVEL_RS = ME * 1000         # R$ 17.400.000
DISTORCAO_ESPERADA_RS = DISTORCAO_TOLERAVEL_RS * PERC_DISTORCAO_ESPERADA
SEMENTE = 241003384
# Fatores de limite superior (Poisson, 95%) para k = 0..10 erros
FATORES_POISSON_95 = [3.00, 4.75, 6.30, 7.76, 9.16, 10.52, 11.85, 13.15, 14.44, 15.71, 16.97]
DATA_BASE = "2025-12-31"
DESPESA_VENDA_VRL = 0.30                   # premissa sintética para VRL (preço de venda é sintético)
PERDA_DERRETIMENTO = 0.08                  # premissa sintética (política nota 7.3)
