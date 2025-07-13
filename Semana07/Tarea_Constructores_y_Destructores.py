class Boutique:
    """
    Clase que representa una boutique de ropa.
    Utilizando el método constructor (__init__) y destructor (__del__).
    """

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.ropa_disponible = []
        print(f"La boutique '{self.nombre}' ha sido inaugurada en {self.direccion}.")

    def agregar_ropa(self, prenda):
        self.ropa_disponible.append(prenda)
        print(f"Se ha agregado la prenda: {prenda}")

    def mostrar_inventario(self):
        if self.ropa_disponible:
            print(f"Inventario de '{self.nombre}':")
            for prenda in self.ropa_disponible:
                print(f"- {prenda}")
        else:
            print("La boutique aún no tiene prendas disponibles.")

    def __del__(self):
        print(f"La boutique '{self.nombre}' ha cerrado sus puertas.")

# PROGRAMA PRINCIPAL DE EJECUCIÓN ************

# Crear una boutique
mi_boutique = Boutique("Moda Lilly's", "Av. Jorge Añasco 73")

# Agregar prendas
mi_boutique.agregar_ropa("Vestido de verano")
mi_boutique.agregar_ropa("Pantalón de mezclilla")
mi_boutique.agregar_ropa("Blusa elegante")

# Mostrar el inventario
mi_boutique.mostrar_inventario()

# Eliminar el objeto boutique (simula cierre del local)
del mi_boutique