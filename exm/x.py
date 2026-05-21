import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

df_csv = pd.read_csv("ventas.csv")

# Mostrar primeras filas
print(df_csv.head()) #columnas, non-null, type columns
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
df = pd.read_csv("datos.csv") #cargar csv
# Información general
#print(df.columns)
print("\nINFO GENERAL:")
print(df.info()) #columnas, non-null, type columns
#(filas, columnas)
print(df.shape)

# Seleccionar fila por índice
print("\nPRIMERA FILA:")
print(df.iloc[0]) 
# df.iloc[fila, columna]
# mascara boleana = Filtrar ventas mayores a 150
filtro = df[df["Ventas"] > 150] #boolean masc
print(filtro)
# Contar vacíos
print(df.isnull().sum()) #sum of nulls for columns
# Reemplazar vacíos por (0)
df["Edad"] = df["Edad"].fillna(0) #change nan for (x)

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
    title="histograma",
    grid=True,
    xlabel="hola_horizontal",
    ylabel="vertical",
)
# SCATTER
df.plot(
    kind="scatter",
    x="Ventas",
    y="Gastos",
    ax=axs[1,1],
    title="scatter",
    grid=True,
    xlabel="hola_horizontal",
    ylabel="vertical",
)
# PIE
grupo.plot(
    kind="pie", 
    autopct="%1.1f%%",
    ax=axs[2,0],
    title="pie grafic",
)
# Dtermina el Espacio vacío en fig, axs
axs[2,1].axis("off")

plt.tight_layout() #ordena graficos evita que se sobrepongan
fig.suptitle("Todos los gráficos\n")
fig.subplots_adjust(top=0.90)#separa titulos de grafics
plt.show() 
"""
df["New"] = np.where(
    df["Ventas"] != 0,
    df["Edad"] / df["Ventas"],
    0
)
np.where(condición, valor_si_true, valor_si_false)
"""
# ==============================
# RESUMEN RÁPIDO SEABORN (sns)
# ==============================

# IMPORTS
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# DATASET
# ------------------------------

tips = sns.load_dataset("tips")
# ver datos
tips.head()
# columnas
tips.columns
# info
tips.info()
#Ver todos los datasets de seaborn
print(sns.get_dataset_names())

# ==============================
# GRÁFICOS PRINCIPALES
# ==============================
# --------------------------------
# 1. SCATTERPLOT
# relación entre 2 variables
# --------------------------------
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)
plt.show()
# --------------------------------
# 2. LINEPLOT
# líneas / tendencias
# --------------------------------
sns.lineplot(
    data=tips,
    x="size",
    y="tip"
)
plt.show()
# --------------------------------
# 3. BARPLOT
# categorías vs promedio
# --------------------------------
sns.barplot(
    data=tips,
    x="day",
    y="total_bill"
)
plt.show()
# --------------------------------
# 4. HISTPLOT
# distribución
# --------------------------------
sns.histplot(
    data=tips,
    x="total_bill",
    bins=10
)
plt.show()
# --------------------------------
# 5. BOXPLOT
# cuartiles y outliers
# --------------------------------
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)
plt.show()
# --------------------------------
# 6. VIOLINPLOT
# distribución avanzada
# --------------------------------
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill"
)
plt.show()
# --------------------------------
# 7. COUNTPLOT
# contar categorías
# --------------------------------
sns.countplot(
    data=tips,
    x="day"
)
plt.show()
# --------------------------------
# 8. HEATMAP
# matriz de correlación
# --------------------------------
corr = tips.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True
)
plt.show()
# ==============================
# PARÁMETROS IMPORTANTES
# ==============================
# hue     -> color por categoría
# style   -> estilo
# bins    -> divisiones histograma
# palette -> colores
# annot   -> mostrar números
# figsize -> tamaño figura
# ==============================
# FIG Y AXS
# ==============================
fig, axs = plt.subplots(1, 2)
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    ax=axs[0]
)
sns.histplot(
    data=tips,
    x="total_bill",
    ax=axs[1]
)
plt.tight_layout()
plt.show()
# ==============================
# ESTILOS
# ==============================
sns.set_style("darkgrid")
# opciones:
# darkgrid
# whitegrid
# dark
# white
# ticks
# ==============================
# CONCEPTOS CLAVE
# ==============================
# scatterplot -> relación
# histplot    -> distribución
# barplot     -> promedio
# countplot   -> conteo
# boxplot     -> outliers
# heatmap     -> correlación
##Labs old 

##exam claude 18/05
#Lambda
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums)) #filter(funcion, lista)
print(result)
#try/except Exception
try:
    num = int(input("Número: "))
    print(10 / num)

except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Debes escribir un número")

#decoradores
def decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("Después")
    return wrapper
@decorador
def saludar():
    print("Hola")
saludar()

#Concepto clave: Herencia y polimorfismo
class Animal:
    def sonido(self):
        return "..."
class Perro(Animal):
    def sonido(self):
        return "Guau"
#Explicación: __str__ define lo que retorna str(objeto) y print(objeto). Es la representación amigable para humanos. __repr__ es la representación técnica para desarrolladores. Implementarlos hace tus clases mucho más depurables.  
class Persona:

    def __str__(self):
        return "Persona normal"
#todo ¿Cuál es el propósito del decorador @property en Python?Explicación: @property permite acceder a circulo.area sin paréntesis ()**, encapsulando la lógica de cálculo. Junto con @setter y @deleter, implementa getters/setters de forma pythonica, manteniendo la interfaz limpia y el encapsulamiento.

