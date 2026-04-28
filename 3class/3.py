#ARCHIVOS PLANOS 24/07 clase 09

#manera correcta con el close
reader = open('dog_breeds.txt')
try:
    print('WORKS')
finally:
    reader.close()

"""
Modos
Modo	Nombre	Descripción
'r'	    Read	Modo lectura (default)
'w'	    Write	Modo escritura (sobrescribe si el archivo ya existe)
'a'	    Append	Modo anexar (agrega contenido al final)
'x'	    eXclusive creation	Modo creación exclusiva (error si el archivo ya existe, no sobreescribe)
'b'	    Binary	Modo binario (para archivos no de texto)
"""
with open('dog_breeds.txt', mode='r') as reader:
    print('WORKS')

#---------ejemplo
file = open('dog_breeds.txt', 'r')
print(type(file))

content = file.read()
print(content)
print(type(content))

#abrir con binario
# en binario
file_b = open('dog_breeds.txt', 'rb')
print(type(file_b))

content_b = file_b.read()
print(content_b)
print(type(content_b))

#read files
with open('dog_breeds.txt', 'r') as reader:
# Imprimir el archivo entero
  print(reader.read())

#reemplanzando palotes
with open('dog_breeds_palote.txt', 'r') as reader:
  content = reader.read()
  breeds = content.replace("\n", "|").split("|")
  print(breeds)

# Extra: para usar más de un separador a la vez:
    # se necesita bibliotecas extra como re (regular expressions)
import re

with open('dog_breeds_palote.txt', 'r') as reader:
    content = reader.read()
    # Divide usando | o \n como separadores
    breeds = re.split(r'\||\n', content)
    # Opcional: eliminar entradas vacías
    breeds = [b.strip() for b in breeds] #sin espacios
    print(breeds)

###buscqueda semantica (lo veremsos en clases) y lexico grafica 

#read vs readline vs readlines
with open('dog_breeds.txt', 'r') as reader:
    print(reader.readline())
    print(reader.readline())
    print(reader.readline()) 

with open('dog_breeds.txt', 'r') as reader:
    print(reader.readlines())

# Opción 2: leer como lista convirtiendo el tipo
f = open('dog_breeds.txt', 'r')
out = list(f)
f.close()

print(out)

# Opción 3.a: iterar con while loop
with open('dog_breeds.txt', 'r') as reader:
# Leer e imprimir línea por línea
    line = reader.readline()
    while line != '':  # EOF (fin de archivo) es vacio
        print(line, end='')
        line = reader.readline()

