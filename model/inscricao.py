from controller.controladorCurso import ControladorCurso
from controller.controladorInscricao import ControladorInscricao
from model.curso import Curso
from model.aluno import Aluno
# Fazer a ligação com  o pontilhado, acho que deve ser pra puxar dos dois

class Inscricao():
    def __init__(self, curso: Curso, aluno: Aluno, preco_pago: float, data_hora: int):
        self.__curso = curso
        self.__aluno = aluno
        self.__preco_pago =  preco_pago
        self.__data_hora = data_hora

    @property
    def curso (self):
        return self.__curso

    @property
    def aluno (self):
        return self.__aluno

    @property
    def preco_pago(self):
        return self.__preco_pago

    @property
    def data_hora(self):
        return self.__data_hora

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno
