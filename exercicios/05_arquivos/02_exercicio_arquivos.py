"""Exercício 02.

Relatório de Uso do Espaço em Disco
Desenvolva um programa que gere um relatório ordenado do uso de espaço em disco por
usuário, a partir das informações contidas em um arquivo de texto.
O arquivo "usuarios.txt" possui o seguinte formato:
    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125
O programa deve criar um arquivo "relatório.txt" no seguinte formato, ordenando os
usuários pelo espaço utilizado, de forma decrescente:
    ACME Inc.         Uso do espaço em disco pelos usuários
    -------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso

    1    anderson       1187,99 MB           46,02%
    2    rosemary       752,88 MB            29,16%
    3    alexandre      434,99 MB            16,85%
    4    antonio        117,73 MB            4,56%
    5    carlos         87,03 MB             3,37%
    6    cesar          0,94 MB              0,04%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
Observação: Utilize 1 KB = 1024 bytes e 1 MB = 1024 KB.
"""

import pathlib


def bytes_para_megabytes(tamanho_em_bytes):
    return tamanho_em_bytes / 1024**2


def calcular_porcentagem_uso(espaco_usuario, espaco_total):
    return espaco_usuario / espaco_total * 100


BASE_DIR = pathlib.Path(__file__).parent

entrada = open(BASE_DIR / "arquivos" / "02_usuarios.txt", "r", encoding="utf8")
linhas = entrada.readlines()
entrada.close()

usuarios = []
total_espaco_ocupado = 0

for linha in linhas:
    nome, espaco = linha.split()
    espaco = int(espaco)
    usuarios.append((nome, espaco))
    total_espaco_ocupado += espaco

usuarios.sort(key=lambda u: u[1], reverse=True)

relatorio = open(
    BASE_DIR / "arquivos" / "02_usuarios_relatorio.txt",
    "w",
    encoding="utf8",
)
relatorio.write("ACME Inc.\tUso do espaço em disco pelos usuários\n")
relatorio.write("-" * 49 + "\n")
txt_nr = "Nr."
txt_usuario = "Usuário"
txt_espaco = "Espaço utilizado"
txt_prc_uso = "% do uso"
relatorio.write(f"{txt_nr:<5}{txt_usuario:<15}{txt_espaco:<20}{txt_prc_uso:<8}\n\n")
for indice, (usuario, espaco) in enumerate(usuarios, 1):
    espaco_mb = bytes_para_megabytes(espaco)
    prc_ocupado = calcular_porcentagem_uso(espaco, total_espaco_ocupado)

    txt_espaco_mb = f"{espaco_mb:.2f} MB".replace(".", ",")
    txt_prc_uso = f"{prc_ocupado:.2f}%".replace(".", ",")

    relatorio.write(f"{indice:<5}{usuario:<15}{txt_espaco_mb:<20}{txt_prc_uso:<8}\n")

espaco_total_mb = bytes_para_megabytes(total_espaco_ocupado)
espaco_medio_mb = espaco_total_mb / len(usuarios)

relatorio.write(f"\nEspaço total ocupado: {espaco_total_mb:.2f} MB".replace(".", ","))
relatorio.write(f"\nEspaço médio ocupado: {espaco_medio_mb:.2f} MB".replace(".", ","))

relatorio.close()

print("Relatório gerado com sucesso.")
