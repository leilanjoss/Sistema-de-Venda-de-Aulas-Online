from model.aula import Aula
# from model.material import Material
from model.professor import Professor
from model.curso import Curso
from controller.controladorProfessor import ControladorProfessor
import PySimpleGUI as sg
from DAOs.professor_dao import ProfessorDAO
# from controller.controladorCurso import ControladorCurso


class TelaCurso:
        
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.__controlador_professor = ControladorProfessor()
        self.__professor_DAO = ProfessorDAO()

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
        self.__window.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- CURSO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('1 - Inserir Curso', "RD1", key='1')],
            [sg.Radio('2 - Alterar Curso', "RD1", key='2')],
            [sg.Radio('3 - Listar Cursos', "RD1", key='3')],
            [sg.Radio('4 - Excluir Curso', "RD1", key='4')],
            [sg.Radio('0 - Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

    # def pegar_dados_curso(self):
    #     # NEW
    #     sg.ChangeLookAndFeel('LightGreen2')

    #     lista_professores = [professor.cpf for professor in self.__professor_DAO.get_all()]

    #     layout = [
    #         [sg.Text('-------- DADOS CURSO ----------', font=("Helvica", 25))],
    #         [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
    #         [sg.Text('Preço atual:', size=(15, 1)), sg.InputText('', key='preco_atual')],
    #         [sg.Text('Descrição do curso:', size=(15, 1)), sg.InputText('', key='descricao')],
    #         [sg.Text('Tempo:', size=(15, 1)), sg.InputText('', key='tempo')],
    #         [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
    #         [sg.Text('Professor:', size=(15, 1)), sg.Combo(lista_professores, key='professor')],
    #         [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
    #         [sg.Text('Descrição da Aula:', size=(15, 1)), sg.InputText('', key='descricao_aula')],
    #         [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    #         ]
        
    #     self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)

    #     button, values = self.open()

    #     if button == 'Confirmar':
    #         nome = values['nome']
    #         preco_atual = values['preco_atual']
    #         tempo = values['tempo']
    #         descricao = values['descricao']
    #         codigo_curso = values['codigo_curso']
    #         professor_selecionado = values['professor']

    #         titulo = values['titulo']
    #         descricao_aula = values['descricao_aula']

    #         for professor in self.__professor_DAO.get_all():
    #             if professor.cpf == professor_selecionado:
    #                 professor_selecionado = professor
    #                 break

    #         if professor_selecionado is None:
    #             sg.popup('Selecione um professor válido.')
    #             self.__window.close()
    #             return None

    #         self.__window.close()
    #         # print('prof', professor_selecionado)
    #         # print('prof1', professor_selecionado.cpf)
    #         return {
    #             "nome": nome,
    #             "preco_atual": preco_atual,
    #             "tempo": tempo,
    #             "codigo_curso": codigo_curso,
    #             "descricao": descricao,
    #             "professor": professor,
    #             "titulo": titulo,
    #             "descricao_aula": descricao_aula
    #         }
           
    #     else:
    #         self.__window.close()
    #         return None

    def pegar_dados_curso(self):
        sg.ChangeLookAndFeel('LightGreen2')

        lista_professores = [professor.cpf for professor in self.__professor_DAO.get_all()]

        layout = [
            [sg.Text('-------- DADOS CURSO ----------', font=("Helvetica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Preço atual:', size=(15, 1)), sg.InputText('', key='preco_atual')],
            [sg.Text('Descrição do curso:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Text('Tempo:', size=(15, 1)), sg.InputText('', key='tempo')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
            [sg.Text('Professor:', size=(15, 1)), sg.Combo(lista_professores, key='professor')],
            [sg.Text('-------- AULAS ----------', font=("Helvetica", 20))],
            [sg.Text('Título da Aula:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text('Descrição da Aula:', size=(15, 1)), sg.InputText('', key='descricao_aula')],
            [sg.Button('Adicionar Aula'), sg.Button('Confirmar'), sg.Cancel('Cancelar')],
            [sg.Text('Aulas Adicionadas:', font=("Helvetica", 15))],
            [sg.Listbox(values=[], size=(50, 10), key='aulas_adicionadas')],
        ]
        
        self.__window = sg.Window('Sistema de venda de aulas online').Layout(layout)
        aulas = []

        while True:
            button, values = self.__window.Read()
            
            if button == 'Adicionar Aula':
                titulo = values['titulo']
                descricao_aula = values['descricao_aula']
                if titulo and descricao_aula:
                    aulas.append(Aula(titulo, descricao_aula))
                    self.__window.Element('aulas_adicionadas').Update([f'{aula.titulo}: {aula.descricao_aula}' for aula in aulas])
                    self.__window.Element('titulo').Update('')
                    self.__window.Element('descricao_aula').Update('')
                else:
                    sg.popup('Por favor, preencha os campos de título e descrição da aula.')
            
            elif button == 'Confirmar':
                nome = values['nome']
                preco_atual = values['preco_atual']
                tempo = values['tempo']
                descricao = values['descricao']
                codigo_curso = values['codigo_curso']
                professor_selecionado = values['professor']

                for professor in self.__professor_DAO.get_all():
                    if professor.cpf == professor_selecionado:
                        professor_selecionado = professor
                        break

                if professor_selecionado is None:
                    sg.popup('Selecione um professor válido.')
                    continue

                if not aulas:
                    sg.popup('Adicione pelo menos uma aula.')
                    continue

                self.__window.close()
                return {
                    "nome": nome,
                    "preco_atual": preco_atual,
                    "tempo": tempo,
                    "codigo_curso": codigo_curso,
                    "descricao": descricao,
                    "professor": professor_selecionado,
                    "aulas": aulas
                }
            
            # elif button in (None, 'Cancelar'):
            else:
                self.__window.close()
                return None


    # def mostrar_cursos(self, cursos):
    #     array_cursos = []
    #     for curso in cursos:
    #         # print('curso.aulas.titulo', curso.aulas.titulo)
            
    #         row = [curso.codigo_curso, 
    #             curso.nome, 
    #             curso.preco_atual, 
    #             curso.tempo, 
    #             curso.descricao,
    #             curso.professor.nome,
    #             # curso.aulas.titulo,
    #             # curso.aulas.descricao_aula
    #             curso.aulas
    #             ]
            
    #         array_cursos.append(row)

    #     #sg.set_options(font=("Helvica", 14))
    #     toprow = ['Codigo', 'Nome', 'Preço', 'Tempo', 'Descrição', 'Professor', 'Título'] 
    #     tbl1 = sg.Table(values=array_cursos,
    #                     headings=toprow,
    #                     auto_size_columns=True,
    #                     display_row_numbers=False,
    #                     justification='left', key='-TABLE-',
    #                     selected_row_colors='white on seagreen',
    #                     enable_events=False,
    #                     expand_x=True,
    #                     expand_y=True,
    #                     enable_click_events=False)
    #     layout = [[tbl1]]
    #     self.__window = sg.Window("Cursos", layout, size=(715, 200), resizable=True)
    #     button, values = self.open()
    #     self.__window.close()

    def mostrar_cursos(self, cursos):
        array_cursos = []
        for curso in cursos:
            curso_row = [
                curso.codigo_curso,
                curso.nome,
                curso.preco_atual,
                curso.tempo,
                curso.descricao,
                curso.professor.nome,
                "AULAS:"
            ]
            array_cursos.append(curso_row)

            if isinstance(curso.aulas, list):
                for aula in curso.aulas:
                    aula_row = [
                        "",
                        "", 
                        "", 
                        "", 
                        "",  
                        "",  
                        f"{aula.titulo}: {aula.descricao_aula}"
                    ]
                    array_cursos.append(aula_row)
            else:
                array_cursos.append(["", "", "", "", "", "", "Nenhuma aula cadastrada"])

        toprow = ['Código', 'Nome', 'Preço', 'Tempo', 'Descrição', 'Professor', 'Aulas'] 
        tbl1 = sg.Table(
            values=array_cursos,
            headings=toprow,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='left',
            key='-TABLE-',
            selected_row_colors='white on seagreen',
            enable_events=False,
            expand_x=True,
            expand_y=True,
            enable_click_events=False
        )
        layout = [[tbl1]]
        self.__window = sg.Window("Cursos", layout, size=(800, 400), resizable=True)
        button, values = self.open()
        self.__window.close()

    def selecionar_curso(self):
        sg.ChangeLookAndFeel('LightGreen2')
        layout = [
            [sg.Text('-------- SELECIONAR CURSO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do curso que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CÓDIGO:', size=(15, 1)), sg.InputText('', key='codigo_curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona curso').Layout(layout)

        button, values = self.open()
        codigo_curso = values['codigo_curso']
        self.__window.close()
        return codigo_curso   

    def mostrar_mensagem(self, msg: str):
        sg.popup("", msg)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
