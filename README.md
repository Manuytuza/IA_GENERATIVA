# 🐍 PYTHON & IA - GUÍA FINAL (ULTRA RESUMEN)

## 📑 ÍNDICE
1. Base
2. Funciones
3. Estructuras
4. Loops
5. Strings
6. List Comprehension
7. Programación Funcional
8. Enumerate
9. Clases
10. Herencia
11. Encapsulamiento
12. Input y Validación
13. Diccionarios
14. Mapeo
15. Generadores (yield)
16. Errores con yield
17. Estado
18. Errores clave
19. Buenas prácticas
20. Ejemplos clave
21. Benchmark
22. Mini proyecto
23. Clave final

---

## 🧠 BASE
Dato → Información = dato + contexto  
Python: imperativo + POO + funcional  

---

## 🔧 FUNCIONES
```python
def f(a):
    return a
```
✔ Función ≠ método → obj.metodo()

---

## 📦 ESTRUCTURAS
- Lista [] → mutable  
- Tupla () → inmutable  
- Dict {key: val}  
- Set {} → sin orden ni duplicados  

---

## 🔁 LOOPS
- for / while  
- break → corta  
- continue → salta  
- pass → no hace nada  

---

## 🔤 STRINGS (INMUTABLES)
```python
texto = " manuel ytuza "
texto = texto.strip()
lista = texto.split()
nuevo = ",".join(lista)
```
✔ no cambian → reasignar  

---

## ⚡ LIST COMPREHENSION
```python
[exp for x in lista if cond]
```
✔ izquierda transforma  
✔ derecha itera  

Tipos:
- [] lista  
- {} sin : → set  
- {} con : → dict  

---

## 🧩 PROGRAMACIÓN FUNCIONAL
```python
from functools import reduce

l = [1,2,3,4,5]

map_res = list(map(lambda x: x**2, l))
filter_res = list(filter(lambda x: x < 4, l))
reduce_res = reduce(lambda x,y: x*y, l, 5)
```

---

## 🔢 ENUMERATE
```python
for i, v in enumerate([1,2,3]):
    print(i, v)
```

---

## 🧱 CLASES
```python
class A:
    def __init__(self):
        self.x = 1
```

---

## 🧬 HERENCIA
```python
class Padre:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Hijo(Padre):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
```

---

## 🔒 ENCAPSULAMIENTO
```python
self._x
```

---

## ⌨️ INPUT + VALIDACIÓN
```python
try:
    num = int(input("ingresa numero: "))
except ValueError:
    print("error")
```

---

## 📚 DICCIONARIOS
```python
dic = {"a":1}
dic.get("a", 0)
```

---

## 🧠 MAPEO (dicc ={})
✔ dict reemplaza múltiples if

---

## 🔄 GENERADORES (YIELD)
```python
def g():
    yield 1
    yield 2

gen = g()
print(next(gen))
print(next(gen))
```

---

## ⚠️ ERRORES CON YIELD
❌ pensar que es lista  
❌ olvidar next()  
✔ 1 yield = 1 salida  

---

## 🧠 ESTADO
✔ yield guarda estado  
✔ next continúa  

---

## ❌ ERRORES CLAVE
- no reasignar strings  
- confundir función/método  
- usar list como variable  
- no validar input  
- confiar en get  
- pensar que next reinicia  

---

## ✅ BUENAS PRÁCTICAS
✔ validar siempre  
✔ nombres claros  
✔ separar lógica  
✔ entender flujo  

---

## 🚀 EJEMPLOS CLAVE

### ENUMERATE + INVERSIÓN
```python
lstr = " ytuza cusirramos ".strip()
var_cy = []

for i, v in enumerate(lstr):
    inv = lstr[len(lstr)-1-i]
    if inv != " ":
        var_cy.append(inv)

print(var_cy)
```

---

### LIST / DICT COMPREHENSION
```python
t1 = (1,2,3,4,5,6)

lc = [(v,i) for i,v in enumerate(t1) if i > 2]
ldic = {i:v for i,v in enumerate(t1)}
```

---

### STRINGS
```python
lstr = " manuel ytuza "

lstr = lstr.strip()
li_split = lstr.split()
li_join = ",".join(li_split)
```

---

### FUNCIONAL
```python
ll1 = [1,2,3,4,5]

map_res = list(map(lambda x: x**x, ll1))
filter_res = list(filter(lambda x: x < 4, ll1))
```

---

