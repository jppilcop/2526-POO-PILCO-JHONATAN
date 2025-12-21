# Cálculo del promedio semanal del clima usando funciones

def ingresar_temperaturas():
    """
    Función que solicita al usuario las temperaturas diarias
    y las almacena en una lista
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal de temperaturas
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# ----- Programa principal -----
if __name__ == "__main__":
    print("Cálculo del promedio semanal del clima (Programación Tradicional)")

    temps = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temps)

    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")
