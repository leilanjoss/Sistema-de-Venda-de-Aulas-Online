class Material:
    def __init__(self):
        pass

    @property
    def descricao_material(self):
        return self.__descricao_material

    @property
    def anexo(self):
        return self.__anexo
    
    @descricao_material.setter
    def descricao_material(self, descricao_material):
        self.__descricao_material = descricao_material
    
    @anexo.setter
    def anexo(self, anexo):
        self.__anexo = anexo
