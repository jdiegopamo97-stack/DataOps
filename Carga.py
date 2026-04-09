import pandas as pd
from Transformación import transformacion
from Credenciales import conexion_repo_final

print("\nCARGA DE DATOS...")

df=transformacion()

def carga():
#   df.to_csv("Informe Final.csv", index=False)

    con=conexion_repo_final()

    df.to_sql(
        con=con,
        name="Datos_informe_final",
        if_exists="replace",
        index=False,
    )

    print("Datos guardados en Informe Final")


