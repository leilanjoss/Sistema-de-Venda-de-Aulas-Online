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

    def inserir_professor(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_professor = Professor(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_professor, Professor):
            for professor in self.__professores:
                if professor.cpf == cpf:
                    return None
            if novo_professor not in self.__professores:
                self.__professores.append(novo_professor)
                return novo_professor

    def pegar_professor_por_cpf(self, cpf: int):
        for professor in self.__professores:
            if(professor.cpf == cpf):
                return professor
        return None
    
    def excluir_professor(self):
        self.__professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            self.__professores.remove(professor)
            self.__professores()
        else:
            self.__tela_professor.mostra_mensagem("ATENCAO: professor não existente")

    # def listar_professores(self):
    #     if not self.__professores:
    #         self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado.")
    #     else:
    #         for professor in self.__professores:
    #             self.__tela_professor.mostra_professor({
    #                 "nome": professor.nome,
    #                 "email": professor.email,
    #                 "telefone": professor.telefone,
    #                 "cpf": professor.cpf,
    #                 "cidade": professor.cidade,
    #                 "sigla estado": professor.sigla_estado,
    #                 "rua": professor.rua,
    #                 "numero": professor.numero
    #             })


    def alterar_professor(self):
        self.__professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if(professor is not None):
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.cidade = novos_dados_professor["cidade"]

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_professor,
            2: self.alterar_professor,
            3: self.__professores,
            4: self.excluir_professor,
            0: self.retornar
        }
        continua = True
        while continua:
            # opcao = self.__tela_professor.tela_opcoes()
            # funcao_escolhida = lista_opcoes.get(opcao)
            # if funcao_escolhida:
            #     funcao_escolhida()
            # else:
            #     self.__tela_professor.mostrar_mensagem("Opção inválida. Escolha novamente.")
            lista_opcoes[self.__tela_professor.tela_opcoes()]()