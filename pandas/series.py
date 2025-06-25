# EJEMPLO 2 DE CREACIÓN Y MANIPULACIÓN DE UNA SERIE CON PANDAS

# Importar pandas
import pandas as pd

# Crear una Serie de ejemplo: notas de un estudiante
notas = pd.Series([85, 90, 78, 92, 88], index=["Matemáticas", "Física", "Química", "Biología", "Historia"])

# Acceder a un elemento por índice
print("\nNota de Matemáticas:")
print(notas["Matemáticas"])

# Filtrar notas mayores a 85
print("\nNotas mayores a 85:")
print(notas[notas > 85])

# Sumar todas las notas
print("\nSuma total de las notas:")
print(notas.sum())

# Calcular el promedio de las notas
print("\nPromedio de las notas:")
print(notas.mean())

# Ordenar las notas de mayor a menor
print("\nNotas ordenadas de mayor a menor:")
print(notas.sort_values(ascending=False)) # ascending=False; para ordenar de mayor a menor
# print(notas.sort_values())
# Agregar una nueva asignatura
notas["Geografía"] = 80
print("\nSerie después de agregar Geografía:")
print(notas)

# Eliminar una asignatura
#notas = notas.drop("Historia")
#print("\nSerie después de eliminar Historia:")
#print(notas)

# Verificar si existe un índice específico
print("\n¿Existe 'Física' en la Serie?")
print("Física" in notas)

# Operaciones matemáticas: incrementar todas las notas en 5 puntos
print("\nNotas incrementadas en 5 puntos:")
print(notas + 5)

# Transformar las notas a porcentajes (escala 0-100)
print("\nNotas como porcentajes:")
print((notas / 100) * 100)
