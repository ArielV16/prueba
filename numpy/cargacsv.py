import numpy as np

# Cargar los datos desde el archivo CSV (sin la columna 'Estudiante_ID')
datos = np.genfromtxt("estudiantes_notas.csv", delimiter=",", skip_header=1, usecols=(1, 2, 3))

print("Datos cargados:\n", datos)
print("Forma de los datos:", datos.shape)

