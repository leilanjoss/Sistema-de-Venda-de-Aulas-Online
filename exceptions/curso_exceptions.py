# CURSO
class CursoNExisteException(Exception):
    def __init__(self):
        self.mensagem = "Esse curso não existe"
        super().__init__(self.mensagem)

class CursoRepetidoException(Exception):
    def __init__(self, curso):
        self.mensagem = "O curso com código {} já existe"
        super().__init__(self.mensagem.format(curso.codigo_curso))