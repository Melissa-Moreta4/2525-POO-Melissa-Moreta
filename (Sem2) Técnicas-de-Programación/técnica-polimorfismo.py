#ejemplo de Polimorfismo.

class Animal:
    def _init_(self, nombre):
        self.nombre = nombre

    def hacer_ruido(self):
        print("Haciendo ruido")

class Perro(Animal):
    def _init_(self, nombre, raza):
        super()._init_(nombre)
        self.raza = raza

    def hacer_ruido(self):
        print("Guau!")

class Gato(Animal):
    def _init_(self, nombre, color):
        super()._init_(nombre)
        self.color = color

    def hacer_ruido(self):
        print("Miau!")

# El método hacer_ruido se implementa de manera diferente en cada clase
# (Perro y Gato), pero todos tienen la misma interfaz común (clase Animal).