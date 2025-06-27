#Cargar el archivo estudiantes_notas en su entorno de trabajo.
#Cambiar dimensiones: Experimentar con diferentes formas del arreglo.
#Normalización: Comparar métodos de normalización (Min-Max y Z-Score).
#Operaciones estadísticas: Calcular desviación estándar, promedios, etc.
#Filtro de datos: Filtrar estudiantes que cumplan ciertos criterios, como obtener más de 70 en Matemáticas.

import numpy as np 

datos = np.genfromtxt("estudiantes_notas.csv", delimiter=",", skip_header=1, usecols=(1,2,3))

#cambiar dimensiones 

array_de_pruebas = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12],
                    [13,14,15,16,17,18], [19,20,21,22,23,24]])

nuevo_Arreglo = array_de_pruebas.reshape(1,24)

print("este es un array de prueba para modificar las dimensiones", nuevo_Arreglo)

#normalizacion hecha con min-max

min_val= np.min(datos)
max_Val= np.max(datos)

array_minmax_estudiantes=(datos - min_val) / (max_Val - min_val)

print("este es el modo de normalizar en min-max\n", array_minmax_estudiantes)

#normalizacion hecha con z-score

media= np.mean (datos)
desviacion= np.std(datos)

array_zscore_estudiantes= (datos - media) / desviacion

print("esta es el modo de normalizar en z-score\n", array_zscore_estudiantes)

#desviacion estandar 

desviacion_estandar = np.std(datos)

#forma de sacar los promedio 

#suma= np.sum(datos, axis=1)
#promedio= np.round(suma / 3, decimals=2)

# Promedios por estudiante 
promedio = np.round(np.mean(datos, axis=1), 2)
print("Promedios de los estudiantes:\n", promedio)


#filtrado de las notas 70 en matematicas

filtrar = datos[:,0] > 70
estudiantes_filtrados = datos[filtrar]

print ("estudiantes con las notas >70 \n", estudiantes_filtrados)
