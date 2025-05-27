"""Exercício 22.

Interrogatório Simulado
Elabore um programa que faça ao usuário cinco perguntas relacionadas a um suposto
crime:
    a. "Telefonou para a vítima?";
    b. "Esteve no local do crime?";
    c. "Mora perto da vítima?";
    d. "Devia para a vítima?";
    e. "Já trabalhou com a vítima?".
Classifique e exiba a participação da pessoa no crime como:
    a. "Inocente", se responder positivamente a no máximo uma pergunta;
    b. "Suspeita", se responder positivamente a duas perguntas;
    c. "Cúmplice", se responder positivamente a três ou quatro perguntas;
    d. "Assassino", se responder positivamente a todas as perguntas.
"""

# respostas_positivas = 0

# print("Responda S (sim) ou N (não) para as perguntas.")

# if input("Telefonou para a vítima? ").lower() == "s":
#     respostas_positivas += 1  # É igual a: respostas_positivas = respostas_positivas + 1

# if input("Esteve no local do crime? ").lower() == "s":
#     respostas_positivas += 1

# if input("Mora perto da vítima? ").lower() == "s":
#     respostas_positivas += 1

# if input("Devia para a vítima? ").lower() == "s":
#     respostas_positivas += 1

# if input("Já trabalhou com a vítima? ").lower() == "s":
#     respostas_positivas += 1

# if respostas_positivas == 5:
#     classificacao = "Assassino"
# elif respostas_positivas == 3 or respostas_positivas == 4:
#     classificacao = "Cúmplice"
# elif respostas_positivas == 2:
#     classificacao = "Suspeita"
# else:
#     classificacao = "Inocente"

# print(f"Com base nas respostas, a pessoa é classificada como: {classificacao}.")


# Criando a lista das perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

respostas = []
# Verificando se a resposta é "S" ou "N"
for pergunta in perguntas:
    while True:
        resposta: str = input(pergunta + " (s/n): ").strip().lower()
        if resposta.startswith("s"):
            respostas.append("s")
            break
        elif resposta.startswith("n"):
            respostas.append("n")
            break
        else:
            print("Resposta invalida, por favor responda com 's' ou 'n'.")
# Contando a quantidade de "S"
suspeita = respostas.count("s")
# Classificando pela quantidade de "S"
if suspeita == 2:
    print("Suspeita")
elif 3 <= suspeita <= 4:
    print("Cumplice")
elif suspeita == 5:
    print("Assassino")
else:
    print("Inocente")
