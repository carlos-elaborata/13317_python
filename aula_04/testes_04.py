# pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

# print(pessoa["nome"])
# print(pessoa["idade"])
# print(pessoa["cidade"])
# print(pessoa["endereco"])  # Erro
# print(pessoa.get("nome"))
# print(pessoa.get("idade"))
# print(pessoa.get("cidade", "Cidade não cadastrada."))
# print(pessoa.get("endereco"))
# print(pessoa.get("endereco", "Endereço não cadastrado."))

# pessoa["cidade"] = "Curitiba"
# pessoa["endereco"] = "Rua X"
# print(pessoa)
# pessoa.update({"cidade": "Curitiba", "endereco": "Rua X"})
# print(pessoa)

# del pessoa
# del pessoa["cidade"]
# print(pessoa)
# del pessoa["bairro"]  # Erro
# cidade = pessoa.pop("cidade")
# print(pessoa)
# print(cidade)
# bairro = pessoa.pop("bairro", "Bairro não cadastrado.")
# print(bairro)


a = 5

if a > 5:
    print("Maior do que cinco!")
    print("Batman")
else:
    print("Menor do que cinco!")
    print("Robin")
print("Fim do programa.")
