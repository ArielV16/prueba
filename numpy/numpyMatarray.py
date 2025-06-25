#OPERACIONES MATEMATICAS Y ESTADISTICAS DE NUMPY 
#Suma — np.sum().
#Raíz cuadrada — np.sqrt().
#Media — np.mean().
#Varianza — np.var().
#Desviación estándar — np.std().
#Mediana - np.median().
#Mínimo - np.min().
#Máximo - np.max().

#Contar

#Contar Elementos Específicos:

#np.count_nonzero(condición) para contar elementos que cumplan una condición.
#np.sum(condición) para contar cuántas veces aparece un valor específico.
#np.count_nonzero con el parámetro axis, para contar elementos en filas o columnas.
#np.unique para identificar elementos únicos y su frecuencia.
import numpy as np

array_2d = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])

#suma de elementos 

suma = np.sum(array_2d)

print("esta es la suma de todo: ", suma)

print("sumas de elementos de la primera fila: ", np.sum(array_2d[0]))

#raiz cuadrada de elementos 

raiz_cuadrada = np.round(np.sqrt(array_2d),1) # Pueden probar anteponiendo np.round () para redondear decimales
print("Raíz cuadrada de elementos:\n", raiz_cuadrada)

# Media de elementos
media = np.mean(array_2d)
print("Media de elementos:", media)

# Varianza de elementos
varianza = np.var(array_2d)
print("Varianza de elementos:", varianza)

# Mediana de elementos
mediana = np.median(array_2d)
print("Mediana de elementos:", mediana)

# Mediana elementos tercera fila
mediana_fila = np.median(array_2d[2])
print("Mediana de elementos tercera fila:", mediana_fila)

# Suma de primera fila matriz
suma_fila = np.sum(array_2d[0])
print("Suma de la primera fila:", suma_fila)

# Máximo elemento del array
maximo = np.max(array_2d)
print("Máximo elemento del array:", maximo)

# Minimo elemento del array
minimo = np.min(array_2d)
print("Mínimo elemento del array:", minimo)

# Máximo elemento de la primera fila del array
maximo_fila = np.max(array_2d[0])
print("Máximo elemento de la primera fila:", maximo_fila)

# sumar dos arrays
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
suma_arrays = array_1 + array_2
print("Suma de arrays:", suma)

# Multiplicación de arrays
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
multiplicacion_arrays = array_1 * array_2
print("Multiplicación de arrays:", multiplicacion_arrays)

# Suma a lo largo del eje 0 (colapsa filas, opera sobre columnas)
sum_axis0 = np.sum(array_2d, axis=0)
print("Suma a lo largo de axis=0 (columnas):", sum_axis0)  

# Suma a lo largo del eje 1 (colapsa columnas, opera sobre filas)
sum_axis1 = np.sum(array_2d, axis=1)
print("Suma a lo largo de axis=1 (filas):", sum_axis1)

# Crear un array
array = np.array([[1, 2, 3,1], [4, 5, 6,4]])
# Contar todos los elementos
total_elementos = array.size
print("Total de elementos:", total_elementos)


# Contar elementos mayores que 3
contador_mayores = np.count_nonzero(array > 3)
print("Cantidad de elementos mayores que 3:", contador_mayores)


# Contar cuántas veces aparece el número 2
contador_dos = np.sum(array == 2)
print("Cantidad de veces que aparece el 2:", contador_dos)


# Contar elementos mayores que 2 por fila
contador_filas = np.count_nonzero(array > 2, axis=1)
print("Elementos mayores que 2 por fila:", contador_filas)


# Contar elementos únicos
valores, frecuencias = np.unique(array, return_counts=True)
print("Valores únicos:", valores)
print("Frecuencias:", frecuencias)

# Ejemplo 1: Filtrar Elementos en un Arreglo de 2 Dimensiones
# Supongamos que tenemos un arreglo con datos de estudiantes: filas representan estudiantes y columnas representan sus notas
#en Matemáticas, Lenguaje y Ciencias.

