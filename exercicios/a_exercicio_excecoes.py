"""Exercício A.

Utilizando tratamento de exceções, crie um programa que, dado um valor inteiro
informado pelo usuário, retorne a divisão de 1 por este (1 / valor).
Se o valor informado for zero, o programa deve informar “Infinito” como resultado.
Caso o valor informado não seja um número, o programa deve informar o usuário e
continuar solicitando valores até que este seja.
"""

while True:
    try:
        numero = int(input("Informe um número inteiro: "))
        resultado = 1 / numero
    except ValueError:
        print("Valor inválido. Informe um número inteiro.")
    except ZeroDivisionError:
        print("Infinito")
        break
    else:
        print(resultado)
        break
