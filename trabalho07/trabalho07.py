def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn

    return n


def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class Fracao:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum

    def __add__(self, outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        novaFracao = Fracao(novoNum // divComum, novoDen // divComum)

        if novaFracao.getNum() / novaFracao.getDen() < 1:
            return novaFracao
        elif novaFracao.getNum() / novaFracao.getDen() == 1:
            return 1
        else:
            parteInt = novaFracao.getNum() // novaFracao.getDen()
            novoNum2 = novaFracao.getNum() - parteInt * novaFracao.getDen()
            return FracaoMista(parteInt, novoNum2, novaFracao.getDen())


class FracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__num = num
        self.__den = den
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira

    def __add__(self, outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)

        parteInt = self.getParteInteira() + outraFrac.getParteInteira()
        novaFracao = FracaoMista(parteInt // divComum,
                                 novoNum // divComum, novoDen // divComum)

        if novaFracao.getNum() / novaFracao.getDen() < 1:
            # como não há parte inteira, podemos retornar uma fração simples
            return Fracao(novoNum // divComum, novoDen // divComum)
        elif novaFracao.getNum() / novaFracao.getDen() == 1:
            return 1
        else:
            parteInt = (novaFracao.getNum() // novaFracao.getDen()
                        ) + novaFracao.getParteInteira()
            novoNum2 = novaFracao.getNum() - (novaFracao.getNum() //
                                              novaFracao.getDen()) * novaFracao.getDen()
            return FracaoMista(parteInt, novoNum2, novaFracao.getDen())

    def __str__(self):
        return str(self.__parteInteira) + ' ' + str(self.getNum()) + '/' + str(self.getDen())


if __name__ == "__main__":
    frac1 = Fracao(7, 6)
    frac2 = Fracao(13, 7)
    frac3 = frac1 + frac2
    print(frac3)

    frac4 = Fracao(1, 4)
    frac5 = Fracao(3, 4)
    frac6 = frac4 + frac5
    print(frac6)

    frac7 = FracaoMista(3, 1, 2)
    frac8 = FracaoMista(4, 2, 3)
    frac9 = frac7 + frac8
    print(frac9)
