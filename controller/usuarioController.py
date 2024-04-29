from ..model.aluno import Aluno
from ..model.professor import Professor

class UsuarioController:
    def __init__(self):
        self.__alunos = []
        self.__professores = []

    def inserir_aluno(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_aluno = Aluno(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_aluno, Aluno):
            for aluno in self.__alunos:
                if aluno.cpf == cpf:
                    return None
            if novo_aluno not in self.__alunos:
                self.__alunos.append(novo_aluno)
                return novo_aluno
            
    def inserir_professor(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_professor = Professor(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_professor, Professor):
            for professor in self.__professores:
                if professor.cpf == cpf:
                    return None
            if novo_professor not in self.__professores:
                self.__professors.append(novo_professor)
                return novo_professor

    # def excluir_aluno():
    # def excluir_professor():
