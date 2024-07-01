from controller.controladorInscricao import ControladorInscricao
from DAOs.inscricao_dao import InscricaoDAO
from view.telaInscricao import TelaInscricao

class ControladorRelatorio:
    def __init__(self):
        self.__controlador_inscricao = ControladorInscricao(self) 
        self.__inscricao_DAO = InscricaoDAO()
        self.__tela_inscricao = TelaInscricao()

    def gerar_relatorio_inscricoes_por_curso(self):
        codigo_curso = self.__tela_inscricao.pegar_codigo_curso()
        self.__controlador_inscricao.listar_inscricoes()

        if codigo_curso is None:
            return

        inscricoes = self.__inscricao_DAO.get_all()
        
        inscricoes_por_curso = [inscricao for inscricao in inscricoes if int(inscricao.curso.codigo_curso) == codigo_curso]
        
        total_inscricoes = len(inscricoes_por_curso)
        self.__tela_inscricao.mostrar_mensagem(f"Total de inscrições para o curso {codigo_curso}: {total_inscricoes}")

    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()
    
    def abrir_tela(self):
        from view.telaRelatorio import TelaRelatorio
        lista_opcoes = {
            1: self.gerar_relatorio_inscricoes_por_curso,
            0: self.retornar
        }
        continua = True
        while continua:
            opcao_escolhida = TelaRelatorio().tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                break
                
    
