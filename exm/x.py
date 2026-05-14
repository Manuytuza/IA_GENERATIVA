
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

df_csv = pd.read_csv("ventas.csv")

# Mostrar primeras filas
print(df_csv.head()) 

# Información general
print(df_csv.info())

# Estadísticas
print(df_csv.describe())

#-------------------------------------------

# Abrir JSON
with open("datos.json", "r") as archivo_json:

    datos_json = json.load(archivo_json)

# Mostrar contenido JSON
print("\nCONTENIDO JSON:")
print(datos_json)

# Convertir JSON a DataFrame
df_json = pd.DataFrame(datos_json)

#-------------------------------------------------
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nARRAY NUMPY:")
print(matriz)

# Operaciones matemáticas
print("\nSUMA:")
print(np.sum(matriz))

print("\nPROMEDIO:")
print(np.mean(matriz))

print("\nMÁXIMO:")
print(np.max(matriz))

print("\nMÍNIMO:")
print(np.min(matriz))

###---------------------------------------
df = pd.DataFrame(datos) 
# Información general
#print(df.columns)
print("\nINFO GENERAL:")
print(df.info()) 
# Seleccionar fila por índice
print("\nPRIMERA FILA:")
print(df.iloc[0]) 
# df.iloc[fila, columna]
# Filtrar ventas mayores a 150
filtro = df[df["Ventas"] > 150] 