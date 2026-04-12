#Utilizar una comprensión de listas para crear una nueva lista con los cuadrados delos números del 1 al 10.
l1=[x**2 for x in range(1,11)]
print(l1)

#Dada una lista de cadenas, usar una comprensión de listas para crear una nueva listaque contenga solo las cadenas que comiencen con una vocal.
l2=["ana", "juan", "andres", "omar", "anton"]
l3 =[x for x in l2 if x[0]=="a"]
print(l3)

#Utilizar una función lambda para crear una función que retorne el cuadrado de un número.
function = lambda x : x**2
print(function(3)) 
print((lambda x : x**2)(5)) # directo in print

# Aplicar una función lambda a una lista de número para duplicar cada elemento.

duplic = lambda l : [x*2 for x in l]
suma = lambda listax : list(map(lambda x:x*2, listax)) #forma sin list comprencion 
l4 = [1,2,3,4]
print(duplic(l4))
print(suma(l4))


#Utilizar la función Map para aplicar una función Lambda que convierta temperatura de Celsius a Fahrenheit en una lista de temperaturas.

lc = [20,30,40,24,56]

convertir = lambda l1 :list(map((lambda x: (9/5*x)+32), l1))

print(convertir(lc))

#Aplicar la función Reduce para encontrar el producto de todos los números en una lista dada.
from functools import reduce

def multiplicar(ll):
    return reduce(lambda x,y : x*y, ll,1)

print(f"- reduce sale {int(multiplicar(lc))}")

#Utilizar la función Filter para crear una nueva lista que contenga solo los números pares de una lista dada.
import random 
lf= [random.randint(1,100) for x in range(1,20)]
l5 = filter(lambda x: x%2 == 0, lf)
print(f" es filter: {list(l5)}") 

#Crear una función generadora que genere la secuencia de Fibonacci hasta un numero dado.
#yield

def fibonacci(x):
    rpta =[]
    a,b = 0,1
    for _ in range(x):
        #if a not in rpta: evito repeticiones
        rpta.append(a)       
        a,b = b, a+b
    return(rpta)

print(fibonacci(15))

#usando fucnion generadora, se pausa hasta esperar solicitud de dato

def fibonacci2(y):
    a,b =0,1
    for _ in range(y):
        yield a
        a,b = b, a+b

l2 =[]
for yield_num in fibonacci2(20):
    l2.append(yield_num)

print(l2)

#ejemplo real con sensores 

import time

def sensores(n):
    i = 0
    while i < n:
        yield f"dato_{i}"
        i += 1
        time.sleep(1)

sensor = sensores(2)

print(next(sensor))
print(next(sensor))
#print(next(sensor)) : genera error ya que el iterador no pasa de 2

#2) Definir una función decoradora que registre los argumentos y valores de retorno de una función.

"""
lvar = []
def gen_argum ():
    var_1 =[x for x in range(1,24) if x%2 != 0]
    def registro(var_1):
        for i in range(len(var_1)):
            lvar.append(var_1[i])
    registro(var_1)

gen_argum()
print(lvar)
"""
def decorade(func):
    def wrapper(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)

        result = func(*args, **kwargs)

        print("return", result)
        return result
    return wrapper

@decorade
def suma(x,y,n):
    
    return f"{x+y} es la edad de {n}"

suma(22,45 ,n = "manu")

#3) Aplicar el decorador a una función que realice un cálculo simple.
def deco(fun):
    def wrapper(*arg, **kwarg):
        print("argum :", arg )
        print("kwarg :", kwarg)

        result = fun(*arg , **kwarg)
        print(result)

        return result #"se devuelve el resultadod e func"
    
    print("decorador activado")
    return wrapper

@deco
def restar(x,y):
    return x-y 

restar(30,2) 