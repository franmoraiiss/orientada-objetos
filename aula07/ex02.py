from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisciplina):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisciplina = listaDisciplina

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getListaDisciplina(self):
        return self.__listaDisciplina

    @abstractmethod
    def printDescricao(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisciplina):
        super().__init__(nome, endereco, idade, listaDisciplina)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulacao: {}'.format(self.getTitulacao()))
        print('Disciplinas Ministradas:')

        lista = self.getListaDisciplina()
        for disciplina in lista:
            print('Nome: {} - Carga Horária: {}'.format(disciplina.getNomeDisciplina(),
                  disciplina.getCargaHoraria()))


class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisciplina):
        super().__init__(nome, endereco, idade, listaDisciplina)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereco: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))
        print('Disciplinas cursadas:')

        lista = self.getListaDisciplina()
        for disciplina in lista:
            print('Nome: {} - Carga Horária: {}'.format(disciplina.getNomeDisciplina(),
                  disciplina.getCargaHoraria()))


class Disciplina():
    def __init__(self, nomeDisciplina, cargaHoraria):
        self.__nomeDisciplina = nomeDisciplina
        self.__cargaHoraria = cargaHoraria

    def getNomeDisciplina(self):
        return self.__nomeDisciplina

    def getCargaHoraria(self):
        return self.__cargaHoraria


if __name__ == "__main__":
    disc1 = Disciplina('POO', 64)
    disc2 = Disciplina('Estrutura de Dados', 64)
    disc3 = Disciplina('Banco de Dados', 32)

    listaDiscProfessor = [disc1, disc2]
    listaDiscAluno = [disc2, disc3]

    prof = Professor('Pedro', 'Av. BPS', 23, 'Doutor', listaDiscProfessor)
    prof.printDescricao()
    print()

    aluno = Aluno('Marcelo', 'Rua Tigre Maia', 20, 'SIN', listaDiscAluno)
    aluno.printDescricao()
