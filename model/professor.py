from model.abstractUsuario import AbstractUsuario


class Professor(AbstractUsuario):
    def __init__(self, 
                 nome: str, 
                 email: str, 
                 #senha: str,
                 telefone: int, 
                 cpf: int,  
                 cidade: str, 
                 sigla_estado: str, 
                 rua: str, 
                 numero: int):
        super().__init__(nome, email, telefone, cpf, cidade, sigla_estado, rua, numero)

    # def __str__(self):
    #     return f"Cidade: {self.__cidade}, Estado: {self.__sigla_estado}, Rua: {self.__rua}, Número: {self.__numero}"

    # def __repr__(self):
    #     return self.endereco
