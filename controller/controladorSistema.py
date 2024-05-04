from controller.controladorUsuario import ControladorUsuarios
from view.telaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios
        self.__tela_sistema = TelaSistema

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_alunos(self):
        self.__controlador_usuarios.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_alunos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()