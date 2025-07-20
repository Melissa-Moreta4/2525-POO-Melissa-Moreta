# Programa sobre vehículos motorizados que implementa:
# Herencia, encapsulamiento y polimorfismo usando Programación Orientada a Objetos (POO)

class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__kilometraje = kilometraje  # Encapsulado (privado)

    def obtener_kilometraje(self):
        return self.__kilometraje

    def mostrar_info(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, kilometraje, puertas):
        super().__init__(marca, modelo, anio, kilometraje)
        self.puertas = puertas

    def mostrar_info(self):
        return f"Automóvil: {self.marca} {self.modelo}, {self.puertas} puertas, Año: {self.anio}, Km: {self.obtener_kilometraje()}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, kilometraje, tipo_motor):
        super().__init__(marca, modelo, anio, kilometraje)
        self.tipo_motor = tipo_motor

    def mostrar_info(self):
        return f"Motocicleta: {self.marca} {self.modelo}, Motor: {self.tipo_motor}, Año: {self.anio}, Km: {self.obtener_kilometraje()}"


# Crear objetos (instancias)
auto = Automovil("Chevrolet", "Cruze", 2022, 35000, 4)
moto = Motocicleta("Suzuki", "Hayabusa", 2023, 10000, "1340cc")

# Polimorfismo: ambos tienen el método mostrar_info
print(auto.mostrar_info())
print(moto.mostrar_info())

# Acceso al atributo encapsulado mediante método
print("Kilometraje automóvil:", auto.obtener_kilometraje(), "km")
print("Kilometraje motocicleta:", moto.obtener_kilometraje(), "km")

