# Importamos librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Cargar dataset 
df = pd.read_csv('Ecommerce Customers.csv')

# Primer vistazo a los datos
print(df.head())
print(df.describe())

# Seleccionamos solo las columnas numéricas relevantes para análisis
variables_numericas = ['Avg_Session_Length', 'Time_on_App', 'Time_on_Website', 'Length_of_Membership', 'Yearly_Amount_Spent']
df_numericas = df[variables_numericas]

# Histogramas para ver distribución de variables numéricas
df_numericas.hist(bins=30, color='teal', edgecolor='black', figsize=(12,8))
plt.suptitle('Distribución de Variables Numéricas')
plt.show()

# Pairplot para observar relaciones entre variables numéricas
sns.pairplot(df_numericas, kind='scatter', plot_kws={'alpha':0.5, 'color':'blue'})
plt.suptitle('Relaciones entre Variables Numéricas', y=1.02)
plt.show()

# Mapa de calor de correlación entre variables numéricas
plt.figure(figsize=(8,6))
sns.heatmap(df_numericas.corr(), annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación entre Variables Numéricas')
plt.show()

# Gráfico de dispersión entre Time_on_App y Yearly_Amount_Spent
sns.scatterplot(x='Time_on_App', y='Yearly_Amount_Spent', data=df, alpha=0.6, color='darkorange')
plt.title('Tiempo en App vs Gastos Anuales')
plt.xlabel('Tiempo en App (minutos)')
plt.ylabel('Gastos Anuales ($)')
plt.grid(True)
plt.show()

# Gráfico de dispersión entre Time_on_Website y Yearly_Amount_Spent
sns.scatterplot(x='Time_on_Website', y='Yearly_Amount_Spent', data=df, alpha=0.6, color='green')
plt.title('Tiempo en Website vs Gastos Anuales')
plt.xlabel('Tiempo en Website (minutos)')
plt.ylabel('Gastos Anuales ($)')
plt.grid(True)
plt.show()

# Gráfico de regresión lineal entre Length_of_Membership y Yearly_Amount_Spent
sns.lmplot(x='Length_of_Membership', y='Yearly_Amount_Spent', data=df, scatter_kws={'alpha':0.4}, height=6, aspect=1.5)
plt.title('Regresión lineal: Duración de Membresía vs Gastos Anuales')
plt.show()
