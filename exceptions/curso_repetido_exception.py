class CursoRepetidoException(Exception):
    def __init__(self, codigo_curso):
        self.mensagem = "O amigo com código {} já existe"
        super().__init__(self.mensagem.format(codigo_curso))