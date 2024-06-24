class ProfessorRepetidoException(Exception):
    def __init__(self, professor):
        self.mensagem = "O professor com CPF {} já existe"
        super().__init__(self.mensagem.format(professor.cpf))