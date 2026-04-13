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
#2)Implementar el método __init__ para inicializar los atributos al crear un objeto.
#3)Crear tres objetos de la clase Persona con diferentes valores de atributos.
#4)Acceder y modificar los atributos de los objetos.
