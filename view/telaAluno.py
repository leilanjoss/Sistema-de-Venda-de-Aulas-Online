import PySimpleGUI as sg


class TelaAluno:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        # print("-------- ALUNOS ----------")
        # print("Escolha a opcao")
        # print("1 - Incluir Aluno")
        # print("2 - Alterar Aluno")
        # print("3 - Listar Alunos")
        # print("4 - Excluir Aluno")
        # print("0 - Retornar")

        # opcao = int(input("Escolha a opção: "))
        # return opcao

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
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- ALUNOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Aluno', "RD1", key='1')],
            [sg.Radio('Alterar Aluno', "RD1", key='2')],
            [sg.Radio('Listar Alunos', "RD1", key='3')],
            [sg.Radio('Excluir Aluno', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)
    
    def pegar_dados_aluno(self):
        # print("-------- DADOS ALUNO ----------")
        # nome = input("Nome: ")
        # email = input("E-mail: ")
        # telefone = input("Telefone: ")
        # cpf = input("CPF: ")
        # cidade = input("Cidade: ")
        # sigla_estado = input("Sigla do Estado: ")
        # rua = input("Rua: ")
        # numero = input("Número: ")
        # cartao = input('Cartão: ')

        # return {"nome": nome, 
        #         "email": email, 
        #         "telefone": telefone, 
        #         "cpf": cpf, 
        #         "cidade": cidade, 
        #         "sigla_estado": sigla_estado, 
        #         "rua": rua, 
        #         "numero": numero,
        #         "cartao": cartao}
            sg.ChangeLookAndFeel('DarkTeal4')
            layout = [
                [sg.Text('-------- DADOS ALUNO ----------', font=("Helvica", 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                [sg.Text('E-mail:', size=(15, 1)), sg.InputText('', key='email')],
                [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
                [sg.Text('Sigla do Estado:', size=(15, 1)), sg.InputText('', key='sigla_estado')],
                [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
                [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                [sg.Text('Cartão:', size=(15, 1)), sg.InputText('', key='cartao')],
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
            cartao = values['cartao']

            self.close()
            return {
                "nome": nome, 
                "email": email, 
                "telefone": telefone, 
                "cpf": cpf, 
                "cidade": cidade, 
                "sigla_estado": sigla_estado, 
                "rua": rua, 
                "numero": numero,
                "cartao": cartao
            }

    def mostrar_aluno(self, dados_aluno):
        # print(">Nome do Aluno: ", dados_aluno["nome"])
        # print(">E-mail do Aluno: ", dados_aluno["email"])
        # print(">Telefone do Aluno: ", dados_aluno["telefone"])
        # print(">CPF do Aluno: ", dados_aluno["cpf"])
        # print(">Endereço do Aluno: ", dados_aluno["endereco"])
        # print(">Cartão do Aluno: ", dados_aluno["cartao"])
        string_todos_alunos = ""
        for dado in dados_aluno:
            string_todos_alunos += "NOME DO ALUNO: " + dado["nome"] + '\n'
            string_todos_alunos += "EMAIL DO ALUNO: " + dado["email"] + '\n'
            string_todos_alunos += "TELEFONE DO ALUNO: " + str(dado["telefone"]) + '\n'
            string_todos_alunos += "CPF DO ALUNO: " + str(dado["cpf"]) + '\n'
            string_todos_alunos += "CIDADE DO ALUNO: " + dado["cidade"] + '\n'
            string_todos_alunos += "SIGLA DO ESTADO DO ALUNO: " + dado["sigla_estado"] + '\n'
            string_todos_alunos += "RUA DO ALUNO: " + dado["rua"] + '\n'
            string_todos_alunos += "NÚMERO DA RUAN DO ALUNO: " + str(dado["numero"]) + '\n'
            string_todos_alunos += "DETALHES DO CARTÃO DO ALUNO: " + dado["cartao"] + '\n\n'


    def selecionar_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do aluno que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona aluno').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf


    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
