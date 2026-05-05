##NUMPY
import numpy as np
print(np)
print(np.__version__)

dat = np.random.randn(4,2,3) #ultimo numero de clumnas, 2 filas, 4 matrices, 2 es tercer acto o hipercubo
#print(data)
data = np.random.randn(2,3)#0 es escalar, uno es vector, 2 es matriz y mas son tensores de dimensiones
#randn es distribucion normal o dausiana :salen mas cercanos al 0 como un campana
data * 3 #entiende que quiere multiplicar cada elemento
data.shape #ver dimenciones uso de axy ##ver

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print(type(data1))
print(arr1) #array no lleva comas ##ver dif
print(type(arr1))

print(arr1.shape)

#cada corchete es 1 dimension
matriz1 = np.array([[6, 7.5, 8, 0, 1]])
print(matriz1)
print(matriz1.shape)

#dimensiones de un array

#clase 29
#ver primeros 11 minutos de conda
#Generar arrays
print(np.zeros((3, 6)))# todo con zeros
print(np.ones((3, 6))) # todo con unos
print(np.arange(15)) #15 primero naturales

#multiplica elementos, no son matrices
arr = np.array([[1., 2., 3.],
                [4., 5., 6.],
                [7., 8., 9.]
                ])

print(arr * arr)
print(arr - arr)

#como ingresar archivos en las matrices
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
                 )
print(arr2d)
print(arr2d[0])
print(arr2d[0][2]) #iguales --print(arr2d[0,2])

#slicing solo 2 columnas
#columnas , filas
print(arr2d[1: , :2])

##reshape
arr_flat = np.arange(32)
print(arr_flat)
arr_flat2 = arr_flat.reshape(8,4) #reorganiza siempre con 32 elmentos
print(arr_flat2)
print(arr_flat2.shape)

##Transpose
arr_flat.reshape(8,4).T
# alternativa: np.transpose()  (es mejor para tensores 3+ dimensiones)

##np.transpose(arr_flat.reshape(8,4))
#Transformaciones con operaciones comunes
#Comparación con listas de python nativo
# comparar generando colecciones de 100 millones de elementos
import time
import numpy as np

start_lista = time.time()
lista_mill = [i for i in range(10**8)]
end_lista = time.time()
lapso_lista = end_lista - start_lista
print("tiempo como lista (seg): ", lapso_lista)

start_array = time.time()
array_mill = np.arange(10**8)
end_array = time.time()
lapso_array = end_array - start_array
print("tiempo como array (seg): ", lapso_array)

print("proporción: ", np.round(lapso_array/lapso_lista,3))

#Generación PSEUDO-aleatoria y semillas
import random

# Diferenciar entre random.randint() y np.random.randint()
# Las librerías random y numpy tomaron convenciones distintas:
  # random.randint() NO respeta esa convención de python de excluir el valor de cierre
  # np.random.randint() SI respeta la convención

# Además, la versión de numpy permite un 3er argumento: cantidad de números a generar
# Extra: comparar con random.randrange() que sí

print([random.randint(1, 5) for i in range(5)])
print([random.randrange(1, 5) for i in range(5)])

print(np.random.randint(1, 5, 5))

"""
Estadísticos elementales
Usualmente llamamos a los métodos de agregación/reducción de numpy, ej. np.mean(array). Pero en algunos casos, hay métodos de la clases en un ndarray, principalmente:

.sum() → suma
.mean() → promedio
.std() → desviación estándar
.var() → varianza
.min() → mínimo
.max() → máximo
.prod() → producto
.cumsum() → suma acumulada
.cumprod() → producto acumulado
"""
#PANDAS
#SERIES
import numpy as np
import pandas as pd
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(type(obj))
#cambiar index 
obj2 = pd.Series([4, 7, -5, 3],
                 index=['d', 'b', 'a', 'c']
                 )
