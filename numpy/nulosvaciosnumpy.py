# EJEMPLO DE MANEJO DE DATOS NULOS O VACÍOS

import numpy as np

############# Ejemplo arreaglo 1D ###########
# Crear un arreglo 1D con datos nulos
array_1d = np.array([1, 2, np.nan, 4, 5])
# Identificar datos nulos
print("Datos nulos (True indica np.nan):", np.isnan(array_1d))
# Rellenar datos nulos con la media
array_1d_filled = np.where(np.isnan(array_1d), np.nanmean(array_1d), array_1d)
print("Arreglo con datos nulos reemplazados por la media:", array_1d_filled)

############# Ejemplo arreaglo 2D ###########
# Crear un arreglo 2D con datos nulos
array_2d = np.array([[1, 2, np.nan], [4, np.nan, 6]])
# Identificar datos nulos
print("Datos nulos:\n", np.isnan(array_2d))
# Eliminar filas con datos nulos
array_2d_no_nans = array_2d[~np.isnan(array_2d).any(axis=1)] # El operador ~ invierte un arreglo booleano:
print("Arreglo sin filas con datos nulos:\n", array_2d_no_nans)
# Rellenar datos nulos con un valor específico (por ejemplo, 0)
array_2d_relleno = np.nan_to_num(array_2d, nan=0)
print("Arreglo con datos nulos reemplazados por 0:\n", array_2d_relleno)

############# Ejemplo arreaglo 3D ###########

# Crear un arreglo 3D con datos nulos
array_3d = np.array([[[1, 2, np.nan], [4, 5, 6]],
                     [[np.nan, 8, 9], [10, 11, np.nan]]])
# Identificar datos nulos
print("Datos nulos en 3D:\n", np.isnan(array_3d))
# Rellenar datos nulos con la mediana
mediana = np.nanmedian(array_3d)
array_3d_relleno = np.where(np.isnan(array_3d), mediana, array_3d)
print("Arreglo 3D con datos nulos reemplazados por la mediana:\n", array_3d_relleno)