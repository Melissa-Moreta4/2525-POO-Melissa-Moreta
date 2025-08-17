#Tarea: Sistema de Gestión de Inventarios
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.cantidad = nueva_cantidad
                print("Cantidad actualizada.")
                return
        print("Producto no encontrado.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.precio = nuevo_precio
                print("Precio actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("Inventario actual:")
            for p in self.productos:
                print(p)

# ------------------- MENÚ INTERACTIVO -------------------
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
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)

        elif opcion == "4":
            id_producto = input("Ingrese ID del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_precio(id_producto, nuevo_precio)

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