## 🧪 BENCHMARK
```python
import timeit

def for_time():
    y = []
    for i in range(1000000):
        y.append(i)
    return y

def lc_time():
    return [i for i in range(1000000)]

print(timeit.timeit(for_time, number=5))
print(timeit.timeit(lc_time, number=5))
```

---

## 🧩 MINI PROYECTO
```python
class familia:
    familia = "canguro"

    def __init__(self, name, age, sueño, superpoder):
        self.name = name
        self.age = age
        self.sueño = sueño
        self.superpoder = superpoder
    
    def ficha(self):
        print(f"me llamo {self.name} tengo {self.age} años, mi sueño es {self.sueño}, mi superpoder es {self.superpoder} y soy de la familia {self.familia}") 

    def choise_person(self):
        print("Conoce a nuestra familia:")

        dicc = {
            1:manuel,
            2:dany,
            3:emi,
            4:alice,
            5:"salir"
        }

        while True:
            try:
                num = int(input("""
1: manuel
2: dany
3: emi
4: alice
5: salir
: """))

                if num < 1 or num > 5:
                    print("error de rango")
                    continue

                if num == 5:
                    print("fin")
                    break

                dicc[num].ficha()

            except ValueError:
                print("dato invalido")
```

---

## 🔥 CLAVE FINAL
✔ Flujo > sintaxis  
✔ Estado > resultado  
✔ Pensar > codear  

# lambda y slicing en [: :]
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # orden (sort) según parte entera
print(sorted_ids)


# Ventas por regiones (for+2 / reduce)
ventas_lista = [
    {'Norte': 100, 'Sur': 150, 'Este': 200},
    {'Norte': 50, 'Sur': 60, 'Oeste': 70},
    {'Este': 30, 'Oeste': 40, 'Sur': 80},
    {'Sur': 20}
]

venta_default = {'Norte': 0, 'Sur': 0, 'Este': 0, 'Oeste': 0, 'Central': 0}

from functools import reduce

## sin reduce 2 +for----------------

venta_default_l1 = {'Norte': 0, 'Sur': 0, 'Este': 0, 'Oeste': 0, 'Central': 0}
def merch_dicc(l1,l2):
    copia = l1.copy()
    for dicc in l2:
        print(f"1er for {dicc}\n")
        for key, value in dicc.items():
            print(key,value)
            copia[key] = copia.get(key,0) + value  
            print(f" 2do for key = {key} : {copia}")
        print("\n")
    return copia
merch_dicc(venta_default_l1, ventas_lista_l2)

print(f"rpt final {venta_default_l1} \n")

#  con REDUCE--------------------------------
print(f"incio metodo reduce \n")
from functools import reduce

def merch_dicc2 (l1,l2):
        copia2 = l1.copy()
        for key, value in l2.items():
            print(key,value) 
            copia2[key] = copia2.get(key,0) + value  
            print(f" 2do for key = {key} : {copia2}")
        print("\n")
        return copia2 

resultado = reduce(merch_dicc2, ventas_lista_l2, venta_default_l1)
print(resultado)  


# zip + list comprenhension

listas = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sum_gpt = [x+y+z for x,y,z in zip(*listas)]
sum_gpt_1 = [sum(values)for values in zip(*listas)]
print(sum_gpt)
print(sum_gpt_1)

print()


# Aperturar archivos/ yield
def open_cvs(archivo):
    with open (archivo, "r") as archivo:
        while True:
            contenido = archivo.readline()
            if not contenido:
                break
            yield contenido
lineas = open_cvs("tec.csv")

for linea in lineas:
    print(len(linea))
    print(linea)




---

# 🚀 SIGUIENTES PASOS (MASTER PRODUCTION)

## 📑 ÍNDICE - CONCEPTOS POR TRABAJAR

1. Estructuras avanzadas  
2. Manejo de archivos  
3. POO nivel pro  
4. Errores avanzados  
5. Módulos y paquetes  
6. Entornos virtuales  
7. Testing  
8. Debugging  
9. Git y GitHub pro  
10. APIs  
11. Bases de datos  
12. Pandas  
13. Visualización  
14. Automatización  
15. Web scraping  
16. Introducción IA  
17. Machine Learning  
18. Deep Learning  
19. NLP  
20. Proyectos reales  
21. Performance  
22. Arquitectura  
23. Deployment  
24. Mentalidad senior  

---

## 🧠 1. ESTRUCTURAS AVANZADAS
Continuación de: listas, dict, set  

