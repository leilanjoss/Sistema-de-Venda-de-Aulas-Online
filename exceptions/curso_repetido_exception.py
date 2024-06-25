class CursoRepetidoException(Exception):
    def __init__(self, curso):
        self.mensagem = "O amigo com código {} já existe"
        super().__init__(self.mensagem.format(curso.codigo_curso))