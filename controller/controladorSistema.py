from view.telaSistema import TelaSistema
# from controller.controladorUsuario import ControladorUsuarios
from controller.controladorCurso import ControladorCurso
from controller.controladorProfessor import ControladorProfessor

class ControladorSistema:

    def __init__(self):
        # self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = ControladorCurso(self)
        self.__controlador_professores = ControladorProfessor(self)

    # @property
    # def controlador_usuarios(self):
    #     return self.__controlador_usuarios
    
    @property
    def controlador_cursos(self):
        return self.__controlador_cursos

    @property
    def controlador_professores(self):
        return self.__controlador_professores
    
    def cadastrar_professores(self):
        self.__controlador_professores.abrir_tela()
    
    def inicializar_sistema(self):
        self.__tela_sistema.tela_opcoes()
    
    def encerrar_sistema(self):
        exit(0)
    
    def abrir_tela(self):
        lista_opcoes = {
            1: self.cadastrar_professores,
            # 2: self.__controlador_alunos.abrir_tela,  # Adicione isso quando o controlador de alunos estiver pronto
            0: self.encerrar_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Escolha novamente.")