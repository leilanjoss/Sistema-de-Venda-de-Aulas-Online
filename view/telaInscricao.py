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
        # elif values['5']:
        #     opcao = 5
        # elif values['6']:
        #     opcao = 6
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
        [sg.Radio('2 - Atualizar inscrição', "RD1", key='2')],
        [sg.Radio('3 - Listar inscrições', "RD1", key='3')],
        [sg.Radio('4 - Excluir inscrições', "RD1", key='4')],
        # [sg.Radio('5 - Relatório Total de Receitas', "RD1", key='5')],
        # [sg.Radio('6 - Relatório De Inscrições por Curso', "RD1", key='6')],
        [sg.Radio('0 - Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Sistema de aulas').Layout(layout)

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.close()

    def mostrar_inscricao(self, inscricoes):
        # string_inscricoes = ""
        # string_inscricoes += "NOME DO CURSO" + dados_inscricao['nome_curso'] + '\n'
        # string_inscricoes += "NOME DO ALUNO" + dados_inscricao['nome_aluno'] + '\n'
        # string_inscricoes += "PREÇO PAGO" + dados_inscricao['preco_pago'] + '\n'

        # sg.Popup('------LISTA DE INSCRIÇÕES------', )
        
        array_inscricoes = []
        for inscricao in inscricoes:
            row = [inscricao.aluno.cpf, inscricao.curso.codigo_curso, inscricao.data_hora, inscricao.id] 
            array_inscricoes.append(row)
        toprow = ['Curso', 'Aluno', 'Data e Hora', 'ID']
        tbl1 = sg.Table(values=array_inscricoes,
                        headings=toprow,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='left', key='-TABLE-',
                        selected_row_colors='white on seagreen',
                        enable_events=False,
                        expand_x=True,
                        expand_y=True,
                        enable_click_events=False)
        layout = [[tbl1]]
        self.__window = sg.Window("Inscrições", layout, size=(715, 200), resizable=True)
        button, values = self.open()
        self.__window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def pegar_dados_inscricao(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- DADOS INSCRIÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('CPF do Aluno:', size=(15, 1)), sg.InputText('', key='cpf_aluno')],
            [sg.Text('Código do Curso:', size=(15, 1)), sg.InputText('', key='cod_curso')],
            [sg.Text('Data/hora:', size=(15, 1)), sg.InputText('', key='data_hora')],
            [sg.Text('ID de inscrição:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de aulas').Layout(layout)

        button, values = self.open()
        cpf_aluno = values['cpf_aluno']
        cod_curso = values['cod_curso']
        data_hora = values['data_hora']
        id_inscricao = values['id']

        self.__window.close()
        return {
            "cpf_aluno": cpf_aluno,
            "cod_curso": cod_curso,
            "data_hora": data_hora,
            "id_inscricao": id_inscricao,
        }
    
    # RELATORIO
    # def pegar_cpf_professor(self):
    #     layout = [
    #         [sg.Text('CPF do Professor:'), sg.InputText(key='cpf_professor')],
    #         [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    #     ]
    #     window = sg.Window('CPF do Professor', layout)

    #     event, values = window.read()
    #     window.close()
    #     return values['cpf_professor']

    # def pegar_codigo_curso(self):
    #     layout = [
    #         [sg.Text('Código do Curso:'), sg.InputText(key='codigo_curso')],
    #         [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    #     ]
    #     window = sg.Window('Código do Curso', layout)

        event, values = window.read()
        window.close()
        return values['codigo_curso']
