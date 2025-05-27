"""Exercício 21.

Cálculo de Fatorial
Desenvolva um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário.
Exemplo:
    5! = 5 x 4 x 3 x 2 x 1 = 120
"""

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

termos_fatorial = []

for i in range(numero, 0, -1):
    fatorial = fatorial * i
    termos_fatorial.append(str(i))

expressao_fatorial = f"{numero}! = " + " x ".join(termos_fatorial) + f" = {fatorial}"
print(expressao_fatorial)
