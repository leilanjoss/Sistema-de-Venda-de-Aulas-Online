import PySimpleGUI as sg
from controller.controladorRelatorio import ControladorRelatorio


class TelaRelatorio():
    # def tela_opcoes(self):
    #     print("-----TELA DE RELATÓRIO-----")
    #     print("Escolha sua opção")
    #     print("1 - Mostrar relatório total de receitas")
    #     print("2 - Mostrar relatório inscricoes por curso")
    #     print("0 - Retornar")
        
    #     opcao = int(input("Escolha uma opção: "))
    #     return opcao


    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.__controlador_relatorio = ControladorRelatorio()
        # self.__controlador_relatorio = controlador_relatorio

    def tela_opcoes(self):
        button, values = self.open()
        if values['1']:
            opcao = 1
        # if values['2']:
        #     opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- TELA DE RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            # [sg.Radio('1 - Mostrar relatório total de receitas', "RD1", key='1')],
            [sg.Radio('1 - Mostrar relatório inscricoes por curso', "RD1", key='1')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

    
    def pegar_cpf_professor(self):
        layout = [
            [sg.Text('CPF do Professor:'), sg.InputText(key='cpf_professor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('CPF do Professor', layout)

        event, values = window.read()
        window.close()
        return values['cpf_professor']

    def pegar_codigo_curso(self):
        layout = [
            [sg.Text('Código do Curso:'), sg.InputText(key='codigo_curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Código do Curso', layout)

        event, values = window.read()
        window.close()
        # return values['codigo_curso']
        try:
            codigo_curso = int(values['codigo_curso'])
        except ValueError:
            codigo_curso = None
        return codigo_curso


    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values
