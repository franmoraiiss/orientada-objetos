from abc import ABC, abstractmethod


class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def calculaImposto(self, salarioBruto):
        if salarioBruto < 1903.9:
            imposto = 0
        elif salarioBruto < 2826.66:
            imposto = 7.5
        elif salarioBruto < 3751.06:
            imposto = 15
        elif salarioBruto < 4664.68:
            imposto = 22.5
        else:
            imposto = 27.5

        return (salarioBruto * imposto) / 100

    @abstractmethod
    def getSalario(self):
        pass


class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    def setSalario(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self, salarioBruto):
        return self.__salarioBruto

    def getSalario(self):
        previdencia = self.__salarioBruto * 0.11
        imposto = self.calculaImposto(self.__salarioBruto)
        return self.__salarioBruto - (previdencia + imposto)


class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora

    def getSalarioHora(self):
        return self.__salarioHora

    def getSalario(self):
        salarioBruto = self.__salarioHora * self.getCargaHoraria()
        imposto = self.calculaImposto(salarioBruto)
        return salarioBruto - imposto


if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)

    profs = [prof1, prof2, prof3]
    for prof in profs:
        print('Nome: {} - Salário: {}'.format(prof.getNome(), prof.getSalario()))
