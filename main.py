import pandas as pd

#####EXTRACT

print("EXTRACCIÓN DE DATOS...")

captura = pd.read_csv("datos_captura.csv", sep=";")
sensores = pd.read_csv("datos_sensores.csv",sep=";")

print("Datos de captura:")
print(captura.head())

print("Datos de sensores:")
print(sensores.head())


####TRANSFORM

print("\nTRANSFORMACIÓN DE DATOS...")

# Unir datasets
df = pd.merge(captura, sensores, on="Fecha", how="left")

# Eliminar duplicados
df = df.drop_duplicates()

# Manejo de nulos
df["Temperatura"] = df["Temperatura"].fillna(df["Temperatura"].mean())

# Convertir fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Estandarizar texto
df["Especie"] = df["Especie"].str.upper()

# Convertir a toneladas
df["Toneladas"] = df["Toneladas"] / 1000

print("\nDatos transformados:")
print(df)


####LOAD

print("\nCARGA DE DATOS...")

df.to_csv("Informe Final.csv", index=False)

print("Datos guardados en Informe Final.csv")
