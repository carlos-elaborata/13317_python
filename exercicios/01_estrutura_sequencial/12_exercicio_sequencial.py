"""Exercício 12.

Peso Ideal (Homens)
Crie um programa que calcule o peso ideal de um homem com base na sua altura.
Fórmula:
    (72.7 * h) - 58
"""

altura = float(input("Digite a altura da pessoa em metros: "))
nome = "João"
peso_ideal = (72.7 * altura) - 58

mensagem = f"O peso ideal para o {nome}, de altura de {altura} metros, é de {peso_ideal:.1f} kg."

print(mensagem)
