from model.aluno import Aluno
from view.telaAluno import TelaAluno
from model.endereco import Endereco
from DAOs.aluno_dao import AlunoDAO

class ControladorAluno:
    def __init__(self, controlador_sistema):
        # self.__alunos = []
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno()
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
            self.__aluno_DAO.add(novo_aluno)
            self.__tela_aluno.mostrar_mensagem("Aluno inserido.")
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno já existente.")

    def pegar_aluno_por_cpf(self, cpf: str):
        # for aluno in self.__alunos:
        for aluno in self.__aluno_DAO.get_all():
            if aluno.cpf == cpf:
                return aluno
        return None
      
    def excluir_aluno(self):
        self.listar_alunos()
        cpf = self.__tela_aluno.selecionar_aluno()
        aluno = self.pegar_aluno_por_cpf(cpf)
        if aluno is not None:
            self.__aluno_DAO.remove(aluno) #Ou aluno.cpf
            self.__tela_aluno.mostrar_mensagem("Aluno excluído.")
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não existente.")

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
            self.__aluno_DAO.update(aluno)

            self.__tela_aluno.mostrar_mensagem('Aluno alterado.')
            self.__tela_aluno.mostrar_mensagem('Aluno alterado.')
        else:
            self.__tela_aluno.mostrar_mensagem('Não foi possível alterar o aluno.')
            self.__tela_aluno.mostrar_mensagem('Não foi possível alterar o aluno.')


    def listar_alunos(self):
        # if not self.__aluno_DAO.get_all():
        #     self.__tela_aluno.mostrar_mensagem("Nenhum aluno cadastrado.")
        #     print("passou aqui")
        #     print(self.__aluno_DAO.get_all)
            
        # else:
        #     dados_alunos = []
        #     for aluno in self.__aluno_DAO.get_all():
        #         dados_alunos.append({"nome": aluno.nome})
        #         # self.__tela_aluno.mostrar_aluno({
        #         #     "nome": aluno.nome,
        #         #     # "email":    aluno.email,
        #         #     # "telefone": aluno.telefone,
        #         #     "cpf": aluno.cpf,
        #         #     # "cartao": aluno.cartao,
        #         #     # "endereco": str(aluno.endereco)
        #         # })

        #     self.__tela_aluno.mostrar_aluno(dados_alunos)
        #     print(self.__aluno_DAO.get_all())
        try:
            alunos = self.__aluno_DAO.get_all()
            print(f"Alunos no DAO: {alunos}")  # Para verificação de conteúdo
            if not alunos:
                self.__tela_aluno.mostrar_mensagem("Nenhum aluno cadastrado.")
            else:
                dados_alunos = [{"nome": aluno.nome} for aluno in alunos]
                self.__tela_aluno.mostrar_aluno(dados_alunos)
                print(dados_alunos)  # Para debug
        except Exception as e:
            print(f"Erro ao listar alunos: {e}")       
        
                # print("------------------------------")

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
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
    