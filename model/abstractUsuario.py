from model.endereco import Endereco
from abc import ABC, abstractmethod

class AbstractUsuario(ABC):
    @abstractmethod
    def __init__(self, 
                 nome: str, 
                 email: str,
                #  senha: str,
                 telefone: int,
                 cpf: int, 
                 cidade: str, 
                 sigla_estado: str, 
                 rua: str, 
                 numero: int):
        self.__nome = nome
        self.__email = email
        # self.__senha = senha
        self.__telefone = telefone
        self.__cpf = cpf
        self.__endereco = Endereco(cidade, sigla_estado, rua, numero)

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    # @property
    # def senha(self) -> str:
    #     return self.__senha

    @property
    def telefone(self) -> int:
        return self.__telefone

    @property
    def cpf(self) -> int:
        return self.__cpf

    @property
    def endereco(self) -> Endereco:
        return self.__endereco
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    # @senha.setter
    # def senha(self, senha):
    #     if isinstance(senha, str):
    #         self.__senha = senha
    
    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, int):
            self.__telefone = telefone

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, Endereco):
            self.__endereco = endereco

    # def __repr__(self):
    #     return f"Endereco(cidade='{self.__cidade}', sigla_estado='{self.__sigla_estado}', rua='{self.__rua}', numero={self.__numero})"