"""Exercício 06.

Conversão de Hora
Faça um programa que converta a hora de notação de 24 horas para notação de 12 horas.
Por exemplo, deve converter 14:25 em 2:25 P.M.
Implemente funções para a conversão e para exibir o resultado.
Inclua um loop permitindo ao usuário repetir a operação com novos valores.
"""


# Definição da função que converte hora de formato 24h para 12h com indicação de AM/PM
def converter_hora(hora_24, minutos):
    # Determina AM ou PM com base na hora
    if hora_24 < 12:
        am_pm = "A.M."
    else:
        am_pm = "P.M"

    # 00:00 -> 12:00 A.M.
    # Ajusta a hora para o formato 12 horas
    if hora_24 not in {12, 0}:
        hora_12 = hora_24 % 12
    else:
        hora_12 = 12

    # Formata e retorna a hora convertida
    return f"{hora_12:02}:{minutos:02} {am_pm}"


# Loop para permitir múltiplas conversões
while True:
    # Solicitação de entrada da hora e dos minutos pelo usuário
    hora_24 = int(input("Digite as horas (0 a 23): "))
    minutos = int(input("Digite os minutos (0 a 59): "))

    # Verificação de validade da hora e minutos inseridos
    if hora_24 < 0 or hora_24 > 23 or minutos < 0 or minutos > 59:
        # Se o horário não for válido, volte para o começo do loop
        print("Por favor, digite um horário válido.")
        continue

    # Imprime o resultado da conversão de hora
    print(converter_hora(hora_24, minutos))

    continuar = input("Deseja converter outra hora? (S/N) ").lower()
    if continuar != "s":
        break


print("Conversões finalizadas.")
