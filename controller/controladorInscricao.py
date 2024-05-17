# Verificar caminho e nome de alguns imports já que eu fiz antes de criar os arquivos
from view.telaListagemCursos import TelaListagemCursos #Verificar
from view.telaInscricao import TelaInscricao #Verificar
from controladorSistema import ControladorSistema
from controladorRelatorio import ControladorRelatorio #Verificar
from model.inscricao import Inscricao
from model.aluno import Aluno
from model.curso import Curso


class ControladorInscricao:
    def __init__(self, controlador_sistema):
        self.__inscricoes = []
        self.__tela_listagem_cursos = TelaListagemCursos()
        self.__controlador_sistema = controlador_sistema
        
    
    def inserir_inscricao(self, inscricao: Inscricao):
        if (isinstance(inscricao, Inscricao) and inscricao is not None and inscricao is not self.__inscricoes):
            self.__inscricoes.append(inscricao)

    def excluir_inscricao(self, inscricao):
        if (isinstance(inscricao, Inscricao) and inscricao is not None and inscricao is not self.__inscricoes):
            self.__inscricoes.remove(inscricao)

    def atualizar_inscricao(self, codigo_curso, aluno, preco_pago, data_hora):
        for inscricao in self.__inscricoes:
            if inscricao.curso == codigo_curso:
                inscricao.aluno = aluno
                inscricao.preco_pago = preco_pago
                inscricao.data_hora = data_hora

    def listar_inscricoes_por_curso(self, curso):
        num_inscricoes = 0
        for curso_busca in self.__inscricoes.curso:
            if curso_busca == curso:
                num_inscricoes += 1
        return num_inscricoes
    
    def retornar(self):
        self.__controlador_sistema.abrir_tela()
        
    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_inscricao,
                        2: self.excluir_inscricao,
                        3: self.atualizar_inscricao,
                        4: self.__inscricoes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela]
    
    