import numpy as np

#ej de array unidimensional

#crear un array unidimensional 

array_1d = np.array([1,2,3,4]) # usamos el np.array()
print("array unidimensional:", array_1d)

#ver el tipo de dato del array

print("el tipo de dato del array es:", type(array_1d)) # se usa type()

# mostrar el primer elemento del array

print ("primer elemento del array:", array_1d[0])

#mostramos algunos elementos del array

print ("elemento 2 y 3 del array:", array_1d[1:3]) # igual que en una lista 

#ej de array bidimensional

#crear array bidimensional 
array_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

#se muestra el array completo

print("array bidimensional \n", array_2d)

#primera fila del array 

print("primera fila del array: \n", array_2d[0])

#segunda fila del array

print("segunda fila del array \n", array_2d[1])

#tercera fila del array 

print("tercera fila del array: \n", array_2d[2])

#primera columna del array

print("primera columna del array: \n", array_2d[:,0])

#segunda columna del array 

print("segunda columna del array: \n", array_2d[:,1])

#tercera columna del array 

print("tercera columna del array: \n", array_2d[:,2])

#mostrar un elemento del array  

print("elementos [1,2] del array: \n", array_2d[1,2])

#mostrar los ultimos dos elementos almacenados en la ultima fila del array 

print ("los ultimos elementos alamacenados  en fila: \n", array_2d[2,1:])

#mostrar los ultimos dos elementos almacenados en la ultima columna del array

print ("los ultimos elementos alamacenados en la columna: \n", array_2d[1:,2])

# Crear un array de tres dimensiones
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11,12]]])

# Mostrar todo el array 3d
print("Array tridimensional:\n", array_3d)

# Mostar primera matriz del array 3d
print ("Primera matriz del array 3d:\n",array_3d[0])

# Mostar segunda matriz del array 3d
print ("Segunda matriz del array 3d:\n",array_3d[1])

# Mostar primera fila de la matriz 1
print ("Primera fila de la matriz 1 del array 3d:\n",array_3d[0][0])

# Mostar segunda fila de la matriz 1
print ("Segunda fila de la matriz 1 del array 3d:\n",array_3d[0][1])

# Mostrar toda la columna 1 de la matriz 2
print ("Columna 1 de la matriz 2 del array 3d:\n",array_3d[1][:,1])

# Mostrar toda la fila 1 de la matriz 2
print ("Fila 1 de la matriz 2 del array 3d:\n",array_3d[1][1,:])

# Mostar el primer elemento de la matriz 1
print ("Primer elemento de la matriz 1 del array 3d:\n",array_3d[0][0][0])

# Mostar un elemento almacenado en una fila del array 3d
print ("Elemento [1, 1, 2] en el array 3:\n", array_3d[1, 1, 2])

# Mostar los dos últimos elementos de la fila 1 de la matriz 2
print ("Dos últimos elementos de fila 2 en matriz 2 del array 3:\n", array_3d[1][1][1:])

# Mostar los dos últimos elementos de la columna 3 de la matriz 2
print ("Dos últimos elementos de columna 3 en matriz 2 del array 3:\n", array_3d[1][:,2])

# ej recreacion de un array de tres dimensiones 

#recreasion de un array de 3 dimensiones (3D)

array_3d1 = np.array([[[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255]],
                    [[100, 100, 100], [120, 120, 120], [140, 140, 140],[160, 160, 160], [180, 180, 180]],
                    [[200, 200, 200], [220, 220, 220], [240, 240, 240], [255, 255, 255], [0, 0, 0]]
])

#mostrar todo el array

print("este es un array completo de tres dimensiones: \n", array_3d1)

#mostrar la primera matriz del array

print("primera matriz del array: \n", array_3d1[0])

#mostrar la segunda matriz del array

print("segunda matriz del array: \n", [1])

#mostrar la primera fila de la matriz 1

print ("Primera fila de la matriz 1 del array 3d:\n",array_3d1[0][0])

# Mostar segunda fila de la matriz 1

print ("Segunda fila de la matriz 1 del array 3d:\n",array_3d1[0][1])

# Mostrar toda la columna 1 de la matriz 2

print ("Columna 1 de la matriz 2 del array 3d:\n",array_3d1[1][:,1])

# Mostrar toda la fila 1 de la matriz 2

print ("Fila 1 de la matriz 2 del array 3d:\n",array_3d1[1][1,:])

# Mostar el primer elemento de la matriz 1

print ("Primer elemento de la matriz 1 del array 3d:\n",array_3d1[0][0][0])

# Mostar un elemento almacenado en una fila del array 3d

print ("Elemento [1, 1, 2] en el array 3:\n", array_3d1[1, 1, 2])

# Mostar los dos últimos elementos de la fila 1 de la matriz 2

print ("Dos últimos elementos de fila 2 en matriz 2 del array 3:\n", array_3d1[1][1][1:])

# Mostar los dos últimos elementos de la columna 3 de la matriz 2

print ("Dos últimos elementos de columna 3 en matriz 2 del array 3:\n", array_3d1[1][:,2][3:])

### Conocer el número de dimensiones usando ndim

print("Dimensión del array unidimensional:", array_1d.ndim)
print("Dimensión del array bidimensional:", array_2d.ndim)
print("Dimensión del array tridimensional:", array_3d1.ndim)
print("Dimensión primera matriz  array tridimensional:", array_3d1[0].ndim) # dimensión de la primera matriz 2d
print("Dimensión segunda matriz array tridimensional:", array_3d1[1].ndim) # dimensión de la segunda matriz 2d
print("Dimensión tercera matriz array tridimensional:", array_3d1[2].ndim) # dimensión de la tercera matriz 2d

### Conocer tamaño del array 1d y forma, usando size y shape:

print("Tamaño del array 1D:", array_1d.size)
print("Forma del array 1D:", array_1d.shape)

### Conocer tamaño del array 2d y forma, usando size y shape:

print("Tamaño del array 2D:", array_2d.size)
print("Forma del array 2D:", array_2d.shape)

### Conocer tamaño del array 3d y forma, usando size y shape:

print("Tamaño del array 3D:", array_3d1.size)
print("Forma del array 3D:", array_3d1.shape)
print("Tamaño del array 3D1:", array_3d1.size)
print("Forma del array 3D1:", array_3d1.shape)

# Crear array 2d

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print ("Array 2d:\n", array_2d)
print("Forma del array 2D:", array_2d.shape)

# La forma original tiene la forma (2, 3) o sea, 6 elementos.

#Para cambiar la forma, la nueva debe tener también 6 elementos.

nuevo_array1 = array_2d.reshape(3,2) #(2,3)
print ("Nuevo array:\n", nuevo_array1)
print("Forma del nuevo array:", nuevo_array1.shape)

nuevo_array2= array_2d.reshape(1,6) #(6,1)
print ("Nuevo array:\n", nuevo_array2)
print("Forma del nuevo array:", nuevo_array2.shape)
