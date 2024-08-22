# Description: Clase que genera un informe consolidado de los productos en el inventario.
class Informe:
    def __init__(self, productos):
        self.productos = productos

    # Método para generar un informe consolidado de los productos en el inventario.
    def generar_informe(self):
        with open("Informe_Inventario.txt", "w") as archivo:
            archivo.write("Informe Consolidado de Inventario:\n")
            archivo.write("Código | Nombre | Fecha       | Cantidad | Operación\n")
            archivo.write("----------------------------------------------------\n")
            for producto in self.productos:
                registros = producto.obtener_registros()
                for registro in registros:
                    archivo.write(f"{producto.codigo} | {producto.nombre} | {registro[0]} | {registro[1]} | {registro[2]}\n")
            print("Informe consolidado generado exitosamente como 'Informe_Inventario.txt'.")