from model.curso import Curso
from model.professor import Professor
from view.telaProfessor import TelaProfessor
from view.telaCurso import TelaCurso


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_curso = TelaCurso()

    @property
    def cursos(self):
        return self.__cursos
    
    def pegar_curso_por_codigo(self, codigo_curso):
        for curso in self.__cursos:
            if curso.codigo_curso == codigo_curso:
                return curso
        return None
    
    def inserir_curso(self):
        curso = self.__tela_curso.pegar_dados_curso()
        curso_ja_existe = self.pegar_curso_por_codigo(curso.codigo_curso)
        if curso_ja_existe is None:
            self.__cursos.append(curso)
            self.__tela_curso.mostrar_mensagem("--Curso inserido.")
        else:
            self.__tela_curso.mostrar_mensagem("--Curso já existente.")

    def excluir_curso(self):
        codigo_curso = self.__tela_curso.selecionar_curso()
        curso = self.pegar_curso_por_codigo(codigo_curso)
        if curso is not None:
            self.__cursos.remove(curso)
            self.__tela_curso.mostrar_mensagem("--Curso excluído.")
        else:
            self.__tela_curso.mostrar_mensagem("--Curso não existente.")
    
    def listar_cursos(self):
        if not self.__cursos:
            self.__tela_curso.mostrar_mensagem("--Nenhum curso cadastrado.")
        else:
            return self.__tela_curso.mostrar_cursos(self.__cursos)
    

    def alterar_curso(self):
       codigo = self.__tela_curso.selecionar_curso()              
       curso_alterado = self.__tela_curso.pegar_dados_curso()
       self.atualizar_curso(codigo, curso_alterado)

    def atualizar_curso(self, codigo_curso, curso):
        i = 0
        for c in self.__cursos:
            if c.codigo_curso == codigo_curso:                
                self.__cursos[i] = curso                
                return
            i += 1    
    
    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_curso, 
                        2: self.alterar_curso, 
                        3: self.listar_cursos, 
                        4: self.excluir_curso, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
    
        