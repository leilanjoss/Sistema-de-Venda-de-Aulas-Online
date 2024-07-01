from model.inscricao import Inscricao
from controller.controladorCurso import ControladorCurso
from view.telaInscricao import TelaInscricao
from controller.controladorAluno import ControladorAluno
from model.aluno import Aluno
from model.curso import Curso
from DAOs.inscricao_dao import InscricaoDAO

class ControladorInscricao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_curso = ControladorCurso()
        self.__tela_inscricao = TelaInscricao()
        self.__controlador_aluno = ControladorAluno()
        self.__inscricao_DAO = InscricaoDAO()

    def inserir_inscricao(self):
        self.__controlador_aluno.listar_alunos()
        self.__controlador_curso.listar_cursos()
        dados_inscricao = self.__tela_inscricao.pegar_dados_inscricao()
        
        print(dados_inscricao)
        print(dados_inscricao['cpf_aluno']) # Ambos deram certo
        
        aluno = self.__controlador_aluno.pegar_aluno_por_cpf(dados_inscricao['cpf_aluno'])
        curso = self.__controlador_curso.pegar_curso_por_codigo(dados_inscricao['cod_curso'])
        
        if isinstance(aluno, Aluno) and isinstance(curso, Curso):
            nova_inscricao = Inscricao(curso, aluno, int(dados_inscricao['data_hora']), int(dados_inscricao['id_inscricao']))
            print(nova_inscricao)
            self.__inscricao_DAO.add(nova_inscricao)
            self.__tela_inscricao.mostrar_mensagem("Aluno inserido")
        else:
            self.__tela_inscricao.mostrar_mensagem("Aluno ou curso não encontrado")
            
        print(self.__inscricao_DAO.get_all())


    def excluir_inscricao(self):
        # codigo_curso = input("Digite o código do curso: ")
        # inscricao_a_excluir = None
        # for inscricao in self.__inscricoes:
        #     if inscricao.curso.codigo_curso == codigo_curso:
        #         inscricao_a_excluir = inscricao
        #         break
        # if inscricao_a_excluir:
        #     self.__inscricoes.remove(inscricao_a_excluir)
        #     self.__tela_inscricao.mostrar_mensagem("Inscrição excluída com sucesso!")
        # else:
        #     self.__tela_inscricao.mostrar_mensagem("Inscrição não encontrada!")
        self.listar_inscricoes()
        cpf = self.__tela_aluno.selecionar_aluno()
        aluno = self.pegar_aluno_por_cpf(cpf)
        if aluno is not None:
            self.__aluno_DAO.remove(aluno.cpf)
            self.__tela_aluno.mostrar_mensagem("Aluno excluído.")
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_mensagem("Aluno não existente.")
    
    def atualizar_inscricao(self):
        codigo_curso = input("Digite o código do curso: ")
        for inscricao in self.__inscricoes:
            if inscricao.curso.codigo_curso == codigo_curso:
                cpf_aluno = input("Digite o novo CPF do aluno: ")
                preco_pago = float(input("Digite o novo preço pago: "))
                data_hora = input("Digite a nova data e hora: ")
                inscricao.aluno = cpf_aluno
                inscricao.preco_pago = preco_pago
                inscricao.data_hora = data_hora
                self.__tela_inscricao.mostrar_mensagem("Inscrição atualizada com sucesso!")
                return
        self.__tela_inscricao.mostrar_mensagem("Inscrição não encontrada!")
    
    # RELATORIO
    # def gerar_relatorio_total_receitas(self):
    #     cpf_professor = self.__tela_inscricao.pegar_cpf_professor()
    #     receita_total = 0
    #     for inscricao in self.__inscricao_DAO.get_all():
    #         if inscricao.curso.professor.cpf == cpf_professor:
    #             receita_total += inscricao.curso.preco
    #     self.__tela_inscricao.mostrar_mensagem(f"Total de receitas do professor {cpf_professor}: R${receita_total:.2f}")

    # def gerar_relatorio_inscricoes_por_curso(self):
    #     curso_codigo = self.__tela_inscricao.pegar_codigo_curso()  # Obtemos o código do curso da tela de inscrições
    #     inscricoes_por_curso = [inscricao for inscricao in self.__inscricao_DAO.get_all() if inscricao.curso.codigo_curso == curso_codigo]
    #     total_inscricoes = len(inscricoes_por_curso)
    #     self.__tela_inscricao.mostrar_mensagem(f"Total de inscrições para o curso {curso_codigo}: {total_inscricoes}")

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def finalizar_sistema(self):
        exit()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_inscricao,
            2: self.atualizar_inscricao,
            3: self.listar_inscricoes,
            4: self.excluir_inscricao,
            # 5: self.gerar_relatorio_total_receitas,
            # 6: self.gerar_relatorio_inscricoes_por_curso,
            0: self.retornar
        }
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_inscricao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Escolha novamente.")

    def listar_inscricoes(self):
        print(self.__inscricao_DAO.get_all())
        if not self.__inscricao_DAO:
            self.__tela_inscricao.mostrar_mensagem("Nenhum aluno cadastrado.")
        else:
            self.__tela_inscricao.mostrar_inscricao(self.__inscricao_DAO.get_all())
            
