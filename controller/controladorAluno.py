# from controladorUsuario import ControladorUsuarios
from model.aluno import Aluno
from view.telaAluno import TelaAluno

class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
            
    def inserir_aluno(self, nome, email,telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_aluno = Aluno(nome, email, telefone, cpf, cidade, sigla_estado, rua, numero)
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
        pass
        
    def listar_alunos(self):
       pass

    def retornar(self):
        self.__controlador_sistema.abrir
        
    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_aluno,
            2: self.alterar_aluno,
            3: self.__alunos,
            4: self.excluir_aluno,
            0: self.retornar
        }
        continua = True
        while continua:
            # opcao = self.__tela_aluno.tela_opcoes()
            # funcao_escolhida = lista_opcoes.get(opcao)
            # if funcao_escolhida:
            #     funcao_escolhida()
            # else:
            #     self.__tela_aluno.mostrar_mensagem("Opção inválida. Escolha novamente.")
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
    