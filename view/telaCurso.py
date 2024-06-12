from model.aula import Aula
from model.material import Material
from model.professor import Professor
from model.curso import Curso
from controller.controladorProfessor import ControladorProfessor
import PySimpleGUI as sg


class TelaCurso:
    # def __init__(self):
    #     self.__controlador_professor = ControladorProfessor()
        
    # def tela_opcoes(self):
    #     print("-------- CURSO ----------")
    #     print("Escolha a opção")
    #     print("1 - Inserir Curso")
    #     print("2 - Alterar Curso")
    #     print("3 - Listar Cursos")
    #     print("4 - Excluir Curso")
    #     print("0 - Retornar")

    #     opcao = int(input("Escolha a opção: "))
    #     return opcao

    # def pegar_dados_curso(self):
    #     print("-------- DADOS DO CURSO ----------")
    #     curso = Curso()
    #     curso.nome = input("Nome do Curso: ")
    #     curso.preco_atual = float(input("Preço atual do Curso: "))
    #     curso.descricao = input("Descrição do Curso: ")
    #     curso.tempo = (input("Tempo do Curso em semanas: "))
    #     curso.codigo_curso = (input("Código do Curso: "))
    #     self.__controlador_professor.listar_professores()
    #     curso.professor = self.__controlador_professor.pegar_professor_por_cpf(input("Digite o cpf do Professor desejado: "))
    #     numero_de_aulas = int(input("Digite o número de aulas: "))
    #     for i in range(numero_de_aulas):
    #         print("Aula " + str((i+1)))
    #         aula = Aula()
    #         aula.titulo = input("Título da Aula: ")
    #         aula.descricao_aula = input("Descrição da Aula: " )
    #         aula.link = input("Link da Aula: ")
    #         material = Material()
    #         material.anexo = input("Link do Anexo do Material: ")
    #         material.descricao_material = input("Descrição do Material: ")
    #         aula.adicionar_material(material)
    #         curso.adicionar_aula(aula)
            
    #     return curso

    # def mostrar_cursos(self, cursos):
    #     for curso in cursos:
    #         print(curso)
    #         print("------------------------------")

    # def selecionar_curso(self):
    #     codigo_curso = input('Código do curso que você deseja selecionar: ')
    #     return codigo_curso

    # def mostrar_mensagem(self, msg):
    #     print(msg)
        
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- CURSO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('1 - Inserir Curso', "RD1", key='1')],
            [sg.Radio('2 - Alterar Curso', "RD1", key='2')],
            [sg.Radio('3 - Listar Cursos', "RD1", key='3')],
            [sg.Radio('4 - Excluir Curso', "RD1", key='4')],
            [sg.Radio('0 - Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

    def pegar_dados_aluno(self):
        ...    #Implementar e corrigir
        
    def mostrar_aluno(self, dados_aluno):
        ...    #Implementar e corrigir

    def selecionar_aluno(self):
        ...    #Implementar e corrigir     

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
