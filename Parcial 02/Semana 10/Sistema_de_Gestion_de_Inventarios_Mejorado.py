import os
                                    # Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_line(self):
        """Convierte el producto a una línea de texto para guardar en archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    def from_line(line):
        """Crea un objeto Producto desde una línea de archivo."""
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None

# Clase Inventario con archivo y diccionario
class Inventario:
    def __init__(self, archivo="Inventario.txt"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: Producto}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga inventario desde el archivo."""
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            return
        try:
            with open(self.archivo, "r") as f:
                for line in f:
                    producto = Producto.from_line(line)
                    if producto:
                        self.productos[producto.id_producto] = producto
            print("Inventario cargado correctamente desde archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al leer archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
            print("Inventario guardado en archivo.")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al escribir archivo: {e}")

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID ya existe.")
            return
        self.productos[producto.id_producto] = producto
        print("Producto añadido correctamente.")
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            print("Cantidad actualizada.")
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].precio = nuevo_precio
            print("Precio actualizado.")
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("Inventario actual:")
            for p in self.productos.values():
                print(p)

def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Cantidad debe ser número entero y precio un número decimal.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto: ")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                inventario.actualizar_cantidad(id_producto, nueva_cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "4":
            id_producto = input("Ingrese ID del producto: ")
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                inventario.actualizar_precio(id_producto, nuevo_precio)
            except ValueError:
                print("Error: El precio debe ser un número decimal.")

        elif opcion == "5":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "6":
            inventario.mostrar_productos()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()