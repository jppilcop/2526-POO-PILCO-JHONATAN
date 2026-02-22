import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_line(self):
        """
        Convierte el producto en una línea de texto
        para guardarlo en el archivo.
        """
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo.
        Si el archivo no existe, lo crea.
        Maneja errores de lectura.
        """
        try:
            if not os.path.exists(self.archivo):
                # Crear archivo si no existe
                open(self.archivo, "w").close()
                print("Archivo de inventario creado.")

            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[id_producto] = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                    except ValueError:
                        print(f"Línea corrupta ignorada: {linea.strip()}")

            print("Inventario cargado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.
        Maneja errores de escritura.
        """
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(producto.to_line())
            print("Inventario guardado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El producto ya existe.")
            return

        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()
        print("Producto añadido exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio

        self.guardar_en_archivo()
        print("Producto actualizado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        del self.productos[id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos.values():
            print(f"ID: {producto.id_producto} | "
                  f"Nombre: {producto.nombre} | "
                  f"Cantidad: {producto.cantidad} | "
                  f"Precio: ${producto.precio:.2f}")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print("Error: Cantidad o precio inválido.")

        elif opcion == "2":
            try:
                id_producto = input("ID del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)

            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()