class Casa:
    Familia: str = "Amador"
    colonia: str = "Paseos del sol"
    direccion: str = "Rafael Vaca 1539"

    def __init__(self, nombre, edad) -> None:
        self.nombre: str = nombre
        self.edad : int = edad

    @classmethod
    def cambiarCasa(cls, colonia: str, direccion: str):
        cls.colonia = colonia
        cls.direccion =direccion

edgar = Casa("Edgar Amador", 10)
Papa = Casa("Juan Amador", 30)
Mama = Casa("Margarita de Amador", 29)

Papa.cambiarCasa("Parques del bosque","Bahia de pelicanos 123" )

print(Papa.direccion)
print(Mama.direccion)