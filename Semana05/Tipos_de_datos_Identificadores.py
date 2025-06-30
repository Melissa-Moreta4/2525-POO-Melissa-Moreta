# Conversor de unidades de longitud: convierte entre metros, kilómetros y centímetros.
# Este programa permite al usuario ingresar una cantidad en una unidad de medida
# y luego seleccionar a qué otra unidad desea convertirla.

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """
    Convierte un valor de una unidad de longitud a otra.

    Parámetros:
        valor (float): cantidad a convertir
        unidad_origen (str): unidad de medida de origen ('m', 'km', 'cm')
        unidad_destino (str): unidad de medida de destino ('m', 'km', 'cm')

    Retorna:
        float: valor convertido
    """
    # Convertimos primero a metros
    if unidad_origen == 'km':
        valor_en_metros = valor * 1000
    elif unidad_origen == 'cm':
        valor_en_metros = valor / 100
    else:
        valor_en_metros = valor

    # Ahora convertimos desde metros a la unidad deseada
    if unidad_destino == 'km':
        return valor_en_metros / 1000
    elif unidad_destino == 'cm':
        return valor_en_metros * 100
    else:
        return valor_en_metros


# Inicio del programa
print("Conversor de unidades de longitud: metros, kilómetros y centímetros")

# Entrada de datos
cantidad_str = input("Ingresa la cantidad que deseas convertir: ")
unidad_origen = input("Ingresa la unidad de origen (m, km, cm): ").lower()
unidad_destino = input("Ingresa la unidad de destino (m, km, cm): ").lower()

# Conversión de entrada a tipo numérico
cantidad = float(cantidad_str)

# Validación de unidades válidas
unidades_validas = ['m', 'km', 'cm']
es_valido = unidad_origen in unidades_validas and unidad_destino in unidades_validas

# Booleano de control
conversion_exitosa = False

if es_valido:
    resultado = convertir_longitud(cantidad, unidad_origen, unidad_destino)
    print(f"{cantidad} {unidad_origen} equivalen a {resultado} {unidad_destino}.")
    conversion_exitosa = True
else:
    print("Error: unidad inválida. Usa únicamente 'm', 'km' o 'cm'.")

# Mostrar si la conversión se realizó exitosamente
print("¿La conversión fue exitosa?", conversion_exitosa)