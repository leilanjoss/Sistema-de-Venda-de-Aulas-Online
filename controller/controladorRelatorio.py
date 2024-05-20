from controller.controladorInscricao import ControladorInscricao
from view.telaRelatorio import TelaRelatorio

class ControladorRelatorio:
    def __init__(self):
        self.__controlador_inscricao = ControladorInscricao
        self.__tela_relatorio = TelaRelatorio
    
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

    def abrir_tela(self):
        lista_opcoes = {
            1: self.gerar_relatorio_total_receitas,
            2: self.gerar_relatorio_inscricoes_por_curso,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_relatorio.tela_opcoes()]()
