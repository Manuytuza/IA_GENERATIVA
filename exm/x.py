
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
#df = pd.DataFrame(datos) 
df = pd.read_csv("datos.csv")
# Información general
#print(df.columns)
print("\nINFO GENERAL:")
print(df.info()) 
#(filas, columnas)
print(df.shape)

# Seleccionar fila por índice
print("\nPRIMERA FILA:")
print(df.iloc[0]) 
# df.iloc[fila, columna]
# mascara boleana = Filtrar ventas mayores a 150
filtro = df[df["Ventas"] > 150] 
print(filtro)
# Contar vacíos
print(df.isnull().sum())
# Reemplazar vacíos por (0)
df["Edad"] = df["Edad"].fillna(0)

#ordenar sort_value("segun_esto")
ordenado = df.sort_values("Ventas")
#crear new column 
df["IGV"] = df["Ventas"] * 0.18
print(df)

#df.groupby("columna_a_agrupar")["columna_operacion"].funcion()
groupby_pd = df.groupby("Ciudad")["Ventas"].agg(["sum", "mean", "max"])
print(groupby_pd)

# Exportar CSV
df.to_csv("resultado.csv", index=False)

# DataFrame completo
df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr"],
    "Ciudad": ["Lima", "Lima", "Cusco", "Arequipa"],
    "Nombre": ["Ana", "Luis", "Carlos", "Maria"],
    "Ventas": [100, 200, 150, 250],
    "Gastos": [80, 120, 90, 140]
})

grupo = df.groupby("Ciudad")["Ventas"].sum()
# Crear una sola figura con espacios
fig, axs = plt.subplots(3, 2, figsize=(12,10))
# LINEA
df.plot(
    x="Mes",
    y="Ventas",
    kind="line",
    ax=axs[0,0],
    title="line"
)

# BARRAS
df.plot(
    x="Mes",
    y="Ventas",
    kind="bar",
    ax=axs[0,1],
    title="bar"
)

"""
plt.title("GRÁFICO DE BARRAS")
plt.xlabel("Nombre")
plt.ylabel("Ventas")
"""
# HISTOGRAMA
df["Ventas"].plot(
    kind="hist",
    ax=axs[1,0],
    title="histograma"
)
# SCATTER
df.plot(
    kind="scatter",
    x="Ventas",
    y="Gastos",
    ax=axs[1,1],
    title="scatter"
)
# PIE
grupo.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=axs[2,0],
    title="pie grafic"
)
# Espacio vacío
axs[2,1].axis("off")

plt.tight_layout() #ordena graficos evita que se sobrepongan
fig.suptitle("Todos los gráficos\n")
fig.subplots_adjust(top=0.90)#separa titulos de grafics
plt.show()