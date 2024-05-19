from model.professor import Professor
from view.telaProfessor import TelaProfessor

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    @property
    def professores(self):
        return self.__professores
    
    @property
    def tela_professor(self):
        return self.__tela_professor

    def inserir_professor(self):
        # novo_professor = Professor(**dados_professor)
        # if isinstance(novo_professor, Professor) and novo_professor not in self.__professores:
        #     self.__professores.append(novo_professor)
        #     return novo_professor
        # return None
        dados_professor = self.__tela_professor.pegar_dados_professor()
        prof = self.pegar_professor_por_cpf(dados_professor["cpf"])
        if prof is None:
            professor = Professor(dados_professor["nome"], 
                                  dados_professor["email"], 
                                  dados_professor["telefone"], 
                                  dados_professor["cpf"], 
                                  dados_professor["cidade"],
                                  dados_professor["sigla_estado"],
                                  dados_professor["rua"],
                                  dados_professor["numero"],
                                  )
            self.__professores.append(professor)
            self.__tela_professor.mostrar_mensagem("Professor inserido.")
        else:
            self.__tela_professor.mostrar_mensagem("Professor já existente.")

    def pegar_professor_por_cpf(self, cpf: int):
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
            self.__tela_professor.mostrar_mensagem("Professor excluído.")
        else:
            self.__tela_professor.mostrar_mensagem("Professor não existente.")

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
            professor.cidade = novos_dados_professor["cidade"]
            professor.sigla_estado = novos_dados_professor["sigla_estado"]
            professor.rua = novos_dados_professor["rua"]
            professor.numero = novos_dados_professor["numero"]

            self.__tela_professor.mostrar_mensagem('Professor alterado:')
            self.__tela_professor.mostrar_professor(novos_dados_professor)
        else:
            self.__tela_professor.mostrar_mensagem('Não foi possível alterar o professor.')

    def listar_professores(self):
        if not self.__professores:
            self.__tela_professor.mostrar_mensagem("Nenhum professor cadastrado.")
        else:
            for professor in self.__professores:
                self.__tela_professor.mostrar_professor({
                    "nome": professor.nome,
                    "email": professor.email,
                    "telefone": professor.telefone,
                    "cpf": professor.cpf,
                    # "cidade": professor.cidade or "Cidade desconhecida",
                    # "sigla estado": professor.sigla_estado,
                    # "rua": professor.rua,
                    # "numero": professor.numero
                    "endereco": professor.__endereco(),
                })

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

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
            # opcao = self.__tela_professor.tela_opcoes()
            # if opcao in lista_opcoes:
            #     dados_professor = self.__tela_professor.pegar_dados_professor() if opcao == 1 else {}
            #     lista_opcoes[opcao](dados_professor)
            # else:
            #     self.__tela_professor.mostrar_mensagem("Opção inválida. Escolha novamente.")
            lista_opcoes[self.__tela_professor.tela_opcoes()]()