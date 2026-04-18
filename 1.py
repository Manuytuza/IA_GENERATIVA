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
mi_lista_rep =(1,2,3,3,4,56,7,7,8,9,3)
ejemplo= [index for index, value in enumerate(mi_lista_rep) if value == 3] 

print("analizando" , ejemplo)

lista = ["a", "b", "c"]
#-----------------------------------------
for i in range(len(lista)):
    print(i, lista[i])

mi_lista = [1,2,3,4,3]
#-----------------------------------------
for i, v in enumerate(mi_lista):
    if v == 3:
        print("Está en la posición:", i)

mi_nueva_lista =[1,2,3,3,4,5,6]
#.append(4) agrega un elemento a listas
mi_nueva_lista.extend([4,5,6]) #suma como append pero mas de 1

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

mi_diccionario={'manu': 70,
                       'andres': 90,
                       'Juana':8}

# nota: busca, si encuentra, reemplaza/actualiza; si no encuentra, crea
mi_diccionario["Mario"] = 30

## Forma 2: con .update(), actualiza datos
mi_diccionario.update({'Ernesto': 70,
                       'Ignacio': 90,
                       'Juan':8,
                       "maria":33})

## Forma 3: con .setdefault() para evitar reemplazos no queridos si encuentra algo no aplicada nada
mi_diccionario.setdefault('Ernesto', 40)

# ... pero hay otras opciones
print(mi_diccionario.get('nombre3')) # arroja None
print(mi_diccionario.get('nombre3', 'oye, no encontré esa key')) # arroja el mensaje #####

## en diccionarios: pop() necesita como argumento una key
# en sets: pop() borra el primer item del orden de aparción (porque no están indexados)
mi_diccionario.pop('maria')

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
for i in lista:	# trabajo con el Elemento
    print(i)
for i in range(2):	# trabajo con Número (contador / posible índice)
    print(i)

#break, continue(pasa al sigueinte for nos sigue codigo), pass (solo continua codigo) = solo para bucles for

#while loop

#solucion in one line de ejercicio 3 
print(list(map(lambda i: "TRIPLE-QUINTO" if i%15==0 else "TRIPLE" if i%3==0 else "QUINTO" if i%5==0 else i, range(1,21))))

##15/04 clase 05 

#FUNCIONES 
#parametro termino general y argumento son los que instancian a los parametros
#round==redondeo
#scope , no se recomienda usar "global" sin comillas antes de la variable por comflicto en proyectos grandes 
# nonlocal : permite que var suba un nivel 
def func_mayor():
    print("sin corchete solo almacena def")
var_rara_1 = func_mayor   #almacena la función, se usa en generadores
print(var_rara_1)
var_rara_2 = func_mayor() #almacena el output de la función
print(var_rara_2)

#funciones anidadascon MEMORIA

def mult(n1):
  def operation(n2):
    return n1**n2
  return operation

var1 = 5
var2 = 2

func_op = mult(var1)

var1 = 4
# no se usa el valor nuevo porque la función se llamó antes de la re-definición

result = func_op(var2)
print(result)

# alternativa en un solo paso:
print(mult(var1)(var2))

#IV.4 PARÁMETROS ESPECIALES *args y **kwargs
# Argumentos especiales: *args
  # (en realidad puede ser cualquier string precedido de *)
def sum_var_args_1(*args):
  return sum(args)

sum_var_args_1(1,2,3,4,5,6,7)

# un poco más complejo:
def sum_var_args_2(*args):
  m=0
  for i in args:
    m += i*1.25
  return m

sum_var_args_2(1,2,3,4,5,6,7)

# Argumentos especiales: **kwargs
  # (en realidad puede ser cualquier string precedido de **)

def apellido_alumnos(**kwargs):
  print("El apellido es " + kwargs["apellido"])

apellido_alumnos(nombre = "Julio", apellido = "Santos")
apellido_alumnos(apellido = "Torres", nombre = "Marta", edad=13)
apellido_alumnos(grado = "5to", nombre = "Norberto", apellido = "Velarde")

# ARGS trabajo con tuplas (1,) o 1,
#kwargs key "=" value 

def crear_receta(**kwargs):
    receta = "Ingredientes para receta:\n"
    for ingrediente, cantidad in kwargs.items():
        receta += f"{cantidad} de {ingrediente}\n"
    return receta

# Crear una receta pasando ingredientes como argumentos con nombre
print(crear_receta(harina="200g", azucar="100g", mantequilla="50g", huevos="2 unidades"))

#doc - string (comentarios con """)

def sum_var_args(*args):
  """
  Esta es una función muy importante porque así lo hemos necesitado (bla bla bla)
  Argumentos:
    *args: una tupla no vacía con valores numéricas
  Return: la suma de dichos valores
  """
  return sum(args)

sum_var_args(1,2,3,4,5,6)

#inicio clase 06 de IA GENERATIVA ------------

#pendeinte repasar :  PARÁMETROS ESPECIALES *args y **kwargs , sumar sorter uso structura


#class padre es opcional poner ()
#se recomienda poner un doc 
#atributos por defecto y los demas que varian con __init__
#INSTANCIAR es crear individuos de la class

class PerroCasero:  # CamelCase  (distinto al snake_case)
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

