"""Exercício 22.

Fatorial com Restrições e Repetições
Altere o programa de cálculo do fatorial para permitir múltiplas execuções pelo
usuário, aceitando apenas números inteiros positivos menores que 16.
"""

while True:
    numero = int(input("Digite um número entre 1 e 15 para calcular o fatorial: "))

    while numero < 1 or numero > 15:
        print("Número fora do intervalo permitido.")
        numero = int(input("Digite um número entre 1 e 15 para calcular o fatorial: "))

    fatorial = 1

    termos_fatorial = []

    for i in range(numero, 0, -1):
        fatorial = fatorial * i
        termos_fatorial.append(str(i))

    expressao_fatorial = (
        f"{numero}! = " + " x ".join(termos_fatorial) + f" = {fatorial:,}"
    )
    print(expressao_fatorial)

    if input("Deseja calcular outro fatorial? (S/N): ").upper() != "S":
        break
