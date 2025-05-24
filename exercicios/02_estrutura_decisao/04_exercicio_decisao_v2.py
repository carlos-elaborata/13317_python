"""Exercício 04.

Classificação de Letras
Elabore um programa que solicite uma letra ao usuário e verifique se ela é uma vogal ou
consoante.
"""

letra = input("Digite uma letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante")
