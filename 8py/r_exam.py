import csv

# ── LEER ─────────────────────────────────────────────────────────────
with open("archivo.csv", "r") as f:
    for linea in f:               # opción 1: línea a línea
        print(linea, end='')

with open("archivo.csv", "r") as f:
    reader = csv.reader(f)        # opción 2: csv.reader → da listas
    for fila in reader:
        print(fila)               # ['col1', 'col2', ...]

# ── AGREGAR FILAS (append) ────────────────────────────────────────────
nuevas = [
    "1,Juan,30,Lima",
    "2,Maria,25,Cusco",
]
with open("archivo.csv", "a") as f:
    for linea in nuevas:
        f.write(linea + "\n")     # ← LA MÁS LIMPIA y fácil de recordar

# con csv.writer (más robusto si hay comas en los datos)
filas = [
    ["1", "Juan", "30", "Lima"],
    ["2", "Maria", "25", "Cusco"],
]
with open("archivo.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(filas)       # writerows = toda la lista de golpe

import pandas as pd

df = pd.read_csv("archivo.csv")
df = pd.read_csv("archivo.csv", index_col=0)   # si hay columna índice duplicada

# ── VER DATOS ─────────────────────────────────────────────────────────
df.head(5)           # primeras 5
df.tail(15)          # últimas 15  ← pregunta P2.1
df[-15:]             # mismo resultado
df.shape             # (filas, columnas)  ← pregunta P2.2
filas, columnas = df.shape

# ── ELIMINAR COLUMNA ──────────────────────────────────────────────────
df.drop(columns='Unnamed: 0', inplace=True)   # ← pregunta P2.3
# o al cargar:
df = pd.read_csv("archivo.csv", index_col='Unnamed: 0')

# ── FILTRAR + CALCULAR ────────────────────────────────────────────────
# Patrón: df.loc[CONDICIÓN, 'columna'].operacion()
df.loc[df['sex'] == 'Male', 'age'].mean()        # ← pregunta P2.4

# Alternativa con []  (también válida)
df[df['sex'] == 'Male']['age'].mean()

# ── CONTAR ELEMENTOS QUE CUMPLEN CONDICIÓN ───────────────────────────
# Truco: sumar máscara booleana (True=1, False=0)
(df['native-country'] == 'Cuba').sum()           # ← pregunta P2.5
# o con len():
len(df.loc[df['native-country'] == 'Cuba'])

# Calcular porcentaje con 2 decimales:
porc = (num / len(df)) * 100
print(f"El porcentaje es: {round(porc, 2)} %")

# ── AGRUPAR Y COMPARAR GRUPOS ─────────────────────────────────────────
# Patrón 1: filtrar → .mean()
grupo_a = df.loc[df['salary'] == '<=50K', 'age'].mean()   # ← pregunta P2.6
grupo_b = df.loc[df['salary'] == '>50K', 'age'].mean()

# Patrón 2: groupby (más compacto)
df.groupby('salary')['age'].mean().round(2)

# ── CONTAR POR CATEGORÍA (para gráficos) ─────────────────────────────
df['salary'].value_counts()                # ← pregunta PE1
df.groupby('salary')['age'].count()        # equivalente

import matplotlib.pyplot as plt

serie = df['salary'].value_counts()

serie.plot.pie()              # gráfico de pie  ← pregunta PE1
serie.plot(kind='pie')        # equivalente
serie.plot(kind='bar')        # barras
serie.plot(kind='line')       # línea

plt.show()

import numpy as np

# Simular moneda con probabilidad 70% cara ← pregunta PE2
moneda = np.random.choice([1, 0], size=50, p=[0.7, 0.3])

# Alternativa manual (la del examen):
import random
valores = [1,1,1,1,1,1,1,0,0,0]   # 7 caras, 3 sellos
resultados = [valores[random.randint(0,9)] for _ in range(50)]

# Graficar con matplotlib
plt.plot(moneda)
plt.show()

# Verificar si un número es primo
def es_primo(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    # all() → True si TODOS los elementos son True

# Primos de Mersenne: números de la forma 2^p - 1
# donde tanto el número como p son primos
for p in range(2, 20):
    if es_primo(p):
        m = 2**p - 1
        if es_primo(m):
            print(m)   # → 3, 7, 31 (los únicos menores de 100)

# =============================================================================
# RESUMEN ULTRA-RÁPIDO — PATRONES CLAVE DEL EXAMEN
# =============================================================================
 
# PATRÓN 1: Abrir y agregar filas a CSV sin Pandas
# with open("f.csv", "a") as f:
#     for linea in lista_de_strings:
#         f.write(linea + "\n")
 
# PATRÓN 2: Cargar y eliminar columna índice
# df = pd.read_csv("f.csv", index_col=0)
 
# PATRÓN 3: Ver últimas N filas
# df.tail(N)  o  df[-N:]
 
# PATRÓN 4: Tamaño del dataframe
# filas, columnas = df.shape
 
# PATRÓN 5: Filtrar + calcular  ← EL MÁS IMPORTANTE
# df.loc[df['col'] == 'valor', 'otra_col'].mean()
# df.loc[df['col'] == 'valor', 'otra_col'].sum()
# df.loc[df['col'] == 'valor', 'otra_col'].count()
 
# PATRÓN 6: Contar cuántos cumplen condición  ← TRUCO MÁS CORTO
# (df['col'] == 'valor').sum()   # True=1, False=0
 
# PATRÓN 7: Porcentaje con 2 decimales
# round((n / len(df)) * 100, 2)
# f"{valor:.2f} %"
 
# PATRÓN 8: Comparar grupos (una línea)
# df.groupby('col_grupo')['col_valor'].mean().round(2)
 
# PATRÓN 9: Gráfico de pie desde value_counts
# df['col'].value_counts().plot.pie()
# plt.show()
 
# PATRÓN 10: Verificar si es primo
# n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
