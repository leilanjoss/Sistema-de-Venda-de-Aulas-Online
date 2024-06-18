import PySimpleGUI as sg


class TelaSistema:
    # def tela_opcoes(self):
    #     print("--- SISTEMA DE VENDAS DE AULAS ONLINE ---")
    #     print("Escolha sua opção")
    #     print("1 - Menu Professor")
    #     print("2 - Menu Aluno")
    #     print("3 - Menu Cursos")
    #     print("4 - Menu Relatórios")
    #     print("5 - Menu Inscrições")
    #     print("0 - Finalizar sistema")

    #     opcao = int(input("Escolha a opção: "))
    #     return opcao

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
        if values['5']:
            opcao = 5
        
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('--- SISTEMA DE VENDAS DE AULAS ONLINE ---', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('1 - Menu Professor', "RD1", key='1')],
            [sg.Radio('2 - Menu Aluno', "RD1", key='2')],
            [sg.Radio('3 - Menu Cursos', "RD1", key='3')],
            [sg.Radio('4 - Menu Relatórios', "RD1", key='4')],
            [sg.Radio('5 - Menu Inscrições', "RD1", key='5')],
            [sg.Radio('0 - Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
