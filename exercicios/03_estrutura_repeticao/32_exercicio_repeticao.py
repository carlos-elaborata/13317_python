"""Exercício 32.

Censo em Academia
Elabore um programa para coletar dados de clientes de uma academia (código, altura e
peso), calculando e informando os dados do cliente mais alto, mais baixo, mais gordo,
mais magro, além da média de altura e peso dos clientes.
"""

# Inicializa listas para armazenar dados dos clientes
clientes = []
alturas = []
pesos = []

# Loop para coletar dados do clientes até que o código 0 seja inserido
while True:
    codigo = input("Digite o código do cliente (ou 0 para terminar): ")

    if codigo == "0":
        break

    altura = float(input("Altura em metros: "))
    peso = float(input("Peso em quilogramas: "))

    # Adiciono os dados coletados as listas
    clientes.append((codigo, altura, peso))
    alturas.append(altura)
    pesos.append(peso)

print(clientes)
print(alturas)
print(pesos)

if clientes:
    # mais_alto = max(clientes, key=lambda x: x[1])
    mais_alto = max(alturas)
    indice_mais_alto = alturas.index(mais_alto)
    cliente_mais_alto = clientes[indice_mais_alto]

print("Fim do programa")
