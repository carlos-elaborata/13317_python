"""Exercício 03.

Processamento de Dados de Alunos
Implemente um programa que processe informações de alunos de uma escola a partir de um
arquivo CSV, realizando cálculos e atualizações nos dados.
O arquivo "dados.csv" contém as seguintes colunas:
    Nome;
    Idade;
    Nota 1;
    Nota 2;
    Nota 3.
O programa deve:
    a. Calcular a média das notas de cada aluno e adicioná-la em uma nova coluna
        chamada "Média";
    b. Ordenar os dados pelo nome do aluno em ordem alfabética.
    c. Escrever os dados atualizados em um novo arquivo "dados_atualizados.csv".
    d. Receber o nome de um aluno como entrada do usuário e exibir na tela a média das
        notas desse aluno.
"""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent / "arquivos"
arq_entrada = "03_dados.csv"
arq_saida_csv = "03_dados_atualizados.csv"
arq_saida_excel = "03_dados_atualizados.xlsx"


def carregar_dados(arq_entrada):
    return pd.read_csv(BASE_DIR / arq_entrada)


def calcular_media(df_alunos: pd.DataFrame):
    df_alunos["Média"] = df_alunos[["Nota 1", "Nota 2", "Nota 3"]].mean(1).round(2)

    return df_alunos


def salvar_dados(df_alunos: pd.DataFrame, arq_saida_csv, arq_saida_excel):
    df_alunos.to_csv(BASE_DIR / arq_saida_csv, index=False)
    df_alunos.to_excel(
        BASE_DIR / arq_saida_excel,
        index=False,
        sheet_name="Dados dos Alunos",
    )


def consultar_aluno(df_alunos: pd.DataFrame):
    while True:
        nome_aluno = input(
            "\nDigite o nome de um aluno para ver a sua média;\n"
            'Digite "lista" para ver todos os alunos;\n'
            'Ou pressione "Enter" para encerrar: '
        )
        if not nome_aluno:
            break

        if nome_aluno.lower() == "lista":
            print("\nLista de Alunos")
            print(df_alunos["Nome"].to_string(index=False))
        else:
            aluno = df_alunos[df_alunos["Nome"].str.lower() == nome_aluno.lower()]

            if not aluno.empty:
                print(f"\nA média de {nome_aluno} é {aluno['Média'].to_numpy()[0]:.2f}")
            else:
                print("\nAluno não encontrado.")


def processar_dados(arq_entrada, arq_saida_csv, arq_saida_excel):
    df_alunos = carregar_dados(arq_entrada)
    df_alunos = calcular_media(df_alunos)
    df_alunos = df_alunos.sort_values("Nome")
    salvar_dados(df_alunos, arq_saida_csv, arq_saida_excel)
    consultar_aluno(df_alunos)

    print("\nPrograma encerrado.")


processar_dados(arq_entrada, arq_saida_csv, arq_saida_excel)
