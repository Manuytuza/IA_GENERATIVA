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