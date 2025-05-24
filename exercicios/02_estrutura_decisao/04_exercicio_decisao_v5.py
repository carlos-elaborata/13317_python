"""Exercício 04.

Classificação de Letras
Elabore um programa que solicite uma letra ao usuário e verifique se ela é uma vogal ou
consoante.
"""

from curses.ascii import isdigit


letra = input("Digite uma letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Digite somente UMA letra (A-Z).")
