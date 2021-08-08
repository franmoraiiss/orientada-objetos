# Exercício 2
# Leia dois número correspondentes a um intervalo, gere e
# imprima um número randômico dentro desse intervalo.

import random

num1 = int(input("Digite o começo do intervalo: "))
num2 = int(input("Digite o final do intervalo: "))

print(random.randrange(num1, num2))
