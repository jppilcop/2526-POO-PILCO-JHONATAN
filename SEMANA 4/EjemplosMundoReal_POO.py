# Contexto: Sistema educativo para la gestión de estudiantes y cursos

class Estudiante:
    """
    Clase que representa a un estudiante
    """
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)
        print(f"{self.nombre} se ha inscrito en el curso {curso.nombre}")

    def mostrar_cursos(self):
        print(f"Cursos de {self.nombre}:")
        for curso in self.cursos:
            print(f"- {curso.nombre}")


class Curso:
    """
    Clase que representa un curso académico
    """
    def __init__(self, nombre, docente):
        self.nombre = nombre
        self.docente = docente
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} agregado al curso {self.nombre}")

    def mostrar_estudiantes(self):
        print(f"Estudiantes inscritos en {self.nombre}:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")


class Docente:
    """
    Clase que representa a un docente
    """
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def mostrar_info(self):
        return f"Docente: {self.nombre}, Área: {self.area}"


# ----- Uso del sistema -----
if __name__ == "__main__":
    docente1 = Docente("Paúl Pilco", "Matemáticas")

    curso1 = Curso("Álgebra", docente1)
    curso2 = Curso("Programación", docente1)

    estudiante1 = Estudiante("Byron Ruiz", "A001")
    estudiante2 = Estudiante("Ariel Zela", "A002")

    curso1.agregar_estudiante(estudiante1)
    curso1.agregar_estudiante(estudiante2)

    estudiante1.inscribirse(curso1)
    estudiante1.inscribirse(curso2)

    curso1.mostrar_estudiantes()
    estudiante1.mostrar_cursos()
