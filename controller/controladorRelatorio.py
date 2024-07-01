from controller.controladorInscricao import ControladorInscricao
# from view.telaRelatorio import TelaRelatorio
from DAOs.inscricao_dao import InscricaoDAO
from view.telaInscricao import TelaInscricao
# from view.telaRelatorio import TelaRelatorio

class ControladorRelatorio:
    def __init__(self):
        self.__controlador_inscricao = ControladorInscricao(self) 
        # self.__tela_relatorio = TelaRelatorio() 
        self.__inscricao_DAO = InscricaoDAO()
        self.__tela_inscricao = TelaInscricao()
        # self.__tela_relatorio = TelaRelatorio()


    # def gerar_relatorio_total_receitas(self, cpf_professor):
    #     # receita = 0
    #     # for inscricao in self.__controlador_inscricao.inscricoes:
    #     #     if inscricao.curso.professor.cpf == cpf_professor:
    #     #         receita += inscricao.preco_pago
    #     # print(f'O total de receitas do professor com o CPF: {cpf_professor} tem o total de receitas de {receita} reais')
    #     receita = 0
    #     for inscricao in self.__inscricao_DAO.get_all():
    #         if inscricao.curso.professor.cpf == cpf_professor:
    #             receita += inscricao.preco_pago
    #     # print(f'O total de receitas do professor com o CPF: {cpf_professor} tem o total de receitas de {receita} reais')
    #     return receita

    # # def gerar_relatorio_inscricoes_por_curso(self, curso_codigo):
    # #     inscricoes_por_curso = [
    # #         inscricao for inscricao in self.__inscricao_DAO.get_all() if inscricao.curso.codigo_curso == curso_codigo
    # #     ]
    # #     print (f'O curso com o código:{curso_codigo} possui {len(inscricoes_por_curso)} inscrições')
    # def gerar_relatorio_inscricoes_por_curso(self, curso_codigo):
    #     inscricoes_por_curso = [
    #         inscricao for inscricao in self.__inscricao_DAO.get_all() if inscricao.curso.codigo_curso == curso_codigo
    #     ]
    #     return len(inscricoes_por_curso)
        
    # def gerar_relatorio_total_receitas(self):
    #     cpf_professor = self.__tela_inscricao.pegar_cpf_professor()
    #     receita_total = 0
    #     for inscricao in self.__inscricao_DAO.get_all():
    #         print('2222inscricao.curso.preco_atual', inscricao.curso.preco_atual)
    #         print('111inscricao.curso.professor.cpf', inscricao.curso.professor.cpf)
    #         if inscricao.curso.professor.cpf == cpf_professor:
    #             receita_total += inscricao.curso.preco_atual
    #             print('333inscricao.curso.preco_atual', inscricao.curso.preco_atual)
    #     self.__tela_inscricao.mostrar_mensagem(f"Total de receitas do professor {cpf_professor}: R${receita_total:.2f}")
  
    # def gerar_relatorio_inscricoes_por_curso(self):
    #     curso_codigo = self.__tela_inscricao.pegar_codigo_curso()
    #     inscricoes_por_curso = [inscricao for inscricao in self.__inscricao_DAO.get_all() if inscricao.curso.codigo_curso == curso_codigo]
    #     total_inscricoes = len(inscricoes_por_curso)
    #     self.__tela_inscricao.mostrar_mensagem(f"Total de inscrições para o curso {curso_codigo}: {total_inscricoes}")

    def gerar_relatorio_inscricoes_por_curso(self):
        codigo_curso = self.__tela_inscricao.pegar_codigo_curso()
        self.__controlador_inscricao.listar_inscricoes()

        if codigo_curso is None:
            self.__tela_inscricao.mostrar_mensagem("Código do curso inválido ou não informado.")
            return

        inscricoes = self.__inscricao_DAO.get_all()
        print(f"Inscrições retornadas do DAO: {[f'Curso: {inscricao.curso.codigo_curso}' for inscricao in inscricoes]}")  # Debug
        
        # Certifique-se de que estamos comparando o mesmo tipo
        inscricoes_por_curso = [inscricao for inscricao in inscricoes if int(inscricao.curso.codigo_curso) == codigo_curso]
        print(f"Inscrições para o curso {codigo_curso}: {[f'Curso: {inscricao.curso.codigo_curso}' for inscricao in inscricoes_por_curso]}")  # Debug
        
        # Contar o total de inscrições para o curso específico
        total_inscricoes = len(inscricoes_por_curso)
        self.__tela_inscricao.mostrar_mensagem(f"Total de inscrições para o curso {codigo_curso}: {total_inscricoes}")

    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()
    
    def abrir_tela(self):
        from view.telaRelatorio import TelaRelatorio
        lista_opcoes = {
            # 1: self.gerar_relatorio_total_receitas,
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
                
    
