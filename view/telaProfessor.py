class TelaProfessor():
    def tela_opcoes(self):
        print("-------- PROFESSOR ----------")
        print("Escolha a opção")
        print("1 - Incluir Professor")
        print("2 - Alterar Professor")
        print("3 - Listar Professores")
        print("4 - Excluir Professor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_professor(self):
        print("-------- DADOS PROFESSOR ----------")
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        cidade = input("Cidade: ")
        sigla_estado = input("Sigla do Estado: ")
        rua = input("Rua: ")
        numero = input("Número: ")

        return {"nome": nome, 
                "email": email, 
                "telefone": telefone, 
                "cpf": cpf, 
                "cidade": cidade, 
                "sigla_estado": sigla_estado, 
                "rua": rua, 
                "numero": numero}

    def mostrar_professor(self, dados_professor):
        print(">Nome do Professor: ", dados_professor["nome"])
        print(">E-mail do Professor: ", dados_professor["email"])
        print(">Telefone do Professor: ", dados_professor["telefone"])
        print(">CPF do Professor: ", dados_professor["cpf"])
        print(">Endereço do Professor: ", dados_professor["endereco"])

    def selecionar_professor(self):
        cpf = input("CPF do professor que deseja selecionar: ")
        return cpf

    def mostrar_mensagem(self, msg):
        print(msg)
