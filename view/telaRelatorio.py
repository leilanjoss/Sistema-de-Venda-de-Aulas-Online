import PySimpleGUI as sg

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
        def __init__(self):
            self.__window = None
            self.init_opcoes()

    def tela_opcoes(self):
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- TELA DE RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('1 - Mostrar relatório total de receitas', "RD1", key='1')],
            [sg.Radio('2 - Mostrar relatório inscricoes por curso', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)



