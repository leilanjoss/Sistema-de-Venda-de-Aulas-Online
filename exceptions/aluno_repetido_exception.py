class AlunoRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O aluno com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))