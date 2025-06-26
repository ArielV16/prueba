import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler

#Cargamos el csv

df = pd.read_csv('datos_estudiantes_desafio.csv')

#visualizamos el head y el tail para verificar si esta bien 
print("Visualizacion del head\n",df.head())
print("Visualizacion del tail\n",df.tail())

#visualizamos el conjunto de datos con .shape
print("Conjunto de datos",df.shape)

#Visualizamos las estadisticas descriptivas de las columnas con .describe()
print("Estadisticas descriptivas de las columnas", df.describe())

#Buscamos el rango de edad con .mode()
rango_edad = df["Edad"].mode() 
print("Rango de edad comun",rango_edad)

#identificamos si hay valores nulos o vacios
#al usar el codigo df.isnull() el output seria false o true pero si pones df.isnull().sum()
#nos hara identificar mas rapido los valores nulos ya que suma los valores de cada columna para ver si son nulos
print("Hay valores nulos?", df.isnull().sum())

#promedio general por asignatura 

df["General"] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1)

print(df[["Estudiante_ID","General"]])

#promedio por estudiantes

df["Promedio"] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1)

print(df[["Estudiante_ID","Promedio"]])


#Determinar el porcentaje de estudiantes que tienen una calificación mayor o igual a 60 en las tres asignaturas.
#Pregunta: ¿Qué comuna tiene el promedio más alto en matemáticas?

#print("\nNotas como porcentajes:")
#print((notas / 100) * 100)


#mas o menos esta
porcentaje_mayor = ((df["Nota_Matemáticas"] >=60) & (df["Nota_Lenguaje"] >=60 ) & (df["Nota_Ciencias"] >=60 ))

print (porcentaje_mayor)


promedio_notas_por_comuna = df.groupby("Comuna")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].mean()
print("promedio de notas ordenadas por genero\n", promedio_notas_por_comuna)

#Filtrar estudiantes con calificaciones promedio mayores a 80 y mostrarlos en un nuevo DataFrame.
#Agrupar los datos por género y calcular el promedio de calificaciones por género.

mayor_por_80 = (df[df["Promedio"] >80 ])
print(mayor_por_80)


grupo_genero = df.groupby("Genero")[["Nota_Matemáticas", "Nota_Lenguaje", "Nota_Ciencias"]].mean()
print(grupo_genero)


#Normalizar las columnas de calificaciones y horas de estudio usando NumPy o Scikit-learn.
#Convertir las categorías de la columna Genero en variables numéricas (One-Hot Encoding).
#Pregunta: ¿Cuál es el rango de las calificaciones después de la normalización.


# Seleccionar solo las columnas 'Horas_de_estudio' y 'Promedio'
columns_to_normalize = ['Horas_de_estudio', 'Promedio']

# Crear el objeto MinMaxScaler
scaler = MinMaxScaler()

# Normalizar las columnas seleccionadas
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

print(df[columns_to_normalize])


#¿Qué hace pd.get_dummies()?
#La función pd.get_dummies() toma una columna categórica y la convierte en columnas binarias (0 o 1) para cada posible valor de esa columna. Por ejemplo, si tienes una columna con valores ['Masculino', 'Femenino', 'Masculino'], el One-Hot Encoding la convierte en dos columnas, una para Masculino y otra para Femenino, y asigna 1 donde el valor corresponde y 0 donde no.

#¿Por qué usar drop_first=True?
#Cuando tenemos columnas categóricas con más de dos valores (como Masculino, Femenino y tal vez Otro), drop_first=True elimina la primera columna generada. Esto se hace para evitar la trampa de multicolinealidad, ya que si dejamos todas las columnas generadas, las columnas de variables binarias estarán relacionadas entre sí y podrían causar problemas en los modelos de machine learning.

#Ejemplo con tu DataFrame:
#Imaginemos que tu DataFrame tiene una columna Genero con valores ['Masculino', 'Femenino', 'Masculino', 'Femenino']. Aquí te muestro cómo quedaría después de aplicar el One-Hot Encoding.

# Aplicar One-Hot Encoding

df_encoded = pd.get_dummies(df, columns=['Genero'], drop_first=True)

print("\nDataFrame con One-Hot Encoding:")
print(df_encoded)

#Crear gráficos utilizando Matplotlib (https://matplotlib.org/stable/gallery/index.html).
#Distribución de calificaciones por asignatura.
#Promedio de calificaciones por comuna (gráfico de barras).
#Crear un gráfico de dispersión que relacione Horas_de_estudio y Nota_Matemáticas.
#Pregunta: ¿Qué patrón observas entre horas de estudio y desempeño en matemáticas?


plt.figure(figsize=(10, 6))

