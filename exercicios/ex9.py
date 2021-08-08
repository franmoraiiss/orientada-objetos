def isPalindrome(word):
    if(word == word[::-1]):
        return True
    else:
        return False


word = input("Informe a string: ")
word = word.lower()

if(isPalindrome(word)):
    print("A string é um palíndromo")
else:
    print("A string NÃO é um palíndromo")
