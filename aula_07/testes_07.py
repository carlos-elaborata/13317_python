# frutas = ["abacate", "abacaxi", "ameixa", "amora"]

# for indice, fruta in enumerate(frutas):
#     print(f"{indice} -> {fruta}")


# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pares = []
# for n in numeros:
#     if n % 2 == 0:
#         pares.append(n)
# print(pares)

# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pares = [n for n in numeros if n % 2 == 0]
# print(pares)


# def somar(a, b):
#     print(int(a) + int(b))


# a = somar(4, 5)
# print(a)


# def somar(a, b):
#     total = a + b
#     return total


# resultado_1 = somar(4, 5)
# print(resultado_1)

# print(somar(7, 8))
# print(somar(-4, -12))


def saudar_usuario(nome, sobrenome, saudacao="Olá"):
    print(f"{saudacao} {nome} {sobrenome}")


# saudar_usuario("João", "de Almeida", "Oi")
# saudar_usuario("Maria", "Helena")

saudar_usuario(saudacao="Oi", nome="João", sobrenome="de Almeida")
saudar_usuario(sobrenome="Helena", nome="Maria")

saudar_usuario("Vitória", saudacao="Hello", sobrenome="Albino")