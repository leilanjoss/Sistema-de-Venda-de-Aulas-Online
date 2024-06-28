from model.inscricao import Inscricao
from DAOs.dao import DAO

class InscricaoDAO(DAO):
    def __init__(self):
        super().__init__('inscricao.pkl')

    def add(self, inscricao: Inscricao):
        if((inscricao is not None) and isinstance(inscricao, Inscricao) and isinstance(inscricao.id, int)):
            super().add(inscricao.id, inscricao)
            print(f"Inscrição added: {inscricao}")

    def remove(self, key: int):
        print(f"Inscrição: {key}")
        if isinstance(key, int):
            super().remove(key)
            print(f"Inscrição removed with key: {key}")

    def update(self, inscricao: Inscricao):
        if((inscricao is not None) and isinstance(inscricao, Inscricao) and isinstance(inscricao.id, int)):
            super().update(inscricao.id, inscricao)
