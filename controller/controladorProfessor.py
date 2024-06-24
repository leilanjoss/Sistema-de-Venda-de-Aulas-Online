from model.professor import Professor
from view.telaProfessor import TelaProfessor
from model.endereco import Endereco
from DAOs.professor_dao import ProfessorDAO


class ControladorProfessor:
    def __init__(self):
        # self.__professores = []
        self.__professor_DAO = ProfessorDAO()
        self.__professor_DAO.add(Professor("João Silva","joaosilva@gmail.com", "111111", "1", "Florianopolis", "SC", "Rua das Laranjeiras", "10"))
        self.__tela_professor = TelaProfessor()
       
    # @property
    # def professores(self):
    #     return self.__professores
    
    @property
    def tela_professor(self):
        return self.__tela_professor

    def inserir_professor(self):
        dados_professor = self.__tela_professor.pegar_dados_professor()
        professor = self.pegar_professor_por_cpf(dados_professor["cpf"])
        if professor is None:
            novo_professor = Professor(dados_professor["nome"], 
                                  dados_professor["email"], 
                                  dados_professor["telefone"], 
                                  dados_professor["cpf"], 
                                  dados_professor["cidade"],
                                  dados_professor["sigla_estado"],
                                  dados_professor["rua"],
                                  dados_professor["numero"],
                                  )
            # self.__professores.append(novo_professor)
            self.__professor_DAO.add(novo_professor)
            self.__tela_professor.mostrar_mensagem("Professor inserido.")
        else:
            self.__tela_professor.mostrar_mensagem("Professor já existente.")

    def pegar_professor_por_cpf(self, cpf: str):
        for professor in self.__professor_DAO.get_all():
            if professor.cpf == cpf:
                return professor
        return None
    
    def excluir_professor(self):
        self.listar_professores()
        cpf = self.__tela_professor.selecionar_professor()
        professor = self.pegar_professor_por_cpf(cpf)
        if professor is not None:
            self.__professor_DAO.remove(professor.cpf)
            self.__tela_professor.mostrar_mensagem("Professor excluído.")
            self.listar_professores()
        else:
            self.__tela_professor.mostrar_mensagem("Professor não existente.")

    def alterar_professor(self):
        # self.listar_professores()
        cpf_professor = self.__tela_professor.selecionar_professor()
        professor = self.pegar_professor_por_cpf(cpf_professor)
        if professor is not None:
            novos_dados_professor = self.__tela_professor.pegar_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.endereco = Endereco(novos_dados_professor["cidade"],
                                          novos_dados_professor["sigla_estado"],
                                          novos_dados_professor["rua"],
                                          novos_dados_professor["numero"]),
            self.__professor_DAO.update(professor)

            self.__tela_professor.mostrar_mensagem('Professor alterado.')
        else:
            self.__tela_professor.mostrar_mensagem('Não foi possível alterar o professor.')

    def listar_professores(self):
        if not self.__professor_DAO:
            self.__tela_professor.mostrar_mensagem("Nenhum professor cadastrado.")
        else:
            # dados_professores = []
            # for professor in self.__professor_DAO.get_all():
            #     dados_professores.append({
            #         "nome": professor.nome,
            #         # "email": professor.email,
            #         # "telefone": professor.telefone,
            #         "cpf": professor.cpf,
            #         # "endereco": str(professor.endereco)
            #     })
            self.__tela_professor.mostrar_professor(self.__professor_DAO.get_all())
    

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
        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()

    