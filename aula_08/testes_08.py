# a = max(1, 2, 3)
# print(a)
# b = max(4, 5, 6, 7, 8, 9)
# print(b)


# def somar(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(total)


# somar(1, 2, 3)
# somar(10, 20, 30, 40, 50)


# def imprimir_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave.title()} -> {valor}")


# imprimir_info(nome="João", idade=30, cidade="Curitiba")
# print("-" * 20)
# imprimir_info(produto="Banana", preco=2.99)

# dicionario = dict(chave="valor", produto="maça", valor=5)
# print(dicionario)


# numeros = [25, 30, 20]
# numeros.sort(reverse=True)
# print(numeros)

# pessoas = [
#     {"nome": "João", "idade": 25},
#     {"nome": "Maria", "idade": 30},
#     {"nome": "Pedro", "idade": 20},
# ]

# pessoas.sort(key=lambda dicionario: dicionario["idade"], reverse=True)
# print(pessoas)


# arquivo = open("meu_arquivo.txt", "r")
# conteudo = arquivo.read()
# arquivo.close()
# print([conteudo])


# arquivo = open("meu_arquivo.txt", "r")
# linha = arquivo.readline()
# while linha:
#     print(linha.strip())
#     linha = arquivo.readline()
# arquivo.close()

# arquivo = open("meu_arquivo.txt", "r")
# linhas = arquivo.readlines()
# arquivo.close()
# print(linhas)
# for linha in linhas:
#     print(linha.strip())


# arquivo = open("meu_arquivo_2.txt", "a")
# arquivo.write("Escrevendo no arquivo!\n")
# arquivo.write(
#     """Este arquivo tem
# várias linhas!\n"""
# )
# arquivo.close()

frutas = ["Abacate\n", "Melancia\n", "Amora"]
arquivo = open("meu_arquivo_2.txt", "w")
arquivo.writelines(frutas)
arquivo.close()
