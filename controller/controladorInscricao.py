from view.telaListagemCursos import TelaListagemCursos # Verificar se o caminho está correto
from model.inscricao import Inscricao
from controller.controladorCurso import ControladorCurso

class ControladorInscricao():
    def __init__(self, controlador_sistema):
        self.__inscricoes = []
        self.__tela_listagem_cursos = TelaListagemCursos()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_curso = ControladorCurso

    @property
    def inscricoes(self):
        return self.__inscricoes

    def inserir_inscricao(self, inscricao: Inscricao):
        if isinstance(inscricao, Inscricao) and inscricao not in self.__inscricoes:
            self.__inscricoes.append(inscricao)

    def excluir_inscricao(self, inscricao: Inscricao):
        if isinstance(inscricao, Inscricao) and inscricao in self.__inscricoes:
            self.__inscricoes.remove(inscricao)

    def atualizar_inscricao(self, codigo_curso, aluno, preco_pago, data_hora):
        for inscricao in self.__inscricoes:
            if inscricao.curso.codigo == codigo_curso:
                inscricao.aluno = aluno
                inscricao.preco_pago = preco_pago
                inscricao.data_hora = data_hora

    def listar_inscricoes_por_curso(self, curso):
        num_inscricoes = 0
        for inscricao in self.__inscricoes:
            if inscricao.curso == curso:
                num_inscricoes += 1
        return num_inscricoes

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def controlador_curso(self):
        return self.controlador_curso.listar_cursos()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_inscricao,
            2: self.excluir_inscricao,
            3: self.atualizar_inscricao,
            4: self.__tela_listagem_cursos.listar_cursos,
            0: self.retornar
        }
        continua = True
        while continua:
            opcao = self.__controlador_curso.listar_cursos
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            if opcao == 0:
                continua = False
