# Description: Archivo principal de la aplicación, se encarga de inicializar la interfaz gráfica de la aplicación. 
#autor: Arnold Oswaldo Acosta
import tkinter as tk
from interfazinventario import InterfazInventario

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazInventario(root)
    root.mainloop()