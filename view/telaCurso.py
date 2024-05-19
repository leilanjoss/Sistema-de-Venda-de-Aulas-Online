class TelaCurso:
    def tela_opcoes(self):
        print("-------- CURSO ----------")
        print("Escolha a opção")
        print("1 - Inserir Curso")
        print("2 - Excluir Curso")
        print("3 - Alterar Curso")
        print("4 - Listar Cursos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_curso(self):
        print("-------- DADOS DO CURSO ----------")
        nome = input("Nome do curso: ")
        preco_atual = float(input("Preço atual do curso: "))
        descricao = input("Descrição do curso: ")
        tempo = int(input("Tempo do curso em semanas: "))
        codigo_curso = int(input("Código do curso: "))
        professor = input("Professor do curso: ")
        aulas = input("Aulas do curso: ")
        return {
            "nome": nome,
            "preco_atual": preco_atual,
            "descricao": descricao,
            "tempo": tempo,
            "codigo_curso": codigo_curso,
            "professor": professor,
            "aulas": aulas
        }

    def mostrar_curso(self, dados_curso):
        print("NOME DO CURSO: ", dados_curso["nome"])
        print("PREÇO ATUAL DO CURSO: ", dados_curso["preco_atual"])
        print("DESCRIÇÃO DO CURSO: ", dados_curso["descricao"])
        print("TEMPO DO CURSO: ", dados_curso["tempo"])
        print("CÓDIGO DO CURSO: ", dados_curso["codigo_curso"])
        print("PROFESSOR DO CURSO: ", dados_curso["professor"])
        print("AULAS CURSO: ", dados_curso["aulas"])
        print("\n")

    def selecionar_curso(self):
        codigo_curso = input('Código do curso que você deseja selecionar: ')
        return codigo_curso

    def mostrar_mensagem(self, msg):
        print(msg)
