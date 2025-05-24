"""Exercício 04.

Classificação de Letras
Elabore um programa que solicite uma letra ao usuário e verifique se ela é uma vogal ou
consoante.
"""

letra = input("Digite uma letra: ").lower()

vogais = ["a", "e", "i", "o", "u"]

if letra in vogais:
    print("Vogal")
else:
    print("Consoante")
