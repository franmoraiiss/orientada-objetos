# Exercício 7

# Leia valores numéricos e os coloque numa lista. A leitura
# termina quando o valor 0 for digitado. Em seguida,
# calcule a média dos valores digitados e informe o
# usuário.

numList = []

while True:
    num = int(input("Digite um número: "))
    if (num == 0):
        break
    numList.append(num)

soma = 0
for num in numList:
    soma += num

media = soma / len(numList)
print("A média dos valores digitados é: " + str(media))
