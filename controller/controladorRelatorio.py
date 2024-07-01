from controller.controladorInscricao import ControladorInscricao
# from view.telaRelatorio import TelaRelatorio
from DAOs.inscricao_dao import InscricaoDAO
from view.telaInscricao import TelaInscricao

class ControladorRelatorio:
    def __init__(self):
        self.__controlador_inscricao = ControladorInscricao(self) 
        # self.__tela_relatorio = TelaRelatorio() 
        self.__inscricao_DAO = InscricaoDAO()
        self.__tela_inscricao = TelaInscricao()


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
    def gerar_relatorio_total_receitas(self):
        cpf_professor = self.__tela_inscricao.pegar_cpf_professor()
        receita_total = 0

        # Verifica se o CPF foi fornecido
        if not cpf_professor:
            self.__tela_inscricao.mostrar_mensagem("CPF do professor não fornecido.")
            return

        # Obtém todas as inscrições
        inscricoes = self.__inscricao_DAO.get_all()

        # Verifica se há inscrições
        if not inscricoes:
            self.__tela_inscricao.mostrar_mensagem("Nenhuma inscrição encontrada.")
            return

        for inscricao in inscricoes:
            curso = inscricao.curso
            if curso and curso.professor and curso.professor.cpf == cpf_professor:
                preco_atual = curso.preco_atual
                if preco_atual is not None:
                    receita_total += preco_atual
                    # Debug: imprime o preço atual e o CPF do professor
                    print(f"Professor CPF: {curso.professor.cpf} - Preço Atual: {preco_atual}")

        # Exibe a mensagem com o total de receitas
        self.__tela_inscricao.mostrar_mensagem(f"Total de receitas do professor {cpf_professor}: R${receita_total:.2f}")

    def gerar_relatorio_inscricoes_por_curso(self):
        curso_codigo = self.__tela_inscricao.pegar_codigo_curso()
        inscricoes_por_curso = [inscricao for inscricao in self.__inscricao_DAO.get_all() if inscricao.curso.codigo_curso == curso_codigo]
        total_inscricoes = len(inscricoes_por_curso)
        self.__tela_inscricao.mostrar_mensagem(f"Total de inscrições para o curso {curso_codigo}: {total_inscricoes}")


    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()
    
    def abrir_tela(self):
        from view.telaRelatorio import TelaRelatorio
        lista_opcoes = {
            1: self.gerar_relatorio_total_receitas,
            2: self.gerar_relatorio_inscricoes_por_curso,
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
            # lista_opcoes[self.__tela_relatorio.tela_opcoes()]()


            # opcao_escolhida = self.__tela_relatorio.tela_opcoes()
            # funcao_escolhida = lista_opcoes[opcao_escolhida]
            # if funcao_escolhida:
            #     if opcao_escolhida == 1:
            #         nome_professor = input("Digite o cpf do professor: ")
            #         funcao_escolhida(nome_professor)
            #     elif opcao_escolhida == 2:
            #         codigo_curso = input("Digite o código do curso: ")
            #         funcao_escolhida(codigo_curso)
            #     elif opcao_escolhida == 0:
            #         funcao_escolhida()
            # else:
            #     print("Opção inválida. Escolha novamente.")
                
    
