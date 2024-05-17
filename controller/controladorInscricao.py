# Verificar caminho e nome de alguns imports já que eu fiz antes de criar os arquivos
from view.telaListagemCursos import TelaListagemCursos #Verificar
from view.telaInscricao import TelaInscricao #Verificar
from controladorSistema import ControladorSistema
from controladorRelatorio import ControladorRelatorio #Verificar
from model.inscricao import Inscricao

class ControladorInscricao:
    def __init__(self, controlador_sistema):
        self.__inscricoes = []
        self.__tela_listagem_cursos = TelaListagemCursos()
        self.__controlador_sistema = controlador_sistema
    
    def inserir_inscricao(self, inscricao: Inscricao):
        if (isinstance(inscricao, Inscricao) and inscricao is not None and inscricao is not self.__inscricoes):
            self.__inscricoes.append