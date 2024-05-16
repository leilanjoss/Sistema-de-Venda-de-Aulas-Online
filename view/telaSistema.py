class TelaSistema:
    def tela_opcoes(self):
        print("-------- Sistema de Vendas de Aulas Online ---------")
        print("Escolha sua opcao")
        print("1 - Menu Professor")
        print("2 - Menu Aluno")
        print("0 - Finalizar sistema")

        opcao = int(input("Escolha a opcao:"))
        return opcao