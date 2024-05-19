class TelaSistema:
    def tela_opcoes(self):
        print("--- SISTEMA DE VENDAS DE AULAS ONLINE ---")
        print("Escolha sua opção")
        print("1 - Menu Professor")
        print("2 - Menu Aluno")
        print("3 - Menu Cursos")
        print("0 - Finalizar sistema")

        opcao = int(input("Escolha a opção: "))
        return opcao