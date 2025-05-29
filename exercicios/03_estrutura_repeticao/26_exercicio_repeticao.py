"""Exercício 26.

Simulação de Eleição
Faça um programa que peça o número total de eleitores e registre o voto de cada um em
três candidatos disponíveis, mostrando ao final o número de votos de cada candidato.
"""

total_eleitores = int(input("Informe o número total de eleitores: "))

# votos = []
# for e in range(total_eleitores):
#     votos.append(int(input(f"Eleitor {e + 1}, vote (1, 2 ou 3 para os candidatos): ")))

votos = [
    int(input(f"Eleitor {e + 1}, vote (1, 2 ou 3 para os candidatos): "))
    for e in range(total_eleitores)
]

print(f"Votos para o Candidato 1: {votos.count(1)}")
print(f"Votos para o Candidato 2: {votos.count(2)}")
print(f"Votos para o Candidato 3: {votos.count(3)}")
