from DAOs.dao import DAO
from model.professor import Professor

#cada entidade terá uma classe dessa, implementação bem simples.
class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professores.pkl')

    def add(self, professor: Professor):
        if((professor is not None) and isinstance(professor, Professor) and isinstance(professor.cpf, int)):
            super().add(professor.cpf, professor)

    def update(self, professor: Professor):
        if((professor is not None) and isinstance(professor, Professor) and isinstance(professor.cpf, int)):
            super().update(professor.cpf, professor)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)