class Publication:

    def __init__(self,name: str, year: int) -> None:
        self.name = name
        self.year = year

    def get_name(self)->int:
        return self.name


class Book(Publication):
    def __init__(self,name: str, year: int, pages: int)->None:
        super().__init__(name, year)
        self.pages = pages

    def __str__(self)->None:
        return f"Tipo: Book, Nombre: {self.name}, Año: {self.year}, Pages: {self.pages}"
class Magazine(Publication):
    def __init__(self,name: str, year: int, pages: int)->None:
        super().__init__(name, year)
        self.pages = pages

    def __str__(self)->None:
        return f"Tipo: Magazine, Nombre: {self.name}, Año: {self.year}, Pages: {self.pages}"
class Newspaper(Publication):
    def __init__(self,name: str, year: int, brand: str)->None:
        super().__init__(name, year)
        self.brand = brand
    def __str__(self)->None:
        return f"Tipo: Newspaper, Nombre: {self.name}, Año: {self.year}, Pages: {self.brand}"

libro = Book('Cien años de salchichas',2023, 205)
print(libro)
revista = Magazine('Vogue',2023,55)
print(revista)
periodico = Newspaper('New York Times', 2023,'New York CORP')
print(periodico)