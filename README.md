# proyecto_poo_unal
Proyecto poo, Entre las opciones planteadas se opto por el desarrollo de una aplicación que emule un sistema de gestión de inventario para una bodega utilizando Python, tomando tambien el plateamiento de que la aplicacion maneje una interfaz grafica GUI, para lo cual se hizo uso de tkinter la cual se desglosa a detalle mas adelante, y tambien la opcion de un modulo que genera informes de los productos en un archivo txt, como primer medida pasamos a desarrollar nuestro diagrama de clases. 

DIAGRAMA DE CLASES

***
```mermaid
classDiagram
    class Producto {
        - _codigo : str
        - _nombre : str
        - _descripcion : str
        - _precio : float
        - _stock : int
        - _registros : list
        + codigo : str
        + nombre : str
        + descripcion : str
        + precio : float
        + stock : int
        + entrada(cantidad: int)
        + salida(cantidad: int)
        + obtener_inventario() dict
        + obtener_registros() list
    }

    class Informe {
        - productos : list~Producto~
        + generar_informe()
    }

    class InventarioGUI {
        - productos : list~Producto~
        + registrar_entrada()
        + registrar_salida()
        + ver_inventario()
        + generar_informe_consolidado()
    }

    Informe o-- Producto 
    InventarioGUI --> Producto 
```
