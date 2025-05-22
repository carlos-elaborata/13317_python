"""Exercício 04.

Média das Notas
Faça um programa que peça quatro notas bimestrais e apresente a média delas.
"""

notas = []

notas.append(int(input("Digite a 1ª nota: ")))
notas.append(int(input("Digite a 2ª nota: ")))
notas.append(int(input("Digite a 3ª nota: ")))
notas.append(int(input("Digite a 4ª nota: ")))

# soma = notas[0] + notas[1] + notas[2] + notas[3]
media = sum(notas) / len(notas)

print(media)
