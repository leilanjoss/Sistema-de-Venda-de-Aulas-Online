from model.material import Material


class Aula:
    def __init__(self):
        self.__materiais = []

    def adicionar_material(self, material: Material):
        if isinstance(material, Material):
            self.__materiais.append(material)

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
    
    @materiais.setter
    def materiais(self, materiais):
        self.__materiais = materiais
