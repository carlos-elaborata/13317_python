# lista = ["a", "b", "c", "d"]
# dicionario = {"a": 1, "b": 2, "c": 3}
# tupla = ("a", "b", "c", "d")
# # Conjunto = Set, imutável, não é ordenado, não pode ter valores repetidos
# conjunto = {"a", "b", "c", "d", "a"}
# print(conjunto)


# nomes = ["Fulano", "Beltrano", "Sicrano"]
# for i in nomes:
#     if i == "Beltrano":
#         continue
#     print(i)
# print("Fim do programa")


# nomes = ["Fulano", "Beltrano", "Sicrano"]
# for i in nomes:
#     if i == "Beltrano":
#         break
#     print(i)
# print("Fim do programa")


while True:
    valor = int(input("Digite um número: "))
    if valor == 0:
        break
    print(valor)

print("Fim do programa")
