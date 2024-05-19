from model.abstractUsuario import AbstractUsuario


class Aluno(AbstractUsuario):
    def __init__(self, 
                 nome: str, 
                 email: str, 
                 senha: str, 
                 telefone: int, 
                 cpf: int,  
                 cidade: str, 
                 sigla_estado: str, 
                 rua: str, 
                 numero: str, 
                 cartao: str): #str ou int
        super().__init__(nome, email, telefone, cpf, cidade, sigla_estado, rua, numero)
        self.__cartao = cartao

    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, cartao):
        if isinstance(cartao, str):
            self.__cartao = cartao
