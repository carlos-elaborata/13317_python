"""Exercício 31.

Remoção de Idade de Dicionário
Desenvolva um programa que inicie com um dicionário contendo as informações "Nome":
"Ana", "Idade": 25, "Profissão": "Engenheira", e "País": "Brasil".
O programa deve remover a entrada referente à idade do dicionário e, depois, exibir o
dicionário atualizado.
"""

pessoa = {"nome": "Ana", "idade": 25, "profissao": "Engenheira", "pais": "Brasil"}

# del pessoa["idade"]
pessoa.pop("idade")

print(pessoa)
