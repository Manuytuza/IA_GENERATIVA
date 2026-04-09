#primera clase 06/04 IA
#Nootbock LLM proyecto final
#Tareas diarias y trabajos diarios 
#grupos de trabajo y estudio
#verificar entregas enviadas
#se suben los trabajos en grupo de forma individual 
#10 de junio presentacion de proyecto final 
##Dato: Es un elemento en bruto, sin interpretar. Datos + contexto = información 
#Zapier Y N8N IR ANALIZANDO
##CONFIGURAR gpu con CUDA

#----------------------------------------------------------------------------
#clase 02 08/04/2026

#git y github se pasa para final del curso
#USAREMOS CONDA SHELL
"""
COLECCIONES SON : 
listas =[a,1,2],
diccionarios= {"a":10,"b":20} key:value 

FUNCIONES: 
def nombre(param1, param2): 
    inst1 
    inst2 
    return valor 
cuando se llamma nombre(argumento1, argumento2)

LIST COMPREHENSION 
[x+1 for x in range(5)if x%2==2]

FUNCION ANONIMA
func = lambda x,y : x+y
"""
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