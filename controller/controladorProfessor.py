from model.professor import Professor
from view.telaProfessor import TelaProfessor
from model.endereco import Endereco
from DAOs.professor_dao import ProfessorDAO
from exceptions.professor_exceptions import ProfessorRepetidoException, ProfessorNExisteException

class ControladorProfessor:
    def __init__(self):
        self.__professor_DAO = ProfessorDAO()
        self.__tela_professor = TelaProfessor()

    @property
    def tela_professor(self):
        return self.__tela_professor

    def inserir_professor(self):
        dados_professor = self.__tela_professor.pegar_dados_professor()
        professor_existente = self.pegar_professor_por_cpf(dados_professor["cpf"])
        if professor_existente:
            raise ProfessorRepetidoException(dados_professor["cpf"])
        novo_professor = Professor(
            dados_professor["nome"], 
            dados_professor["email"], 
            dados_professor["telefone"], 
            dados_professor["cpf"], 
            Endereco(
                dados_professor["cidade"],
                dados_professor["sigla_estado"],
                dados_professor["rua"],
                dados_professor["numero"]
            )
        )
        self.__professor_DAO.add(novo_professor)
        self.__tela_professor.mostrar_mensagem("Professor inserido com sucesso.")

    def pegar_professor_por_cpf(self, cpf: int):
        for professor in self.__professor_DAO.get_all():
            if professor.cpf == cpf:
                return professor
        return None

    def excluir_professor(self):
        self.listar_professores()
        cpf = self.__tela_professor.selecionar_professor()
        professor = self.pegar_professor_por_cpf(cpf)
        if not professor:
            raise ProfessorNExisteException()
        self.__professor_DAO.remove(cpf)
        self.__tela_professor.mostrar_mensagem("Professor excluído com sucesso.")
        self.listar_professores()

    def alterar_professor(self):
        self.listar_professores()
        cpf_professor = self.__tela_professor.selecionar_professor()
        professor = self.pegar_professor_por_cpf(cpf_professor)
        if not professor:
            self.__tela_professor.mostrar_mensagem('Professor não encontrado.')
            return
        novos_dados_professor = self.__tela_professor.pegar_dados_professor()
        professor.nome = novos_dados_professor["nome"]
        professor.email = novos_dados_professor["email"]
        professor.telefone = novos_dados_professor["telefone"]
        professor.endereco = Endereco(
            novos_dados_professor["cidade"],
            novos_dados_professor["sigla_estado"],
            novos_dados_professor["rua"],
            novos_dados_professor["numero"]
        )
        self.__professor_DAO.update(professor)
        self.__tela_professor.mostrar_mensagem('Professor alterado com sucesso.')

    def listar_professores(self):
        professores = self.__professor_DAO.get_all()
        if not professores:
            self.__tela_professor.mostrar_mensagem("Nenhum professor cadastrado.")
        else:
            self.__tela_professor.mostrar_professor(professores)

    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_professor,
            2: self.alterar_professor,
            3: self.listar_professores,
            4: self.excluir_professor,
            0: self.retornar
        }
        while True:
            opcao = self.__tela_professor.tela_opcoes()
            acao = lista_opcoes.get(opcao)
            if acao:
                acao()
            else:
                break
