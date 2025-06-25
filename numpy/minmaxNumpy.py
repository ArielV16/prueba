# EJEMPLOS DE NORMALIZACIÓN MAX-MIN/Z-SCORE

import numpy as np

####### Min-Max Normalization#######

# Arreglo 1D
array_1d = np.array([10, 20, 30, 40])
# Min-Max Normalization
min_val = np.min(array_1d)
max_val = np.max(array_1d)
array_minmax = (array_1d - min_val) / (max_val - min_val)
print("Arreglo Normalizado (Min-Max):", array_minmax)

# Arreglo 2D
array_2d = np.array([[10, 20], [30, 40]])
# Min-Max Normalization
min_val = np.min(array_2d)
max_val = np.max(array_2d)
array_minmax_2d = (array_2d - min_val) / (max_val - min_val)
print("Arreglo 2D Normalizado (Min-Max):\n", array_minmax_2d)

# Arreglo 3D
array_3d = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
# Min-Max Normalization
min_val = np.min(array_3d)
max_val = np.max(array_3d)
array_minmax_3d = (array_3d - min_val) / (max_val - min_val)
print("Arreglo 3D Normalizado (Min-Max):\n", array_minmax_3d)

# Min-Max Normalization por columna
min_val_col = np.min(array_2d, axis=0)
max_val_col = np.max(array_2d, axis=0)
array_minmax_col = (array_2d - min_val_col) / (max_val_col - min_val_col)
print("Normalización Min-Max Por Columna:\n", array_minmax_col)

# Min-Max Normalization por fila
min_val_fila = np.min(array_2d, axis=1).reshape(-1, 1) # ¿Qué pasa si omitimos reshape (-1,1?)
max_val_fila = np.max(array_2d, axis=1).reshape(-1, 1)
array_minmax_fila = (array_2d - min_val_fila) / (max_val_fila - min_val_fila)
print("Normalización Min-Max Por Fila:\n", array_minmax_fila)


####### Z-Score#######

# Z-Score Normalization 1D
media = np.mean(array_1d)
desviacion = np.std(array_1d)
array_zscore = (array_1d - media) / desviacion
print("Arreglo Normalizado (Z-Score) una dimensión:", array_zscore)

# Z-Score Normalization 2D
media = np.mean(array_2d)
desviacion = np.std(array_2d)
array_zscore_2d = (array_2d - media) / desviacion

print("Arreglo 2D Normalizado (Z-Score):\n", array_zscore_2d)

# Z-Score Normalization 3D
media = np.mean(array_3d)
desviacion = np.std(array_3d)
array_zscore_3d = (array_3d - media) / desviacion

print("Arreglo 3D Normalizado (Z-Score):\n", array_zscore_3d)


