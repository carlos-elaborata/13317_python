"""Exercício 04.

Crescimento Populacional
Implemente um programa que calcule o tempo necessário para que a população do país A,
que possui 80.000 habitantes e cresce 3% ao ano, ultrapasse ou iguale a população do
país B, com 200.000 habitantes e crescimento anual de 1,5%.
"""

pop_a = 80000
TAXA_A = 0.03

pop_b = 200000
TAXA_B = 0.015

anos = 0

while pop_a < pop_b:
    pop_a += pop_a * TAXA_A
    pop_b += pop_b * TAXA_B
    anos += 1
    print(f"Ano {anos}:")
    print(f"População A: {pop_a}")
    print(f"População B: {pop_b}\n")

print(
    f"São necessário {anos} anos para que a população de A ultrapasse ou igual a de B."
)
