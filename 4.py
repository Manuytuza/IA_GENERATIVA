##NUMPY
import numpy as np
print(np)
print(np.__version__)

dat = np.random.randn(4,2,3) #ultimo numero de clumnas, 2 filas, 4 matrices, 2 es tercer acto o hipercubo
#print(data)
data = np.random.randn(2,3)#0 es escalar, uno es vector, 2 es matriz y mas son tensores de dimensiones
#randn es distribucion normal o dausiana :salen mas cercanos al 0 como un campana
data * 3
data.shape #ver dimenciones uso de axy ##ver

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print(type(data1))
print(arr1) #array no lleva comas ##ver dif
print(type(arr1))

print(arr1.shape)

#cada corchete es 1 dimension
matriz1 = np.array([[6, 7.5, 8, 0, 1]])
print(matriz1)
print(matriz1.shape)

#dimensiones de un array