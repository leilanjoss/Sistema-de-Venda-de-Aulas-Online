from model.abstractUsuario import AbstractUsuario

class Aluno(AbstractUsuario):
    def __init__(self, nome: str, email: str, senha: str, telefone: int, cpf: int,  cidade: str, sigla_estado: str, rua: str, numero: int):
        super().__init__(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)