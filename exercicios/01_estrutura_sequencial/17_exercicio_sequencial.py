"""Exercício 17.

Loja de Tintas (Otimizada)
Faça um programa para uma loja de tintas.
O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
Considere que cada litro de tinta cobre uma área de 7 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 570,00 ou em galões de 3,5 litros, que
custam R$ 130,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em
3 situações:
    a. Comprar apenas latas de 18 litros;
    b. Comprar apenas galões de 3,5 litros;
    c. Uma combinação de ambos de forma que o custo seja minimizado.
Adicione 10% de folga à quantidade de tinta a ser comprada e arredonde os valores de
forma que somente latas cheias sejam vendidas.
"""

import math

# Constantes
COBERTURA_TINTA = 7  # metros quadrados por litro
LATA_LITROS = 18  # litros por lata
LATA_PRECO = 570  # reais por lata
GALAO_LITROS = 3.5  # litros por galão
GALAO_PRECO = 130  # reais por galão
FOLGA = 1.10  # 10% de folga

# Solicita o tamanho da área a ser pintada em metros quadrados.
area = float(input("Digite o tamanho da área a ser pintada (m²): "))

# Calcula o total de litros de tinta necessários e adiciona 10% de folga
litros_necessarios = area / COBERTURA_TINTA * FOLGA

# Calcula a quantidade de latas necessárias arredondando para cima
latas_necessarias = math.ceil(litros_necessarios / LATA_LITROS)
# Calcula a quantidade de galões necessárias arredondando para cima
galoes_necessarios = math.ceil(litros_necessarios / GALAO_LITROS)

# Calcula o preço total ao comprar apenas latas
latas_somente = latas_necessarias * LATA_PRECO
# Calcula o preço total ao comprar apenas galões
galoes_somente = galoes_necessarios * GALAO_PRECO

# Para o cenário misto, calcula primeiro o número de latas arredondando para baixo
latas_mista = math.floor(litros_necessarios / LATA_LITROS)
# Calcula os litros restantes depois de usar as latas
litros_restantes = litros_necessarios - (latas_mista * LATA_LITROS)
# Calcula o número de galões necessários para os litros restantes, arredondando para
# cima
galoes_misto = math.ceil(litros_restantes / GALAO_LITROS)
# Calcula o custo misto somando o custo das latas e dos galões
preco_misto = latas_mista * LATA_PRECO + galoes_misto * GALAO_PRECO

# Exibe os resultado
print(f"\nQuantidade de latas de 18 litros necessárias: {latas_necessarias}")
print(f"Preço total ao comprar apenas latas de 18 litros: R$ {latas_somente:.2f}")
print(f"\nQuantidade de galões de 3,5 litros necessárias: {galoes_necessarios}")
print(f"Preço total ao comprar apenas galões de 3,5 litros: R$ {galoes_somente:.2f}")
print("\nMelhor combinação (latas de 18 litros e galões de 3,5 litros):")
print(f"Quantidade de latas de 18 litros: {latas_mista}")
print(f"Quantidade de galões de 3,5 litros: {galoes_misto}")
print(f"Preço total da melhor combinação: R$ {preco_misto:.2f}")
