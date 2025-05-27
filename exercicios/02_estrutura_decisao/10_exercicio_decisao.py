"""Exercício 10.

Aumento Salarial
Implemente um programa que calcule o reajuste salarial dos colaboradores de uma
organização conforme a seguinte tabela de critérios, baseando-se no salário atual:
    a. Salários até R$ 280,00 (inclusive): Aumento de 20%
    b. Salários até R$ 700,00 (inclusive): Aumento de 15%
    c. Salários até R$ 1500,00 (inclusive): Aumento de 10%
    d. Salários acima de R$ 1500,00: Aumento de 5%
O programa deve exibir o salário antes do reajuste, o percentual aplicado, o valor do
aumento e o novo salário.
"""

salario_atual = float(input("Qual é o salário atual do colaborador? "))

percentual = None

if salario_atual > 0 and salario_atual <= 280:
    percentual = 0.2
elif salario_atual > 280 and salario_atual <= 700:
    percentual = 0.15
elif salario_atual > 700 and salario_atual <= 1500:
    percentual = 0.1
elif salario_atual > 1500:
    percentual = 0.05
else:
    print("Valor inválido!")

if percentual is not None:
    aumento = salario_atual * percentual
    novo_salario = salario_atual + aumento

    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual * 100}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
