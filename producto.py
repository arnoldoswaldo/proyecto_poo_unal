# Description: Clase Producto que representa un producto en el inventario.
import datetime
from informe import Informe
class Producto:
    def __init__(self, codigo, nombre, descripcion, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = 0
        self._registros = []

    # Propiedades de solo lectura para los atributos del producto.
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    # Método para registrar la entrada de un producto al inventario. Incluye validaciones para verificar si el producto ya existe.
    def entrada(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._stock += cantidad
        fecha = datetime.datetime.now()
        self._registros.append((fecha, cantidad, "Entrada"))

    # Método para registrar la salida de un producto del inventario.incluye validaciones para verificar si el producto existe y si hay suficiente stock disponible.
    def salida(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if cantidad <= self._stock:
            self._stock -= cantidad
            fecha = datetime.datetime.now()
            self._registros.append((fecha, cantidad, "Salida"))
        else:
            raise ValueError("No hay suficiente stock disponible.")

    # Método para obtener el inventario del producto.
    def obtener_inventario(self):
        return {
            "codigo": self._codigo,
            "nombre": self._nombre,
            "descripcion": self._descripcion,
            "precio": self._precio,
            "stock": self._stock
        }
    
    # Método para obtener los registros de entradas y salidas del producto.
    def obtener_registros(self):
        return self._registros
    