# class TelaProfessor():
#     def tela_opcoes(self):
        # print("-------- PROFESSOR ----------")
        # print("Escolha a opção")
        # print("1 - Incluir Professor")
        # print("2 - Alterar Professor")
        # print("3 - Listar Professores")
        # print("4 - Excluir Professor")
        # print("0 - Retornar")

    #     opcao = int(input("Escolha a opção: "))
    #     return opcao

    # def pegar_dados_professor(self):
    #     print("-------- DADOS PROFESSOR ----------")
    #     nome = input("Nome: ")
    #     email = input("E-mail: ")
    #     telefone = input("Telefone: ")
    #     cpf = input("CPF: ")
    #     cidade = input("Cidade: ")
    #     sigla_estado = input("Sigla do Estado: ")
    #     rua = input("Rua: ")
    #     numero = input("Número: ")

    #     return {"nome": nome, 
    #             "email": email, 
    #             "telefone": telefone, 
    #             "cpf": cpf, 
    #             "cidade": cidade, 
    #             "sigla_estado": sigla_estado, 
    #             "rua": rua, 
    #             "numero": numero}

    # def mostrar_professor(self, dados_professor):
    #     print(">Nome do Professor: ", dados_professor["nome"])
    #     print(">E-mail do Professor: ", dados_professor["email"])
    #     print(">Telefone do Professor: ", dados_professor["telefone"])
    #     print(">CPF do Professor: ", dados_professor["cpf"])
    #     print(">Endereço do Professor: ", dados_professor["endereco"])

    # def selecionar_professor(self):
    #     cpf = input("CPF do professor que deseja selecionar: ")
    #     return cpf

    # def mostrar_mensagem(self, msg):
    #     print(msg)
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
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
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
        sg.ChangeLookAndFeel('DarkTeal4')
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

        self.close()
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

    def mostrar_professor(self, dados_professor):
        string_todos_professores = ""
        for dado in dados_professor:
            string_todos_professores += "NOME DO PROFESSOR: " + dado["nome"] + '\n'
            string_todos_professores += "EMAIL DO PROFESSOR: " + dado["email"] + '\n'
            string_todos_professores += "TELEFONE DO PROFESSOR: " + str(dado["telefone"]) + '\n'
            string_todos_professores += "CPF DO PROFESSOR: " + str(dado["cpf"]) + '\n'
            string_todos_professores += "CIDADE DO PROFESSOR: " + dado["cidade"] + '\n'
            string_todos_professores += "SIGLA DO ESTADO DO PROFESSOR: " + dado["sigla_estado"] + '\n'
            string_todos_professores += "RUA DO PROFESSOR: " + dado["rua"] + '\n'
            string_todos_professores += "NÚMERO DA RUA DO PROFESSOR: " + str(dado["numero"]) + '\n\n'
        sg.popup(string_todos_professores)

    def selecionar_professor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR PROFESSOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do professor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona professor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values