# Descripción: Módulo para manejar la base de datos SQLite de la aplicación de inventario de producto
import sqlite3
from tkinter import ttk, messagebox # Importamos el módulo messagebox de tkinter para mostrar mensajes de error al usuario 
from producto import Producto  

# Clase para manejar la base de datos
class BaseDatos:
    def __init__(self):
        # Conexión a la base de datos 
        self.conexion = sqlite3.connect("inventario.db")
        self.cursor = self.conexion.cursor()  # Creación de un cursor para ejecutar consultas en SQL
        self.crear_tabla()  # Llamada al método para crear la tabla si no existe

    # Método para crear la tabla de productos si no existe
    def crear_tabla(self):
        # Ejecución de la consulta SQL para crear la tabla de productos 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                producto_id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                precio REAL NOT NULL,
                cantidad_stock INTEGER NOT NULL,
                proveedor TEXT
            )
        ''')
        self.conexion.commit()  # Confirmación de los cambios en la base de datos

    # Método para obtener todos los productos de la base de datos
    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()  # obtiene todas las filas de la consulta
        return [Producto(*row) for row in rows] # retorna una lista de objetos Producto

    def agregar_producto(self, producto):
        # Ejecución de la consulta SQL para insertar un nuevo producto en la tabla
        self.cursor.execute('''
            INSERT INTO productos (nombre, descripcion, precio, cantidad_stock, proveedor)
            VALUES (?, ?, ?, ?, ?)
        ''', (producto.nombre, producto.descripcion, producto.precio, producto.cantidad_stock, producto.proveedor))
        self.conexion.commit()  # Confirmación de los cambios en la base de datos
    
    # Método para eliminar un producto de la base de datos
    def eliminar_producto(self, producto):
        self.cursor.execute('''
             DELETE FROM productos WHERE producto_id=?               
        ''', (producto.producto_id,))
        self.conexion.commit()
        
    def actualizar_producto(self, producto):
        try:
            # Ejecutar la consulta SQL para actualizar el producto
            self.cursor.execute('''
                UPDATE productos SET nombre=?, descripcion=?, precio=?, cantidad_stock=?, proveedor=? WHERE producto_id=?
            ''', (producto.nombre, producto.descripcion, producto.precio, producto.cantidad_stock, producto.proveedor, producto.producto_id))
            self.conexion.commit()  # Confirmar los cambios en la base de datos
            messagebox.showinfo("Éxito", "Producto modificado correctamente.")
    
        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            messagebox.showerror("Error en base de datos", f"No se pudo actualizar el producto: {error}")
    
    # Método para buscar productos por nombre en la base de datos
    def buscar_productos_por_nombre(self, nombre):
        try:
            # Consulta SQL para buscar productos por coincidencia de nombre
            self.cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
            productos = self.cursor.fetchall()
            self.conexion.commit()
        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            messagebox.showerror("Error en base de datos", f"No se pudo obtener el producto: {error}")
        return productos
    
    def buscar_productos_por_proveedor(self, proveedor):
        try:
            # Consulta SQL para buscar productos por proveedor
            self.cursor.execute("SELECT * FROM productos WHERE proveedor=?", (proveedor,))
            productos = self.cursor.fetchall()
            self.conexion.commit()
        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            messagebox.showerror("Error en base de datos", f"No se pudo obtener el producto: {error}")
        return productos

    def buscar_producto_por_id(self, producto_id):
        try:
            # Consulta SQL para buscar un producto por ID
            self.cursor.execute("SELECT * FROM productos WHERE producto_id=?", (producto_id,))
            producto = self.cursor.fetchone()
            self.conexion.commit()
        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            messagebox.showerror("Error en base de datos", f"No se pudo obtener el producto: {error}")
        return producto
    
    def cerrar_conexion(self):
        self.conexion.close()  # Cierre de la conexión a la base de datos