class Endereco:
    def __init__(self, cidade: str, sigla_estado: str, rua: str, numero: int):
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(sigla_estado, str):
            self.__sigla_estado = sigla_estado
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(numero, str):
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
        return self.__numero

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
        if isinstance(numero, str):
            self.__numero = numero
    
    def __repr__(self):
        return f"Endereco(cidade='{self.cidade}', sigla_estado='{self.sigla_estado}', rua='{self.rua}', numero='{self.numero}')"

    # def __str__(self):
    #     return f"Cidade: {self.__cidade}, Estado: {self.__sigla_estado}, Rua: {self.__rua}, Número: {self.__numero}"1
    