"""Exercício 11.

Data por Extenso
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
formato "DD de mesPorExtenso de AAAA".
A função deve validar a data para verificar se é uma data real (por exemplo, que não
exista 30 de fevereiro) e retornar None caso a data seja inválida.
"""

import calendar


def data_por_extenso(data: str):
    dias_meses = {
        1: {"nome": "Janeiro", "dias": 31},
        2: {"nome": "Fevereiro", "dias": 28},
        3: {"nome": "Março", "dias": 31},
        4: {"nome": "Abril", "dias": 30},
        5: {"nome": "Maio", "dias": 31},
        6: {"nome": "Junho", "dias": 30},
        7: {"nome": "Julho", "dias": 31},
        8: {"nome": "Agosto", "dias": 31},
        9: {"nome": "Setembro", "dias": 30},
        10: {"nome": "Outubro", "dias": 31},
        11: {"nome": "Novembro", "dias": 30},
        12: {"nome": "Dezembro", "dias": 31},
    }

    dia, mes, ano = data.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if calendar.isleap(ano):
        dias_meses[2]["dias"] = 29

    if mes < 1 or mes > 12 or dia < 1 or dia > dias_meses[mes]["dias"]:
        return None

    mes_extenso = dias_meses[mes]["nome"]

    return f"{dia:02} de {mes_extenso} de {ano}"


print(data_por_extenso("18/02/1992"))
print(data_por_extenso("33/01/1992"))
print(data_por_extenso("29/02/2025"))
print(data_por_extenso("29/02/2024"))
