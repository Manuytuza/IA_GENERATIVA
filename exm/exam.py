# ==========================================================
# GUÍA COMPLETA PYTHON + NUMPY + PANDAS + GRÁFICOS
# ==========================================================
# TEMAS:
# 1. Abrir archivos TXT
# 2. Abrir archivos CSV
# 3. Abrir archivos JSON
# 4. Fundamentos de NumPy
# 5. Fundamentos de Pandas
# 6. DataFrames
# 7. Limpieza de datos
# 8. Funciones principales
# 9. GroupBy
# 10. Merge
# 11. Generación de gráficos
# ==========================================================


# ==========================================================
# IMPORTAR LIBRERÍAS
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


# ==========================================================
# 1. ABRIR ARCHIVO TXT
# ==========================================================

# Abrir archivo en modo lectura
archivo_txt = open("datos.txt", "r")

# Leer contenido completo
contenido = archivo_txt.read()

# Mostrar contenido
print("CONTENIDO TXT:")
print(contenido)

# Cerrar archivo
archivo_txt.close()


# ==========================================================
# 2. LEER ARCHIVO CSV
# ==========================================================

# Leer archivo CSV
df_csv = pd.read_csv("ventas.csv")

# Mostrar primeras filas
print("\nPRIMERAS FILAS CSV:")
print(df_csv.head())

# Información general
print("\nINFORMACIÓN CSV:")
print(df_csv.info())

# Estadísticas
print("\nESTADÍSTICAS CSV:")
print(df_csv.describe())


# ==========================================================
# 3. LEER ARCHIVO JSON
# ==========================================================

# Abrir JSON
with open("datos.json", "r") as archivo_json:

    datos_json = json.load(archivo_json)

# Mostrar contenido JSON
print("\nCONTENIDO JSON:")
print(datos_json)

# Convertir JSON a DataFrame
df_json = pd.DataFrame(datos_json)

print("\nDATAFRAME DESDE JSON:")
print(df_json)


# ==========================================================
# 4. FUNDAMENTOS DE NUMPY
# ==========================================================

# Crear array
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


# ==========================================================
# MATRICES NUMPY
# ==========================================================

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMATRIZ:")
print(matriz)

# Crear matriz de ceros
print("\nMATRIZ CEROS:")
print(np.zeros((3, 3)))

# Crear matriz de unos
print("\nMATRIZ UNOS:")
print(np.ones((2, 2)))


# ==========================================================
# 5. FUNDAMENTOS DE PANDAS
# ==========================================================

# Crear Series
serie = pd.Series([100, 200, 300, 400])

print("\nSERIES:")
print(serie)


# ==========================================================
# 6. CREAR DATAFRAME
# ==========================================================

datos = {

    "Nombre": [
        "Ana",
        "Luis",
        "Carlos",
        "María"
    ],

    "Edad": [
        23,
        30,
        28,
        np.nan
    ],

    "Ciudad": [
        "Arequipa",
        "Lima",
        "Cusco",
        "Tacna"
    ],

    "Ventas": [
        100,
        200,
        150,
        300
    ]
}

df = pd.DataFrame(datos)
df.to_csv("datos.csv", index=False)
print("\nDATAFRAME:")
print(df)


# ==========================================================
# ESTRUCTURA DEL DATAFRAME
# ==========================================================

# Ver columnas
print("\nCOLUMNAS:")


# Ver índices
print("\nÍNDICES:")
print(df.index)

# Tipos de datos
print("\nTIPOS DE DATOS:")
print(df.dtypes)

# Información general
print("\nINFO GENERAL:")
print(df.info())

#(filas, columnas)
print(df.shape)

# ==========================================================
# 7. SELECCIÓN DE DATOS
# ==========================================================

# Seleccionar una columna
print("\nCOLUMNA NOMBRE:")
print(df["Nombre"])

# Seleccionar varias columnas
print("\nNOMBRE Y EDAD:")
print(df[["Nombre", "Edad"]])

# Seleccionar fila por índice
print("\nPRIMERA FILA:")
print(df.iloc[0])


