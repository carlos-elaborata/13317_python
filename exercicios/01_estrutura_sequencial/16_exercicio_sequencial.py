"""Exercício 16.

Loja de Tintas (Simples)
Faça um programa para uma loja de tintas.
O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
Considere que cada litro de tinta cobre uma área de 7 metros quadrados e que a tinta é
vendida em latas de 18 litros, custando R$ 570,00 cada.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""

import math

# Define a cobertura da tinta, o volume da lata e o custo por lata
cobertura_tinta = 7  # metros quadrados cobertos por litro de tinta
lata_litros = 18  # litros por lata
lata_preco = 570  # reais por lata de 18 litros

# Solicita o tamanho da área a ser pintada em metros quadrados.
area = float(input("Digite o tamanho da área a ser pintada (m²): "))

# Calcula o total de litros de tinta necessários
litros_necessarios = area / cobertura_tinta

# Calcula a quantidade de latas necessárias
latas_necessarias = math.ceil(litros_necessarios / lata_litros)

# Calcula o custo total baseado no número de latas necessárias
preco_total = latas_necessarias * lata_preco

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total das latas de tinta necessárias: R$ {preco_total:.2f}")
