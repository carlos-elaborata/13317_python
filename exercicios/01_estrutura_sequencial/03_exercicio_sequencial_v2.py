"""Exercício 03.

Soma de Dois Números
Desenvolva um programa que solicite dois números ao usuário e mostre o resultado da soma
desses números.
"""

numeros = []

numeros.append(int(input("Digite o 1º número: ")))
numeros.append(int(input("Digite o 2º número: ")))

soma = sum(numeros)
print(f"A soma de {numeros[0]} com {numeros[1]} resulta em {soma}.")
