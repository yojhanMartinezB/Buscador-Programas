
import pandas as pd


df = pd.read_csv("movilidad_candelaria.csv")


cadenas_corredores = (
    df["corredor"]
    .dropna()
    .astype(str)
    .str.strip()
)



corredores = sorted(
    cadenas_corredores.unique(),
    key=str.casefold
)


print("Total de registros:", len(df))
print("Cantidad de corredores únicos:", len(corredores))

print("\nPrimeros 20 corredores:")
for corredor in corredores[:20]:
    print(corredor)
