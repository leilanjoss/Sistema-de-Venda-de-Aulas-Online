from controladorUsuario import ControladorUsuarios
from model.aluno import Aluno
from view.telaAluno import TelaAluno

class ControladorAluno(ControladorUsuarios):
    def __init__(self, controlador_sistema, alunos):
        super().__init__(controlador_sistema)
        self.__alunos = alunos
        self.__tela_professor = TelaAluno()
            
    def inserir_aluno(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_aluno = Aluno(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_aluno, Aluno):
            for aluno in self.__alunos:
                if aluno.cpf == cpf:
                    return None
            if novo_aluno not in self.__alunos:
                self.__alunos.append(novo_aluno)
                return novo_aluno
            
    def excluir_aluno(self, aluno):
        if isinstance(aluno, Aluno) and aluno is not None and aluno in self.__alunos:
            self.__alunos.remove(aluno)
            return aluno

    def alterar_aluno(self):
        super().alterar_aluno()
        
    def listar_alunos(self):
        return super().listar_alunos()

    def retornar(self):
        self.__controlador_sistema.abrir
        
    def abrir_tela(self):
        return super().abrir_tela()
    