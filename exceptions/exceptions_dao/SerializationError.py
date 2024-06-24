from exceptions.exceptions_dao.DAOException import DAOException

class SerializationError(DAOException):
    def __init__(self, message):
        super().__init__(message)
