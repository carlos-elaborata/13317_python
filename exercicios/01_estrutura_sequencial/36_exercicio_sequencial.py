"""Exercício 36.

Combinação de Informações de Livros em Dicionário
Crie um programa que possua dois dicionários representando livros.
O primeiro com as informações "Titulo": "1984", "Autor": "George Orwell", e
"Ano_Publicacao": 1949; o segundo com "Titulo": "Brave New World", "Autor": "Aldous
Huxley", e "Ano_Publicacao": 1932.
O programa deve combinar esses dois dicionários em uma única estrutura, utilizando as
chaves "Livro_1" e "Livro_2" para cada livro, respectivamente, e exibir a estrutura
combinada.
"""

livro_1 = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
livro_2 = {"titulo": "Brave New World", "autor": "Aldous Huxley", "ano": 1932}

biblioteca = {"livro_1": livro_1, "livro_2": livro_2}

print(biblioteca)
