from model.aluno import Aluno
from model.professor import Professor
from view.telaAluno import TelaAluno

class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__professores = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def inserir_aluno(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
        novo_aluno = Aluno(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
        if isinstance(novo_aluno, Aluno):
            for aluno in self.__alunos:
                if aluno.cpf == cpf:
                    return None
            if novo_aluno not in self.__alunos:
                self.__alunos.append(novo_aluno)
                return novo_aluno
            
    def pega_aluno_por_cpf(self, cpf: int):
        for aluno in self.__alunos:
            if(aluno.cpf == cpf):
                return aluno
            return None
        
    def alterar_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_cpf(cpf_aluno)

        if(aluno is not None):
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.email = novos_dados_aluno["email"]
            aluno.telefone = novos_dados_aluno["telefone"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.cidade = novos_dados_aluno["cidade"]
            aluno.sigla_estado = novos_dados_aluno["sigla_estado"]
            aluno.rua = novos_dados_aluno["rua"]
            aluno.numero = novos_dados_aluno["numero"]
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: aluno não existente")

    def listar_alunos(self):
        for aluno in self.__alunos:
            if self.__alunos == []:
                "Esse aluno não existe"
            else:
                self.__tela_aluno.mostra_aluno({"nome": aluno.nome,
                                                "email": aluno.email,
                                                "telefone": aluno.telefone,
                                                "cpf": aluno.cpf,
                                                "cidade": aluno.cidade,
                                                "sigla estado": aluno.sigla_estado,
                                                "rua": aluno.rua,
                                                "numero": aluno.numero})
                #mostrar 'endereco' ou cada um?
    def excluir_aluno(self):
        self.listar_alunos()
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_cpf(cpf_aluno)

        if(aluno is not None):
            self.__alunos.remove(aluno)
            self.lista_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: aluno não existente")
                
    # def inserir_professor(self, nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero):
    #     novo_professor = Professor(nome, email, senha, telefone, cpf, cidade, sigla_estado, rua, numero)
    #     if isinstance(novo_professor, Professor):
    #         for professor in self.__professores:
    #             if professor.cpf == cpf:
    #                 return None
    #         if novo_professor not in self.__professores:
    #             self.__professors.append(novo_professor)
    #             return novo_professor

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_aluno, 2: self.alterar_aluno, 3: self.listar_alunos, 4: self.excluir_aluno, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
    # def excluir_professor():
