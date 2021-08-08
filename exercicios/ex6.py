# Exercício 6

# Leia uma string e verifique se a mesma é um
# palíndromo.

word = input("Informe a string: ")
word = word.lower()

if(word == word[::-1]):
    print("A string é um palíndromo")
else:
    print("A string NÃO é um palíndromo")
