class Libro:
    titulo: str
    autor: str
    isbn: str
    disponibilidad: bool
    def __init__(self, titulo: str, autor: str, isbn: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True  
    def prestar(self):
        if self.disponibilidad == True:
            print(f"Te presto el libro")
            self.disponibilidad = False
        else:
            print(f"No disponible por ahora")
    def devolver(self):
        self.disponibilidad = True
        
    def informacionLibro(self):
            print(f"Titulo: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"ISBN: {self.isbn}")
            print(f"Disponibilidad: {self.disponibilidad}")

mi_objeto = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-16-148410-0")
mi_objeto.prestar()
mi_objeto.informacionLibro()