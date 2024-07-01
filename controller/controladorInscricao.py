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
        
        aluno = self.__controlador_aluno.pegar_aluno_por_cpf(int(dados_inscricao['cpf_aluno']))
        curso = self.__controlador_curso.pegar_curso_por_codigo(dados_inscricao['cod_curso'])
        
        if isinstance(aluno, Aluno) and isinstance(curso, Curso):
            nova_inscricao = Inscricao(curso, aluno, int(dados_inscricao['data_hora']), int(dados_inscricao['id_inscricao']))
            self.__inscricao_DAO.add(nova_inscricao)
            self.__tela_inscricao.mostrar_mensagem("Inscrição inserida")
        else:
            self.__tela_inscricao.mostrar_mensagem("Aluno ou curso não encontrado")
            
    

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
        id = self.__tela_inscricao.selecionar_inscricao()
        inscricao = self.pegar_inscricao_por_id(id)
        if inscricao is not None:
            self.__inscricao_DAO.remove(inscricao.id)
            self.__tela_inscricao.mostrar_mensagem("Inscrição excluída.")
            self.listar_inscricoes()
        else:
            self.__tela_inscricao.mostrar_mensagem("Inscrição não existente.")
    
    def atualizar_inscricao(self):
        self.listar_inscricoes()
        id = self.__tela_inscricao.selecionar_inscricao()
        inscricao = self.pegar_inscricao_por_id(id)
        print('pegar inscricao por id:')
        
        print(inscricao)
        for inscricao in self.__inscricao_DAO.get_all():
            if inscricao.id == id:
                novos_dados_inscricao = self.__tela_inscricao.pegar_dados_inscricao()
                curso_alterado = self.__controlador_curso.pegar_curso_por_codigo(novos_dados_inscricao['cod_curso'])
                aluno_alterado = self.__controlador_aluno.pegar_aluno_por_cpf(int(novos_dados_inscricao['cpf_aluno']))
                
        print('Esse é o curso:')
        print(curso_alterado)
        
        print('Esse é aluno:')
        print(aluno_alterado)
        
        if curso_alterado is not None and aluno_alterado is not None:
            inscricao.curso = curso_alterado
            inscricao.aluno = aluno_alterado
            inscricao.data_hora = novos_dados_inscricao['data_hora']
            inscricao.id = novos_dados_inscricao['id_inscricao']

            self.__tela_inscricao.mostrar_mensagem("Inscrição atualizada com sucesso!")
        else:
            self.__tela_inscricao.mostrar_mensagem("Curso ou aluno não encontrado")

    
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
            self.__tela_inscricao.mostrar_mensagem("Nenhuma inscrição cadastrada.")
        else:
            self.__tela_inscricao.mostrar_inscricao(self.__inscricao_DAO.get_all())
            
    def pegar_inscricao_por_id(self, id: str):
        for inscricao in self.__inscricao_DAO.get_all():
            if inscricao.id == id:
                return inscricao
        return None
