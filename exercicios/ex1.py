# Exercício 1
# Ler duas strings e verificar se a segunda está contida na primeira

first_string = input("Digite a primeira string: ")

second_string = input("Digite a segunda string: ")

if(second_string in first_string):
    print("-> Está contida")
else:
    print("-> Não está contida")
