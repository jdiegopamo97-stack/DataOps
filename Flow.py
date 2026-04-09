from prefect import Flow
from Extraccion import extract
from Transformacion import transformacion
from Carga import carga


@Flow
def proceso_etl():
    # Extraccion
    extract()

    # Transformación
    df = transformacion()

    # Carga
    carga()


proceso_etl()
