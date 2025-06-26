# Ejemplo
from sklearn.preprocessing import MinMaxScaler

# Datos de ejemplo
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [5, 15, 25]})
# Salida del dataframe original
print ("DataFrame original :\n", df)

# Escalar al rango [0, 1]
# Inicialización del Escalador
# # Se crea una instancia de la clase MinMaxScaler.
# Este escalador transformará los valores de cada columna para que estén
#dentro del rango [0, 1], utilizando la fórmula: valor escalado = valor-minimo (máximo-mínimo)
scaler = MinMaxScaler()

# Transformación y Escalado
# scaler.fit_transform(df)
# Calcula el mínimo y el máximo de cada columna en el DataFrame df.
# Escala cada valor de acuerdo con la fórmula anterior.
# pd.DataFrame(..., columns=df.columns):
# Convierte el resultado (que es un array de NumPy) nuevamente en un DataFrame de Pandas.
# Asigna los mismos nombres de columnas que el DataFrame original (df.columns).
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("Datos escalados al rango [0, 1]:\n", df_scaled)


