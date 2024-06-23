from model.aula import Aula
from model.professor import Professor


class Curso:
    # def __init__(self):
    #      self.__aulas = []
    def __init__(self,
                 nome: str,
                 preco_atual: float,
                 descricao: str,
                 tempo: str,
                 codigo_curso: str,
                 professor: Professor,
                 titulo: str,
                 link: str,
                 descricao_aula: str,
                #  descricao_material: str,
                #  anexo: str
                 ):
        self.__nome = nome
        self.__preco_atual = preco_atual
        self.__descricao = descricao
        self.__tempo = tempo
        self.__codigo_curso = codigo_curso
        if isinstance(professor, Professor):
            self.__professor = professor
        self.__aulas = Aula(titulo, link, descricao_aula)
        # self.__aulas = []

    # def adicionar_aula(self, aula: Aula):
    #     if isinstance(aula, Aula):
    #         self.__aulas.append(aula)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco_atual(self):
        return self.__preco_atual

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tempo(self):
        return self.__tempo

    @property
    def codigo_curso(self):
        return self.__codigo_curso

    @property
    def professor(self):
        return self.__professor

    @property
    def aulas(self):
        return self.__aulas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @preco_atual.setter
    def preco_atual(self, preco_atual):
        self.__preco_atual = preco_atual

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    @codigo_curso.setter
    def codigo_curso(self, codigo_curso):
        self.__codigo_curso = codigo_curso
    
    @professor.setter
    def professor(self, professor):
        self.__professor = professor
    
    @aulas.setter
    def aulas(self, aulas):
        self.__aulas = aulas

    def nome_professor(self):
        return self.__professor.nome

    # def __repr__(self):
    #     tostring =  f"""
    #     Código do Curso: {self.__codigo_curso} 
    #     Nome: {self.__nome}  
    #     Nome do Professor: { self.__professor.nome}
    #     CPF do Professor: { self.__professor.cpf}
    #     Preço: {self.__preco_atual}
    #     Descrição do Curso: {self.__descricao}
    #     Tempo: {self.__tempo}

    #     Aulas: """        
    #     for aula in self.__aulas:
    #         tostring += f"""
    #         Título: {aula.titulo} 
    #         Descrição da Aula: {aula.descricao_aula}
    #         Link da Aula: {aula.link}
    #         Material: {aula.materiais[0].anexo} - {aula.materiais[0].descricao_material}"""
    #     return tostring

        