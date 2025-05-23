"""Exercício 35.

Adição de Média das Notas a Dicionário
Faça um programa que inicie com um dicionário representando um estudante, contendo
"Nome": "Lucas", "Notas": [85, 90, 78, 92, 88], e "Idade": 20.
O programa deve calcular a média das notas e adicionar essa média ao dicionário com a
chave "Média".
Após isso, exiba o dicionário atualizado.
"""

estudante = {"nome": "Lucas", "notas": [85, 90, 78, 92, 88], "idade": 20}

notas = estudante["notas"]
media_notas = sum(notas) / len(notas)

# estudante["media"] = media_notas
estudante.update({"media": media_notas})

print(estudante)
