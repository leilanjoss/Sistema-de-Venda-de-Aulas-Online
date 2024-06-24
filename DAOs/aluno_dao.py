from DAOs.dao import DAO
from model.aluno import Aluno

#cada entidade terá uma classe dessa, implementação bem simples.
class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str)):
            super().add(aluno.cpf, aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str)):
            super().update(aluno.cpf, aluno)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    # def remove(self, key:int):
    #     if(isinstance(key, int)):
    #         return super().remove(key)

    def remove(self, key: str):
        print(f"Aluno: {key}")
        if isinstance(key, str):
            super().remove(key)
            print(f"Aluno removed with key: {key}")