# Crear un arreglo de ejemplo (2D)
datos_2d = np.array([
    [38.08, 70.12, 19.33],  # Estudiante 1
    [95.12, 54.07, 54.65],  # Estudiante 2
    [73.47, 31.64, 87.42],  # Estudiante 3
    [60.27, 81.57, 73.49],  # Estudiante 4
])

# Filtrar todos los datos que cumplan una condición
array_booleano = datos_2d > 30
print("Array booleano:\n", array_booleano) # ¿Qué significa la salida?
# Mostar los datos que cumplen la condición
print("Aplicando el filtro para elementos mayores a 30:\n", datos_2d[array_booleano])

# Filtrar estudiantes con notas en Matemáticas mayores a 50
filtro_matematicas = datos_2d[:, 0] > 50  # Columna 0 es Matemáticas
print ("Filtro matemáticas", filtro_matematicas)
print("Estudiantes con nota en Matemáticas > 50:\n", datos_2d[filtro_matematicas])

# Filtrar estudiantes con Ciencias (columna 2) entre 20 y 80
filtro_ciencias = (datos_2d[:, 2] > 20) & (datos_2d[:, 2] < 80)
print ("Filtro ciencias", filtro_ciencias)
print("Estudiantes con nota en Ciencias entre 20 y 80:\n", datos_2d[filtro_ciencias])


# Ejemplo 2: Filtrar Elementos en un Arreglo de 3 Dimensiones
# En un arreglo 3D, cada capa puede representar un conjunto de datos,
# como diferentes escuelas, y cada fila y columna los datos de los estudiantes.
# Crear un arreglo de ejemplo (3D)
datos_3d = np.array([
    [  # Escuela 1
        [38.08, 70.12, 19.33],  # Estudiante 1
        [95.12, 54.07, 54.65],  # Estudiante 2
    ],
    [  # Escuela 2
        [73.47, 31.64, 87.42],  # Estudiante 1
        [60.27, 81.57, 73.49],  # Estudiante 2
    ]
])

# Filtrar datos donde todas las notas sean mayores a 30
filtro_general = np.all(datos_3d > 30, axis=2) # Entrega un arreglo booleano con True o False
print ("Veamos el array con el filtro:\n", filtro_general)
print("Ahora apliquemos el filtro para ver a los estudiantes con todas las notas > 30:\n", datos_3d[filtro_general])
# Por qué no basta con mostrar filtro_general directamente
# filtro_general no contiene los datos filtrados, sino un array de booleanos:
# filtro_general es un array de True y False que indica, para cada estudiante, si cumple la condición de que todas sus notas son mayores a 30.
# Este array no incluye los valores de las notas, sino únicamente la evaluación lógica para cada estudiante.

############ No olvidar############:
# Primera dimensión (axis=0): Representa escuelas (tamaño 2: Escuela 1 y Escuela 2).
# Segunda dimensión (axis=1): Representa los estudiantes dentro de cada escuela (tamaño 2: Estudiante 1 y Estudiante 2).
# Tercera dimensión (axis=2): Representa las notas de cada estudiante (tamaño 3: Matemáticas, Lenguaje, Ciencias).

############# Por qué axis=2#########
# Cuando queremos analizar las notas de cada estudiante, trabajamos en la tercera dimensión (axis=2), ya que:
# Cada fila del array tridimensional en la segunda dimensión (axis=1) corresponde a un estudiante.
# Cada nota dentro de esa fila está en la tercera dimensión (axis=2).
# Por lo tanto:
# Usar np.all(datos_3d > 30, axis=2) indica que queremos evaluar las notas a lo largo de la tercera dimensión para cada estudiante.

# Si evaluamos la forma de datos_3d.shape, tenemos (2, 2, 3), lo que significa:
# 2 escuelas (axis=0),
# 2 estudiantes por escuela (axis=1),
# 3 notas por estudiante (axis=2).

# Filtrar estudiantes en la primera escuela con notas en Ciencias > 50
filtro_ciencias_escuela1 = datos_3d[0, :, 2] > 50  # Primera escuela, columna Ciencias
print("Estudiantes en Escuela 1 con nota en Ciencias > 50:\n", datos_3d[0][filtro_ciencias_escuela1])