########codigo anteior ############ para que corra
class RussellTerrier(PerroCasero):

    altura = 'chato'
#self si mismo
    def correr(self, velocidad):
        self.velocidad = 0 # contrastar con self.velocidad = velocidad
        return f"{self.nombre} corre a {velocidad} m/s"

    def acelerar(self, incremento):
        """método para incrementar velocidad"""
        self.velocidad += incremento
        print(f"el perro acelera a {self.velocidad} m/s")

    def desacelerar(self, disminucion):
        """método para disminuir velocidad"""
        self.velocidad = max(0, self.velocidad - disminucion) #revisar elige el mayor, declara base como maximo anulando -int y SUMAR A README
        print(f"el perro desacelera hasta los {self.velocidad} m/s")


#clase que hereda de la clase PerroCasero
class Bulldog(PerroCasero):
    def sonreir(self):
        return f"{self.nombre} sonríe!"

    # modificar en la clase hija un método de la clase madre
      # mismo método, distintos comportamiento (polimorfismo)#######
    def ladrar(self, sonido):
        return f"{self.nombre} gruñe: {sonido}"


# se heredan elementos de la clase pariente
perrito_chiquito_1 = RussellTerrier("Jim", 12)

# pero también maneja sus propios elementos
print(f"velciddad no retorno 10 se queda en 0 {perrito_chiquito_1.correr(10)}")

perrito_chiquito_1.acelerar(8)
perrito_chiquito_1.desacelerar(2)

##ABASTRACCION: LO MINIMO indispensable de funcionamiento 
#lower-super-islower-issuper

## II MANEJO DE ERRORES
##zerodivisionerror
#syntaxError = FALTA ALGUN SIGNO 
#NAMEeRROR - NO SE DEFINIO VAR

#raise except
x = 19
if x < 21:
  pass
  #raise Exception(f'x no debe ser menor a 21 . Y el valor de x aquí es: {x}') #detiene todo por eso no correo lo demas

#assert
import sys

#assert('linux' in sys.platform), "Este código solo corre en Linux."
#assert('win64' in sys.platform), "Este código solo corre en Windows."

input("Presiona Enter para cerrar...")
#try
a=2

try:
  10/a  # jugar cambiando valores
except:
  print("Hubo excepciones")
else:
  print("No hubo excepciones")
finally:
  print("Haya o no excepciones, igual muestra esto")

print()
#repasar HOYYYYYYYYY 
try:
    x = 19
    if x < 21:
        raise Exception(f'x no debe ser menor a 21 . Y el valor de x aquí es: {x}')

    import sys
    assert('linux' in sys.platform), "Este código solo corre en Linux."

except Exception as e:
    print("Error:", e)

input("Presiona Enter para cerrar...")
print()
#en list comprehension
cuadrados_2 = [i*i for i in range(10)]
print(cuadrados_2)

frase = 'tres tristes tigres comen trigo en el trigal'
vowels = [i for i in frase if i in 'aeiou']
print(vowels)

#-------STRING
frase_2 = 'trEs Tristes tigres@_'

def es_consonante(letter):
    vocales = 'aeiou'
    return letter.isalpha() and letter.lower() not in vocales

consonants = [i for i in frase_2 if es_consonante(i)]
consonants
#PUEDO GUARDO FUNCIONES EN EL LUGAR DE I INCIAL
#----------------------
# Podría transformarse el string a lista
nombre = "juan"

lista_nombre = list(nombre)
resultado_nombre_1 = [i.upper() for i in lista_nombre]
print(resultado_nombre_1)

# pero no es necesario, se puede aplicar directamente al string
resultado_nombre_2 = [i.upper() for i in nombre]
print(resultado_nombre_2)

"""
Orden del "if" respecto del "for": diferencia entre if para filtrar vs if para transformar

Si la condición "if" es únicamente para filtrar, irá después del "for"
Si la condición "if" es para transformar elementos, irá antes del "for"
"""
precio_orig = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
precio_2_list_a = [i if i > 0 else 0 for i in precio_orig] # se usa para transformar
print(precio_2_list_a)

#SET COMPREHENSIONS CONJUNTOS
cita = "memento mori"
vocales_uniq = {i for i in cita if i in 'aeiou'}
vocales_uniq

#LAMBDA
lambda x, y: x**3 + y**3
_(2, 3)
# funciona solo si se llama inmediatamente después
# solo funciona una vez. Por eso no es muy recomendable usarlo

(lambda x:
(x % 2 and 'impar' or 'par'))(17)

#LOS VALORES POR DEFECTO SIEMPRE A LA DERECHA
# argumentos posicionales vs nombrados (positional vs keyword arguments)
  # argumentos por default para parámetros
def mi_suma_nueva_familia(x, y, z=0):
  """
  Suma las edades de los miembros de una familia que acaba de tener un hijo
  Args:
    x: edad del padre,
    y: edad de la madre,
    z: edad del hijo
  Returns: suma de edades
  """
  return x + y + z

mi_suma_nueva_familia(25, 24)

(lambda *args: sum(args))(1,2,3,4,5,6,7,8,9)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)


# revisar 

sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # orden (sort) según parte entera
print(sorted_ids)