class Calculadora:
    def __init__ (self):
        print("Constructor")

    def suma(self, num1, num2):
        #Resive dos valores, los suma y los almacena en resultado
        resultado = num1 + num2
        #Imprme el texto Resultado y el valor de la variable resultado
        print(f"Resultado: {resultado}")
        #Imprme el texto Resultado y el valor de la variable resultado
        #convierte el tipo a dato string
        print("Resultado: " + str(resultado))
        
#Crea una instancia de la clase calculadora es decir crea un objeto
mi_objeto = Calculadora()

#invica al metodo sumar y le envia dos numeros
mi_objeto.suma(10,8)

#invica al metodo sumar y le envia dos cadenas
mi_objeto.suma("que","rollo")
