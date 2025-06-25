#Parte 1: Exploración Inicial

#Visualice el DataFrame completo.
#Use df.head() para observar las primeras filas y df.tail() para las últimas filas.
#Obtenga información general sobre los datos:
#Número de filas y columnas.
#Tipos de datos y si hay valores faltantes.
#Calcule un resumen estadístico de las columnas numéricas.


#Parte 2: Filtrado de Datos

#Seleccione los estudiantes mayores de 25 años.
#Filtre los estudiantes que tengan más de 90 en Matemáticas.
#Encuentre los estudiantes de la comuna "Coronel" que tengan un promedio de notas mayor a 85.


#Parte 3: Agrupamiento y Agregación

#Promedio de notas por género:

#Calcule el promedio de las notas en Matemáticas, Lenguaje y Ciencias agrupado por género.
#Número de estudiantes por comuna:
#Muestre cuántos estudiantes hay en cada comuna.
#Máxima nota en cada asignatura por comuna:
#Encuentre la nota más alta en Matemáticas, Lenguaje y Ciencias agrupada por comuna.


#Parte 4: Creación de Nuevas Columnas

#Calcule el promedio de notas por estudiante:

#Crear una nueva columna Promedio_Notas con el promedio de Matemáticas, Lenguaje y Ciencias.
#Crear una columna Rango_Edad:
#Clasifica a los estudiantes como "Mayor de 25" o "Menor de 25".
#Filtrar a los estudiantes con un promedio de notas mayor a 90 y clasifícarlos por rango de edad.
#Parte 5: Ordenamiento y Selección

#Ordena los datos:

#Muestre el DataFrame ordenado por Promedio_Notas de forma descendente.
#Seleccione columnas específicas:
#Muestre únicamente las columnas Estudiante_ID, Edad y Promedio_Notas.


#Parte 6: Identificación de Datos Faltantes o Anómalos

#Revise si hay valores nulos en el DataFrame:
#Use isnull() para identificar columnas con valores faltantes.
#Identificar estudiantes con notas extremas:
#Encuentre estudiantes con notas menores a 10 en Matemáticas.
#Parte 7: Tablas Pivot

#Crear una tabla pivot para analizar los datos:
#Promedio de notas por comuna y género.
#Parte 8: Exportación de Datos

#Guarde los datos procesados:
#Exporte el DataFrame con las columnas adicionales (Promedio_Notas y Rango_Edad) en un archivo CSV.
#Exporte un subconjunto filtrado:
#Guarde en un archivo CSV los estudiantes con un promedio de notas mayor a 85.


import numpy as np
import pandas as pd

# Aquí leeremos el archivo que creamos al comienzo de la sesión de hoy

df = pd.read_csv('estudiantes_notas.csv')

                                    ####parte 1####
print(df)

# mostramos lo primero con head
print ("este es el head del array\n",df.head())

#mostramos lo ultimo con tail
print("este es el tail del array\n",df.tail())

print(df.info())

# contamos la cantidad de columnas y filas con shape
num_filas_shape, num_columnas_shape = df.shape
print(f"Número de filas: {num_filas_shape}")
print(f"Número de columnas: {num_columnas_shape}")

#vemos los tipos de datos
tipo_datos = df.dtypes
print("\nse pueden ver los tipos de datos aqui: \n",tipo_datos)

#valores faltantes
print("\n¿Dónde hay valores faltantes?\n", df.isnull().sum())

#hacer un resumen estadistico de las columnas numericas
print ("resumen estadistico: \n", df.describe())

                                        ####parte 2####




#Seleccione los estudiantes mayores de 25 años.

print("estudiantes mayores a 25 años \n", df[df["Edad"] > 25])

#Filtre los estudiantes que tengan más de 90 en Matemáticas.

print("estudiantes con mas de 90 en matematicas \n", df[df["Nota_Matemáticas"] > 90].head())

#Encuentre los estudiantes de la comuna "Coronel" que tengan un promedio de notas mayor a 85.

df['Promedio_Notas'] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1)
filtro = (df["Comuna"] == "Coronel") & (df["Promedio_Notas"] > 85)
print("Estudiantes de Coronel con promedio mayor a 85:\n", df[filtro])


                                        ####parte3####

