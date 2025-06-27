#Importación de librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# 📦 Carga del archivo (debe estar en el mismo directorio que este notebook)
df = pd.read_csv("Ecommerce Customers.csv")

# Primer vistazo a los datos
print(df.head())
print(df.info())
print(df.describe())

# Selección de variables relevantes
variables = ['Avg_Session_Length', 'Time_on_App', 'Time_on_Website', 
            'Length_of_Membership', 'Yearly_Amount_Spent']
df_segundo = df[variables]

# Gráfico de dispersión: Avg_Session_Length vs Time_on_App
sns.scatterplot(x='Avg_Session_Length', y='Time_on_App', data=df_segundo, color="red", alpha=0.5)
plt.title('Relación entre Promedio de Sesión y Tiempo en la App')
plt.xlabel('Promedio de Sesión')
plt.ylabel('Tiempo en App')
plt.grid(True)
plt.show()

# Gráfico de dispersión: Avg_Session_Length vs Time_on_Website
sns.scatterplot(x='Avg_Session_Length', y='Time_on_Website', data=df_segundo, color="blue", alpha=0.5)
plt.title('Relación entre Promedio de Sesión y Tiempo en Website')
plt.xlabel('Promedio de Sesión')
plt.ylabel('Tiempo en Website')
plt.grid(True)
plt.show()

# Diagrama de caja para todas las variables numéricas
sns.boxplot(data=df_segundo, palette="pastel")
plt.title("Distribución y Outliers en Variables Numéricas")
plt.xticks(rotation=45)
plt.show()

# Mapa de calor de correlaciones
plt.figure(figsize=(10,8))
sns.heatmap(df_segundo.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Mapa de Correlación entre Variables")
plt.show()

# Regresión lineal: Length_of_Membership vs Gasto Anual
sns.lmplot(x='Length_of_Membership', y='Yearly_Amount_Spent', data=df_segundo, height=6, aspect=1.5)
plt.title("Relación Lineal entre Tiempo de Membresía y Gasto Anual")
plt.show()

# Regresión lineal: Time_on_App vs Gasto Anual
sns.lmplot(x='Time_on_App', y='Yearly_Amount_Spent', data=df_segundo, height=6, aspect=1.5)
plt.title("Relación Lineal entre Tiempo en App y Gasto Anual")
plt.show()

# Clasificación de usuarios por preferencia de uso (App vs Website)
df['Preferred_Device'] = df['Time_on_App'] > df['Time_on_Website']
sns.boxplot(x='Preferred_Device', y='Yearly_Amount_Spent', data=df, palette="Set2")
plt.xticks([0,1], ['Website', 'App'])
plt.title("Gasto Anual según Plataforma Preferida")
plt.xlabel("Preferencia de Uso")
plt.ylabel("Gasto Anual")
plt.show()
