class good_of_war:
    name = ""
    fuerza = 0
    edad = 0
    vida = 0
    origen = ""

    def __init__(self, name, fuerza, edad, vida, origen):
        self.name = name
        self.fuerza = fuerza
        self.edad = edad  
        self.vida = vida 
        self.origen = origen
    def stadistic(self):
        print(self.name, self.fuerza, self.edad, self.vida, self.origen)
    def presentation(self):
        print(f"me llamo {self.name} tengo {self.edad} años, mi fuerza es de {self.fuerza}, vida {self.vida} y soy de {self.origen}")
    def up_level(self, fuerza, vida):
        self.fuerza += fuerza
        self.vida *= vida
    def ataque(self, enemigo):
        enemigo.vida = enemigo.vida - self.fuerza
        return enemigo.vida 

kratos = good_of_war("the gosth", 99, 200, 1000, "sparta")
thor = good_of_war("thor", 100, 1000, 200, "irlanda")

class hijos(good_of_war):
    def __init__(self, name,fuerza, edad, vida, origen,runa):
        #good_of_war.__init__(self, name,fuerza, edad, vida, origen)
        super().__init__(name,fuerza, edad, vida, origen) #llamma atributos padre
        self.runa = runa #siempre se declara

    def change_arm(self): #cambia runa
        arms = int(input("num 1.pistola, 2.bomba, 3.granada, 4.misil, 5.basuca"))
        dic_arm={
            1:[1, "pistola"] , 
            2:[2, "bomba" ],
            3:3,
            4:4,
            5:5
        }
        
        self.runa = dic_arm.get(arms,"arma noexiste")
    def presentation(self): 
        super().presentation() #llama modul padre
        print("espada",self.runa) #aumenta esta linea

#print(kratos.name)

thor.presentation()
#print("fight")
#kratos.stadistic() 
#kratos.up_level(100,5)
kratos.presentation()
kratos.ataque(thor)
thor.presentation()

loki = hijos("loki",40, 15,40,"midgar",35)
loki.presentation()
print(loki.runa)
loki.change_arm()
loki.presentation()

#min 19.25


#------- mañana 12/04
#_______ morning 15/04. no se hereda se usa parte de codigo book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Crear libros
b1 = Book("1984", "Orwell")
b2 = Book("Python", "Guido")

# Crear biblioteca
lib = Library()

# Agregar libros
lib.add_book(b1)
lib.add_book(b2)

# Mostrar
lib.display_books()

