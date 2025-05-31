# import testes_10

# testes_10.validar_idade(52)


# import cowsay

# cowsay.stegosaurus("Hello World")

# from math import sqrt

# print(sqrt(25))


import requests

cep = input("Digite um CEP: ")

resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(resposta.json())