# Opción 3.b: iterar print y readlines
with open('dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='') #end = como termina cada linea

# Opción 3.c: iterar directamente en reader
with open('dog_breeds.txt', 'r') as reader:
# Leer e imprimir línea por línea
    for line in reader:
        print(line, end='')

###### w escritura

# write
### CUIDADO: no agrega, reemplaza
file = open('dog_breeds.txt', 'w')
#file.write("Samoyedo")
file.close()

#volvemos a cargar el archivo y esta es la forma correcta
#WRITING
with open('dog_breeds.txt', 'r') as reader:
    dog_breeds = reader.readlines()

# Generar un nuevo archivo con la lista invertida
with open('dog_breeds_reversed.txt', 'w') as writer:
    # escribir de modo invertido
    for breed in reversed(dog_breeds):
        writer.write(breed)

# no muestra nada, pero se creó el archivo 
# para mostrar el contenido del nuevo archivo
with open('dog_breeds_reversed.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

##Archivos que no son de texto byte-----------------------------------------

#LEER BINARIO
#es una foto de un perro
with open('jack_russell.png', 'rb') as byte_reader:
    print(byte_reader.read())
    # print(byte_reader.read(3))
    # print(byte_reader.read(2))
    # print(byte_reader.read(1))
    # print(byte_reader.read(1))

# PERO, ¿CÓMO VEMOS LA IMAGEN?
# Con librerías especializadas, p.ej.: PILLOW

# pip install pillow
# import PIL.Image #se importa PIL.Image pára llamar
from PIL import Image #aqui solo llamada Image
from IPython.display import display

image = Image.open('jack_russell.png')
display(image)
#image.show() #abre aplicación local

# 'a': append
# añadir al final del texto
with open('dog_breeds.txt', mode='a') as a_writer:
    a_writer.write('Sin Pelo\n')
with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())

#trabajar con 2 archivos al mismo tiempo
d_r_path = 'dog_breeds.txt'
d_w_path = 'dog_breeds_reversed.txt'
with open(d_r_path, 'r') as reader, open(d_w_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
###CSV
#opcion 1 - caracteres
import csv

with open('birthday.csv') as csv_file:
    csv_reader = csv.reader(csv_file,
                            delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {row}')
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
    print('Processed {line_count} lines.') 

#####ver [0]

#opcion 2 diccionario
import csv

with open('birthday.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {}'.format(row.keys()))
            line_count += 1
        print('\t{} works in the {} department, and was born in {}.'.format(row["name"], row["department"], row["birthday month"]))
        line_count += 1
    print('Processed {} lines.'.format(line_count))

#opcion 2 diccionario
import csv

with open('birthday.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {}'.format(row.keys()))
            line_count += 1
        print('\t{} works in the {} department, and was born in {}.'.format(row["name"], row["department"], row["birthday month"]))
        line_count += 1
    print('Processed {} lines.'.format(line_count))

#WRITE CSV

#opcion 1
import csv
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file,
                                 delimiter=',',
                                 quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['name', 'dpmt', 'b-month'])
    employee_writer.writerow(['John Smith', 'Accounting', 'January'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'April'])

#opcion 2 diccionario
import csv
with open('employee_file2.csv', mode='w') as csv_file:
    encabezados = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file,
                            fieldnames=encabezados)
    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'birth_month': 'March', 'dept': 'IT'})
    writer.writerow({'emp_name': 'Alonso Molina', 'dept': 'HR', 'birth_month': 'April'})
    writer.writerow({'emp_name': 'Pedro Aguilar', 'dept': 'IT', 'birth_month': 'March'})
#CSV CON PANDAS
import pandas as pd
df = pd.read_csv('hrdata.csv')
df.head()

#cambio de indice
df = pd.read_csv('hrdata.csv',
                 index_col='Name')
#terinar dever colap
#TAREA USAR for para evitar que la primra fila se interpre como cabezales en pandas colap antes de JSON
import csv

# Data
temperaturas = [
[68,65,68,70,74,72],
[67,67,70,72,72,70],
[68,70,74,76,74,73]
]

file_path = "temperaturas.csv"

# crear un archivo csv

with open(file_path, mode="w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow([""]*len(temperaturas[0]))
  for fila in temperaturas:
    writer.writerow(fila)

#df = pd.read_csv("temperaturas.csv", header=None)
with open(file_path,mode="r") as reader:
  final =reader.read()

print(final)

#INCIO DE CLASE 10 
#PREGUNTAS DE decoradores "@functools.wraps" mantiene atributos de la funcion decorada
#Operador MORSA ingresa valores dentro de la operacion ":="

#JSON
import json 

# definir un diccionario
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

type(data)
# serializar (convertir dict en str)
json_string = json.dumps(data)
print(json_string)
type(json_string)
# serializar con indentación para facilitar la lectura
json_string = json.dumps(data,
                         indent=2)
print(json_string)
###reVISAR CASA
with open("data_file_ind.json", "r") as read_file:
    data = json.load(read_file)
print(data)
print(type(data))

# Se puede usar .loads() también para directamente generar un json pero mostrarlo como dict

njson_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
ndata = json.loads(njson_string)
print(ndata)

type(ndata)

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1],
                   reverse=True)

print(top_users)


# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
  # the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print(max_users)

#write new json file
# Define a function to filter out completed TODOs
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos,
              data_file,
              indent=2)