#Parte 3: Agrupamiento y Agregación

#Promedio de notas por género:

promedio_notas_por_genero = df.groupby("Genero")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].mean()
print("promedio de notas ordenadas por genero\n", promedio_notas_por_genero)

#Calcule el promedio de las notas en Matemáticas, Lenguaje y Ciencias agrupado por género.

###lo mismo de arriba

#Número de estudiantes por comuna:

#df_ordenado = df.sort_values(by="Promedio_Notas", ascending=False)
#print("\npromedio de notas:\n", df_ordenado)

#Muestre cuántos estudiantes hay en cada comuna.

estudiantes_por_comuna = df.groupby("Comuna")[["Estudiante_ID"]].count()
print("\ncantidad de estudiantes por comuna\n", estudiantes_por_comuna)

#Máxima nota en cada asignatura por comuna:

maxima_nota_asignatura_comuna = df.groupby("Comuna")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].max()
print("\nmaxima nota de asignatura por cada comuna\n", maxima_nota_asignatura_comuna)

#Encuentre la nota más alta en Matemáticas, Lenguaje y Ciencias agrupada por comuna.

###lo mismo de arriba

#Calcule el promedio de notas por estudiante:


                                ####parte 4####


#Crear una nueva columna Promedio_Notas con el promedio de Matemáticas, Lenguaje y Ciencias.

#esta creado mas arriba
#df['Promedio_Notas'] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1)

#Crear una columna Rango_Edad:
#Clasifica a los estudiantes como "Mayor de 25" o "Menor de 25".
#Filtrar a los estudiantes con un promedio de notas mayor a 90 y clasifícarlos por rango de edad.

df["Rango_Edad"] = "menor a 25"
df.loc[df["Edad"] > 25, "Rango_Edad"] = "mayor de 25"
estudiantes_filtrado = df[df["Promedio_Notas"] > 90]

print("\nestudiantes filtrados por su promedio y edad\n", estudiantes_filtrado[["Estudiante_ID", "Promedio_Notas", "Rango_Edad"]])

                                ####Parte 5####
#Ordena los datos:
#Muestre el DataFrame ordenado por Promedio_Notas de forma descendente.

df_ordenado2 = df.sort_values(by="Promedio_Notas", ascending=False)
print("\nordenado por promedio de forma descendente\n", df_ordenado2)

#Seleccione columnas específicas:
#Muestre únicamente las columnas Estudiante_ID, Edad y Promedio_Notas.

print("\nDe prueba\n", df[["Estudiante_ID", "Edad", "Promedio_Notas"]])

                                ####Parte 6####
#Revise si hay valores nulos en el DataFrame:
#Use isnull() para identificar columnas con valores faltantes.

print("\nNúmero de datos nulos por columna:\n", df.isnull().sum())

#Identificar estudiantes con notas extremas:
#Encuentre estudiantes con notas menores a 10 en Matemáticas.

mayores_22 = df[df['Edad'] > 22]
print("Estudiantes con edad mayor a 22:\n", mayores_22)

menor_10 = df[df["Nota_Matemáticas"] < 10]
print("estudiantes con notas menores a 10", menor_10)

                                ####Parte 7####

#Crear una tabla pivot para analizar los datos:
#Promedio de notas por comuna y género.

tabla_piv = df.pivot_table(
    values=["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"], index=["Comuna", "Genero"], aggfunc="mean")
print("\nTabla Pivot (Promedio de notas por comuna y género):\n", tabla_piv)


                                ####Parte 8####

#Guarde los datos procesados:
#Exporte el DataFrame con las columnas adicionales (Promedio_Notas y Rango_Edad) en un archivo CSV.
df.to_csv('estudiantes_procesados.csv', index=False)
print("Archivo 'estudiantes_procesados.csv' guardado con éxito.")


#Exporte un subconjunto filtrado:
#Guarde en un archivo CSV los estudiantes con un promedio de notas mayor a 85.
df_filtrado = df[df['Promedio_Notas'] > 85]
df_filtrado.to_csv('estudiantes_promedio_mayor_85.csv', index=False)
print("Archivo 'estudiantes_promedio_mayor_85.csv' guardado con éxito.")
