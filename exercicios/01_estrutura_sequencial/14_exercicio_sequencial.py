"""Exercício 14.

Multa por Excesso de Pesca
Você foi contratado pela Secretaria de Meio Ambiente para criar um sistema que ajude na
fiscalização da pesca em reservas naturais.
De acordo com a legislação local, pescadores têm um limite de captura de 50 quilos de
peixes por dia para evitar a superexploração.
Para cada quilo excedente, é imposta uma multa de R$ 4,00.
Seu programa deve:
    a. Solicitar a quantidade total de peixes pescados (em quilos) por um pescador em
        um único dia;
    b. Calcular e exibir qualquer excesso de peso além do limite permitido de 50
        quilos;
    c. Se houver excesso, calcular e exibir o valor da multa que o pescador deve
        pagar.
"""

limite = 50  # kilos de peixe por dia
multa_kg = 4  # reais por kilo excedente

peso_peixes = float(input("Peso dos peixes em kg: "))

excesso = peso_peixes - limite
excesso = max(0, excesso)

multa_total = excesso * multa_kg

print(f"Total pescado: {peso_peixes} kg")
print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa_total:.2f}")
