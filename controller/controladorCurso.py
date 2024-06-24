from view.telaCurso import TelaCurso
from model.curso import Curso
from model.aula import Aula
from DAOs.curso_dao import CursoDAO


class ControladorCurso:
    def __init__(self, controlador_sistema):
        # self.__cursos = []
        self.__curso_dao = CursoDAO()
        # self.__controlador_sistema = controlador_sistema
        self.__tela_curso = TelaCurso()

    # @property
    # def cursos(self):
    #     return self.__cursos
    
    def pegar_curso_por_codigo(self, codigo_curso):
        for curso in self.__curso_dao.get_all():
            if curso.codigo_curso == codigo_curso:
                return curso
        return None
    
    def inserir_curso(self):
        # curso = self.__tela_curso.pegar_dados_curso()
        # curso_ja_existe = self.pegar_curso_por_codigo(curso.codigo_curso)
        # if curso_ja_existe is None:
        #     self.__cursos.append(curso)
        #     self.__tela_curso.mostrar_mensagem("Curso inserido.")
        # else:
        #     self.__tela_curso.mostrar_mensagem("Curso já existente.")
        dados_curso = self.__tela_curso.pegar_dados_curso()
        curso = self.pegar_curso_por_codigo(dados_curso["codigo_curso"])
        if curso is None:
            novo_curso = Curso(dados_curso["nome"], 
                               dados_curso["preco_atual"], 
                               dados_curso["descricao"], 
                               dados_curso["tempo"], 
                               dados_curso["codigo_curso"],
                               dados_curso["professor"],
                               dados_curso["titulo"],
                               dados_curso["link"],
                               dados_curso["descricao_aula"],
                               )
            self.__curso_dao.add(novo_curso)
            self.__tela_curso.mostrar_mensagem("Curso inserido.")

            print("INSERIDO")
        else:
            self.__tela_curso.mostrar_mensagem("Curso já existente.")

    def excluir_curso(self):
        # codigo_curso = self.__tela_curso.selecionar_curso()
        # curso = self.pegar_curso_por_codigo(codigo_curso)
        # if curso is not None:
        #     self.__cursos.remove(curso)
        #     self.__tela_curso.mostrar_mensagem("Curso excluído.")
        # else:
        #     self.__tela_curso.mostrar_mensagem("Curso não existente.")
        self.listar_cursos()
        codigo_curso = self.__tela_curso.selecionar_curso()
        curso = self.pegar_curso_por_codigo(codigo_curso)
        if curso is not None:
            self.__curso_dao.remove(curso.codigo_curso)
            self.__tela_curso.mostrar_mensagem("Curso excluído.")
            self.listar_cursos()
        else:
            self.__tela_curso.mostrar_mensagem("Curso não existente.")

    
    def listar_cursos(self):
        if not self.__curso_dao:
            self.__tela_curso.mostrar_mensagem("Nenhum curso cadastrado.")
        else:
            self.__tela_curso.mostrar_cursos(self.__curso_dao.get_all())

    def alterar_curso(self):
    #    codigo = self.__tela_curso.selecionar_curso()              
    #    curso_alterado = self.__tela_curso.pegar_dados_curso()
    #    self.atualizar_curso(codigo, curso_alterado)
    
    # self.listar_cursos()
        codigo_curso = self.__tela_curso.selecionar_curso()
        curso = self.pegar_curso_por_codigo(codigo_curso)
        if curso is not None:
            novos_dados_curso = self.__tela_curso.pegar_dados_curso()
            curso.nome = novos_dados_curso["nome"]
            curso.tempo = novos_dados_curso["tempo"]
            curso.descricao = novos_dados_curso["descricao"]
            curso.professor = novos_dados_curso["professor"]
            curso.preco_atual = novos_dados_curso["preco_atual"]
            curso.codigo_curso = novos_dados_curso["codigo_curso"]
            curso.aula = Aula(novos_dados_curso["titulo"],
                                          novos_dados_curso["link"],
                                          novos_dados_curso["descricao_aula"],)
            self.__curso_dao.update(curso)

            self.__tela_curso.mostrar_mensagem('Curso alterado.')
        else:
            self.__tela_curso.mostrar_mensagem('Não foi possível alterar o curso.')

    # def atualizar_curso(self, codigo_curso, curso):
    #     # i = 0
    #     # for c in self.__cursos:
    #     #     if c.codigo_curso == codigo_curso:                
    #     #         self.__cursos[i] = curso                
    #     #         return
    #     #     i += 1    
    #     pass
    
    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_curso, 
                        2: self.alterar_curso, 
                        3: self.listar_cursos, 
                        4: self.excluir_curso, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
    
        