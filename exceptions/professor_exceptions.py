# PROFESSOR
class ProfessorNExisteException(Exception):
    def __init__(self):
        self.mensagem = "Esse professor não existe"
        super().__init__(self.mensagem)

class ProfessorRepetidoException(Exception):
    def __init__(self, professor):
        self.mensagem = "O professor com CPF {} já existe"
        super().__init__(self.mensagem.format(professor.cpf))