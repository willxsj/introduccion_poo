"""
" Alcance de las variables
" Tipo de dato string
"""
class Variables:

    texto : str = "Esto es un 'texto'"#esta es una variable de clase

    def __init__(self, cadena:str):
        self.cadena = cadena # esta es una variable que puees utilizar en def


    def contarCaracteres(self, texto:str)-> None:#Cuenta el numero de caracteres no su posicion
        print(len(texto))#4
        print(len(self.cadena))#5
        print(len(self.texto))

    def caracter(self, posicion:int) -> None:#Te devuelve el caracter  que tu le pongas 
        print(self.cadena[posicion])
        print(self.otro_texto)

    otro_texto : str = "MMMMM"# esta es una variable que puees utilizar en def ya que esta a la misma altura de espacios




mi_objeto = Variables("adios")
mi_objeto.contarCaracteres("hola")
mi_objeto.caracter(3)