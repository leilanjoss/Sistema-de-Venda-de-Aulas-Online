class DAOException(Exception):
    #Exceção base para erros no DAO
    def __init__(self, message):
        super().__init__(message)