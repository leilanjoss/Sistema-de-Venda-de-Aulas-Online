class TelaAluno:
    def tela_opcoes(self):
        print("-------- ALUNOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_aluno(self):
        print("-------- DADOS ALUNO ----------")
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        cidade = input("Cidade: ")
        sigla_estado = input("Sigla do Estado: ")
        rua = input("Rua: ")
        numero = input("Número: ")
        cartao = input('Cartão: ')

        return {"nome": nome, 
                "email": email, 
                "telefone": telefone, 
                "cpf": cpf, 
                "cidade": cidade, 
                "sigla_estado": sigla_estado, 
                "rua": rua, 
                "numero": numero,
                "cartao": cartao}

    def mostrar_aluno(self, dados_aluno):
        print(">Nome do Aluno: ", dados_aluno["nome"])
        print(">E-mail do Aluno: ", dados_aluno["email"])
        print(">Telefone do Aluno: ", dados_aluno["telefone"])
        print(">CPF do Aluno: ", dados_aluno["cpf"])
        print(">Endereço do Aluno: ", dados_aluno["endereco"])
        print(">Cartão do Aluno: ", dados_aluno["cartao"])


    def selecionar_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        return cpf

    def mostrar_mensagem(self, msg: str):
        print(msg)