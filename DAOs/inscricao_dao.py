from model.inscricao import Inscricao
from DAOs.dao import DAO

class InscricaoDAO(DAO):
    def __init__(self):
        # self.__inscricoes = []
        super().__init__('inscricao.pkl')

    def add(self, inscricao: Inscricao):
        self.__inscricoes.append(inscricao)

    def remove(self, inscricao: Inscricao):
        self.__inscricoes.remove(inscricao)

    def update(self, inscricao: Inscricao):
        index = self.__inscricoes.index(inscricao)
        self.__inscricoes[index] = inscricao

    def get_all(self):
        return self.__inscricoes
