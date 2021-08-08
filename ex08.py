from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getCpf(self):
        return self.__cpf

    @abstractmethod
    def printDescricao(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Professor cadastrado:')
        print('Professor {}'.format(self.getNome()))
        print('Título: {}'.format(self.getTitulacao()))
        print('CPF: {}'.format(self.getCpf()))
        print('Idade: {}'.format(self.getIdade()))
        print('Endereço: {}'.format(self.getEndereco()))


class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Aluno cadastrado:')
        print('Nome: {}'.format(self.getNome()))
        print('CPF: {}'.format(self.getCpf()))
        print('Idade: {}'.format(self.getIdade()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Curso: {}'.format(self.getCurso()))


class TitulacaoInvalida(Exception):
    pass


class IdadeProfInvalida(Exception):
    pass


class CursoInvalido(Exception):
    pass


class IdadeAlunoInvalida(Exception):
    pass


class CpfInvalido(Exception):
    pass


if __name__ == "__main__":
    alunos = [
        ('Pedro', 'Rua Laranjeiras', 18, 23203021668, 'CCO'),
        ('Pedrita', 'Av. BPS', 19, 64468028629, 'ADM'),
        ('Pedroso', 'Rua Laranjeiras', 20, 64468028629, 'SIN'),
        ('Peter', 'Av. BPS', 12, 64835580664, 'CCO'),
        ('Pedroso', 'Rua Laranjeiras', 20, 33945839723, 'SIN'),
    ]

    professores = [
        ('Marcos', 'Av. Brasil', 20, 13982827663, 'doutor'),
        ('Marcia', 'Av. Paulista', 35, 13982827663, 'doutor'),
        ('Marcio', 'Rua Nova', 30, 13982827663, 'mestre'),
        ('Marcinha', 'Av. BPS', 35, 13982827663, 'doutor'),
        ('Marcinho', 'Rua Laranjeiras', 28, 13256587663, 'mestre')
    ]

    cadastro = {}

    print("\nLista de Exceptions: ")
    for nome, endereco, idade, cpf, titulacao in professores:
        try:
            if ((titulacao != 'doutor')):
                raise TitulacaoInvalida
            if (idade < 30):
                raise IdadeProfInvalida
            if cpf in cadastro:
                raise CpfInvalido()
        except TitulacaoInvalida:
            print('{} não é uma titulação válida'.format(titulacao))
        except CpfInvalido:
            print('O CPF {} já está cadastrado'.format(cpf))
        except IdadeProfInvalida:
            print('{} é uma idade inválida para ser professor'.format(idade))
        else:
            cadastro[cpf] = Professor(nome, endereco, idade, cpf, titulacao)

    print()

    for nome, endereco, idade, cpf, curso in alunos:
        try:
            if (curso != 'CCO') and (curso != 'SIN'):
                raise CursoInvalido
            if (len(curso) < 3):
                raise CursoInvalido
            if (idade < 18):
                raise IdadeAlunoInvalida
            if cpf in cadastro:
                raise CpfInvalido
        except CpfInvalido:
            print('O CPF {} já está cadastrado'.format(cpf))
        except IdadeAlunoInvalida:
            print('{} é uma idade inválida para ser aluno'.format(idade))
        except CursoInvalido:
            print('O curso {} não é válido'.format(curso))
        else:
            cadastro[cpf] = Aluno(nome, endereco, idade, cpf, curso)

    print("\nLista de Cadastrados Final - (cadastro bem sucedido):")
    for cadastrado in cadastro:
        cadastro[cadastrado].printDescricao()
        print()
