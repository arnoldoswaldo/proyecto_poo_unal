# description: Este archivo contiene la implementación de la interfaz gráfica de usuario (GUI) para el sistema de inventario. utiliza la biblioteca tkinter para crear la interfaz gráfica y las clases Producto e Informe para gestionar los productos y generar informes, respectivamente.
import tkinter as tk
from tkinter import messagebox
from producto import Producto
from informe import Informe

class InventarioGUI:
    # Constructor de la clase, root es la ventana principal de la aplicación.
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")
        
        # Lista de productos
        self.productos = []

        # Interfaz para registrar producto
        self.frame_registro = tk.Frame(root)
        self.frame_registro.pack(pady=10)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_registro, text="Código:").grid(row=0, column=0)
        tk.Label(self.frame_registro, text="Nombre:").grid(row=1, column=0)
        tk.Label(self.frame_registro, text="Descripción:").grid(row=2, column=0)
        tk.Label(self.frame_registro, text="Precio:").grid(row=3, column=0)
        tk.Label(self.frame_registro, text="Cantidad:").grid(row=4, column=0)
        
        self.codigo_entry = tk.Entry(self.frame_registro)
        self.nombre_entry = tk.Entry(self.frame_registro)
        self.descripcion_entry = tk.Entry(self.frame_registro)
        self.precio_entry = tk.Entry(self.frame_registro)
        self.cantidad_entry = tk.Entry(self.frame_registro)

        # Posicionamiento de los campos de entrada
        self.codigo_entry.grid(row=0, column=1)
        self.nombre_entry.grid(row=1, column=1)
        self.descripcion_entry.grid(row=2, column=1)
        self.precio_entry.grid(row=3, column=1)
        self.cantidad_entry.grid(row=4, column=1)

        # Botones para registrar entrada y salida
        tk.Button(self.frame_registro, text="Registrar Entrada", command=self.registrar_entrada).grid(row=5, column=0, pady=10)
        tk.Button(self.frame_registro, text="Registrar Salida", command=self.registrar_salida).grid(row=5, column=1)

        # Botón para ver inventario y generar informes
        self.frame_informes = tk.Frame(root)
        self.frame_informes.pack(pady=10)

        tk.Button(self.frame_informes, text="Ver Inventario", command=self.ver_inventario).pack(side="left", padx=10)
        tk.Button(self.frame_informes, text="Generar Informe Consolidado", command=self.generar_informe_consolidado).pack(side="left", padx=10)
    
    # Método para buscar un producto por su código. 
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
   
    # Método para registrar la entrada de un producto al inventario. Incluye validaciones para verificar si el producto ya existe.
    def registrar_entrada(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        cantidad = int(self.cantidad_entry.get())

        producto = self.buscar_producto(codigo)
        if not producto:
            producto = Producto(codigo, nombre, descripcion, precio)
            self.productos.append(producto)

        producto.entrada(cantidad)
        messagebox.showinfo("Registro de Entrada", "¡Entrada registrada exitosamente!")
    
    # Método para registrar la salida de un producto del inventario. incluye validaciones para verificar si el producto existe y si hay suficiente stock disponible.
    def registrar_salida(self):
        codigo = self.codigo_entry.get()
        cantidad = int(self.cantidad_entry.get())

        producto = self.buscar_producto(codigo)
        if producto:
            try:
                producto.salida(cantidad)
                messagebox.showinfo("Registro de Salida", "¡Salida registrada exitosamente!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Producto no encontrado.")
    # Método para ver el inventario de productos. muestra una ventana emergente con la información de los productos en el inventario.
    def ver_inventario(self):
        inventario_text = ""
        for producto in self.productos:
            inventario = producto.obtener_inventario()
            inventario_text += (f"Código: {inventario['codigo']}, Nombre: {inventario['nombre']}, "
                                f"Descripción: {inventario['descripcion']}, Precio: {inventario['precio']}, "
                                f"Stock: {inventario['stock']}\n")
        messagebox.showinfo("Inventario", inventario_text)

    # Método para generar un informe consolidado de los productos en el inventario. muestra una ventana emergente con un mensaje de confirmación.
    def generar_informe_consolidado(self):
        informe = Informe(self.productos)
        informe.generar_informe()
        messagebox.showinfo("Informe", "Informe consolidado generado exitosamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioGUI(root)
    root.mainloop()
