import pickle
from abc import ABC, abstractmethod
from exceptions.exceptions_dao.DAOException import DAOException
from exceptions.exceptions_dao.FileNotFoundError import FileNotFoundError
from exceptions.exceptions_dao.KeyNotFoundException import KeyNotFoundException
from exceptions.exceptions_dao.SerializationError import SerializationError

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} #é aqui que vai ficar a lista que estava no controlador. Nesse exemplo estamos usando um dicionario
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    #esse método precisa chamar o self.__dump()
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  #atualiza o arquivo depois de add novo amigo

    def update(self, key, obj):
        try:
            if key in self.__cache:
                self.__cache[key] = obj
                self.__dump()  # Atualiza o arquivo após atualizar um objeto existente
            else:
                raise KeyNotFoundException(key)
        except Exception as e:
            raise DAOException(f"Erro ao atualizar objeto: {e}")

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise KeyNotFoundException(key)
        except Exception as e:
            raise DAOException(f"Erro ao obter objeto: {e}")

    # esse método precisa chamar o self.__dump()
    def remove(self, key):
        try:
            if key in self.__cache:
                self.__cache.pop(key)
                self.__dump()
            else:
                raise KeyNotFoundException(key)
        except Exception as e:
            raise DAOException(f"Erro ao remover objeto: {e}")

    def get_all(self):
        return self.__cache.values()