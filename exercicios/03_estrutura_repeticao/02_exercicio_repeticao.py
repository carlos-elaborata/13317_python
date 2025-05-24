"""Exercício 02.

Cadastro de Usuário e Senha
Desenvolva um programa que receba um nome de usuário e sua senha.
O sistema deve validar se a senha é diferente do nome do usuário.
Caso seja igual, uma mensagem de erro deve ser exibida e as informações solicitadas
novamente até que sejam válidas.
"""

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")

while nome == senha:
    print("Erro: O nome não pode ser igual a senha.")
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
print("Usuário cadastrado com sucesso.")
