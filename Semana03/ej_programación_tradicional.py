#calcular la temperatura promedio de cada semana
def _temperaturas_(calculo_temperaturas):
    las_temperaturas_promedio = {}

    for semana, temperaturas in calculo_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        las_temperaturas_promedio[semana] = promedio

    return las_temperaturas_promedio

"""Se ejecuta una suma de las temperaturas semanales y se divide para el
número (4) de temperaturas que consta cada una"""

# Listado de las semanas con sus temperaturas
calculo_temperaturas = {
    "Semana1" : [36.57, 37.86, 32.71, 36.29],
    "Semana2" : [35.86, 40.57, 44.29, 34.57],
    "Semana3" : [28.86, 39.43, 41.29, 36.57]
}

# llamar a la función y posterior calcular sus temperaturas
calcular_temperaturas_ = _temperaturas_(calculo_temperaturas)

# Resultados en general
print("El promedio de temperaturas semanales:")
for semana, promedio in calcular_temperaturas_.items():
    print(f"{semana}: {promedio:.2f}°C")