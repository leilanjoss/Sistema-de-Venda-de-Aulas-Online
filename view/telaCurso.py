from model.aula import Aula
from model.material import Material
from model.professor import Professor
from model.curso import Curso
from controller.controladorProfessor import ControladorProfessor

class TelaCurso:
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()

    def tela_opcoes(self):
        print("-------- CURSO ----------")
        print("Escolha a opção")
        print("1 - Inserir Curso")
        print("2 - Alterar Curso")
        print("3 - Listar Cursos")
        print("4 - Excluir Curso")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_curso(self):
        print("-------- DADOS DO CURSO ----------")
        curso = Curso()
        curso.nome = input("Nome do curso: ")
        curso.preco_atual = float(input("Preço atual do curso: "))
        curso.descricao = input("Descrição do curso: ")
        curso.tempo = (input("Tempo do curso em semanas: "))
        curso.codigo_curso = (input("Código do curso: "))
        self.__controlador_professor.listar_professores();
        curso.professor = self.__controlador_professor.pegar_professor_por_cpf(input("Digite o cpf do professor: "))
        numero_de_aulas = int(input("Digite o número de aulas: "))
        for i in range(numero_de_aulas):
            print("Aula " + str((i+1)))
            aula = Aula()
            aula.titulo = input("Tĩtulo: ")
            aula.descricao_aula = input("Descrição: " )
            aula.link = input("Link: ")
            material = Material()
            material.anexo = input("Link do anexo: ")
            material.descricao_material = input("Descrição: ")
            aula.adicionar_material(material)
            curso.adicionar_aula(aula)
            
        return curso

    def mostrar_curso(self, cursos):
        for curso in cursos:
            print("NOME DO CURSO: ", curso["nome"])
            print("PREÇO ATUAL DO CURSO: ", curso["preco_atual"])
            print("DESCRIÇÃO DO CURSO: ", curso["descricao"])
            print("TEMPO DO CURSO: ", curso["tempo"])
            print("CÓDIGO DO CURSO: ", curso["codigo_curso"])
            print("PROFESSOR DO CURSO: ", curso["professor"])
            print("AULAS CURSO: ", curso["aulas"])
            print("\n")


    def selecionar_curso(self):
        codigo_curso = input('Código do curso que você deseja selecionar: ')
        return codigo_curso

    def mostrar_mensagem(self, msg):
        print(msg)