from DAOs.dao import DAO
from model.curso import Curso

#cada entidade terá uma classe dessa, implementação bem simples.
class CursoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.cpf, str)):
            super().add(curso.cpf, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.cpf, str)):
            super().update(curso.cpf, curso)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)