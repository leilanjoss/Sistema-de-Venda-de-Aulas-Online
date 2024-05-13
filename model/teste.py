from professor import Professor
from aula import Aula
from curso import Curso
from material import Material

# instância de Professor
professor = Professor("Nome do Professor","email prof", "senha123", "123456789", "12345678910", "Cidade", "SP", "Rua", "123")

# instâncias de Aula
aula1 = Aula("Título da Aula 1", "Link da Aula 1", "Descrição da Aula 1", 1)
aula2 = Aula("Título da Aula 2", "Link da Aula 2", "Descrição da Aula 2", 2)

# add materiais as aulas
material1 = Material("Descrição do Material 1", "Anexo 1")
material2 = Material("Descrição do Material 2", "Anexo 2")
aula1.adicionar_material(material1)
aula2.adicionar_material(material2)

# instância de Curso e adicione as aulas
curso = Curso("Nome do Curso", 100.0, "Descrição do Curso", 10, 1, professor)
curso.adicionar_aula(aula1)
curso.adicionar_aula(aula2)

# acessando e imprimindo os atributos do curso
print("Nome do Curso:", curso.nome)
print("Preço atual:", curso.preco_atual)
print("Descrição:", curso.descricao)
print("Tempo:", curso.tempo)
print("Código do Curso:", curso.codigo_curso)
print("Professor:", curso.professor.nome)

# acessando e imprimindo os atributos das aulas
for aula in curso.aulas:
    print("\nTítulo da Aula:", aula.titulo)
    print("Link:", aula.link)
    print("Descrição:", aula.descricao_aula)
    print("Ordem:", aula.ordem)
    print("Materiais:")
    for material in aula.materiais:
        print("- Descrição:", material.descricao_material)
        print("- Anexo:", material.anexo)