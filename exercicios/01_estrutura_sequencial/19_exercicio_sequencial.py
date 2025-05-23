"""Exercício 19.

Manipulação de Lista de Frutas
Desenvolva um programa que comece criando uma lista contendo cinco nomes de frutas.
Em seguida, o programa deve solicitar ao usuário o nome de uma sexta fruta, que será
adicionada ao final da lista.
Após a adição, o programa deve remover a segunda fruta da lista original.
Finalmente, exiba a lista modificada ao usuário, demonstrando as alterações feitas.
"""

frutas = ["Maça", "Banana", "Cereja", "Pitaya", "Amora"]
frutas.append(input("Digite o nome da 6ª fruta: "))
frutas.pop(1)
print(frutas)
