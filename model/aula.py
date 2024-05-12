from material import Material


class Aula:
    def __init__(self, titulo: str, link: str, descricao_aula: str, ordem: int, descricao_material, anexo):
        self.__titulo = titulo
        self.__link = link
        self.__descricao_aula = descricao_aula
        self.__ordem = ordem
        self.__materiais = Material(descricao_material, anexo)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def link(self):
        return self.__link
    
    @property
    def descricao_aula(self):
        return self.__descricao_aula

    @property
    def ordem(self):
        return self.__ordem
    
    @property
    def materiais(self):
        return self.__materiais
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @link.setter
    def link(self, link):
        self.__link = link

    @descricao_aula.setter
    def descricao_aula(self, descricao_aula):
        self.__descricao_aula = descricao_aula
    
    @ordem.setter
    def ordem(self, ordem):
        self.__ordem = ordem

    @materiais.setter
    def materiais(self, materiais):
        self.__materiais = materiais
