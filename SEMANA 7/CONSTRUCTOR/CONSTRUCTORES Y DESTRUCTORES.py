# --------------------------------------------
# Programa: Uso de Constructores y Destructores
# Autor: Paúl Pilco
# Descripción:
# Este programa demuestra el uso de los métodos
# __init__ (constructor) y __del__ (destructor)
# en una clase de Python.
# --------------------------------------------

class RegistroArchivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea un objeto.
        Inicializa los atributos y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "a")
        print(f"[INFO] Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir_mensaje(self, mensaje):
        """
        Método que escribe un mensaje dentro del archivo.
        """
        self.archivo.write(mensaje + "\n")
        print("[INFO] Mensaje escrito en el archivo.")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto
        es eliminado o el programa finaliza.
        Sirve para liberar recursos.
        """
        self.archivo.close()
        print(f"[INFO] Archivo '{self.nombre_archivo}' cerrado correctamente.")


# ------------------- PROGRAMA PRINCIPAL -------------------

if __name__ == "__main__":
    # Creación del objeto (se ejecuta el constructor)
    registro = RegistroArchivo("registro.txt")

    # Uso del objeto
    registro.escribir_mensaje("Inicio del programa")
    registro.escribir_mensaje("Aplicando constructores y destructores en Python")

    # Eliminación explícita del objeto (opcional)
    del registro

    print("Programa finalizado.")
