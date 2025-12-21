# Cálculo del promedio semanal del clima usando clases

class Clima:
    """
    Clase que representa el clima semanal
    Aplica encapsulamiento al manejar los datos internamente
    """
    def __init__(self):
        self._temperaturas = []  # atributo protegido

    def ingresar_temperatura(self, temperatura):
        """
        Método para agregar una temperatura diaria
        """
        self._temperaturas.append(temperatura)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal
        """
        return sum(self._temperaturas) / len(self._temperaturas)


# ----- Uso de la clase -----
if __name__ == "__main__":
    print("Cálculo del promedio semanal del clima (POO)")

    clima_semanal = Clima()

    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        clima_semanal.ingresar_temperatura(temp)

    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
