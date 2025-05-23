"""Exercício 32.

Atualização de Profissão em Dicionário
Escreva um programa que comece com um dicionário contendo "Nome": "Ana", "Idade": 25,
"Profissão": "Engenheira", e "País": "Brasil".
O programa deve atualizar a profissão de "Engenheira" para "Engenheira de Software" e
exibir o dicionário modificado.
"""

pessoa = {"nome": "Ana", "idade": 25, "profissao": "Engenheira", "pais": "Brasil"}

# pessoa["profissao"] = "Engenheira de Software"
pessoa.update({"profissao": "Engenheira de Software"})

print(pessoa)
