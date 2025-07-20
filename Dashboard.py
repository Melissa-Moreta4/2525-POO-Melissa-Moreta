import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"(Intentado abrir: {ruta_script_absoluta}") # Para depurar ruta
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            print("\n--- Resultado de la Ejecución ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Parcial 01/Semana 02/técnica-abstracción.py',
        '2': 'Parcial 01/Semana 02/técnica-encapsulamiento.py',
        '3': 'Parcial 01/Semana 02/técnica-herencia.py',
        '4': 'Parcial 01/Semana 02/técnica-polimorfismo.py',
        '5': 'Parcial 01/Semana 03/ej_programación_tradicional.py',
        '6': 'Parcial 01/Semana 03/ejemplo_con_POO.py',
        '7': 'Parcial 01/Semana 04/EjemplosMundoReal_POO.py',
        '8': 'Parcial 01/Semana 05/Tipos_de_datos_Identificadores.py',
        '9': 'Parcial 01/Semana 06/Tarea_aplicando_POO.py',
        '10': 'Parcial 01/Semana 07/Tarea_Constructores_y_Destructores.py'
    }

    while True:
        print("\nMenú Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            input("\nPresiona Enter para regresar al Menú Principal...")
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")

if __name__ == "__main__":
    mostrar_menu()