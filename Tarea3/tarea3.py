#25 de enero del 2024
#Tarea 3

#Esta clase hace una lectura del code para crear un diccionario de clases
from __future__ import annotations
from abc import ABC, abstractmethod
import math
class Figura(ABC):
    '''Clase abstracta'''
    #Polimorfismo loco
    @abstractmethod
    def perimetro(self):
        return self.perimetro()
    def area(self):
        return self.area()

class rectangulo(Figura):
    def __init__(self,ladoMayor,ladoMenor):
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def perimetro(self):
        return (self.ladoMayor*2) + (self.ladoMenor*2)
    def area(self):
        return self.ladoMenor*self.ladoMayor

class circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def perimetro(self):
        return (self.radio) * (3.1416*2)
    def area(self):
        return (self.radio*self.radio) * 3.1416

class triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return self.base + self.altura +(((self.altura **2) + (self.base **2)) ** 0.5)

    def area(self):
        return (self.base * self.altura)/2

rec = rectangulo(4,2)
print(rec.perimetro())
print(rec.area())
cir = circulo(5)
print(cir.perimetro())
print(cir.area())
tri = triangulo(3,4)
print(tri.perimetro())
print(tri.area())