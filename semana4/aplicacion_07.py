class ProductoElectronico:
    def __init__(self, nombre: str, precio: float, marca: str) -> None:
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.garantia_meses = 12  # Garantía por defecto

    def cambiarGarantia(self):
        garantia = input("¿Cuántos meses de garantía desea?: ")
        garantia = int(garantia)
        self.garantia_meses = garantia

    def aplicaDescuento(self, descuento: float):
        self.precio = self.precio * (1 - descuento / 100)
        print(f"Precio con descuento del {descuento}%: ${self.precio:.2f}")

    def mostrar(self):
        print("Detalles del producto:")
        print(f"Nombre: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Meses de garantía: {self.garantia_meses}")


producto1 = ProductoElectronico("Smartphone", 8000.0, "Samsung")
print("\nProducto 1:")
producto1.cambiarGarantia()
producto1.aplicaDescuento(10)
producto1.mostrar()
producto2 = ProductoElectronico("Laptop", 15000.0, "HP")
print("\nProducto 2:")
producto2.cambiarGarantia()
producto2.aplicaDescuento(15)
producto2.mostrar()