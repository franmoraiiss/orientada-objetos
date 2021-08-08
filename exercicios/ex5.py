# Exercício 5

# Leia um conjunto de nomes e os armazene numa lista. Em
# seguida, leia um nome e verifique se o mesmo faz parte
# dessa lista.

nameList = []
nameQuantity = int(input("Quantas pessoas haverá na lista? "))

for x in range(nameQuantity):
    name = input("Digite o nome: ")
    nameList.insert(x, name)

searchName = input("Informe um nome a se procurar? ")
if searchName in nameList:
    print(searchName + " está na lista! :D")
else:
    print(searchName + " não está na lista! :(")
