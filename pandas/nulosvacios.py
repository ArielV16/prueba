# EJEMPLO DE MANEJO DE DATOS NULOS O VACÍOS EN PANDAS

# Importar librerías
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo con datos nulos
df = pd.DataFrame({
    'Estudiante': ['Juan', 'Ana', 'Pedro', 'María', 'Carlos'],
    'Matemáticas': [90, np.nan, 78, 85, np.nan],
    'Física': [np.nan, 80, 76, 94, 88],
    'Historia': [75, 88, np.nan, 82, np.nan]
})

print("### DataFrame Original ###")
print(df)

# 1. Detectar Datos Nulos
print("\n### Detectar Datos Nulos ###")
print("¿Dónde hay valores nulos?\n", df.isnull())
print("\nNúmero de datos nulos por columna:\n", df.isnull().sum())

# 2. Eliminar Datos Nulos

# a) Eliminar filas con datos nulos
df_sin_nulos_filas = df.dropna()
print("\n### Eliminar Filas con Datos Nulos ###")
print(df_sin_nulos_filas)

# b) Eliminar columnas con datos nulos
df_sin_nulos_columnas = df.dropna(axis=1)
print("\n### Eliminar Columnas con Datos Nulos ###")
print(df_sin_nulos_columnas)

# 3. Rellenar Datos Nulos
# a) Rellenar con un valor específico
df_rellenado_0 = df.fillna(0)
print("\n### Rellenar Datos Nulos con 0 ###")
print(df_rellenado_0)

# b) Rellenar con la media de la columna
df_rellenado_media = df.copy()
df_rellenado_media['Matemáticas'] = df_rellenado_media['Matemáticas'].fillna(df_rellenado_media['Matemáticas'].mean())
df_rellenado_media['Historia'] = df_rellenado_media['Historia'].fillna(df_rellenado_media['Historia'].mean())
print("\n### Rellenar Datos Nulos con la Media ###")
print(df_rellenado_media)

