# Ejemplo
from sklearn.preprocessing import StandardScaler

# Datos de ejemplo
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [5, 15, 25]})
# Salida del dataframe original
print ("DataFrame original :\n", df)

# Escalar los datos con media=0 y std=1
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("Datos escalados con StandardScaler:\n", df_standardized)
