class Persona:

#Atrubutos
    nombre : str
    edad : int
    sexo : str


#constructor
    def __init__(self, nombre:str, edad:int, sexo:str)-> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

#metodos      
    def hablar(self, mensaje:str) -> None:
        print(mensaje)

    def informacion(self)-> None:
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")

    def correr(self,velocidad:float)->None:
        print(f"velocidad alcanzada: {velocidad} km/hr")


#Objetos de tipo persona
dejah = Persona("dejah thoris",20,"F")
john = Persona("jonh carter",23,"M")

dejah.informacion()
dejah.correr(22.0)
dejah.hablar("holaaaaa")
john.hablar("que rollo")
john.informacion()
dejah.correr(33.0)
