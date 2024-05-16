<<<<<<< HEAD
=======

>>>>>>> c05dfeb9f054186b9e7ca67199f6f66a752fa565
from model.curso import Curso
from model.professor import Professor


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__controlador_sistema = controlador_sistema

    #listar_cursos
    @property
    def cursos(self):
        return self.__cursos
    
    def inserir_curso(self, curso: Curso):
        if isinstance(curso, Curso):
            if curso not in self.__cursos:
                self.__cursos.append(curso)
            #     return 'Curso inserido com sucesso'
            # return 'Esse curso já existe'

    def excluir_curso(self, curso: Curso):
        if isinstance(curso, Curso):
            if curso in self.__cursos:
                self.__cursos.remove(curso)
            #     return ('Curso excluído com sucesso')
            # return ('Esse curso não existe')

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

    def selecionar_curso_por_codigo(self, codigo_curso):
        for curso in self.__cursos:
            if curso.codigo_curso == codigo_curso:
                return curso
        return None
    
    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_curso, 
                        2: self.excluir_curso, 
                        3: self.alterar_curso, 
                        4: self.cursos, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
    
        