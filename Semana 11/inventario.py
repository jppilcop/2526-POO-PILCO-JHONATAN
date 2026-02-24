import json
from producto import Producto


class Inventario:
    """
    Clase que gestiona los productos usando un diccionario.
    La clave es el ID y el valor es el objeto Producto.
    """

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠ El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✔ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✔ Producto eliminado.")
        else:
            print("⚠ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("✔ Producto actualizado.")
        else:
            print("⚠ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = False
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                print(producto)
                encontrados = True

        if not encontrados:
            print("⚠ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # ----------- ARCHIVOS -----------

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump(
                {id: prod.to_dict() for id, prod in self.productos.items()},
                f,
                indent=4
            )
        print("✔ Inventario guardado correctamente.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                for id, prod_data in datos.items():
                    self.productos[id] = Producto.from_dict(prod_data)
            print("✔ Inventario cargado correctamente.")
        except FileNotFoundError:
            print("⚠ No existe archivo previo. Se iniciará inventario vacío.")