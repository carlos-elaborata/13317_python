"""Exercício 02.

Avaliação de Valor
Crie um programa que peça um número ao usuário e informe se este é positivo ou
negativo.
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero == 0:
    print(f"O número {numero} é igual a zero.")
else:
    print(f"O número {numero} é negativo.")
