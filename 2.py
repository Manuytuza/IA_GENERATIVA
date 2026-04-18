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

print(PerroCasero.__doc__) #### Muestra comentarios """ 

#Instanciar
perro_1 = PerroCasero('Pluto', 5)
perro_2 = PerroCasero('Milu', 3)

#estructura base de herencia

class padre():
    n ="fijo_n"
    b ="fijo_b"
    def __init__(self, z,y,x):
        self.x = x
        self.y = y
        self.z = z
    def nombrar(self):
        print(self.n,self.b,self.x,self.y,self.z)

class hijo(padre):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)

hijo1 = hijo("1x","2y","3z")
hijo1.nombrar()

#----------------------------------------------------------------------------
#BENCHMARK medir rendimiento y compararlo
# benchmark = prueba de velocidad

import timeit


# código que quieres medir
def for_time():
    y = []
    for i in range(1000000):   
        y.append(i)
    return y #return dentro de for lo detiene y fuera devuelve producto
"""
        yield y

instancia =y() #sin la instancia vuelve el inicio no tiene memoria
print(next(instancia))
print(next(instancia))
print(next(instancia))
"""
def li_compr_time():
    x = [a for a in range(1000000)]
    return x


for_t = timeit.timeit(for_time, number=5)
com_t = timeit.timeit(li_compr_time, number=5)

print(com_t)
print(for_t)

print(round(com_t-for_t, 4))

#repaso parte uno 18

#lambda y slicing en [: :]
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # orden (sort) según parte entera
print(sorted_ids)

x = "abcde"
x[:2]

#lambda + *args
(lambda *args: sum(args))(1,2,3,4,5,6,7,8,9)

#lambda + **kwargs
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
#pendientes ver max, lambda, with read doc r, errores con import (linux-windous) y corte 