#ahora se llama con nuevo index
print(obj2['b']) #solo se ingres un termino
print(obj2[  ['a', 'b']  ])#mas de uno e un solo elmento

#uso diccionario para crear series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3.index)

#obj3[0]  # de pronta actualización a obj3.iloc[0]
# ver anuncio (hemos usado pandas 2.2.2) de pronta discontinuidad
obj3['Ohio']

#DataFrames#####

#DATAFRAMES (debe ser el mismo número de elementos)
data = {'city': ['Lima', 'Lima', 'Lima', 'Bogotá', 'Bogotá', 'Bogotá'],
        'year': [2000, 2001, 2002, 2000, 2001, 2002],
        'pop': [8.5, 8.7, 9.1, 9.4, 9.6, 9.9]}
frame = pd.DataFrame(data)
print(frame)
frame.head(2) #limitar visualización cabeza
frame.tail(2) #limitar visualización cola

# cambiar el orden (ojo: si no se guarda en una var, solo queda en visualización)
frame = pd.DataFrame(data, columns=['year', 'city', 'pop'])

frame.iloc[-1] #permite trabjar con indce apesar que se cambien llama al orden original

#seleccionar columna
frame['city']
# alternativa: frame.city

# crear una nueva columna y asignar valor (aquí: números consecutivos)
frame['car'] = [2.3, 2.4, 2.5, 2.4, 2.6, 2.8]

#Drop es dejar caer

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Sujeto1', 'Sujeto2', 'Sujeto3', 'Sujeto4'],
                    columns=['Rasgo1', 'Rasgo2', 'Rasgo3', 'Rasgo4'])
data

data2 = data.drop(['Sujeto1', 'Sujeto3'])  # default: axis=0

data2 = data2.drop(['Rasgo2'], axis=1)
# recomendable: usar ['Rango2'], lista, no como str 'Rasgo2'

# modificar columnas (salvar en variable directamente con parámetro "inplace")
data.drop('Rasgo3', inplace=True, axis=1)
data #reemplaza

#Selección mediante filtros
obj = pd.Series(np.arange(4.0), index=['d', 'a', 'c', 'b'])
print(obj)

print(obj[ ['b'] ])
print(type(obj[ ['b'] ]))
print(obj[ ['b'] ] + 1)
obj[ ['b'] ] + 1

#Filtrar por columnas

# volvemos a crear "data" (fue usada para drop arriba)
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Sujeto1', 'Sujeto2', 'Sujeto3', 'Sujeto4'],
                    columns=['Rasgo1', 'Rasgo2', 'Rasgo3', 'Rasgo4'])
print(data)

# filtrar los datos según un criterio aplicado a una columna
data[data['Rasgo3'] > 5]

data.loc[['Sujeto2'] , ['Rasgo2', 'Rasgo4']] # el orden debe ser [fila, columna] (probar invirtiendo)
# notar el problema de presentación (ojo: no de organización) de datos (probar con print)
data.loc[['Sujeto2','Sujeto4'] , ['Rasgo2', 'Rasgo4']]
data.iloc[[1,3] , [1,3]] #igula con idices

#Apply con dataframes
# Apply + funciones lambda
data.apply(lambda x: np.floor(x + 1.5) ** 2)

##Sort
obj.sort_index()

# También con columnas
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
# ordenar por filas
frame.sort_index()
# de reversa en columnas
frame.sort_index(axis=1, ascending=False)

###tarea opcinal # ¿y para ambos? (ordenar filas y columnas)

# aplicado no a índices, sino a valores
obj = pd.Series([4, 7, -3, 2])
obj.sort_values()

#organzia segun la fila "b"
frame.sort_values(by='b', axis=0)

# criterio secundario (agregar en lista)
frame.sort_values(by=['b','a'], axis=0) #primero ve "b" si hay empate e ve el segundo criterior "a"

#enviar lab final
#desarollar scrip NBA

# EMPEZAMO EL DIA 04/05 import requests
download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()

with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")