"""Exercício 01.

Maior entre Dois Números
Escreva um programa que solicite ao usuário dois números e exiba o maior entre eles.
"""

num_1 = float(input("Digite o 1º número: "))
num_2 = float(input("Digite o 2º número: "))

if num_1 > num_2:
    print(f"O 1º número é maior: {num_1}")
elif num_1 == num_2:
    print(f"Os números são iguais: {num_1}")
else:
    print(f"O 2º número é maior: {num_2}")
