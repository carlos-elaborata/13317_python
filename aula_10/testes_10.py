def validar_idade(idade):
    if idade < 0:
        raise ValueError("A idade não pode ser um valor negativo.")
    elif idade > 120:
        raise ValueError("A idade não pode ser maior do que 120.")
    print(f"Idade válida: {idade}")


# try:
#     idade = int(input("Informe a idade: "))
#     validar_idade(idade)
# except ValueError as e:
#     print(f"Erro: {e}")


with open("meu_arquivo.txt", "r", encoding="utf8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
