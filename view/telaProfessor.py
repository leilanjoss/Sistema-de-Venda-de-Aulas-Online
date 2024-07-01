
import PySimpleGUI as sg


class TelaProfessor:
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
            [sg.Text('-------- PROFESSORES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Professor', "RD1", key='1')],
            [sg.Radio('Alterar Professor', "RD1", key='2')],
            [sg.Radio('Listar Professores', "RD1", key='3')],
            [sg.Radio('Excluir Professor', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)
    
    def pegar_dados_professor(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- DADOS PROFESSOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Text('Sigla do Estado:', size=(15, 1)), sg.InputText('', key='sigla_estado')],
            [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        email = values['email']
        telefone = values['telefone']
        cpf = values['cpf']
        cidade = values['cidade']
        sigla_estado = values['sigla_estado']
        rua = values['rua']
        numero = values['numero']

        try:
            cpf = int(''.join(filter(str.isdigit, cpf)))
        except ValueError:
            cpf = None

        self.__window.close()

        return {
            "nome": nome, 
            "email": email, 
            "telefone": telefone, 
            "cpf": cpf, 
            "cidade": cidade, 
            "sigla_estado": sigla_estado, 
            "rua": rua, 
            "numero": numero
        }

    def mostrar_professor(self, professores):
        array_professores = []
        for professor in professores:
            row = [professor.nome, 
                professor.cpf, 
                professor.email, 
                professor.telefone, 
                professor.endereco.cidade,
                professor.endereco.sigla_estado, 
                professor.endereco.rua, 
                professor.endereco.numero 
                ]
            array_professores.append(row)

        toprow = ['Nome', 'CPF', 'E-mail', 'Telefone', 'Cidade', 'Estado', 'Rua', 'Número']
        tbl1 = sg.Table(values=array_professores,
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
        self.__window = sg.Window("Professores", layout, size=(715, 200), resizable=True)
        button, values = self.open()
        self.__window.close()


    def selecionar_professor(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- SELECIONAR PROFESSOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do professor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona professor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']

        try:
            cpf = int(''.join(filter(str.isdigit, cpf)))
        except ValueError:
            cpf = None

        self.__window.close()
        return cpf

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values