class Circulo:
    def __init__(self, radio):
        self._radio = radio
    @property
    def area(self):
        return 3.14159 * self._radio ** 2

# todo ¿Qué característica tienen las clases que heredan de ABC con métodos @abstractmethod? 
from abc import ABC, abstractmethod
class Forma(ABC):
    @abstractmethod # garantizan que ninguna subclase olvide implementar métodos críticos
    def area(self):
        pass

#Siempre usar with open('archivo.csv', 'w', newline='') as f.
with open("archivo.csv", "w") as f:
    f.write("hola")
#todo ¿Qué diferencia hay entre json.dumps() y json.dump()?

#json loads convierte json en dicc python
import json
datos = '{"nombre": "Ana", "notas": [9, 8, 10]}'
obj = json.loads(datos)
print(type(obj), obj["notas"][1]) #todo que hace type

#¿Qué retorna np.where(condición, x, y)?
import numpy as np
a = np.array([5, -3, 8, -1, 2]) #np.where(condicion, si_true, si_false)
res = np.where(a > 0, a, 0)
print(res)

#todo ¿Cuál es el resultado de np.dot(A, B) si A.shape=(2,3) y B.shape=(4,5)
#¿Cuál es la diferencia entre df.dropna() y df.fillna(valor)?
"""
| Método | Acción  |
| ------ | ------- |
| dropna | borra   | nulos
| fillna | rellena |
"""

#¿Cuántas filas retorna pd.merge(df1, df2, on='id', how='inner') si df1 tiene ids [1,2,3] y df2 tiene ids [2,3,4]? Explicación: INNER JOIN retorna solo las filas donde existe coincidencia en ambos DataFrames. Los ids comunes son {2, 3}, por lo tanto 2 filas. LEFT JOIN conserva todos de df1 (3 filas), RIGHT todos de df2 (3 filas), OUTER todos (4 filas).
df1_ids = [1,2,3]
df2_ids = [2,3,4]
pd.merge(df1, df2, on='id', how='inner')
#¿Para qué se usa sns.heatmap() en análisis de datos?..Visualizar correlaciones.
import seaborn as sns
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')


# =====================================================
# DATASETS AUTOMATICOS DE SEABORN (sns)
# =====================================================

# Ver datasets disponibles
print(sns.get_dataset_names())

# Cargar dataset automático
tips = sns.load_dataset("tips")

print(tips.head())

# Otro dataset
iris = sns.load_dataset("iris")

print(iris.head())

# =====================================================
# RESUMEN RAPIDO
# =====================================================
"""

CSV      -> pd.read_csv()
JSON     -> pd.read_json()
Excel    -> pd.read_excel()

Crear DF -> pd.DataFrame()

sns data -> sns.load_dataset("tips")

Ver datos:
.head()
.info()
.describe()

Filtrar:
df[df["columna"] > valor]

Guardar:
.to_csv()
.to_json()

"""


###------------------------------------------------------
## estuctura num primos
cantidad = 5
prime = []
num = 2
while len(prime) < cantidad:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        prime.append(num)
    num += 1
print(prime)

#game random
# 2 BUCLE: crea un código para adivinar un número generado al azar
  # Al inicio deberá pedirse al usuario adivinar un número en un rango del 1 al 20
    # El mensaje debe decir: "Elige un número del 1 al 20"
  # Para cada turno en que el usuario adivine, se deberá responder:
    # "el número real es mayor"
    # "el número real es menor"
  # Cuando acierte, deberá respondérsele "ACERTASTE"
# usar la librería random y el comando random.randint() para generar el número a adivinar

import random

num_oculto = random.randint(1,20)

turno = 0

while turno < 4:
   
    try: #ingresamos try en bucle while para no deterner el proceso
        num_user = int(input("Elige un número del 1 al 20, tiene 4 turnos: "))
    except ValueError:
        print("ingresa un numero")
        continue

    if num_user > 20 or num_user < 1: #filtro de rango establecido
      print("el rango es de 1 a 20")
      continue

    if num_oculto == num_user:
        print(f"ACERTASTE el numero es {num_oculto}")
        break #si aciertas se detiene el bucle
    elif num_oculto > num_user:
        print("El número real es mayor")
    else:
        print("El número real es menor")

    turno += 1 #aumentamos el contador_turno en cada vuelta

    if turno < 4:
      print("Te quedan", 4 - turno, "turnos")

if turno == 4 and num_oculto != num_user:
    print(f"Finalizaron los 4 turnos el numero es {num_oculto}")

# Funciones
# Crear una función que calcule el número de mayúsculas y minúsculas de una cadena (string)
  # tip: usar los métodos islower(), isupper()

var = input("ingresa un string : ")

def contador(var):
  minuscula = 0
  mayuscula = 0

  for n in var:
    if n.islower(): #minuscula
      minuscula +=1
    elif n.isupper():#mayuscula
      mayuscula +=1
    else:
      continue

  print(f"minusculas : {minuscula}")
  print(f"mayusculas : {mayuscula}")

contador(var)



lc4 = [value for index,value in enumerate(lc1) if value not in lc1[:index] ] #index compara hasta index evaluado


# ¿Cómo elimino duplicados?
# output esperado "MAYUSCLO"
lc1 = "MAYUSCULASO"
lc4 = [value for index,value in enumerate(lc1) if value not in lc1[:index] ] #index compara hasta index evaluado
print(f"Con list comprenhencion-Funcional {lc4}") 
