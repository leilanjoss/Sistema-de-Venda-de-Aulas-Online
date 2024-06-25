from DAOs.dao import DAO
from model.curso import Curso


class CursoDAO(DAO):
    def __init__(self):
        super().__init__('cursos.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo_curso, str)):
            super().add(curso.codigo_curso, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo_curso, str)):
            super().update(curso.codigo_curso, curso)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    # def remove(self, key:int):
    #     if(isinstance(key, int)):
    #         return super().remove(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)
