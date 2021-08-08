class ValorMenor(Exception):
    pass


class ValorMaior(Exception):
    pass


nro = 10

while True:
    try:
        i_num = int(input("Digite um número: "))
        if i_num < nro:
            raise ValorMenor
        elif i_num > nro:
            raise ValorMaior
        break
    except ValorMenor:
        print("Valor menor!")
        print()
    except ValorMaior:
        print("Valor maior!")
        print()

print("Parabéns! Você descobriu o número!")
