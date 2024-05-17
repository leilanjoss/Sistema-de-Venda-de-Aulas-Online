from controller.controladorUsuario import ControladorUsuarios
from view.telaSistema import TelaSistema
from controller.controladorCurso import ControladorCurso

class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = ControladorCurso(self)

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    @property
    def controlador_cursos(self):
        return self.__controlador_cursos
    
    def inicializar_sistema(self):
        self.__tela_sistema.tela_opcoes()
    
    #AVALIAR LÓGICA LOGIN E CADASTRO
    def fazer_login(self):
        self.__controlador_usuarios.abrir_tela()
    
    def fazer_cadastro(self):
        self.__controlador_usuarios.abrir_tela()
    
    def encerrar_sistema(self):
        exit(0)
    
    def abrir_tela(self):
        lista_opcoes = {1: self.fazer_login,
                        2: self.fazer_cadastro(),
                        0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()