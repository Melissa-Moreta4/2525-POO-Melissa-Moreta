#ejemplo de Herencia.

class Animal:
    def _init_(self, nombre):
        self.nombre = nombre

    def hacer_ruido(self):
        print("Haciendo ruido de animal")

class Perro(Animal):
    def _init_(self, nombre, raza):
        super()._init_(nombre)  # Llama al constructor de la clase padre
        self.raza = raza

    def hacer_ruido(self):
        print("Guau!")

# La clase Perro hereda el atributo nombre y el método hacer_ruido de la clase Animal,
# y también define sus propios atributos y métodos.