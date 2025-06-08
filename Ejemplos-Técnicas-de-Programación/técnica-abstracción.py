#ejemplo de Abstracción.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_ruido(self):
        pass

class Perro(Animal):
    def hacer_ruido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_ruido(self):
        print("Miau!")

# Con abstracción, la clase animal es una interfaz abstracta.
# y las clases concretas (perro y gato) implementan la funcionalidad.