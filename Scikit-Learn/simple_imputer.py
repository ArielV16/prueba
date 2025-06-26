# Ejemplo
# SimpleImputer: Herramienta de scikit-learn para manejar valores faltantes
#en datos.
#Permite reemplazar los valores faltantes con una estrategia definida,
#como la media, mediana, o un valor constante.
from sklearn.impute import SimpleImputer
# numpy: Biblioteca usada para trabajar con arrays
#y para representar valores faltantes con np.nan
import numpy as np
import pandas as pd

# Datos con valores faltantes
data = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
print ("DataFrame original :\n", data)

# Imputar con la media
# SimpleImputer se configura con la estrategia mean,
# lo que significa que los valores faltantes serán reemplazados por la media
# de cada columna.
# Otras estrategias disponibles:
# median: Usa la mediana.
# most_frequent: Usa el valor más frecuente.
# constant: Usa un valor constante especificado por el usuario.
imputer = SimpleImputer(strategy='mean')

# Imputación de Valores Faltantes:
# imputer.fit_transform(data):
# fit: Calcula la media de cada columna.
# transform: Reemplaza los valores faltantes por la media calculada.
# Los resultados se convierten nuevamente a un DataFrame con los mismos
# nombres de columnas.

data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

print("Datos después de la imputación con la media:\n", data_imputed)
