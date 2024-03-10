#Interfaz de BaseData
from abc import ABC, abstractmethod
array = []

class  DataBase(ABC):
    @abstractmethod
    def insertar(self, data: str) -> bool: 
        self._data  = data
        array.append(self._data)
        return True
    
    @abstractmethod
    def eliminar(self, pos: int) -> bool:
        self._pos  = pos
        array.pop(self._pos)
        return True
    
    @abstractmethod
    def actualizar(self,data) -> None:
        self._data  = data
        return True
