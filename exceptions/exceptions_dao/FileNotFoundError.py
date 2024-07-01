from exceptions.exceptions_dao.DAOException import DAOException

class FileNotFoundError(DAOException):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Arquivo '{filename}' não encontrado.")