#ejemplo de Encapsulación.

class CuentaBancaria:
    def _init_(self, saldo):
        self.__saldo = saldo  # Atributo privado con doble guion bajo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo

# La variable privada __saldo no puede ser accedida directamente,
# solo a través de los métodos depositar, retirar y consultar_saldo.