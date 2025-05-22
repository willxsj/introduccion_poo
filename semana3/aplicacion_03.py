class Mayor_de_3:
    def __init__ (self):
        pass

    def mayor(self, num1:int, num2:int, num3:int)->None:
        if num1 >= num2 and num1 >= num3:
            print(f"El mayor es: {num1}")
        elif num2 >= num1 and num2 >= num3:
            print(f"El mayor es: {num2}")
        else:
            print(f"El mayor es: {num3}")

mi_objeto = Mayor_de_3()

mi_objeto.mayor(1,2,3)
mi_objeto.mayor(1,4,2)
mi_objeto.mayor(5,1,2)
mi_objeto.mayor(6,1,1)
mi_objeto.mayor(1,1,7)
mi_objeto.mayor(1,8,1)
mi_objeto.mayor(9,9,1)
mi_objeto.mayor(10,1,10)
mi_objeto.mayor(1,11,11)
mi_objeto.mayor(12,12,12)