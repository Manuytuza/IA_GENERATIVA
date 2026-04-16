l1 = [1,2,3,4,5,]
t1 = (1,2,3,4,5,6)

t1_2 = {}
t1_1 = enumerate(t1) #iterador
#print(list(t1_1)) [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

for index, value in enumerate(t1):
    t1_2[index] = value
#print(t1_2) {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}

#list comprenhencion
"""
[] → list comprehension
{} sin : → set comprehension
{} con : → dict comprehension
"""
lc = [value for index,value in enumerate(t1)]
#print(lc) [1, 2, 3, 4, 5, 6]
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

#.split
li_split = lstr.split()
print(li_split)

#.join
li_join = ",".join(li_split)
print(li_join)

ll1 = [1,2,3,4,5]
#lambda

def_lamba = lambda x : x**x
var_map = list(map(def_lamba, ll1)) #map
var_filter = list(filter(lambda x: x < 4, ll1)) #filter

from functools import reduce

## La operación será: ((valor_inicial * 1) * 2) * 3
var_reduce = reduce(lambda x,y: x*y, ll1,5)
print(var_reduce)

#enumerate 
#invertir orden de palabra sin usar range reverse o [::-1]
lstr = " manuel ytuza "
var_cy = []
def enumer():
    for index , value in enumerate(lstr):
        if value ! #fin 16/04 remoto
        len(lstr)
        var_cy.append(value)

    print(var_cy)

enumer()
print(var_cy)



