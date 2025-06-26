# Importación del Binarizer:
# Se importa Binarizer desde scikit-learn.
# Binarizer es una herramienta que se utiliza para transformar
# datos numéricos en datos binarios (0 o 1) en función de un umbral (threshold).
# Es útil cuando deseamos convertir datos continuos en datos discretos
# según un valor límite (umbral).
from sklearn.preprocessing import Binarizer
import pandas as pd

# Datos de ejemplo
data = pd.DataFrame({'Notas': [7, 4, 3, 5, 6]})

# Binarización con umbral 5
# Inicialización del Binarizer:
# Se crea un objeto binarizer utilizando la clase Binarizer y se le asigna
# un umbral de 5 (threshold=5).
# Este umbral es el valor de corte para convertir las notas en valores binarios.
# Si una nota es mayor o igual a 5, se convierte en 1. Si es menor que 5, se convierte en 0.
binarizer = Binarizer(threshold=5)

# Transformación de los Datos:
# binarizer.fit_transform(data):
# fit: Calcula el umbral (en este caso no es necesario porque ya lo hemos definido, pero es parte del proceso).
# transform: Aplica la binarización a los datos.
# Las notas que son mayores o iguales a 5 se convierten en 1, y las notas menores a 5 se convierten en 0.
# pd.DataFrame(...):
# Convierte el array resultante en un DataFrame de Pandas con una nueva columna llamada Notas Binarizadas.
data_binarized = pd.DataFrame(binarizer.fit_transform(data), columns=['Notas Binarizadas'])
print("Datos binarizados:\n", data_binarized)
