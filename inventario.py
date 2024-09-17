# Clase Inventario que maneja la lista de productos
class Inventario:
    def __init__(self):
        self.productos = []

    # Método para agregar un producto a la lista
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def modificar_producto(self, producto):
        for i in range(len(self.productos)):
            if self.productos[i].producto_id == producto.producto_id:
                self.productos[i] = producto
                break

    # Método para actualizar el stock de un producto
    def actualizar_stock(self, producto_id, cantidad):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                producto.stock += cantidad
                break

    def eliminar_producto(self, producto):
        self.productos = [p for p in self.productos if p.producto_id != producto.producto_id]


    def buscar_producto(self, producto_id):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                return producto
        return None

    # Método para generar un informe de los productos en el inventario
    def generar_informe(self):
        informe = [producto.obtener_detalles() for producto in self.productos]
        return informe