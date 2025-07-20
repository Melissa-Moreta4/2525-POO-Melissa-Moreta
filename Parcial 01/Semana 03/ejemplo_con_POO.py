class ClimaDiario:
    """
    Clase para almacenar y calcular el promedio semanal de datos del clima.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase ClimaDiario.
        """
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """
        Ingresa una temperatura diaria.

        Args:
            temperatura (float): La temperatura a ingresar.
        """
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de las temperaturas ingresadas.

        Returns:
            float: El promedio semanal de las temperaturas, o None si no hay datos.
        """
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_datos(self):
        """
        Muestra las temperaturas ingresadas y el promedio semanal.
        """
        print("Temperaturas ingresadas:", self.temperaturas)
        promedio = self.calcular_promedio_semanal()
        if promedio is not None:
            print("Promedio semanal:", promedio)
        else:
            print("No hay datos para calcular el promedio.")

if __name__ == '__main__':
    # Crear una instancia de la clase ClimaDiario
    clima = ClimaDiario()

    # Ingresar datos del clima para una semana
    clima.ingresar_temperatura(28.5)
    clima.ingresar_temperatura(29.0)
    clima.ingresar_temperatura(30.8)
    clima.ingresar_temperatura(32.9)
    clima.ingresar_temperatura(29.1)
    clima.ingresar_temperatura(31.5)
    clima.ingresar_temperatura(33.3)

    # Mostrar los datos y el promedio
    clima.mostrar_datos()