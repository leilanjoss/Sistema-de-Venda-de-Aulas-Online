from controller.controladorInscricao import ControladorInscricao
from view.telaRelatorio import TelaRelatorio

class ControladorRelatorio:
    def __init__(self):
        self.__controlador_inscricao = ControladorInscricao(self)  # Inicialize o objeto ControladorInscricao
        self.__tela_relatorio = TelaRelatorio()  # Inicialize o objeto TelaRelatorio

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
        }
        continua = True
        while continua:
            opcao_escolhida = self.__tela_relatorio.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Escolha novamente.")
