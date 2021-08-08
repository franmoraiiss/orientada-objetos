class Aluno:
    def __init__(self, nroMatricula, nome, curso):
        self.__nroMatricula = nroMatricula
        self.__nome = nome
        self.__curso = curso
        self.__disciplinas = []

    def getMatricula(self):
        return self.__nroMatricula

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)


class Curso:
    def __init__(self, nome, grade):
        self.__nome = nome
        self.__grade = grade
        self.__alunos = []
        self.__disciplinas = []

    def getNome(self):
        return self.__nome

    def getGrade(self):
        return self.__grade

    def getAlunos(self):
        return self.__alunos

    def addAlunos(self, aluno):
        self.__alunos.append(aluno)

    def addDisciplina(self, disciplina):
        self.__alunos.append(disciplina)


class Grade:
    def __init__(self, ano):
        self.__ano = ano
        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplinas(self, disciplina):
        self.__disciplinas.append(disciplina)


class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria, grade):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__grade = grade

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getGrade(self):
        return self.__grade


class Historico:
    def __init__(self, aluno):
        self.__aluno = aluno

    def getAluno(self):
        return self.__aluno

    def getHistorico(self):
        aluno = self.getAluno()
        print('Nome - {}'.format(aluno.getNome()))
        print('Curso - {}'.format(aluno.getCurso().getNome()))

        curso = aluno.getCurso()
        grade = curso.getGrade()
        disciplinasGrade = grade.getDisciplinas()
        disciplinasAluno = aluno.getDisciplinas()
        cargaObrigatoria = 0
        cargaEletiva = 0

        for disciplina in disciplinasAluno:
            if(disciplina.getGrade() == aluno.getCurso().getGrade()):
                print('{} - Obrigatória'.format(disciplina.getNome()))
                cargaObrigatoria += disciplina.getCargaHoraria()
            else:
                print('{} - Eletiva'.format(disciplina.getNome()))
                cargaEletiva += disciplina.getCargaHoraria()

        print('Carga Obrigatória - {}'.format(cargaObrigatoria))
        print('Carga Eletiva - {}'.format(cargaEletiva))


if __name__ == "__main__":
    grade1 = Grade(2020)
    grade2 = Grade(2021)
    sin = Curso('SIN', grade1)
    adm = Curso('ECO', grade2)

   # GRADE 1
    disciplina1 = Disciplina(170, 'MAT170', 90, grade1)
    disciplina3 = Disciplina(110, 'COM110', 90, grade1)

   # GRADE 2
    disciplina2 = Disciplina(170, 'MAT170', 90, grade2)
    disciplina4 = Disciplina(110, 'COM110', 90, grade2)

    grade1.addDisciplinas(disciplina1)
    grade1.addDisciplinas(disciplina3)
    grade2.addDisciplinas(disciplina2)
    grade2.addDisciplinas(disciplina4)

    aluno = Aluno(1, 'João', adm)
    aluno.addDisciplina(disciplina1)
    aluno.addDisciplina(disciplina4)

    aluno = Aluno(2, 'Carlos', sin)
    aluno.addDisciplina(disciplina3)
    aluno.addDisciplina(disciplina2)

    hist = Historico(aluno)
    hist.getHistorico()
