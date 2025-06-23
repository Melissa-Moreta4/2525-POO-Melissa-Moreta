# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo      # Tipo: sencilla, doble, suite
        self.precio = precio  # Precio por noche
        self.disponible = True  # Estado de disponibilidad

    def mostrar_info(self):
        """Muestra la información de la habitación"""
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero} ({self.tipo}) - ${self.precio}/noche - {estado}")

    def reservar(self):
        """Cambia el estado de la habitación a ocupada"""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Libera la habitación"""
        self.disponible = True
        print(f"Habitación {self.numero} ha sido liberada.")


# Clase que representa a un huésped
class Huesped:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        print(f"Huésped: {self.nombre} - C.I.: {self.cedula}")


# Clase que representa el sistema de reservas del hotel
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []
        self.reservas = {}  # clave: número de habitación, valor: huésped

    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al sistema"""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print("\n--- Habitaciones disponibles ---")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                habitacion.mostrar_info()

    def hacer_reserva(self, numero_habitacion, huesped):
        """Reserva una habitación para un huésped"""
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.disponible:
                    habitacion.reservar()
                    self.reservas[numero_habitacion] = huesped
                    return
                else:
                    print("La habitación ya está ocupada.")
                    return
        print("Habitación no encontrada.")

    def mostrar_reservas(self):
        print("\n--- Reservas realizadas ---")
        for num, huesped in self.reservas.items():
            print(f"Habitación {num} reservada por {huesped.nombre}")


# --------------------- EJECUCIÓN DEL PROGRAMA ---------------------

# Crear el sistema de reservas
sistema = SistemaReservas()

# Crear habitaciones
h1 = Habitacion(101, "Sencilla", 65)
h2 = Habitacion(102, "Doble", 80)
h3 = Habitacion(103, "Suite", 125.08)

# Agregarlas al sistema
sistema.agregar_habitacion(h1)
sistema.agregar_habitacion(h2)
sistema.agregar_habitacion(h3)

# Mostrar habitaciones disponibles
sistema.mostrar_habitaciones_disponibles()

# Crear un huésped
cliente1 = Huesped("Iván Montero", "1807256836")

# Reservar una habitación
sistema.hacer_reserva(102, cliente1)

# Mostrar habitaciones disponibles nuevamente
sistema.mostrar_habitaciones_disponibles()

# Mostrar todas las reservas
sistema.mostrar_reservas()