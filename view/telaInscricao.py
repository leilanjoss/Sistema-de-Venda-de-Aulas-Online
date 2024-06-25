# class TelaInscricao():
#     def tela_opcoes(self):
#         print("--------TELA DE INSCRIÇÃO--------")
#         print("Escolha sua opção")
#         print("1 - Inserir inscrição")
#         print("2 - Excluir inscrição")
#         print("3 - Atualizar inscrição")
#         print("4 - Retornar")
#         print("0 - Finalizar sistema")

#         opcao = int(input("Escolha uma opção: "))
#         return opcao

#     def mostrar_inscricao(self, dados_inscricao):
#         print("CURSO: ", dados_inscricao["curso"])
#         print("ALUNO: ", dados_inscricao["aluno"])
#         print("PREÇO PAGO: ", dados_inscricao["preco_pago"])
#         print("DATA E HORA: ", dados_inscricao["data_hora"])
#         print("\n")

#     def mostra_mensagem(self, msg: str):
#         print(msg)
import PySimpleGUI as sg


class TelaInscricao():
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
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.__window.close()
        return opcao
    
    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
        [sg.Text('--------TELA DE INSCRIÇÃO--------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('1 - Inserir inscrição', "RD1", key='1')],
        [sg.Radio('2 - Excluir inscrição', "RD1", key='2')],
        [sg.Radio('3 - Atualizar inscrição', "RD1", key='3')],
        [sg.Radio('4 - Retornar', "RD1", key='4')],
        [sg.Radio('0 - Finalizar sistema', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de aulas').Layout(layout)


        
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def mostrar_inscricao(self, dados_inscricao):
        string_inscricoes = ""
        string_inscricoes += "NOME DO CURSO" + dados_inscricao['nome_curso'] + '\n'
        string_inscricoes += "NOME DO ALUNO" + dados_inscricao['nome_aluno'] + '\n'
        string_inscricoes += "PREÇO PAGO" + dados_inscricao['preco_pago'] + '\n'

        sg.Popup('------LISTA DE INSCRIÇÕES------', )
        
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def pegar_dados_inscricao(self, lista_cursos, lista_alunos):
        sg.ChangeLookAndFeel('LightGreen2')

        layout = [
            [sg.Text('-------- DADOS INSCRIÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Aluno:', size=(15, 1)), sg.combo('', key='aluno')],
            [sg.Text('Curso:', size=(15, 1)), sg.InputText('', key='curso')],
            [sg.Text('Data/hora:', size=(15, 1)), sg.InputText('', key='data_hora')],
            [sg.Text('ID de inscrição:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de aulas').Layout(layout)

        button, values = self.open()
        aluno = values['aluno']
        curso = values['curso']
        data_hora = values['data_hora']
        id_inscricao = values['id']

        self.__window.close()
        return {
            "aluno": aluno,
            "curso": curso,
            "data_hora": data_hora,
            "id_inscricao": id_inscricao,
        }

        