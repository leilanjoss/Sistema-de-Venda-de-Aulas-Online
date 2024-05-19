# from controladorUsuario import ControladorUsuarios
from model.aluno import Aluno
from view.telaAluno import TelaAluno

class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
            
    def adicionar_aluno(self):
        dados_aluno = self.__tela_aluno.pegar_dados_aluno()
        aluno = self.pegar_aluno_por_cpf(dados_aluno["cpf"])
        if aluno is None:
            novo_aluno = Aluno(dados_aluno["nome"], 
                            dados_aluno["email"], 
                            dados_aluno["telefone"], 
                            dados_aluno["cpf"], 
                            dados_aluno["cidade"],
                            dados_aluno["sigla_estado"],
                            dados_aluno["rua"],
                            dados_aluno["numero"],
                            dados_aluno["cartao"]
                            )
            self.__alunos.append(novo_aluno)
            self.__tela_aluno.mostrar_mensagem("--Aluno inserido.")
        else:
            self.__tela_aluno.mostrar_mensagem("--Aluno já existente.")

            
    def excluir_aluno(self, aluno):
        #self.listar_alunos()
        cpf = self.__tela_aluno.selecionar_aluno ()
        aluno = self.pegar_aluno_por_cpf(cpf)
        if aluno is not None:
            self.__aluno.remove(aluno)
            self.__tela_aluno.mostrar_mensagem("--Aluno excluído.")
        else:
            self.__tela_aluno.mostrar_mensagem("--Aluno não existente.")

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
    