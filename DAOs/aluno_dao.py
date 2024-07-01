from DAOs.dao import DAO
from model.aluno import Aluno


class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, int)):
            super().add(aluno.cpf, aluno)
            print(f"Aluno added: {aluno}")

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, int)):
            super().update(aluno.cpf, aluno)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        print(f"Aluno: {key}")
        if isinstance(key, int):
            super().remove(key)
            print(f"Aluno removed with key: {key}")