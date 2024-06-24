from exceptions.exceptions_dao.DAOException import DAOException


class KeyNotFoundException(DAOException):
    def __init__(self, key):
        self.key = key
        super().__init__(f"Chave '{key}' não encontrada.")