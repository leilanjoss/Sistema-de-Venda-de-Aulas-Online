from model.professor import Professor
from view.telaProfessor import TelaProfessor
from model.endereco import Endereco



class ControladorProfessor:
    def __init__(self):
        self.__professores = []
        self.__professores.append(Professor("teste","email", "99", "1", "cidade", "SE", "rua", "99"))
        self.__tela_professor = TelaProfessor()
       

    @property
    def professores(self):
        return self.__professores
    
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
            self.__professores.append(novo_professor)
            self.__tela_professor.mostrar_mensagem("--Professor inserido.")
        else:
            self.__tela_professor.mostrar_mensagem("--Professor já existente.")

    def pegar_professor_por_cpf(self, cpf: str):
        for professor in self.__professores:
            if professor.cpf == cpf:
                return professor
        return None
    
    def excluir_professor(self):
        self.listar_professores()
        cpf = self.__tela_professor.selecionar_professor()
        professor = self.pegar_professor_por_cpf(cpf)
        if professor is not None:
            self.__professores.remove(professor)
            self.__tela_professor.mostrar_mensagem("--Professor excluído.")
        else:
            self.__tela_professor.mostrar_mensagem("--Professor não existente.")

    def alterar_professor(self):
        self.listar_professores()
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

            self.__tela_professor.mostrar_mensagem('--Professor alterado.')
        else:
            self.__tela_professor.mostrar_mensagem('--Não foi possível alterar o professor.')

    def listar_professores(self):
        if not self.__professores:
            self.__tela_professor.mostrar_mensagem("--Nenhum professor cadastrado.")
        else:
            for professor in self.__professores:
                self.__tela_professor.mostrar_professor({
                    "nome": professor.nome,
                    "email": professor.email,
                    "telefone": professor.telefone,
                    "cpf": professor.cpf,
                    "endereco": str(professor.endereco)
                })
                print("------------------------------")

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