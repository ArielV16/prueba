import numpy as np
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('estudiantes_notas.csv')

####################################
############# PARTE 1 ##############
####################################

print(df)

# Mostrar primeras filas
print("Este es el head del array\n", df.head())

# Mostrar últimas filas
print("Este es el tail del array\n", df.tail())

# Información general
#print("Informacion del array\n",df.info())
print("Informacion del array\n")
df.info()

# Mostrar cantidad de filas y columnas
num_filas_shape, num_columnas_shape = df.shape
print(f"\nNúmero de filas: {num_filas_shape}")
print(f"Número de columnas: {num_columnas_shape}")

# Tipos de datos
tipo_datos = df.dtypes
print("\nSe pueden ver los tipos de datos aquí:\n", tipo_datos)

# Valores faltantes
print("\n¿Dónde hay valores faltantes?\n", df.isnull().sum())

# Resumen estadístico
print("Resumen estadístico:\n", df.describe())

####################################
############# PARTE 2 ##############
####################################

# Calcular promedio de notas (redondeado)
df['Promedio_Notas'] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1).round().astype(int)

# Estudiantes mayores de 25 años
print("Estudiantes mayores a 25 años:\n", df[df["Edad"] > 25])

# Estudiantes con más de 90 en Matemáticas
print("Estudiantes con más de 90 en Matemáticas:\n", df.loc[df["Nota_Matemáticas"] > 90, ["Estudiante_ID", "Nota_Matemáticas"]].head())

# Estudiantes de "Coronel" con promedio mayor a 85
filtro = (df["Comuna"] == "Coronel") & (df["Promedio_Notas"] > 85)
print("Estudiantes de Coronel con promedio mayor a 85:\n", df.loc[filtro, ["Estudiante_ID", "Comuna", "Promedio_Notas"]])

####################################
############# PARTE 3 ##############
####################################

# Promedio de notas por género
promedio_notas_por_genero = df.groupby("Genero")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].mean().round()
print("Promedio de notas agrupado por género:\n", promedio_notas_por_genero)

# Número de estudiantes por comuna
estudiantes_por_comuna = df.groupby("Comuna")[["Estudiante_ID"]].count()
print("\nCantidad de estudiantes por comuna:\n", estudiantes_por_comuna)

# Máxima nota por comuna y asignatura
maxima_nota_asignatura_comuna = df.groupby("Comuna")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].max()
print("\nMáxima nota por comuna y asignatura:\n", maxima_nota_asignatura_comuna)

####################################
############# PARTE 4 ##############
####################################

# Crear columna Rango_Edad
df["Rango_Edad"] = "menor a 25"
df.loc[df["Edad"] > 25, "Rango_Edad"] = "mayor de 25"

# Filtrar estudiantes con promedio > 90 y mostrar con Rango_Edad
estudiantes_filtrado = df[df["Promedio_Notas"] > 90]
print("\nEstudiantes filtrados por su promedio y edad:\n", estudiantes_filtrado[["Estudiante_ID", "Promedio_Notas", "Rango_Edad"]])

####################################
############# PARTE 5 ##############
####################################

# Ordenar por Promedio_Notas descendente
df_ordenado = df.sort_values(by="Promedio_Notas", ascending=False)
print("\nOrdenado por promedio (descendente):\n", df_ordenado)

# Mostrar columnas específicas
print("\nColumnas específicas:\n", df[["Estudiante_ID", "Edad", "Promedio_Notas"]])

####################################
############# PARTE 6 ##############
####################################

# Verificar valores nulos
print("\nNúmero de datos nulos por columna:\n", df.isnull().sum())

# Estudiantes con notas < 10 en Matemáticas
menor_10 = df[df["Nota_Matemáticas"] < 10]
print("Estudiantes con notas menores a 10 en Matemáticas:\n", menor_10[["Estudiante_ID", "Nota_Matemáticas"]])

####################################
############# PARTE 7 ##############
####################################

# Tabla pivot: promedio de notas por comuna y género
tabla_piv = df.pivot_table(
    values=["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"],
    index=["Comuna", "Genero"],
    aggfunc="mean"
).round()
print("\nTabla Pivot (Promedio de notas por comuna y género):\n", tabla_piv)

####################################
############# PARTE 8 ##############
####################################

# Guardar DataFrame procesado
df.to_csv('estudiantes_procesados.csv', index=False)
print("Archivo 'estudiantes_procesados.csv' guardado con éxito.")

# Guardar estudiantes con promedio > 85
df_filtrado = df[df['Promedio_Notas'] > 85]
df_filtrado.to_csv('estudiantes_promedio_mayor_85.csv', index=False)
print("Archivo 'estudiantes_promedio_mayor_85.csv' guardado con éxito.")
