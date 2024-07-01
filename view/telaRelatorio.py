import PySimpleGUI as sg


class TelaRelatorio():

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- TELA DE RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('1 - Mostrar relatório inscricoes por curso', "RD1", key='1')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)


    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values
