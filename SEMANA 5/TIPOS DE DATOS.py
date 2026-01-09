""" Registro de estudiante y cálculo de su promedio en la materia de MATEMÁTICA
Descripción: Este programa solicita datos básicos de un estudiante,
calcula el promedio de dos calificaciones y determina si está aprobado.
Autor: Estudiante
"""

def calcular_promedio(nota1, nota2):
    """
    Calcula el promedio de dos notas.
    """
    promedio = (nota1 + nota2) / 2
    return promedio


def determinar_aprobacion(promedio):
    """
    Determina si el estudiante está aprobado.
    """
    aprobado = promedio >= 7
    return aprobado


def main():
    # Entrada de datos
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    edad_estudiante = int(input("Ingrese la edad del estudiante: "))
    nota_parcial_1 = float(input("Ingrese la primera nota: "))
    nota_parcial_2 = float(input("Ingrese la segunda nota: "))

    # Procesamiento
    promedio_final = calcular_promedio(nota_parcial_1, nota_parcial_2)
    esta_aprobado = determinar_aprobacion(promedio_final)

    # Salida de resultados
    print("\n--- RESULTADOS ---")
    print(f"Estudiante: {nombre_estudiante}")
    print(f"Edad: {edad_estudiante} años")
    print(f"Promedio final: {promedio_final:.2f}")

    if esta_aprobado:
        print("Estado: APROBADO ")
    else:
        print("Estado: REPROBADO ")


# Ejecución del programa
main()
