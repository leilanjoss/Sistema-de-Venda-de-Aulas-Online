from model.aluno import Aluno
from view.telaAluno import TelaAluno
from model.endereco import Endereco
from DAOs.aluno_dao import AlunoDAO
from exceptions.aluno_exceptions import AlunoRepetidoException
from exceptions.aluno_exceptions import AlunoNExisteException


class ControladorAluno:
    def __init__(self):
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno()

    def inserir_aluno(self):
        dados_aluno = self.__tela_aluno.pegar_dados_aluno()
        aluno = self.pegar_aluno_por_cpf(dados_aluno["cpf"])
        try:
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
                raise AlunoRepetidoException(aluno)
        except AlunoRepetidoException as e:
            self.__tela_aluno.mostrar_mensagem(e)

    def pegar_aluno_por_cpf(self, cpf: int):
        for aluno in self.__aluno_DAO.get_all():
            if aluno.cpf == cpf:
                return aluno
        return None
      
    def excluir_aluno(self):
        self.listar_alunos()
        cpf = self.__tela_aluno.selecionar_aluno()
        aluno = self.pegar_aluno_por_cpf(cpf)
        try:
            if aluno is not None:
                self.__aluno_DAO.remove(aluno.cpf)
                self.__tela_aluno.mostrar_mensagem("Aluno excluído.")
                self.listar_alunos()
            else:
                raise AlunoNExisteException()
        except AlunoNExisteException as e:
            self.__tela_aluno.mostrar_mensagem(e)
     
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
            aluno.endereco = Endereco(
                            novos_dados_aluno["cidade"],
                            novos_dados_aluno["sigla_estado"],
                            novos_dados_aluno["rua"],
                            novos_dados_aluno["numero"]
                        )
            self.__aluno_DAO.update(aluno)

            self.__tela_aluno.mostrar_mensagem('Aluno alterado.')
        else:
            self.__tela_aluno.mostrar_mensagem('Não foi possível alterar o aluno.')

    def listar_alunos(self):
        if not self.__aluno_DAO:
            self.__tela_aluno.mostrar_mensagem("Nenhum aluno cadastrado.")
        else:
            self.__tela_aluno.mostrar_aluno(self.__aluno_DAO.get_all())
    

    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()
        
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
    