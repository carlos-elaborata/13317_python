"""Exercício 17.

Validador de Data
Crie um programa que peça ao usuário para inserir uma data no formato dd/mm/aaaa e
verifique se esta é uma data válida.
Considere os números de dias em cada mês e anos bissextos.
"""

import calendar

# Solicita ao usuário para digitar uma data no formato dd/mm/aaaa
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Divide a string da data em dia, mês e ano
dia, mes, ano = data.split("/")

# Converte dia, mês e ano para inteiros
dia = int(dia)
mes = int(mes)
ano = int(ano)

# Início da lógica de validação

# 1. Validação do mês
if mes >= 1 and mes <= 12:
    # Se o mês é válido, prossegue

    # 2. Determinação se o ano é bissexto
    eh_bissexto = False
    if calendar.isleap(ano):
        # if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        eh_bissexto = True

    # 3. Determinação do número máximo de dias para o mês e ano informado
    dias_no_mes = 31

    if mes == 2:
        if eh_bissexto:
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    elif mes in {4, 6, 9, 11}:
        dias_no_mes = 30

    # 4. Validação do dia
    # O dia deve ser maior ou igual a 1 E menor ou igual a `dias_no_mes`
    if dia >= 1 and dia <= dias_no_mes:
        print("A data é válida.")
    else:
        print("A data é inválida.")
else:
    print("A data é inválida.")
