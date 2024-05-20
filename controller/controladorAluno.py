# from controladorUsuario import ControladorUsuarios
from model.aluno import Aluno
from view.telaAluno import TelaAluno
from model.endereco import Endereco

class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__alunos.append(Aluno("testeALuno","emailALunos", "99", "1", "cidade", "SE", "rua", "99","22", "333"))
        self.__controlador_sistema = controlador_sistema
            
    def inserir_aluno(self):
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

    def pegar_aluno_por_cpf(self, cpf: str):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None
      
    def excluir_aluno(self, aluno):
        self.listar_alunos()
        cpf = self.__tela_aluno.selecionar_aluno()
        aluno = self.pegar_aluno_por_cpf(cpf)
        if aluno is not None:
            self.__aluno.remove(aluno)
            self.__tela_aluno.mostrar_mensagem("--Aluno excluído.")
        else:
            self.__tela_aluno.mostrar_mensagem("--Aluno não existente.")

    def alterar_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.selecionar_aluno()
        aluno = self.pegar_aluno_por_cpf(cpf_aluno)
        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pegar_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.email = novos_dados_aluno["email"]
            aluno.telefone = novos_dados_aluno["telefone"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.cartao = novos_dados_aluno["cartao"]
            aluno.endereco = Endereco(novos_dados_aluno["cidade"],
                                      novos_dados_aluno["sigla_estado"],
                                      novos_dados_aluno["rua"],
                                      novos_dados_aluno["numero"]),

            self.__tela_aluno.mostrar_mensagem('--Aluno alterado.')
        else:
            self.__tela_aluno.mostrar_mensagem('--Não foi possível alterar o aluno.')

        
    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostrar_mensagem("--Nenhum aluno cadastrado.")
        else:
            for aluno in self.__alunos:
                print("******")
                self.__tela_aluno.mostrar_aluno({
                    "nome": aluno.nome,
                    "email":    aluno.email,
                    "telefone": aluno.telefone,
                    "cpf": aluno.cpf,
                    "cartao": aluno.cartao,
                    "endereco": str(aluno.endereco)
                })
                print("******")
    
    def retornar(self):
        self.__controlador_sistema.abrir_tela()
        
    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_aluno,
            2: self.alterar_aluno,
            3: self.listar_alunos,
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
    