# ==============================
# CLASE LIBRO
# ==============================

class Libro:
    """
    Representa un libro dentro de la biblioteca.
    - titulo y autor se almacenan en una TUPLA porque son inmutables.
    - categoria puede cambiar si se requiere.
    - isbn es único para cada libro.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Indica si el libro está disponible para préstamo

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Disponible: {self.disponible}"


# ==============================
# CLASE USUARIO
# ==============================

class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    - nombre
    - id_usuario (único)
    - lista de libros prestados (LISTA)
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar préstamos

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        return [libro.info[0] for libro in self.libros_prestados]

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# ==============================
# CLASE BIBLIOTECA
# ==============================

class Biblioteca:
    """
    Gestiona:
    - Diccionario de libros {ISBN: Libro}
    - Conjunto de IDs únicos
    - Diccionario de usuarios {ID: Usuario}
    """

    def __init__(self):
        self.libros = {}  # Diccionario para acceso rápido por ISBN
        self.usuarios = {}
        self.ids_usuarios = set()  # Conjunto para garantizar unicidad

    # --------------------------
    # Gestión de libros
    # --------------------------

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    # --------------------------
    # Gestión de usuarios
    # --------------------------

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("El ID ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario dado de baja.")
        else:
            print("Usuario no encontrado.")

    # --------------------------
    # Préstamo y devolución
    # --------------------------

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:
                libro.disponible = False
                usuario.prestar_libro(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro in usuario.libros_prestados:
                libro.disponible = True
                usuario.devolver_libro(libro)
                print("Libro devuelto correctamente.")
            else:
                print("El usuario no tiene este libro.")
        else:
            print("Libro o usuario no encontrado.")

    # --------------------------
    # Búsquedas
    # --------------------------

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]


# ==============================
# PRUEBA DEL SISTEMA
# ==============================

if __name__ == "__main__":

    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("1984", "George Orwell", "Distopía", "001")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "002")
    libro3 = Libro("Python Básico", "Juan Pérez", "Programación", "003")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Carlos", "U001")
    usuario2 = Usuario("María", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libro
    biblioteca.prestar_libro("001", "U001")

    # Listar libros prestados
    print("Libros prestados a Carlos:", usuario1.listar_libros())

    # Devolver libro
    biblioteca.devolver_libro("001", "U001")

    # Buscar libro por categoría
    resultados = biblioteca.buscar_por_categoria("Programación")
    print("Libros encontrados en categoría Programación:")
    for libro in resultados:
        print(libro)
