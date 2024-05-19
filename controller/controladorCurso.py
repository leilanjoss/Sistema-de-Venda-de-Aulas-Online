from model.curso import Curso
from model.professor import Professor
from view.telaProfessor import TelaProfessor
from view.telaCurso import TelaCurso


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
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
        dados_curso = self.__tela_curso.pegar_dados_curso()
        curso = self.pegar_curso_por_codigo(dados_curso["codigo_curso"])

        if curso is None:
            novo_curso = Curso(dados_curso["nome"],
                               dados_curso["preco_atual"],
                               dados_curso["descricao"],
                               dados_curso["tempo"],
                               dados_curso["codigo_curso"],
                               dados_curso["professor"]
                                )

            self.__cursos.append(novo_curso)
            self.__tela_curso.mostrar_mensagem("--Curso inserido.")
        else:
            self.__tela_curso.mostrar_mensagem("--Curso já existente.")

    def excluir_curso(self):
        # self.listar_cursos()
        codigo_curso = self.__tela_professor.selecionar_curso()
        curso = self.pegar_professor_por_codigo(codigo_curso)
        if curso is not None:
            self.__cursos.remove(curso)
            self.__tela_curso.mostrar_mensagem("--Curso excluído.")
        else:
            self.__tela_curso.mostrar_mensagem("--Curso não existente.")

    def alterar_curso(self, codigo_curso: int, novo_nome: str, novo_preco: int, nova_descricao: str, novo_tempo: int, novo_professor: Professor):
        for curso in self.__cursos:
            if curso.codigo_curso == codigo_curso:
                curso.nome = novo_nome
                curso.preco_atual = novo_preco
                curso.descricao = nova_descricao
                curso.tempo = novo_tempo
                if isinstance(novo_professor, Professor):
                    curso.professor = novo_professor
                # return 'Curso alterado com sucesso'
    
    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_curso, 
                        2: self.alterar_curso, 
                        # 3: self.listar_cursos, 
                        4: self.excluir_curso, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
    
        