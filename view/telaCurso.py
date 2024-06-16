from model.aula import Aula
# from model.material import Material
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

    def pegar_dados_curso(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- DADOS CURSO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Preço atual:', size=(15, 1)), sg.InputText('', key='preco_atual')],
            [sg.Text('Descrição do curso:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Text('Tempo:', size=(15, 1)), sg.InputText('', key='tempo')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
            [sg.Text('Professor:', size=(15, 1)), sg.InputText('', key='professor')],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text('Link:', size=(15, 1)), sg.InputText('', key='link')],
            [sg.Text('Descrição da Aula:', size=(15, 1)), sg.InputText('', key='descricao_aula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco_atual = values['preco_atual'] 
        tempo = values['tempo'] 
        descricao = values['descricao']
        codigo_curso = values['codigo_curso']
        professor = values['professor']
        titulo = values['titulo']
        link = values['link']
        descricao_aula = values['descricao_aula']

        self.__window.close()
        return {
            "nome": nome, 
            "preco_atual": preco_atual, 
            "tempo": tempo, 
            "codigo_curso": codigo_curso, 
            "descricao": descricao, 
            "professor": professor, 
            "titulo": titulo, 
            "link": link,
            "descricao_aula": descricao_aula
        }
    def mostrar_curso(self, dados_curso):
        dado_apresentacao = dados_curso["nome"] + '(' + dados_curso["codigo_curso"] + ')'

        # Criando a layout para o popup
        layout = [
            [sg.Text('Nome:'), sg.Text(str(dado_apresentacao), size=(40, 1))]
        ]

        # Usando sg.popup_scrolled para exibir os detalhes
        window = sg.Window('Detalhes do Curso', layout)
        event, values = window.read()
        window.close()

        # Fechando a janela
        self.__window.close()

    def selecionar_curso(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- SELECIONAR CURSO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do curso que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CÓDIGO:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona curso').Layout(layout)

        button, values = self.open()
        codigo_curso = values['codigo_curso']
        self.__window.close()
        return codigo_curso   

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
