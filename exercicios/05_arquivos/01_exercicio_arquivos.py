"""Exercício 01.

Filtragem de Endereços de IP
Faça um programa que leia um arquivo de texto contendo uma lista de endereços de IP e
gere outro arquivo, contendo um relatório dos endereços de IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
    200.135.80.9
    192.168.1.1
    8.35.67.74
    257.32.4.5
    85.345.1.2
    1.2.3.4
    9.8.234.5
    192.168.0.256
O arquivo de saída deve ser no formato:
    [Endereços válidos:]
    200.135.80.9
    192.168.1.1
    8.35.67.74
    1.2.3.4
    9.8.234.5

    [Endereços inválidos:]
    257.32.4.5
    85.345.1.2
    192.168.0.256
"""


def validar_ip(ip: str):
    numeros = ip.split(".")

    if len(numeros) != 4:
        return False

    for numero in numeros:
        numero = numero.strip()

        if not numero.isdigit() or int(numero) < 0 or int(numero) > 255:
            return False

    return True


entrada = open("01_ips.txt", "r")
ips = entrada.readlines()
entrada.close()

validos = []
invalidos = []

for ip in ips:
    if validar_ip(ip):
        validos.append(ip)
    else:
        invalidos.append(ip)

saida = open("01_ips_relatorio.txt", "w")
saida.write("[Endereços válidos:]\n")
saida.writelines(validos)
saida.write("\n[Endereços inválidos:]\ns")
saida.writelines(invalidos)
saida.close()

print("Relatório gerado com sucesso.")
