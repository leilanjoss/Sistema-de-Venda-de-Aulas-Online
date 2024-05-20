from controladorInscricao import ControladorInscricao
from controladorCurso import ControladorCurso

class ControladorRelatorio:
    def __init__(self, controlador_inscricao, controlador_curso):
        self.__controlador_inscricao = controlador_inscricao
        self.__controlador_curso = controlador_curso
    
    def gerar_relatorio_total_receitas(self, professor):
        receita = 0
        for inscricao in self.__controlador_inscricao.inscricoes:
            if inscricao.curso.professor == professor:
                receita += inscricao.preco_pago
        return receita
        
    def gerar_relatorio_inscricoes_por_curso(self, curso):
        inscricoes_por_curso = [
            inscricao for inscricao in self.__controlador_inscricao.inscricoes if inscricao.curso == curso
        ]
        return len(inscricoes_por_curso)
