"""Exercício 05.

Avaliação do Aluno
Implemente um programa que leia duas notas parciais de um aluno, calcule a média e
exiba "Aprovado" se a média for maior ou igual a sete, "Reprovado" se for menor que
sete, e "Aprovado com Distinção" se a média for igual a dez.
"""

notas = []

for i in range(2):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite novamente.")
        nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append()


media = sum(notas) / len(notas)

print(f"Média: {media}")

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
