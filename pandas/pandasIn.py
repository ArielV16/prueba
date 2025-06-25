# EJEMPLO DE CREACIÓN DE UN ARCHIVO CON 10.000 REGISTROS

# Importar las librerias
import numpy as np
#import random
import pandas as pd

# Ahora crearemos un diccionario
datos= {
    "Estudiante_ID": np.arange(1, 10001),  # Identificadores únicos
    "Edad": np.random.randint(18, 30, 10000),
    "Nota_Matemáticas": np.random.randint(1, 100, 10000),  # Notas entre 1 y 100
    "Nota_Lenguaje": np.random.randint (1, 100, 10000),  # Notas entre 1 y 100
    "Nota_Ciencias": np.random.randint (1, 100, 10000),  # Notas entre 1 y 100
    "Genero": np.random.choice(['femenino', 'masculino', 'prefiero no decirlo'], 10000),  # Género aleatorio
    "Comuna": np.random.choice(['Coronel', 'Lota', 'Concepción', 'Hualpén', 'Tomé', 'Penco', 'Arauco','San Pedro'], 10000),
    "Promedio_Notas": np.random.randint()
}
######## choice, randint, uniform#########
# Cuándo usar cada uno:
# np.random.choice() : cuando necesitemos elegir aleatoriamente de un conjunto predefinido de valores
# np.random.randint(): cuando necesitemos números enteros aleatorios dentro de un rango específico.
# np.random.uniform(): cuando necesitemos números flotantes (decimales) aleatorios dentro de un rango específico.

# Ahora convirtamos el diccionario a un DataFrame
df= pd.DataFrame(datos)

# Ahora veamos el DataFrame
print (df)

# ¿Cómo podemos mover las columnas Género y Comuna, para que queden después de edad?
df = df[['Estudiante_ID', 'Edad', 'Genero','Comuna', 'Nota_Matemáticas','Nota_Lenguaje','Nota_Ciencias' ]]

# Veamos el nuevo DataFrame
print (df)

####### Ahora guardemos el archivo en formato csv ########
# Guardar el archivo CSV en el entorno temporal de Colab
file_path = 'estudiantes_notas.csv'  # ruta del archivo
df.to_csv(file_path, index=False) # index= false, para no incluir columna de índices.
print(f"Archivo guardado en: {file_path}")