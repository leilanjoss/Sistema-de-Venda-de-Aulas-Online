class TelaInscricao():
    def tela_opcoes(self):
        print("--------TELA DE INSCRIÇÃO--------")
        print("Escolha sua opção")
        print("1 - Inserir inscrição")
        print("2 - Excluir inscrição")
        print("3 - Atualizar inscrição")
        print("4 - Retornar")
        print("0 - Finalizar sistema")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostrar_inscricao(self, dados_inscricao):
        print("CURSO: ", dados_inscricao["curso"])
        print("ALUNO: ", dados_inscricao["aluno"])
        print("PREÇO PAGO: ", dados_inscricao["preco_pago"])
        print("DATA E HORA: ", dados_inscricao["data_hora"])
        print("\n")

    def mostra_mensagem(self, msg: str):
        print(msg)
