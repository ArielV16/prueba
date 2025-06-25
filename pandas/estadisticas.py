# EJEMPLO DE APLICACIÓN DE ESTADÍSTICA DESCRIPTIVA SOBRE UN DATAFRAME

# Importar librería
import pandas as pd

# Crear un DataFrame de ejemplo
datos = {
    'Nombre': ['Ana', 'Luis', 'Pedro', 'Marta'],
    'Edad': [23, 34, 29, 40],
    'Notas': [8.5, 8.5, 7.5, 8.0]
}
df = pd.DataFrame(datos)
print("DataFrame:\n", df)

# Mostrar las primeras filas con head
# El comando head en Pandas se utiliza para mostrar las primeras filas de un DataFrame o una Serie.
# Por defecto, muestra las primeras 5 filas, pero podemos especificar cuántas filas deseamos visualizar.
# Usar head()
print(df.head())


# Obtener un resumen rápido con describe()
# Estadísticas descriptivas
print(df.describe())

# Media (Promedio): mean()
print("Promedio de las edades:", df['Edad'].mean())

# Mediana: median()
print("Mediana de las notas:", df['Notas'].median())

# Moda: mode()
print("Moda de las edades:", df['Edad'].mode())

# Suma de los valores: sum()
print("Suma de las edades:", df['Edad'].sum())

# Producto de los valores: prod()
print("Producto de las notas:", df['Notas'].prod())

# Valor Mínimo: min()
print("Nota máxima:", df['Notas'].min())

#Valor Máximo: max()
print("Nota máxima:", df['Notas'].max())

# Desviación estándar: std()
print("Desviación estándar de las edades:", df['Edad'].std())

# Varianza: var()
print("Varianza de las notas:", df['Notas'].var())

# Contar Valores
print("Número de edades registradas:", df['Edad'].count())
# Frecuencia de cada valor único: value_counts()
print("Frecuencia de cada nota:\n", df['Notas'].value_counts())

# Correlación y Covarianza
# Correlación: corr()
# Mide la relación entre columnas numéricas
#print("Correlación entre Edad y Notas:\n", df[['Edad', 'Notas']].corr())
# Covarianza: cov()
# Mide cómo varían juntas dos columnas
#print("Covarianza entre Edad y Notas:\n", df[['Edad', 'Notas']].cov())

# Operaciones Basadas en Condiciones
# Filtrar valores según una condición
#print("Edades mayores a 30:\n", df[df['Edad'] > 30])

# Contar valores que cumplen una condición
#print("Cantidad de notas mayores a 8:", (df['Notas'] > 8).sum())
