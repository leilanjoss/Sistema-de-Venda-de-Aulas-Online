from model.professor import Professor
from view.telaProfessor import TelaProfessor

class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    @property
    def professores(self):
        return self.__professores

    def inserir_professor(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_professor = Professor(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_professor, Professor):
            for professor in self.__professores:
                if professor.cpf == cpf:
                    return None
            if novo_professor not in self.__professores:
                self.__professores.append(novo_professor)
                return novo_professor

    def pega_professor_por_cpf(self, cpf: int):
        for professor in self.__professores:
            if(professor.cpf == cpf):
                return professor
        return None

    def alterar_professor(self):
        self.listar_professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if(professor is not None):
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.email = novos_dados_professor["email"]
            professor.telefone = novos_dados_professor["telefone"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.cidade = novos_dados_professor["cidade"]
