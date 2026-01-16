# ==========================================
# Sistema Educativo - Programación Orientada a Objetos
# Autor: Paúl Pilco
# Institución: Unidad Educativa Particular Jim Irwin
# ==========================================

# -------- CLASE BASE --------
class Persona:
    def __init__(self, nombre, edad):
        # Encapsulación: atributos privados
        self.__nombre = nombre
        self.__edad = edad

    # Métodos getters (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def mostrar_datos(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"


# -------- CLASE DERIVADA: ESTUDIANTE --------
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        # Herencia: se llama al constructor de la clase base
        super().__init__(nombre, edad)
        self.curso = curso

    # Polimorfismo: sobrescritura del método
    def mostrar_datos(self):
        return (
            f"Estudiante: {self.get_nombre()}\n"
            f"Edad: {self.get_edad()}\n"
            f"Curso: {self.curso}"
        )


# -------- CLASE DERIVADA: DOCENTE --------
class Docente(Persona):
    def __init__(self, nombre, edad, materias, institucion):
        super().__init__(nombre, edad)
        self.materias = materias
        self.institucion = institucion

    # Polimorfismo: mismo método, diferente comportamiento
    def mostrar_datos(self):
        materias_texto = ", ".join(self.materias)
        return (
            f"Docente: {self.get_nombre()}\n"
            f"Edad: {self.get_edad()}\n"
            f"Materias que imparte: {materias_texto}\n"
            f"Institución: {self.institucion}"
        )


# -------- PROGRAMA PRINCIPAL --------
if __name__ == "__main__":
    # Creación de objetos (instancias)
    estudiante1 = Estudiante("ARIEL ZELA", 16, "PRIMERO DE BACHILLERATO")

    docente1 = Docente(
        "Paúl Pilco",
        30,
        ["Matemática", "Razonamiento Numérico"],
        "Unidad Educativa Particular Jim Irwin"
    )

    # Lista de personas (polimorfismo en acción)
    personas = [estudiante1, docente1]

    # Uso del mismo método para distintos objetos
    for persona in personas:
        print("----------------------------")
        print(persona.mostrar_datos())
