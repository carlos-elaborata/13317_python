"""Exercício 08.

Cálculo de Salário
Elabore um programa que calcule o salário mensal de uma pessoa, com base nas horas
trabalhadas por mês e no valor por hora.
"""

valor_hora = float(input("Digite o valor que você ganha por hora: R$ "))
horas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario = valor_hora * horas_mes

print(f"Seu salário no referido mês é de R$ {salario:.2f}")
