
import pandas as pd

archivo = "velocidad_e_intensidad_vehicular_en_medellin (1).csv"


df = pd.read_csv(archivo, sep=None, engine="python", encoding="utf-8")

print(df.shape)

print(df.columns.tolist())


print(
    df["nombre_comuna"]
    .value_counts(dropna=False)
    .to_string()
)



df_candelaria = df[
    df["nombre_comuna"].str.strip().str.casefold()
    == "la candelaria".casefold()
].copy()

print("Registros originales:", len(df))
print("Registros de La Candelaria:", len(df_candelaria))


df_candelaria.to_csv(
    "movilidad_candelaria.csv",
    index=False,
    encoding="utf-8-sig"
)
