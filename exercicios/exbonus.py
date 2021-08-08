# Exercicio bonus
# Escreva um programa que leia o nome e a altura de n pessoas.
# Em seguida informe o nome e altura da pessoa mais alta, e também
# o nome e a altura da pessoa mais baixa

listName = []
listHeight = []

nameQuantity = int(input("Informe o número de pessoas: "))

for nameQuantity in range(0, 4):
    name = input("Digite o nome:")
    listName.append(name)

    height = input("Digite sua altura em centimetros:")
    listHeight.append(height)

handleMaxHeight = listHeight[0]
nameMaxHeight = listName[0]
for i in range(len(listHeight)):
    if(listHeight[i] > handleMaxHeight):
        handleMaxHeight = listHeight[i]
        nameMaxHeight = listName[0]
        break

handleMinHeight = listHeight[0]
nameMinHeight = listName[0]
for i in range(len(listHeight)):
    if(listHeight[i] < handleMinHeight):
        handleMinHeight = listHeight[i]
        nameMinHeight = listName[i]
        break

print("O mais alto é {} e sua altura é {}".format(
    nameMaxHeight, handleMaxHeight))
