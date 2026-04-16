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

print(PerroCasero.__doc__) ####

#Instanciar
perro_1 = PerroCasero('Pluto', 5)
perro_2 = PerroCasero('Milu', 3)