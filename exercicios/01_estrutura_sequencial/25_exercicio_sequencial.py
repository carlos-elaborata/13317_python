"""Exercício 25.

Atualização de Lista de Cores
Desenvolva um programa que comece com uma lista contendo cinco cores distintas.
O programa deve então solicitar ao usuário uma cor.
Esta cor fornecida pelo usuário será utilizada para substituir a terceira cor na lista
original.
Após a substituição, o programa deve exibir a lista atualizada, mostrando a alteração
feita.
"""

cores = ["Azul", "Vermelho", "Verde", "Amarelo", "Preto"]
nova_cor = input("Digite uma nova cor: ")
cores[2] = nova_cor
print(cores)
