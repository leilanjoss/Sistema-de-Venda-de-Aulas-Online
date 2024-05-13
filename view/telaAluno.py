class TelaAluno():
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
        #senha
        return {"nome": nome, "email": email, "telefone": telefone, "cpf": cpf, "cidade": cidade, "sigla_estado": sigla_estado, "rua": rua, "numero": numero}

    def mostrar_aluno(self, dados_aluno):
        print("NOME DO ALUNO: ", dados_aluno["nome"])
        print("E-MAIL DO ALUNO: ", dados_aluno["email"])
        print("FONE DO ALUNO: ", dados_aluno["telefone"])
        print("CPF DO ALUNO: ", dados_aluno["cpf"])
        print("CIDADE DO ALUNO: ", dados_aluno["cidade"])
        print("SIGLA DO ESTADO DO ALUNO: ", dados_aluno["sigla_estado"])
        print("RUA DO ALUNO: ", dados_aluno["rua"])
        print("NÚMERO DO ALUNO: ", dados_aluno["numero"])
        print("\n")
        #senha

    def selecionar_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        return cpf

    def mostrar_mensagem(self, msg):
        print(msg)