l1 = [1,2,3,4,5,]
t1 = (x for x in range(1,20,2)) #generador
print(next(t1))
print(next(t1))

t1_2 = {}
t1_1 = enumerate(t1) #iterador
print(list(t1_1)) #[(0, 5), (1, 7), (2, 9), (3, 11), (4, 13), (5, 15), (6, 17), (7, 19)]

for index, value in enumerate(t1):
    t1_2[index] = value
#print(t1_2) {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}

#list comprenhencion
"""
[] → list comprehension
{} sin : → set comprehension
{} con : → dict comprehension
"""
lc = [(value,index) for index,value in enumerate(t1) if index > 2]
#print(lc) #
t1 = (1,2,3,4,5,6)
ldic ={index: value for index, value in enumerate(t1)}
#print(ldic) {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
#---------------------------------------------------

lstr = " manuel ytuza "
lstr.strip() #elima espacios de los dos lados left and right

#slice(lstr) 
#print(f"slice directo {lstr[slice(2)]} en (2)") slice directo ma en (2)

slice_lstr = slice(0,6)
#print(f"slice in var {lstr[slice_lstr]} en (0,6)") slice in var manuel en (0,6)

"""
def suma(x,y):
    return x+y
var = suma
print(var(4,5))
"""
lstr = " manuel ytuza "

#.split convierte list
li_split = lstr.split()
#print(li_split)

#.join convierte str
li_join = ",".join(li_split)
#print(li_join)

ll1 = [1,2,3,4,5]
#lambda

def_lamba = lambda x : x**x
var_map = list(map(def_lamba, ll1)) #map
var_filter = list(filter(lambda x: x < 4, ll1)) #filter

from functools import reduce

## La operación será: ((valor_inicial * 1) * 2) * 3
var_reduce = reduce(lambda x,y: x*y, ll1,5)
#print(var_reduce)

#enumerate 
#invertir orden de palabra sin usar range reverse o [::-1] y sin ESPACIOS 
lstr = " ytuza cusirramos ".strip()

var_cy = []
def enumer():
    for index , value in enumerate(lstr):
        index_invertido = lstr[((len(lstr)-1)-index)]

        if index_invertido != " " :
            var_cy.append(index_invertido)
            
    print(var_cy)

#enumer()

class familia:
    familia = "canguro"
    def __init__(self, name, age, sueño, superpoder):
        self.name = name
        self.age = age
        self.sueño = sueño
        self.superpoder = superpoder
    
    def ficha (self):
        print(f"me llamo {self.name} tengo {self.age} años, mi sueño es {self.sueño}, mi superpoder es {self.superpoder} y soy de la familia {self.familia}") 

    def choise_person(self):
        print("Conoce a nuestra familia: ingresa el numera de la persona que quieres conocer")
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
    1:manuel,
    2:dany,
    3:emi,
    4:alice
    5:"salir"
    : """))

                if num>5 or num<1:
                    print("error de rango, rango 1-5")
                    continue
                if num == 5:
                    print("recorrido finalizado")
                    break
        
                rpt = dicc.get(num)
            except ValueError:
                print("dato invalido, ingresa un numero")
            else: 
                rpt.ficha()

manuel =familia("manuel", 30, "ser el mejor programador señor", "super inteligencia")
dany =familia("danytza", 37, "millonaria", "pegar a su esposo")
emi =familia("emile", 13, "salir todos los dias", "torturar")
alice =familia("alice", 5, "tener un helicoptero", "imaginar")

t = manuel.choise_person
t()
#fin del dia 16 

#revisamos tomorrow 17 ................................................
def opcion1():
    print("manuel")

def opcion2():
    print("emi")

menu = {
    1: opcion1,
    2: opcion2
}

# menu[1]()  # ejecuta manuel 


# hoy 17
def ejec_auto (num): #generamos def con parametro num
    dicc = { #creamos dicc 
        1: manuel.ficha, #key = int and value = name.ficha( llamamos directamente)
        2: emi.ficha #al no tener () se almacena y espera () para ejecutar
    }

    dicc[num]()  # ejecuta dinámicamente al sumar ()

#ejec_auto(1) #sumamos el argumento


#############
#encapsular def

def calculadora():
    def sumar(x,y):
        return x+y
    def resta(x,y):
        return x-y
    def division(x,y):
        return x/y       
    def multiplicacion(x,y):
        return x*y
    
    dicc_cal ={
            1:sumar,
            2:resta,
            3:division,
            4:multiplicacion
        }
    dicc_cal_name ={
        1:"suma",
        2:"resta",
        3:"division",
        4:"multiplicacion"
    }
   
    while True : 
        try:
            print("\n--------Calculadora pro--------")
            print("x= ingresa el primer numero - y=ingresa el segundo numero")
            x =float(input("primer numero"))
            y =float(input("segundo numero"))
            z = int(input("""
Elije el numero de la operacion:
    1 = suma,
    2 = resta,
    3 = division,
    4 = multiplicacion 
                                           
        :  """))
            
            if z < 1 or z > 4: #if z not in dicc_cal:
                print("numero fuera de rango \n")
                continue
            if z == 3:
                while y == 0: 
                    print("no se puede div entre 0")      
                    y = float(input("agrega un numero entero > 0 : ")) 

        except ValueError:
            print("valor invalido, debe ser un numero")
        else: 
            print(f" el resultado de la {dicc_cal_name[z]} es {dicc_cal[z](x,y)}")
            salir = input("si deseas finalizar escribe 0")
            if salir == "0":
                print(f"funcion calaculadora terminada \n")
                break

calculadora()