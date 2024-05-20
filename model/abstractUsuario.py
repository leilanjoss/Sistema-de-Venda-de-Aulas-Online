from model.endereco import Endereco
from abc import ABC, abstractmethod

class AbstractUsuario(ABC):
    @abstractmethod
    def __init__(self, 
                 nome: str, 
                 email: str,
                 telefone: str,
                 cpf: str, 
                 cidade: str, 
                 sigla_estado: str, 
                 rua: str, 
                 numero: str):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__cpf = cpf
        self.__endereco = Endereco(cidade, sigla_estado, rua, numero)

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @property
    def cpf(self) -> str:
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
    
    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
