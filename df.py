import pandas as pd
import matplotlib.pyplot as plt

with open("datos.csv", "r") as r:
    lineas= r.readlines()


df = pd.read_csv("datos.csv", index_col="id")

#print(df.head(6)) #primero 6
#print(df.info()) #info general
#print(df.shape) #(filas, columns)
#print(df.isnull().sum()) #total null for row

#print(df.head(-5)) #muestra all menos las ultimas 5 filas
#print(df["edad"].unique()) #valores sin repeticion

#print(df[df["edad"]>=27]) #mascara boleanda en todo el dataset
#print(df.describe().T) #estadísticas automáticas
#print(df["fechas"].value_counts()) #total de repticiones por dato

#convierte str en date

df["fecha_upload"] = pd.to_datetime(
df["fechas"],
format= "%d/%m/%Y",
errors="coerce"
)
#print(df["fecha_upload"])

#print(df.loc[df["ciudad"]=="Arequipa", ["fecha_upload"]].agg(["min","max"])) #.loc[FILAS ,COLUMNAS] y .agg([definimos que operacion solicitar])

##print(df.axes) #devulve filas y cpolumnas
df["fechas"]= df["fechas"].str.strip()
fechas_vacias=df[df["fechas"].isnull()]
print(fechas_vacias)
"""
data_with_default_notes["notes"].fillna(
    value="no notes at all",
    inplace=True)
"""
