"""Exercício 05.

Cálculo de Imposto sobre Produto
Crie um programa com uma função chamada "soma_imposto".
A função deve receber dois parâmetros: "taxa_imposto" (percentual de imposto sobre
vendas) e "custo" (custo de um item antes do imposto).
A função deve retornar o custo após adicionar o imposto sobre vendas.
"""


def soma_imposto(taxa_imposto, custo):
    return custo * (1 + taxa_imposto / 100)


custo = float(input("Digite o custo do item: R$ "))
taxa_imposto = float(input("Digite a taxa de imposto em porcentagem: "))

novo_custo = soma_imposto(taxa_imposto, custo)

print(f"Custo do item com imposto: R$ {novo_custo:.2f}")
