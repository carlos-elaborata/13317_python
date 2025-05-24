"""Exercício 33.

Verificação de Chave em Dicionário
Crie um programa que possua um dicionário com as informações "Nome": "Ana", "Idade":
25, "Profissão": "Engenheira", e "País": "Brasil".
O programa deve verificar se a chave "Idade" está presente no dicionário e exibir uma
mensagem confirmando sua presença.
"""

pessoa = {"nome": "Ana", "idade": 25, "profissao": "Engenheira", "pais": "Brasil"}

print("idade" in pessoa)
