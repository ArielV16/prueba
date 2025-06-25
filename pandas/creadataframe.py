# EJEMPLO 1 DE CREACIÓN DE UN DATAFRAME CON PANDAS

# Importar pandas
import pandas as pd

# Crear un DataFrame con un diccionario de datos
datos = {
    'Nombre': ['Ana', 'Luis', 'Pedro', 'Marta'],
    'Edad': [23, 34, 29, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'País': ['Chile', 'Bolivia', "Colombia,","Irlanda"]
}

# Mostrar las edades
print (datos['Edad'])

# Convertir el diccionario a un DataFrame
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("DataFrame:\n", df)


# EJEMPLO 2 DE CREACIÓN DE UN DATAFRAME CON PANDAS

# Crearemos un diccionario con información detallada de varios estudiantes
# Luego, usaremos esa información para crear el DataFrames

# Diccionario con información de estudiantes
estudiantes = {
    "ID": [1, 2, 3, 4],
    "Nombre": ["Juan", "María", "Pedro", "Ana"],
    "Edad": [20, 21, 22, 23],
    "Carrera": ["Ingeniería", "Medicina", "Arquitectura", "Derecho"],
    "Notas": {
        "Matemáticas": [90, 85, 78, 92],
        "Física": [88, 76, 80, 94],
        "Historia": [75, 88, 90, 82]
    }
}

######## Creamos el DataFrame ####################

# 1. Primero haremos uno solamente para las notas
df_notas= pd.DataFrame(estudiantes["Notas"])
# Veamos el DataFrame df_notas
print ("Notas en Dataframe:\n",df_notas)

# 2.Ahora crearemos otro DataFrame con el resto de datos del diccionario
df_estudiantes = pd.DataFrame({
    "ID": estudiantes["ID"],
    "Nombre": estudiantes["Nombre"],
    "Edad": estudiantes["Edad"],
    "Carrera": estudiantes["Carrera"]
})

# 3. Veamos el DataFrame df_estudiantes
print ("Notas en Dataframe:\n",df_estudiantes)

# 4.Ahora debemos combinar ambos DataFrame para dejar uno solo, usando concact
df_final = pd.concat([df_estudiantes, df_notas], axis=1) # ¿Porqué axis=1?
# Ambos DataFrames tienen el mismo número de filas (en este caso, 4),
# y cada fila representa información del mismo estudiante.
# Usar axis=1 permite que los datos de cada estudiante se alineen correctamente en una sola fila del DataFrame combinado.

# Mostrar el DataFrame final
print("DataFrame combinado:\n", df_final)

#################################################


# EJEMPLO 2.1 DE MANIPULACIÓN DEL DATAFRAME

# Mostrar el DataFrame final
print("DataFrame combinado:\n", df_final)

#################################################

# Seleccionar columnas específicas
df_seleccion = df_final[["Nombre", "Carrera"]]
print("Datos seleccionados (Nombre y Carrera):\n", df_seleccion)

# Promedio de notas por estudiante
df_final["Promedio_Notas"] = df_final[["Matemáticas", "Física", "Historia"]].mean(axis=1)
print("DataFrame con promedio de notas:\n", df_final)

# Promedio de notas por asignatura
promedio_asignatura = df_final[["Matemáticas", "Física", "Historia"]].mean(axis=0)
print("Promedio por asignatura:\n", promedio_asignatura)

# Estudiante con mejor nota en matemáticas
mejor_matematicas = df_final.loc[df_final["Matemáticas"].idxmax()]
print("Estudiante con la mejor nota en Matemáticas:\n", mejor_matematicas)
# idxmax() devuelve el índice (fila) del estudiante con la mejor nota.
# df_final.loc[]: Recupera la fila completa asociada al índice encontrado en el paso anterior.
# El resultado es una fila del DataFrame que contiene toda la información del estudiante con la mejor nota en matemáticas.


# Ordenar datos por una columna específica
df_ordenado = df_final.sort_values(by="Promedio_Notas", ascending=False)
print("DataFrame ordenado por promedio de notas:\n", df_ordenado)
# Ordena el DataFrame según los valores de la columna Promedio_Notas.
# by="Promedio_Notas" especifica la columna utilizada para ordenar.
# ascending=False indica un orden descendente (de mayor a menor).
# El resultado es un DataFrame ordenado donde los estudiantes con mayor promedio aparecen primero.

# Calcular el promedio de notas por carrera:
promedio_por_carrera = df_final.groupby("Carrera")[["Matemáticas", "Física", "Historia"]].mean()
print("Promedio de notas por carrera:\n", promedio_por_carrera)
# df_final.groupby("Carrera"): Agrupa las filas del DataFrame según los valores de la columna Carrera.
# Cada grupo corresponde a una carrera distinta.
# [["Matemáticas", "Física", "Historia"]]: Selecciona las columnas relevantes para calcular el promedio.
# .mean(): Calcula el promedio de las columnas seleccionadas dentro de cada grupo (carrera).
# El resultado es un nuevo DataFrame donde cada fila representa una carrera y las columnas son los promedios de las asignaturas.



# EJEMPLO 2.2 DE MANIPULACIÓN DEL DATAFRAME

# Mostrar el DataFrame final
print("DataFrame combinado:\n", df_final)

#################################################

# Filtar estudiantes mayores de 21 años
print("Estudiantes mayores de 21 años:\n", df_final[df_final["Edad"] > 21]) # ¿Porqué no usar simplemente df["Edad"]>21?

# Filtrar por múltiples condiciones
filtro = (df_final["Edad"] > 21) & (df_final["Carrera"] == "Ingeniería")
print("Estudiantes mayores de 21 años en Ingeniería:\n", df_final[filtro])

# Agregar nueva columna con datos nuevos
df_final["Edad_Cuadrado"] = df_final["Edad"] ** 2
print("DataFrame con columna 'Edad_Cuadrado':\n", df_final)

# Eliminar la columna Promedio_Notas
df_sin_promedio = df_final.drop(columns=["Promedio_Notas"])
print("DataFrame sin la columna 'Promedio_Notas':\n", df_sin_promedio)

# Eliminar estudiantes con edad >21
df_mayores_21 = df_final[df_final["Edad"] >= 21]
print("DataFrame con estudiantes mayores o iguales a 21 años:\n", df_mayores_21)

# Renombrar columnas
df_renombrado = df_final.rename(columns={"Matemáticas": "Math", "Física": "Physics"})
print("DataFrame con columnas renombradas:\n", df_renombrado)


######Tablas pivote#######
# La tabla pivote (pivot table) en pandas es una herramienta para reorganizar, resumir y analizar datos de un DataFrame.
# Es como una tabla dinámica en Excel, y permite transformar datos agrupados en un formato más estructurado.

# Concepto Básico
# Filas: Representan los valores únicos de una columna que defines como índice.
# Columnas: Representan los valores únicos de otra columna que defines como encabezado.
# Valores: Es el contenido que se muestra en las intersecciones de filas y columnas, usualmente el resultado de una función agregada como sum, mean, etc.
# Sintaxis: pd.pivot_table(data, values, index, columns, aggfunc).
   # data: El DataFrame base.
   # values: Las columnas que queremos resumir.
   # index: Las columnas que queremos que formen las filas.
   # columns: Las columnas que queremos que formen las columnas.
   # aggfunc: La función de agregación para calcular los valores (por defecto es mean).
   # otras funciones: sum, min, max,median, count, std, var, first, last, mode, prod

# Promedio por carrera
# Queremos ver el promedio de notas por carrera en cada asignatura
tabla_pivot = df_final.pivot_table(values=["Matemáticas", "Física", "Historia"], index="Carrera", aggfunc="mean")
print("Tabla pivot con promedio por carrera:\n", tabla_pivot)

# Conteo de estudiantes por edad y carrera
# Queremos ver cuántos estudiantes hay en cada combinación de edad y carrera
# Tabla pivote para contar estudiantes por edad y carrera
tabla_pivote_conteo = pd.pivot_table(df_final, values="ID", index="Carrera", columns="Edad", aggfunc="count")
print("Conteo de estudiantes por edad y carrera:\n", tabla_pivote_conteo)

# Ejemplo 3: Promedio de notas por edad
# Queremos ver el promedio de cada asignatura agrupada por la edad de los estudiantes.
# Promedio de notas agrupado por edad
tabla_pivote_edad = pd.pivot_table(df_final, values=["Matemáticas", "Física", "Historia"], index="Edad", aggfunc="mean")
print("Promedio de notas por edad:\n", tabla_pivote_edad)


# EJEMPLO 3. FILTRAR DATOS

# Crear el DataFrame
datos = {
    'Estudiante': ['Juan', 'María', 'Pedro', 'Ana', 'Lucas', 'Paula', 'Mateo', 'Sofía'],
    'Género': ['Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino'],
    'Edad': [20, 22, 21, 23, 24, 22, 23, 20],
    'Carrera': ['Ingeniería', 'Medicina', 'Derecho', 'Enfermería', 'Psicología', 'Arquitectura', 'Ingeniería', 'Medicina'],
    'Nota_1': [4.5, 5.0, 3.5, 4.2, 3.8, 5.0, 4.0, 4.8],
    'Nota_2': [3.8, 4.5, 4.0, 4.0, 3.9, 4.8, 4.2, 4.7],
    'Nota_3': [5.0, 4.8, 2.8, 4.5, 4.1, 5.0, 4.3, 4.9],
    'Estado': ['Aprobado', 'Aprobado', 'Reprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado'],
    'Horas_Estudio': [10, 12, 5, 8, 7, 11, 9, 13],
    'Ciudad': ['Santiago', 'Valparaíso', 'Concepción', 'Santiago', 'Valdivia', 'Iquique', 'Santiago', 'Antofagasta']
}

df = pd.DataFrame(datos)
print(df)

# Filtrar estudiantes aprobados
aprobados = df[df['Estado'] == 'Aprobado']
print("Estudiantes aprobados:\n", aprobados)

# Filtrar estudiantes con edad mayor a 22
mayores_22 = df[df['Edad'] > 22]
print("Estudiantes con edad mayor a 22:\n", mayores_22)

# Filtrar por múltiples condiciones (and)
#Estudiantes de Género Femenino Aprobadas
aprobadas = df[(df['Género'] == 'Femenino') & (df['Estado'] == 'Aprobado')]
print("Estudiantes femeninas aprobadas:\n", aprobadas)

# Filtrar por múltiples condiciones (or)
# Estudiantes que son de Santiago o Antofagasta
ciudades_seleccionadas = df[(df['Ciudad'] == 'Santiago') | (df['Ciudad'] == 'Antofagasta')]
print("Estudiantes de Santiago o Antofagasta:\n", ciudades_seleccionadas)

# Filtrar estudiantes con notas mayores a un valor
# Estudiantes con Nota_1 mayor o igual a 4.5
nota_alta = df[df['Nota_1'] >= 4.5]
print("Estudiantes con Nota_1 >= 4.5:\n", nota_alta)

# Filtrar filas basado en texto
# Estudiantes en Carreras Relacionadas con Salud
carreras_salud = df[df['Carrera'].str.contains('Medicina|Enfermería', case=False)]
print("Estudiantes en carreras de salud:\n", carreras_salud)

# Filtrar con Funciones Personalizadas
# Estudiantes con un Promedio de Notas Mayor a 4.5
# Calcular el promedio de notas
df['Promedio'] = df[['Nota_1', 'Nota_2', 'Nota_3']].mean(axis=1)
promedio_alto = df[df['Promedio'] > 4.5]
print("Estudiantes con promedio > 4.5:\n", promedio_alto)
# str.contains(): es un método de pandas que permite verificar si una cadena de texto contiene un patrón específico.
# En este caso, el patrón es 'Medicina|Enfermería', lo que significa "contiene la palabra Medicina o Enfermería".
# case=False: indica que la búsqueda no distingue entre mayúsculas y minúsculas.

# Filtrar con query
# Estudiantes Género Masculino con Nota_2 Mayor a 4
query_result = df.query("Género == 'Masculino' and Nota_2 > 4")
print("Estudiantes masculinos con Nota_2 > 4:\n", query_result)
# Una query es una forma eficiente de filtrar un DataFrame utilizando una cadena de consulta
# en vez de usar directamente condiciones con corchetes ([]).
# Esto permite escribir las condiciones de filtro de manera más intuitiva y similar al lenguaje SQL.

# Filtrar por Rango de Valores
# Estudiantes con Edad entre 20 y 23 (incluye ambos extremos)
rango_edad = df[df['Edad'].between(20, 23)]
print("Estudiantes con edad entre 20 y 23:\n", rango_edad)

# Filtrar y Ordenar al Mismo Tiempo
# Estudiantes con Más de 10 Horas de Estudio, Ordenados por Notas
horas_estudio = df[df['Horas_Estudio'] > 10].sort_values(by='Nota_1', ascending=False)
print("Estudiantes con más de 10 horas de estudio, ordenados por Nota_1:\n", horas_estudio)

