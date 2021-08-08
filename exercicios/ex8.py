# Exercício 8

# Escreva uma função que receba um float representando o
# valor da temperatura em Celsius e retorne a temperatura
# equivalente em Farenheit. Em seguida, escreva um código
# que leia uma temperatura em Celsius e informe o valor
# equivalente em Farenheit.

def convert_temp(temp):
    return (temp * (9/5) + 32)


tempce = float(input("Qual a temperatura atual? (ºC): "))
tempfh = convert_temp(tempce)

print("A temperatura em Farenheit é: " + str(tempfh))
