from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


array = []

#Clase Reporte
class Reporte:
    def  __init__(self, id:int=None, baseDeDatos:DataBase = None):
        self._id = id
        self._baseDeDatos = baseDeDatos

    def abrir():
        pass

#Interfaz de BaseData
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
    

#Clase de MySQL  
class MySQL(DataBase):
    _conexion = ""
    def __init__(self, servidor="localhost", puerto=3306, usuario="root", contrasena="" ,basedatos=""):
        self.servidor = servidor
        self.puerto = puerto
        self.usuario = usuario
        self.contrasena = contrasena
        self.basedatos = basedatos
        
        
    def insertar(self, data: str) -> bool:
        return super().insertar(data)
    
    def actualizar(self, data: str) -> bool:
        return super().actualizar(data)
    
    def eliminar(self, data: str) -> bool:
        return super().eliminar(data)

#Clase de MongoDB  
class MongoDB(DataBase):
    _coleccion = ""
    _clase = None
    def __init__(self, coleccion, clase):
        self._coleccion = coleccion
        self._clase = clase

    def insertar(self, data: str) -> bool:
        return super().insertar(data)
    
    def actualizar(self, data: str) -> bool:
        return super().actualizar(data)
    
    def eliminar(self, data: str) -> bool:
        return super().eliminar(data)


#Implementacion
    dbMySQL = MySQL("localhost","12345","user","password","dbname")
    Reporte1 = Reporte(1, dbMySQL)

    Reporte1._baseDeDatos.insertar('Hola')

    print(array)

    Reporte1._baseDeDatos.eliminar(0)

    print(array)