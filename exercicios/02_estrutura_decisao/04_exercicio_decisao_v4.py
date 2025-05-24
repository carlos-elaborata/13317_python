"""Exercício 04.

Classificação de Letras
Elabore um programa que solicite uma letra ao usuário e verifique se ela é uma vogal ou
consoante.
"""

letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")
