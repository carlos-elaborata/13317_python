"""Exercício 34.

Contagem de Pares Chave-Valor em Dicionário
Desenvolva um programa que contenha um dicionário com "Nome": "Ana", "Idade": 25,
"Profissão": "Engenheira", e "País": "Brasil".
O programa deve contar e exibir o número de pares de chave-valor presentes no
dicionário.
"""

pessoa = {"nome": "Ana", "idade": 25, "profissao": "Engenheira", "pais": "Brasil"}

numero_pares = len(pessoa)

print(f"O dicionário contém {numero_pares} pares de chave-valor.")
