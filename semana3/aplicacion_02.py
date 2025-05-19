class Calculadora:

    def __init__(self):
        #Insica el paso de linea y que se ejecute la siguiente
        pass

    def suma(self, num1, num2):
        resultado = num1 + num2
        print(f"Resultado: {resultado}")


    def resta(self,num1, num2):
        resultado = num1 - num2
        return resultado
        
    def multi(self,num1,num2):
        resultado = num1 * num2
        return resultado

    def div(self , dividendo:int, divisor:int):
        try:
            resultado = dividendo / divisor
            print(f"Resultado: {resultado}")
        except ZeroDivisionError as error:
            print(f"Error 001: {error.args[0]}")
        except TypeError as error:
            print(f"Error 002: {error.args[0]}")
        except Exception as error:
            print(f"Error 003: {error.args[0]}")


mi_objeto = Calculadora()
mi_objeto.suma(10,5)
print(f"Resultado: {mi_objeto.resta(10,5)}")
print(f"Resultado: {mi_objeto.multi(10,5)}")
mi_objeto.div(divisor="hola",dividendo=10)