# ==========================================================
# 8. FILTRAR DATOS
# ==========================================================

# Filtrar ventas mayores a 150
filtro = df[df["Ventas"] > 150]

print("\nFILTRAR VENTAS > 150:")
print(filtro)


# ==========================================================
# 9. DATOS VACÍOS
# ==========================================================

# Detectar vacíos
print("\nDETECTAR VACÍOS:")
print(df.isnull()) 

# Contar vacíos
print("\nCONTAR VACÍOS:")
print(df.isnull().sum())

# Reemplazar vacíos
df["Edad"] = df["Edad"].fillna(0)

print("\nREEMPLAZAR VACÍOS:")
print(df)


# ==========================================================
# 10. FUNCIONES PRINCIPALES
# ==========================================================

# Promedio
print("\nPROMEDIO VENTAS:")
print(df["Ventas"].mean())

# Máximo
print("\nMÁXIMO:")
print(df["Ventas"].max())

# Mínimo
print("\nMÍNIMO:")
print(df["Ventas"].min())

# Suma
print("\nSUMA:")
print(df["Ventas"].sum())

# Contar registros
print("\nCANTIDAD REGISTROS:")
print(df["Ventas"].count())


# ==========================================================
# 11. ORDENAR DATOS
# ==========================================================

ordenado = df.sort_values("Ventas")

print("\nORDENADO:")
print(ordenado)


# ==========================================================
# 12. CREAR NUEVAS COLUMNAS
# ==========================================================

# Crear columna IGV
df["IGV"] = df["Ventas"] * 0.18

print("\nNUEVA COLUMNA IGV:")
print(df)


# ==========================================================
# 13. GROUPBY
# ==========================================================

grupo = df.groupby("Ciudad")["Ventas"].sum()

print("\nGROUPBY CIUDAD:")
print(grupo)


# ==========================================================
# 14. MERGE DE TABLAS
# ==========================================================

clientes = pd.DataFrame({

    "ID": [1, 2, 3],

    "Cliente": [
        "Ana",
        "Luis",
        "Carlos"
    ]
})

compras = pd.DataFrame({

    "ID": [1, 2, 3],

    "Compra": [
        500,
        800,
        300
    ]
})

resultado_merge = pd.merge(
    clientes,
    compras,
    on="ID"
)

print("\nMERGE:")
print(resultado_merge)


# ==========================================================
# 15. EXPORTAR ARCHIVOS
# ==========================================================

# Exportar CSV
df.to_csv("resultado.csv", index=False)

# Exportar Excel
df.to_excel("resultado.xlsx", index=False)


# ==========================================================
# 16. GRÁFICO DE LÍNEAS
# ==========================================================

df.plot(
    x="Nombre",
    y="Ventas",
    kind="line"
)

plt.title("GRÁFICO DE LÍNEAS")
plt.xlabel("Nombre")
plt.ylabel("Ventas")

plt.show()


# ==========================================================
# 17. GRÁFICO DE BARRAS
# ==========================================================

df.plot(
    x="Nombre",
    y="Ventas",
    kind="bar"
)

plt.title("GRÁFICO DE BARRAS")
plt.xlabel("Nombre")
plt.ylabel("Ventas")

plt.show()


# ==========================================================
# 18. GRÁFICO DE TORTA
# ==========================================================

df.plot(
    kind="pie",
    y="Ventas",
    labels=df["Nombre"],
    autopct="%1.1f%%"
)

plt.title("GRÁFICO DE TORTA")

plt.show()


# ==========================================================
# 19. HISTOGRAMA
# ==========================================================

df["Ventas"].plot(
    kind="hist"
)

plt.title("HISTOGRAMA")

plt.show()


# ==========================================================
# 20. SCATTER / DISPERSIÓN
# ==========================================================

df.plot(
    kind="scatter",
    x="Edad",
    y="Ventas"
)

plt.title("GRÁFICO DISPERSIÓN")

plt.show()


# ==========================================================
# FIN DEL PROGRAMA
# ==========================================================

print("\nPROCESO TERMINADO")