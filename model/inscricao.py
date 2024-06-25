from model.curso import Curso
from model.aluno import Aluno

class Inscricao:
    def __init__(self, curso: Curso, aluno: Aluno, data_hora: int, id: int):
        self.__curso = curso
        self.__aluno = aluno
        self.__data_hora = data_hora
        self.__id = id

    @property
    def curso(self):
        return self.__curso

    @property
    def aluno(self):
        return self.__aluno

    @property
    def preco_pago(self):
        return self.__preco_pago

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def id(self):
        return self.__id

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno
