# Ejemplo

# Importación del OneHotEncoder
# Esta herramienta de scikit-learn se utiliza para convertir datos categóricos
# en un formato que los modelos de machine learning puedan manejar: columnas binarias
# o One-Hot Encoding.
# Cada categoría única se convierte en una columna separada con valores 1
# (si pertenece a esa categoría) o 0 (si no pertenece).

from sklearn.preprocessing import OneHotEncoder
import pandas as pd


# Datos categóricos
data = pd.DataFrame({'Género': ['Hombre', 'Mujer', 'Hombre']})

# Codificación One-Hot
#cInicialización del Codificador One-Hot:
# OneHotEncoder convierte los valores categóricos en columnas binarias.
# Parámetro sparse=False:
# Por defecto, OneHotEncoder devuelve una matriz dispersa (sparse matrix) para ahorrar memoria.
# Matriz densa:
# Es una matriz "normal", donde se almacenan todos los valores,
# incluyendo los ceros. Cada elemento se guarda, sin importar si es 0 o cualquier otro número.
# Es más fácil de usar y manipular, pero puede ocupar mucha memoria si la matriz es grande.
# Matriz dispersa:
# Solo guarda los valores no nulos (por ejemplo, los valores distintos de cero).
# Es muy eficiente en memoria cuando la matriz tiene muchos ceros,
# como en la codificación one-hot, porque no guarda los ceros, solo los valores que realmente importan.

# Aquí usamos sparse=False para obtener una matriz densa más fácil de manipular con Pandas.
encoder = OneHotEncoder(sparse_output=False)

# Codificación One-Hot:
# encoder.fit_transform(data):
# fit: Aprende las categorías únicas en la columna Género
# (en este caso, "Hombre" y "Mujer").
# transform: Convierte los datos categóricos en columnas binarias.
# pd.DataFrame(...):
# Convierte el resultado de fit_transform (un array de NumPy) nuevamente en un DataFrame.
# encoder.get_feature_names_out():
# Genera los nombres de las nuevas columnas en función de las categorías únicas encontradas.
# Por ejemplo, genera las columnas Género_Hombre y Género_Mujer.
data_encoded = pd.DataFrame(encoder.fit_transform(data), columns=encoder.get_feature_names_out(['Género']))
print("Datos codificados con One-Hot Encoding:\n", data_encoded)



# Otro ejemplo agregando más categorías
# Supongamos que añadimos las cateogrías "Otro", "prefiero no decirlo":


# Datos con más categorías
data = pd.DataFrame({'Género': ['Hombre', 'Mujer', 'Otro', 'Prefiero no decirlo', 'Hombre', 'Otro']})

# Crear el codificador One-Hot
encoder = OneHotEncoder(sparse_output=False)  # Cambiar sparse_output para scikit-learn >=1.2.0
data_encoded = pd.DataFrame(encoder.fit_transform(data[['Género']]),
                            columns=encoder.get_feature_names_out(['Género']))

print("Datos codificados con One-Hot Encoding:\n", data_encoded)
