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

#---------------------------------------------------
#inicio de clase 03 
#aprox a mitad del curso ir definiendo tema NCP 
print(2**5) # Potenciación

x = -4+2*(6/(2/3)*3)
print(x)

# 1 byte = 8 bit
#FF es 255, sistema hexadecimal
#and or
#type == ver tipo
round(10.5) #redondeo al par o redodneo del BANQUERO 
# solo por legibilidad se puede usar guiones bajos (_) para números grandes
guion:str = 1_000_000.1666 #sugerencia no declaracion
print(guion) 
#bool(str, int, float) == True
#sliceing
xx = "una cadena"
print(xx[1:6])

#.strip() quita espacios y no modifica, se reasigna

#.find("a") == da posicion del primer hallazgo
#.find("a", 3) == desde el indice 3
#.find("a", 3,9) == desde el indice 3 hasta el 9
#.find("a", 3,4) == desde el indice 3 hasta el 4, si no hya indica -1

#.split()== crea una lista, con punto de quiebre del (),("a"),(","), (".\n")

#.join() == inversa de split solo para str y despues asignas
 # ojo: es un método para cadenas, no para listas, por eso el orden extraño
mis_cursos = ["mate", "lenguaje", "ciencias"]
concatenador = ", "

print(concatenador.join(mis_cursos))

#f-string
# tiene aplicaciones especiales para variables numéricas

x = "manzanas"
y = "naranjas"
precio = 4
#precio:.2f == 4.00 == dos decimales
print(f"las {x} cuestan {precio:.2f} soles; por lo tanto, la docena cuesta {precio*12} soles")

#incio clase 13/04

#tupla = (inmutable) and 1,2,3,4, se llama == listas
# desde ... hasta justo antes de ... cada ... print(mi_lista[2:7:2])
# invertir con [::-1] (no modifica el original), si valido en tuplas
# .reverse() sí modifica la lista original, no tuplas

# shallow copy : [:] o .copy()
mi_lista =[1,2,3,4,5,6]
mi_lista_c = mi_lista[:]  # similar a .copy() no afecta lista_incial, dif a solo oner =

# matrices que son 

# usar copy.deepcopy() para copiar todo, total independencia

#copy. reverse() son metodos no funciones

#x in lista, x esta en mi lista
#.count(2) cuantas veces se repite
#,index(1) cual es el indice de 1
    #mi_lista_rep.index(1,9,12)) busca indice de elemnto 1 de indice9 al 11 
ejemplo: [index for index, value in enumerate(mi_lista_rep) if value == 3] 

#.append(4) agrega un elemento a listas
mi_nueva_lista.extend([4,5,6]) #suma como append pero ams de 1 revisar

#✅ list es una función (más exactamente, una clase/constructor)
lista = list([1, 2, 3])

mi_nueva_lista.insert(1, 1.5)  # (agrega por índice, valor) agrega ala izquierda dle indice dado

#pop (opera con los índices)
mi_nueva_lista.pop(1) #elimina, guarda el num y sin pop() elimna el ultimo

# remove opera con elementos
mi_nueva_lista.remove(4) # por valor (si está repetido, borra únicamente el primero)

# Para colecciones en general: usar remove() o discard()
  # remove() arroja ERROR si el elemento no existe
  # discard() no lo hace

del mi_nueva_lista[3] # (opera con índices)

# clear (el objeto sobrevive, pero vacío) vs del (el objeto no sobrevive)
mi_nueva_lista.clear()

#`.sort()` para ordenar y cambia la lista
#mi_lista.sort(reverse = True) # probar con reverse = True  para orden descendente

##DICIONARIOS

#dic ={"key" : "value"} no se puede repetir llaves o se reemplaza, se llama dic["key"]
#mi_diccionario.keys()
#mi_diccionario.values()
#mi_diccionario.items()

# sum() es función, no método #### Funciones → funcion(objeto) y Métodos → objeto.metodo()

# nota: busca, si encuentra, reemplaza/actualiza; si no encuentra, crea
mi_diccionario["Mario"] = 30

## Forma 2: con .update(), actualiza datos
mi_diccionario.update({'Ernesto': 70,
                       'Ignacio': 90,
                       'Juan':8})

## Forma 3: con .setdefault() para evitar reemplazos no queridos si encuentra algo no aplicada nada
mi_diccionario.setdefault('Ernesto', 40)

# ... pero hay otras opciones
print(mi_dicc.get('nombre3')) # arroja None
print(mi_dicc.get('nombre3', 'oye, no encontré esa key')) # arroja el mensaje #####

## en diccionarios: pop() necesita como argumento una key
# en sets: pop() borra el primer item del orden de aparción (porque no están indexados)
mi_diccionario.pop('María')

###SETS desordenados, sin índice, con valores reemplazables, pero no modificables
# set
mi_set = {1,"dos",3,"cuatro",5}
mi_otro_set = {1,2,3,4,5}
# operaciones de conjuntos: operaciones en bits (bitwise operators: &, |, ^ )

mi_set | mi_otro_set
# Alternativa: set.union(mi_set , mi_otro_set)

mi_set & mi_otro_set
# Alternativa: set.intersection(mi_set , mi_otro_set)

mi_set - mi_otro_set
# Alternativa: set.difference(mi_set , mi_otro_set)

mi_set ^ mi_otro_set
# Alternativa: set.symmetric_difference(mi_set , mi_otro_set)

mi_set.update(mi_otro_set)
mi_set
# notar: no es igual que la union (|), pues este sí modifica la variable

###if elif else
###for loop

#for i in list:
#for i in range(1,10+1): no es indice es elemento
#Forma	¿Qué es i?
for i in lista	Elemento
for i in range(...)	Número (contador / posible índice)

#break, continue(pasa al sigueinte for nos sigue codigo), pass (solo continua codigo) = solo para bucles for

#while loop

print(list(map(lambda i: "TRIPLE-QUINTO" if i%15==0 else "TRIPLE" if i%3==0 else "QUINTO" if i%5==0 else i, range(1,21))))