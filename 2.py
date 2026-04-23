#POO
#metofo fucnion propia de una clase
#class PerroCasero:  # CamelCase  (distinto al snake_case)
class PerroCasero:
    """
    Clase que define perritos caseros, con atributos de especie y patas
    y métodos para la edad y labrar
    Inicializa con atributos de nombre y edad
    """
# atributos
    especie = 'canis familiaris'
    patas = 4

    # inicializador
    def __init__(self, nombre, edad):
        """
        inicializa los atributos dinámicos de la clase
        nombre: nombre del perro
        edad: edad del perro
        """
        self.nombre = nombre
        self.edad = edad
    # métodos
    def describir_edad(self):
        return f"{self.nombre} tiene {self.edad} años"

    def ladrar(self, sonido):
        return f"{self.nombre} dice: {sonido}"

print(PerroCasero.__doc__) #### Muestra comentarios """ 

#Instanciar
perro_1 = PerroCasero('Pluto', 5)
perro_2 = PerroCasero('Milu', 3)

#estructura base de herencia

class padre():
    n ="fijo_n"
    b ="fijo_b"
    def __init__(self, z,y,x):
        self.x = x
        self.y = y
        self.z = z
    def nombrar(self):
        print(self.n,self.b,self.x,self.y,self.z)

class hijo(padre):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)

hijo1 = hijo("1x","2y","3z")
hijo1.nombrar()

#----------------------------------------------------------------------------
#BENCHMARK medir rendimiento y compararlo
# benchmark = prueba de velocidad

import timeit


# código que quieres medir
def for_time():
    y = []
    for i in range(1_000_000):   
        y.append(i)
    return y #return dentro de for lo detiene y fuera devuelve producto
"""
        yield y

instancia =y() #sin la instancia vuelve el inicio no tiene memoria
print(next(instancia))
print(next(instancia))
print(next(instancia))
"""
def li_compr_time():
    x = [a for a in range(1000000)]
    return x


for_t = timeit.timeit(for_time, number=5)
com_t = timeit.timeit(li_compr_time, number=5)

print(com_t)
print(for_t)

print(round(com_t-for_t, 4))

#repaso parte uno 18

#lambda y slicing en [: :]
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # orden (sort) según parte entera
print(sorted_ids)

x = "abcde"
x[:2]

#lambda + *args
(lambda *args: sum(args))(1,2,3,4,5,6,7,8,9)

#lambda + **kwargs
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
#pendientes ver max, lambda, with read doc r, errores con import (linux-windous) y corte 

#---------------------------------------------------
# repaso remoto tarde , clase20 /04

# Para aritmética decimal exacta from decimal import DecimalDecimal('0.7') * Decimal('0.7')
 
strings = ['a', 'b', 'c', 'd', 'e']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = list(zip(strings, numeros)) 
# results = list(zip(strings, numeros ,strict=True )), si necesitamos que ambos iterables tengan el mismo # de elementos
print(results) 

#con map
mascotas = ['pepe', 'pipo', 'papo', 'hermenegildo']
mascotas_mayus = list(map(str.upper, mascotas))
#STR es la clase que llama a la ufncion puede ser INT. FLOAT. BOOL.
print(mascotas_mayus)

#ahora custom zip con map
strings = ['a', 'b', 'c', 'd', 'e']
numeros = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), strings, numeros))
print(results)

#filter 1 NECESITA UN BOLEANO para sumar
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_student(nota):
    return nota > 75

over_75 = list(filter(is_student, scores))
print(over_75)

# ejemplo de unir 
mis_bool = list(map(is_student, scores))
[num for num, booleano in zip(scores, mis_bool) if booleano]
#filter 2 ver palindromos 

dromes = ("ana", "patata", "mermelada", "reconocer", "arenera")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes) 

#REDUCE bola de nieve
#EXMOXNIX DAME FUERZAAAA

from functools import reduce
# import functools.reduce //otra forma de llamar

nums = [3, 4, 6, 9, 34, 12]

# valor inicial
from functools import reduce
nums = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    # print("primer elemento: ", first)
    # print("segundo elemento: ", second)
    # print("")
    return first + second

result = reduce(custom_sum, nums, 100) #valor inicial
print(result)

#------ update va sumando del dicc incial cada uno de los dic 
dicts = [{'a': 1}, {'b': 2}, {'a': 3}, {'c': 4}]
print(dicts)

# Función para hacer merge de dos diccionarios
def merge_dicts(d1, d2):
    d1.update(d2)
    # print("primer elemento: ", d1)
    # print("segundo elemento: ", d2)
    # print("")
    return d1

