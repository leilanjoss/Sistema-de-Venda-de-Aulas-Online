from model.abstractUsuario import AbstractUsuario


class Professor(AbstractUsuario):
    def __init__(self, 
                 nome: str, 
                 email: str, 
                 telefone: str, 
                 cpf: str,  
                 cidade: str, 
                 sigla_estado: str, 
                 rua: str, 
                 numero: str):
        super().__init__(nome, email, telefone, cpf, cidade, sigla_estado, rua, numero)

