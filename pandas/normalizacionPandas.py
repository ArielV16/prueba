# EJEMPLO DE MÉTODOS DE NORMALIZACIÓN EN PANDAS

# Importar librería
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Matemáticas': [70, 85, 90, 95, 100],
    'Física': [88, 76, 92, 85, 80],
    'Historia': [75, 88, 70, 90, 95]
}
df = pd.DataFrame(data)

# Normalización Min-Max
df_minmax = (df - df.min()) / (df.max() - df.min())
print("Normalización Min-Max:\n", df_minmax)

# Normalización Z-Score
df_zscore = (df - df.mean()) / df.std()
print("Normalización Z-Score:\n", df_zscore)