# Curvas de densidad para cada asignatura
sns.kdeplot(df['Nota_Matemáticas'], label='Matemáticas', fill=True, color='red', alpha=0.5)
sns.kdeplot(df['Nota_Lenguaje'], label='Lenguaje', fill=True, color='blue', alpha=0.5)
sns.kdeplot(df['Nota_Ciencias'], label='Ciencias', fill=True, color='orange', alpha=0.5)

plt.title('Distribución de Calificaciones por Asignatura')
plt.xlabel('Calificación')
plt.ylabel('Densidad')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
promedio_comuna = df.groupby("Comuna")[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean()
promedio_comuna['Promedio General'] = promedio_comuna.mean(axis=1)
promedio_comuna['Promedio General'].sort_values(ascending=False).plot(kind='bar', color='skyblue')

plt.title("Promedio General de Calificaciones por Comuna")
plt.ylabel("Promedio")
plt.xlabel("Comuna")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(True)
plt.show()



#Crear un gráfico de dispersión que relacione Horas_de_estudio y Nota_Matemáticas.

plt.scatter(df['Horas_de_estudio'], df['Nota_Matemáticas'], color='blue', alpha=0.5)

# Etiquetamos el eje X para indicar que representa el consumo de combustible en condiciones combinadas.
plt.xlabel('Cantidad de horas estudiando')

# Etiquetamos el eje Y para indicar que representa las emisiones de dióxido de carbono por kilómetro.
plt.ylabel('Nota en matematicas')

# Agregamos un título descriptivo para que el gráfico tenga contexto sin necesidad de explicación adicional.
plt.title('dispersion entre hora y notas')

# Agregamos una cuadrícula de fondo para facilitar la lectura de los valores de los ejes y mejorar la interpretación.
plt.grid(True)

# Finalmente, renderizamos y mostramos el gráfico en pantalla.
plt.show()


#Crea histogramas de las variables edad, notas, y tiempo_estudio para ver su distribución.
#Crea un gráfico de dispersión entre tiempo_estudio y notas para ver si hay una posible correlación.
#Usa sns.boxplot() para comparar las notas de estudiantes por género (genero).
#Calcula y visualiza la matriz de correlación entre las variables numéricas usando sns.heatmap().

varia = ['Edad','Promedio','Horas_de_estudio']
df[varia].hist(figsize=(10,8))
plt.suptitle('distribucion de edad hora y notas')
plt.show()


sns.boxplot(
    x='Promedio',           # Variable categórica en el eje X (convertida a string)
    y='Genero',            # Variable numérica en el eje Y
    hue='Promedio',         # Indicamos que la coloración se basa también en los cilindros
    data=df,                     # Dataset que contiene los datos
    palette="Set2",              # Paleta de colores amigable
    legend=False                 # Desactivamos la leyenda para evitar redundancia
)

# Título del gráfico para indicar claramente lo que se está visualizando
plt.title("Comparacion entre promedio y genero")

# Etiqueta del eje X que representa las categorías de cilindros
plt.xlabel("Promedio")

# Etiqueta del eje Y que indica el valor numérico de las emisiones
plt.ylabel("Genero")

# Mostrar el gráfico en pantalla
plt.show()



variables= ['Edad','Horas_de_estudio','Nota_Matemáticas','Nota_Lenguaje','Nota_Ciencias']
plt.figure(figsize=(8, 6))
sns.heatmap(df[variables].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de correlación entre variables")
plt.show()


#Escala las columnas numéricas (edad, tiempo_estudio, notas) usando StandardScaler.
#Convierte las variables categóricas como genero o tipo_escuela en variables numéricas usando OneHotEncoder.
#Crea un nuevo DataFrame con los datos preprocesados y muéstralo.


import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Supongamos que ya tienes cargado tu DataFrame df

# Columnas numéricas a escalar
num_cols = ['Edad', 'Horas_de_estudio', 'Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']

# Columnas categóricas a transformar
cat_cols = ['Genero', 'tipo_escuela']  # Ajusta 'tipo_escuela' si no está en el df

# 1. Escalar columnas numéricas
scaler = StandardScaler()
df_num_scaled = pd.DataFrame(scaler.fit_transform(df[num_cols]), columns=num_cols)

# 2. OneHotEncoder para variables categóricas
encoder = OneHotEncoder(sparse_output=False, drop='first')

df_cat_encoded = pd.DataFrame(encoder.fit_transform(df[cat_cols]),
                            columns=encoder.get_feature_names_out(cat_cols))

# 3. Unir ambos DataFrames
df_preprocessed = pd.concat([df_num_scaled.reset_index(drop=True),
                            df_cat_encoded.reset_index(drop=True)], axis=1)

# Mostrar el DataFrame preprocesado
print(df_preprocessed.head())
