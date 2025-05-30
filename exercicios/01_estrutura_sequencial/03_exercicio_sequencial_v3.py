"""Exercício 03.

Soma de Dois Números
Desenvolva um programa que solicite dois números ao usuário e mostre o resultado da soma
desses números.
"""

numeros = []

for i in range(2):
    while True:
        try:
            numeros.append(int(input(f"Digite o {i + 1}º número: ")))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

soma = sum(numeros)
print(f"A soma de {numeros[0]} com {numeros[1]} resulta em {soma}.")
