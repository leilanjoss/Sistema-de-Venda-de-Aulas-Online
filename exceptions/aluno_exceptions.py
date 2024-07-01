class AlunoNExisteException(Exception):
    def __init__(self):
        self.mensagem = "Esse aluno não existe"
        super().__init__(self.mensagem)

class AlunoRepetidoException(Exception):
    def __init__(self, aluno):
        self.mensagem = "O aluno com CPF {} já existe"
        super().__init__(self.mensagem.format(aluno.cpf))