```python
from collections import Counter, defaultdict

lista = [1,1,2,3,3,3]

# contar elementos
c = Counter(lista)
print(c)  # {3:3,1:2,2:1}

# diccionario automático
d = defaultdict(int)
d["a"] += 1
print(d)  # {'a':1}
```

✔ usar Counter para conteos  
✔ defaultdict evita errores de clave  

---

## 📂 2. MANEJO DE ARCHIVOS
Continuación de: input/output  

```python
# leer archivo
with open("data.txt", "r") as f:
    data = f.read()

# escribir archivo
with open("data.txt", "w") as f:
    f.write("hola mundo")

# json
import json

data = {"a":1}
with open("data.json","w") as f:
    json.dump(data,f)
```

---

## 🧱 3. POO NIVEL PRO
Continuación de: clases  

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

p = Persona("manuel")
print(p)
```

✔ métodos mágicos  
✔ clases limpias  

---

## ⚠️ 4. ERRORES AVANZADOS
```python
try:
    x = int("a")
except ValueError:
    print("error valor")
finally:
    print("siempre ejecuta")
```

✔ finally siempre corre  

---

## 📦 5. MÓDULOS Y PAQUETES
```python
# archivo utils.py
def suma(a,b):
    return a+b

# main.py
from utils import suma
print(suma(2,3))
```

---

## 🧪 6. ENTORNOS VIRTUALES
```bash
python -m venv env
env\Scripts\activate
pip install pandas
```

---

## ✅ 7. TESTING
```python
def suma(a,b):
    return a+b

def test_suma():
    assert suma(2,3) == 5
```

---

## 🐞 8. DEBUGGING
```python
x = 10
print(type(x))
```

✔ usar print y revisar errores  

---

## 🌐 9. GIT Y GITHUB PRO
```bash
git init
git add .
git commit -m "inicio"
git branch nueva
git checkout nueva
```

---

## 🔗 10. APIs
```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)

data = res.json()
print(data[0])
```

---

## 🗄️ 11. BASES DE DATOS
```python
import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

cur.execute("CREATE TABLE test(id INT, name TEXT)")
cur.execute("INSERT INTO test VALUES(1,'manuel')")

conn.commit()
conn.close()
```

---

## 📊 12. PANDAS
```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df["columna"])

# filtro
print(df[df["columna"] > 10])
```

---

## 📈 13. VISUALIZACIÓN
```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)
plt.show()
```

---

## 🤖 14. AUTOMATIZACIÓN
```python
import os

files = os.listdir(".")

for f in files:
    print(f)
```

---

## 🕷️ 15. WEB SCRAPING
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
print(soup.title.text)
```

---

## 🧠 16. INTRO IA
✔ IA = sistema que aprende de datos  

---

## 🤖 17. MACHINE LEARNING
```python
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3]]
y = [2,4,6]

model = LinearRegression()
model.fit(X,y)

print(model.predict([[4]]))
```

---

## 🧠 18. DEEP LEARNING
```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
```

---

## 💬 19. NLP
```python
from sklearn.feature_extraction.text import CountVectorizer

text = ["hola mundo","hola python"]

vec = CountVectorizer()
res = vec.fit_transform(text)

print(res.toarray())
```

---

## 🚀 20. PROYECTOS REALES
Ejemplo:
```python
# leer ventas y analizarlas
import pandas as pd

df = pd.read_csv("ventas.csv")
print(df.groupby("producto").sum())
```

---

## ⚡ 21. PERFORMANCE
```python
# lento
l = []
for i in range(1000000):
    l.append(i)

# rápido
l = [i for i in range(1000000)]
```

---

## 🏗️ 22. ARQUITECTURA
Estructura proyecto:
```
proyecto/
 ├── main.py
 ├── utils.py
 ├── data/
 └── tests/
```

---

## 🌍 23. DEPLOYMENT
```bash
pip install flask
```

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hola"

app.run()
```

---

## 🧠 24. MENTALIDAD SENIOR
✔ entender problema  
✔ dividir en pasos  
✔ escribir simple  

---

## 🔥 MISIÓN FINAL
```python
# PROYECTO 1
# automatizar archivos

# PROYECTO 2
# analizar datos con pandas

# PROYECTO 3
# modelo ML simple
```

---

## 🚀 CLAVE FINAL
✔ ya tienes base  
✔ ahora ejecuta proyectos  
✔ práctica diaria = nivel pro  