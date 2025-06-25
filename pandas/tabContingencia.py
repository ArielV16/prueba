# EJEMPLO DE APLICACIÓN DE TABLAS DE CONTINGENCIA SOBRE UN DATAFRAME

# Importar librería
import pandas as pd

# Crear un DataFrame de ejemplo
datos = {
    'Género': ['Femenino', 'Masculino', 'Femenino', 'Femenino', 'Masculino'],
    'Preferencia': ['A', 'B', 'A', 'C', 'B'],
    'Edad': ['18-25', '26-35', '18-25', '18-25', '26-35']
}
df = pd.DataFrame(datos)

print("DataFrame:\n", df)

# Tabla de contingencia básica
# Crear una tabla de contingencia para relación entre Género y Preferencia:
tabla = pd.crosstab(df['Género'], df['Preferencia'])
print("Tabla de contingencia básica:\n", tabla)

# Agregar totales
# Incluir totales en filas y columnas con el argumento margins=True:
tabla_totales = pd.crosstab(df['Género'], df['Preferencia'], margins=True)
print("Tabla de contingencia con totales:\n", tabla_totales)

# Tablas de contingencia con más de dos Variables
# Analizar tres o más variables categóricas
# Ejemplo: Relación entre Género, Preferencia, y Edad:
tabla_multi = pd.crosstab([df['Género'], df['Edad']], df['Preferencia'], margins=True)
print("Tabla de contingencia múltiple:\n", tabla_multi)