result = reduce(merge_dicts, dicts, {'e':100, 'f':200 ,'g':300})
print(result)

#--------------------------------
# Ventas por regiones
ventas_lista = [
    {'Norte': 100, 'Sur': 150, 'Este': 200},
    {'Norte': 50, 'Sur': 60, 'Oeste': 70},
    {'Este': 30, 'Oeste': 40, 'Sur': 80},
    {'Sur': 20}
]

venta_default = {'Norte': 0, 'Sur': 0, 'Este': 0, 'Oeste': 0, 'Central': 0}

#REPASAR
# Función para combinar diccionarios
def combine_sales(ventas_1, ventas_2):
    combined = ventas_1.copy() # copiar
    for key, value in ventas_2.items():
        combined[key] = combined.get(key,0) + value
        print(combined[key])
    return combined

# Usar reduce para combinar todos
#reduce(funcion, iterable, inicial) ese es el detalle
total_sales = reduce(combine_sales, ventas_lista, venta_default)
print(total_sales)

# VI GENERADORES
import sys
nums_squared_lc = [i**2 for i in range(5)]
sys.getsizeof(nums_squared_lc) # devuelve el tamaño en bytes de un objeto

nums_squared_gc = (i**2 for i in range(5)) # cambiar por números más grandes
sys.getsizeof(nums_squared_gc)

#una forma d ellamar la otra por for 
next(nums_squared_gc)

###Generador con yield
## se corta al acabar

#uso de yield para generar cuadrados
def genera_cuadrados(n):
    for i in range(1, n + 1):
        yield i**2

for num in genera_cuadrados(4):
    print(num)
###############################################
# yield en lectura de archivos
def procesar_linea(mi_lin):
  print(len(mi_lin))
  print(mi_lin)
#__________________________________________
### sin yield
def leer_archivo_total(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines() #sin s es linea por linea
    return contenido

# Uso de la función
logs = leer_archivo_total('cc_datos.txt')
for linea in logs: #de aqui sale LINEA de linea 252
    procesar_linea(linea)
#-----------------------------------------
#### con yield 

def leer_archivo_iter(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        while True:
            contenido = archivo.readline()
            if not linea:
                break
            yield contenido 
"""
def leer_archivo_iter(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        for contenido in archivo:
            yield contenido
"""

# Supón que tenemos un archivo grande llamado "datos.txt"
for linea in leer_archivo_iter('cc_datos.txt'):
    procesar_linea(linea)

# 22 /04 clase 08, training actializado

#Forma más breve (aprovecha que en C, ya se ha preconfigurado para leer por línea)
def leer_archivo_iter(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        yield from archivo

#Caso integrador------------------------------

#ejemplo lectura de csv
file_name = "tec.csv"
lines = (line for line in open(file_name)) #generador
list_line = (s.rstrip().split(",") for s in lines) #quita espacio derechoi y separa por , genera una lista
cols = next(list_line) #guardar columnas
company_dicts = (dict(zip(cols, data)) for data in list_line) #junta cols con data 

print(company_dicts) ##### generar repaso
funding = (int(company_dict["raisedAmt"]) for company_dict in company_dicts if company_dict["round"] == "a") #filtro
total_series_a = sum(funding) #sum
print(total_series_a)

#VII DECORADORES---------------------------------------
def repite_2(func):
    def wrapper_repite_plus(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_repite_plus

@repite_2
def greet(name):
    print(f"Hola {name}")

greet("Narda")

#example 2
# Con decorador
import functools
import time

def ralentiza(func):
    """dormir 1 segundo antes de llamar cada bucle de uso de la función"""
    @functools.wraps(func) #salvaguarda para evitar errores
    def wrapper_ralentiza(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs) #llama funcion
    return wrapper_ralentiza

@ralentiza
def conteo(num_arranque):
    if num_arranque < 1:
        print("¡Despegue!")
    else:
        print(num_arranque)
        conteo(num_arranque - 1)
#shadow libreris 

#ejemplo de class y decoradores

# Encapsulación: para ellos se usa un setter y un getter
  # En Python, como en otros lenguajes, se marca con "_" antes del nombre
    # Pero, a diferencia de otros lenguajes de POO, no es prohibición
    # sino convención y sugerencia.
@property
def edad(self):
    return self._edad

@edad.setter
def edad(self, valor):
    if valor < 0:
      raise ValueError("La edad no puede ser negativa")
    self._edad = valor 

#ver solucionario de lab2

# 22 /04 clase 08 FINALIZADA