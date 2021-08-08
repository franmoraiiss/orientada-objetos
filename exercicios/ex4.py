# Exercício 4
# Utilizando a tabela a seguir, escreva um código que permita
# obter a alíquota do imposto de renda de acordo com o valor da
# renda mensal. Seu programa deve ler o valor da renda e
# imprimir o valor da alíquota, bem como o valor do imposto a
# pagar.

# Renda Alíquota
# De 1.903,99 até 2.826,65 7,5%
# De 2.826,66 até 3.751,05 15%
# De 3.751,06 até 4.664,68 22,5%
# Acima de 4.664,68 27,5%

income = float(input("Insira o valor de sua renda: (xxxx.xx)"))

if(income >= 1903.99 and income <= 2826.65):
    print("Aliquota de: 7.5%")
    tax = income * 0.075

elif(income >= 2826.66 and income <= 3751.05):
    print("Aliquota de: 15%")
    tax = income * 0.15

elif(income >= 3751.06 and income <= 4664.68):
    print("Aliquota de: 22.5%")
    tax = income * 0.225

elif(income >= 4664.68):
    print("Aliquota de: 27.5%")
    tax = income * 0.275

else:
    print("Você não precisa pagar imposto")
    tax = 0

print("Valor a ser pago: " + str(tax))
