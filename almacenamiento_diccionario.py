
import pandas as pd


df = pd.read_csv("movilidad_candelaria.csv")


datos_por_corredor = {}

for _, fila in df.iterrows():
    corredor = str(fila["corredor"]).strip()

    if not corredor or corredor == "nan":
        continue

    if corredor not in datos_por_corredor:
        datos_por_corredor[corredor] = []

    
    medicion = {
        "fecha": fila["fecha"],
        "hora": fila["hora"],
        "velocidad_km_h": fila["velocidad_km_h"],
        "intensidad": fila["intensidad"],
        "sentido": fila["sentido"]
    }

    datos_por_corredor[corredor].append(medicion)


print("Cantidad de corredores:", len(datos_por_corredor))

for nombre, mediciones in list(datos_por_corredor.items())[:3]:
    print(f"\nCorredor: {nombre}")
    print("Cantidad de mediciones:", len(mediciones))
    print("Primera medición:", mediciones[0])
