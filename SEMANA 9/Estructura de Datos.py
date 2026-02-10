# ============================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# Archivo único: inventario.py
# ============================================


# ============================================
# CLASE PRODUCTO
# ============================================

class Producto:
    """
    Representa un producto del inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # -------- GETTERS --------
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # -------- SETTERS --------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ============================================
# CLASE INVENTARIO
# ============================================

class Inventario:
    """
    Gestiona la lista de productos del inventario.
    """

    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if encontrados:
            print("🔍 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos.")

    def mostrar_productos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Inventario:")
            for p in self.productos:
                print(p)


# ============================================
# MENÚ DE USUARIO (INTERFAZ EN CONSOLA)
# ============================================

def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (enter para no cambiar): ")
            precio = input("Nuevo precio (enter para no cambiar): ")

            nueva_cantidad = int(cantidad) if cantidad != "" else None
            nuevo_precio = float(precio) if precio != "" else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida.")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    menu()
