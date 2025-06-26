# Ejemplo
from sklearn.preprocessing import RobustScaler

# Datos de ejemplo
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [5, 15, 25]})
# Salida del dataframe original
print ("DataFrame original :\n", df)

# Escalar los datos con RobustScaler
scaler = RobustScaler()
df_robust = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("Datos escalados con RobustScaler:\n", df_robust)
