#Ejercicio 1: Definición de clases e instanciación de objetos
#1)Definir una clase llamada Persona con los atributos nombre, edad y ciudad.
class Persona:
    def __init__(self, nombre, edad , ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    def saludar(self):
        print(f"me llamo {self.nombre} tengo {self.edad} y soy de {self.ciudad}")

class Spartan(Persona):
    def __init__(self, nombre, edad, ciudad, temperamento):
        super().__init__(nombre, edad, ciudad)
        self.temperamento = temperamento

    def saludar_hijo(self):
        super().saludar()
        print(f"sumamos temperamento {self.temperamento}")

    def change_temp(self):
        #change = int(input("1=sad,2=ansioso, 3=molesto, 4=asquiado"))
        change_dicc={
            1:"sad",
            2:"ansioso",
            3:"molesto",
            4:"asquiado"
        }
        while True:
            try:
                change = int(input("1=sad,2=ansioso, 3=molesto, 4=asquiado :"))
                #self.temperamento = change_dicc.get(change, "opcion wrong")

                if change in change_dicc:
                    self.temperamento = change_dicc[change]
                    print("cambio generado :", self.temperamento)
                    break #necesairo para cerrar while
                else:
                    print("opcion invalida")
            except Exception as e:
                print("el error es", e) 

        
kratos = Spartan("manu", 30, "roma", "happy")
kratos.saludar_hijo()
print(kratos.temperamento)

kratos.change_temp()
print(kratos.temperamento)

kratos.name = "LEON"
print(kratos.name)

##--------------------------------------------------------------------------------------------------##
#2)Implementar el método __init__ para inicializar los atributos al crear un objeto.
# inicio trabajo en casa dia 2 
class superhumanos(): 
    def __init__(self, nombre, edad, poder):
        self.nombre = nombre
        self.edad = edad
        self.poder = poder
    def presentation(self):
        print(f"me llamo {self.nombre} edad {self.edad} y poder {self.poder}")

class villanos(superhumanos):
    def __init__(self, nombre, edad, poder, side, kills, gums):
        super().__init__ (nombre,edad,poder)
        self.side = side
        self.kills = kills
        self.gums = gums

    def dark_historial(self):
        super().presentation()
        print(f"soy del lado {self.side}, mate {self.kills} people y mi gum es {self.gums}")
    
    def change_gums(self):

        dic_gums = {
                    1:"ametralladora",
                    2: "bazuca",
                    3: "callapnicop",
                    4: "shuriquen",
                    5: "machacador de bestias",
                    6: "escopeta"
                }
 
        while True:
            try:
                new_gum = int(input( """Elige un numero : 
    1: ametralladora,
    2: bazuca,
    3: callapnicop,
    4: shuriquen,
    5: machacador de bestias,
    6: escopeta 
            : """))

                #if isinstance(new_gum,  (int, float) ): ya lo valida except 

                #esto ya lo valida get
                if new_gum < 1 or new_gum >6 :
                    print("numero fuera de rango")
                    continue

                self.gums = dic_gums.get(new_gum, "no saldra esto")
                print(f"{self.nombre} cambia su gum por : {self.gums}")
                return self.gums


            except ValueError as e :
                print(f" el error es {e}")
                continue

doomsday = villanos("doomsday",200, "control de materia", "dark", 1000, None)
doomsday.dark_historial()
print(doomsday.gums)
doomsday.change_gums()
print(doomsday.gums)


#3)Crear tres objetos de la clase Persona con diferentes valores de atributos.

deatpool = villanos("pool", 60, "regenracion", "dark and lith", 200, None)
pinguino = villanos("pinguino",80, "habla con pinquingos", "dark", 800, None)
t_800 = villanos("T_800", 10, "terminator_liquido_solido","dark", 1000000, "all")

#4)Acceder y modificar los atributos de los objetos.
deatpool.side = "lith"
pinguino.kills = 2000
t_800.gums = t_800.change_gums()

deatpool.dark_historial()
pinguino.dark_historial()
t_800.dark_historial()

