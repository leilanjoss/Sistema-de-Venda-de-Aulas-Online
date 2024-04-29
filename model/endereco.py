class Endereco:
    def __init__(self, cidade: str, sigla_estado: str, rua: str, numero: int):
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(sigla_estado, str):
            self.__sigla_estado = sigla_estado
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(numero, int):
            self.__numero = numero
    @property
    def cidade(self):
        return self.__cidade

    @property
    def sigla_estado(self):
        return self.__sigla_estado
    
    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.numero

    @cidade.setter
    def cidade(self, cidade):
        if isinstance(cidade, str):
            self.__cidade = cidade
    
    @sigla_estado.setter
    def sigla_estado(self, sigla_estado):
        if isinstance(sigla_estado, str):
            self.__sigla_estado = sigla_estado
    
    @rua.setter
    def rua(self, rua):
        if isinstance(rua, str):
            self.__rua = rua

    @numero.setter
    def numero(self, numero):
        if isinstance(numero, int):
            self.__numero = numero