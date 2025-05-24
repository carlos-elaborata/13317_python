"""Exercício 01.

Validador de Notas
Elabore um programa que solicite uma nota numérica entre zero e dez ao usuário.
Caso o valor fornecido esteja fora do intervalo permitido, o programa deve exibir uma
mensagem de erro e solicitar o valor novamente até que uma entrada válida seja
fornecida.
"""

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido. A nota deve estar entre 0 e 10.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"Nota válida: {nota}")
