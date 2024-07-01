class Aula:
    def __init__(self,
        titulo: str,
        descricao_aula: str,
        ):
        self.__titulo = titulo
        self.__descricao_aula = descricao_aula

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def descricao_aula(self):
        return self.__descricao_aula

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @descricao_aula.setter
    def descricao_aula(self, descricao_aula):
        self.__descricao_aula = descricao_aula
    
