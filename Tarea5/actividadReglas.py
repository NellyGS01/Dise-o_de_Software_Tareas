from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

from pruebadatabasemysql import *


#Clase Reporte
class Reporte:
    def  __init__(self, id:int=None, baseDeDatos:DataBase = None):
        self._id = id
        self._baseDeDatos = baseDeDatos

    def abrir():
        pass

    
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


# Implementacion MySQL
dbMySQL = MySQL("sql10.freesqldatabase.com","sql10689405","ACM1wVFXPb","sql10689405")
print(dbMySQL.insertar("Reporte","Informacion que cura","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
print(dbMySQL.actualizar("Reporte","Informacion que no cura","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
print(dbMySQL.eliminar("Reporte","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
