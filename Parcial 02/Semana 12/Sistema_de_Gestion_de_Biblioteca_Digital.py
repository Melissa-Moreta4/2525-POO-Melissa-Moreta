"""Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar los libros disponibles,
las categorías de libros,los usuarios registrados y el historial de préstamos."""

# ______________________Sistema de Gestión de Biblioteca Digital_______________________

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tupla para título y autor (inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}            # Diccionario ISBN -> Libro
        self.usuarios = {}          # Diccionario ID -> Usuario
        self.ids_usuarios = set()   # Conjunto de IDs únicos

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró el libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("Ya existe un usuario con ese ID.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print("No existe un usuario con ese ID.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("El libro no está disponible.")
            return
        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # sacamos el libro del catálogo
        usuario.libros_prestados.append(libro)
        print(f"Se prestó el libro {libro.info[0]} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # regresa a la biblioteca
                print(f"Libro devuelto: {libro.info[0]} por {usuario.nombre}")
                return
        print("El usuario no tiene este libro prestado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")

# __________________PRUEBAS DEL SISTEMA__________________________

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros (ejemplo con los 5 que pediste)
libros = [
    Libro("Bajo la misma Estrella", "John Green", "Novela", "111"),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", "222"),
    Libro("Alicia en el país de las Maravillas", "Lewis Carroll", "Fantasía", "333"),
    Libro("En busca del tiempo perdido", "Marcel Proust", "Clásico", "444"),
    Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "555"),
]

# Añadir libros
for libro in libros:
    biblioteca.añadir_libro(libro)

# Registrar usuarios
u1 = Usuario("Meli", "U01")
u2 = Usuario("Carlos", "U02")
biblioteca.registrar_usuario(u1)
biblioteca.registrar_usuario(u2)

# Prestar libros
biblioteca.prestar_libro("U01", "111")
biblioteca.prestar_libro("U01", "222")
biblioteca.prestar_libro("U02", "333")

# Listar préstamos
biblioteca.listar_libros_prestados("U01")
biblioteca.listar_libros_prestados("U02")

# Devolver libro
biblioteca.devolver_libro("U01", "111")

# Buscar libros por título
resultados = biblioteca.buscar_libros("titulo", "principito")
print("\nResultado búsqueda por título:")
for r in resultados:
    print(r)