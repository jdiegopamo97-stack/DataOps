import pandas as pd
from Extraccion import extract

print("\nTRANSFORMACIÓN DE DATOS...")

data = extract()

def transformacion():

    # Eliminar duplicados
    df = data.drop_duplicates()

    # Manejo de nulos
    df["Temperatura"] = df["Temperatura"].fillna(df["Temperatura"].mean())

    # Convertir fecha
    df["Fecha"] = pd.to_datetime(df["Fecha"],format="%d/%m/%Y").dt.date

    # Estandarizar texto
    df["Especie"] = df["Especie"].astype(str).str.upper()

    # Convertir a toneladas
    df["Toneladas"] = df["Toneladas"] / 1000

    df.sort_values("Fecha", inplace=True)

    return df

print("Transformacion completa")

