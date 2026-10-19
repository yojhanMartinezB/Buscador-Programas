#Bueno aqui si me medio quede perdido y hasta le tuve q pedir ayuda a la ia con que me creara un buscador porq no tenia ni pnshe idea de como
#crearlo xd y es que comparado con crear un diccionario o cadena que solo imprimia la primera tabla o renglon o lo que uno necesitaba aqui 
#directamente es buscar especiicamente algo lmao
import pandas as pd

df = pd.read_csv("movilidad_candelaria.csv", low_memory=False)


datos_por_corredor = {}

for _, fila in df.iterrows():
    nombre = str(fila["corredor"]).strip()

    if nombre and nombre.casefold() != "nan":
        datos_por_corredor.setdefault(nombre, []).append({
            "fecha": fila["fecha"],
            "hora": fila["hora"],
            "velocidad": fila["velocidad_km_h"],
            "intensidad": fila["intensidad"],
            "sentido": fila["sentido"]
        })


def buscar_prefijo(prefijo):
    prefijo = prefijo.strip().casefold()

    if not prefijo:
        return []

    return sorted(
        [
            nombre for nombre in datos_por_corredor
            if nombre.casefold().startswith(prefijo)
        ],
        key=str.casefold
    )


def mostrar_estadisticas(nombre):
    mediciones = datos_por_corredor[nombre]

    velocidades = [m["velocidad"] for m in mediciones]
    intensidades = [m["intensidad"] for m in mediciones]

    print(f"\nCorredor: {nombre}")
    print(f"Cantidad de mediciones: {len(mediciones)}")
    print(f"Velocidad promedio: {sum(velocidades) / len(velocidades):.2f} km/h")
    print(f"Intensidad promedio: {sum(intensidades) / len(intensidades):.2f}")
    print("\nPrimera medición:")
    print(mediciones[0])


while True:
    prefijo = input("\nPrefijo del corredor (o 'salir'): ").strip()

    if prefijo.casefold() == "salir":
        break

    resultados = buscar_prefijo(prefijo)

    if not resultados:
        print("No se encontraron corredores.")
        continue

    print("\nCorredores encontrados:")
    for i, nombre in enumerate(resultados, start=1):
        print(f"{i}. {nombre}")

    opcion = input(
        "\nEscribe el número del corredor para ver sus estadísticas "
        "o pulsa Enter para otra búsqueda: "
    ).strip()

    if opcion.isdigit():
        numero = int(opcion)

        if 1 <= numero <= len(resultados):
            mostrar_estadisticas(resultados[numero - 1])
        else:
            print("Número fuera del rango.")
