from view.telaSistema import TelaSistema
from controller.controladorCurso import ControladorCurso
from controller.controladorProfessor import ControladorProfessor
from controller.controladorAluno import ControladorAluno
from controller.controladorRelatorio import ControladorRelatorio


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cursos = ControladorCurso(self)
        self.__controlador_professores = ControladorProfessor()
        self.__controlador_alunos = ControladorAluno(self)
        self.__controlador_relatorios = ControladorRelatorio()
    
    @property
    def controlador_cursos(self):
        return self.__controlador_cursos

    @property
    def controlador_professores(self):
        return self.__controlador_professores
    
    @property
    def controlador_alunos(self):
        return self.__controlador_alunos
    
    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios
 
    def cadastrar_professores(self):
        self.__controlador_professores.abrir_tela()

    def cadastrar_alunos(self):
        self.__controlador_alunos.abrir_tela()
    
    def cadastrar_cursos(self):
        self.__controlador_cursos.abrir_tela()

    def relatorios(self):
        self.__controlador_relatorios.abrir_tela

    def inicializar_sistema(self):
        self.abrir_tela()
    
    def encerrar_sistema(self):
        exit(0)
    
    def abrir_tela(self):
        lista_opcoes = {
            1: self.cadastrar_professores,
            2: self.cadastrar_alunos,
            3: self.cadastrar_cursos,
            4: self.relatorios,
            0: self.encerrar_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Escolha novamente.")
