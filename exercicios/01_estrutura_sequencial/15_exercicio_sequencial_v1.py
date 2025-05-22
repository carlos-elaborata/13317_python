"""Exercício 15.

Cálculo de Salário com Descontos
Escreva um programa que solicite ao usuário o valor que ele ganha por hora e o número
de horas trabalhadas no mês.
Calcule e mostre o salário bruto, os valores descontados para o Imposto de Renda (11%),
o INSS (8%) e o sindicato (5%), além do salário líquido (salário bruto - descontos).
Mostre os dados para o usuário conforme a tabela abaixo:
    (+) Salário bruto: R$
    (-) IR (11%): R$
    (-) INSS (8%): R$
    (-) Sindicato (5%): R$
    (-) Descontos: R$
    (=) Salário líquido: R$
"""

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_mes = float(input("Digite o nṹmero de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_mes

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f"(+) Salário bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR (11%): R$ {imposto_renda:.2f}")
print(f"(-) INSS (8%): R$ {inss:.2f}")
print(f"(-) Sindicato (5%): R$ {sindicato:.2f}")
print(f"(-) Descontos: R$ {descontos:.2f}")
print(f"(=) Salário líquido: R$ {salario_liquido:.2f}")
