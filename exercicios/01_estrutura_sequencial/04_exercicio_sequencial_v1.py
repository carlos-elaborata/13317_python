"""Exercício 04.

Média das Notas
Faça um programa que peça quatro notas bimestrais e apresente a média delas.
"""

nota_1 = int(input("Digite a 1ª nota: "))
nota_2 = int(input("Digite a 2ª nota: "))
nota_3 = int(input("Digite a 3ª nota: "))
nota_4 = int(input("Digite a 4ª nota: "))

soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4
# media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(media)
