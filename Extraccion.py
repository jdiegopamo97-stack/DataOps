import pandas as pd
import glob
from collections import defaultdict
from functools import reduce

#####EXTRACT

print("EXTRACCIÓN DE DATOS...")

path=r"C:\Users\Juan Diego\Downloads\Archivos Hayduk\*.csv"


def extract_from_csv(file_to_extract):
    Tabla = pd.read_csv(file_to_extract,sep=";")
    return Tabla

def extract():
    extracted_data=pd.DataFrame(columns=["Fecha"])
    dfs=[]
    for csv_file in glob.glob(path):
        dfs.append(extract_from_csv(csv_file))
    groups = defaultdict(list)
    for df in dfs:
        cols = tuple(sorted(df.columns))
        groups[cols].append(df)

    grouped_dfs = []
    for group in groups.values():
        combined = pd.concat(group, ignore_index=True)
        grouped_dfs.append(combined)

    extracted_data = reduce(
        lambda left, right: pd.merge(left, right, on="Fecha", how="outer"),
            grouped_dfs)

    return extracted_data

a=extract()




