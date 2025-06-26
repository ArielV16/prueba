import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Cargamos el conjunto de datos con la url publica 

url = "https://www.kaggle.com/datasets/iyadavvaibhav/ecommerce-customer-device-usage"


df = pd.read_csv("Ecommerce Customers.csv")


print(df.head())

print(df.describe())

#🧰 Instrucciones

#Selecciona un subconjunto de variables que te parezcan relevantes.
#Aplica gráficos de dispersión, diagramas de caja, mapas de calor, etc.
#Comenta cada paso que realices como lo hemos hecho en este notebook.

# Indicamos las variables que usaremos, indicamos el color que usaremos y la densidad del mismo
plt.scatter(df.Avg_Session_Length, df.Time_on_App, color="red", alpha=0.5)

# Etiquetamos el eje X para indicar que representa el promedio de sesion de los usuarios
plt.xlabel('promedio de sesion')

# Etiquetamos el eje Y para indicar que representa el tiempo usando la app de los usuarios
plt.ylabel('tiempo en la app')


# Agregamos un titulo al grafico
plt.title('Tiempo promedio de los Usuarios usando la App')

# Agregamos una cuadrícula de fondo para facilitar la lectura de los valores de los ejes y mejorar la interpretación.
plt.grid(True)

# Finalmente, renderizamos y mostramos el gráfico en pantalla.
plt.show()


###funciona mas no se ven bien las cajas 

sns.boxplot(
    x='Avatar',
    y='Yearly_Amount_Spent',
    hue='Avatar',
    data=df,
    palette="muted",
    legend=False
)

plt.title("Tiempo de los Usuarios en la website")
# etiquetamos el eje X
plt.xlabel("promedio de sesion")
# etiquetamos el eje Y 
plt.ylabel("tiempo de los usuarios")

#renderizamos el grafico
plt.show()

#mapa de calor
#creo una lista con las variables 
variables=['Avg_Session_Length', 'Time_on_App', 'Time_on_Website']
#le damos un tamaño
plt.figure(figsize=(8,6))

# - creamos el mapa de calor con sns.heatmap (importado de seaborn) 
# - 'annot=True' muestra los valores numéricos dentro de cada celda.
# - 'cmap='coolwarm'' es una paleta de colores que va del azul (negativo) al rojo (positivo).
# - 'fmt=".2f"' limita los números a dos decimales.
sns.heatmap(df[variables].corr(), annot=True, cmap='coolwarm', fmt=".2f")

#agregamos un titulo 
plt.title("correlacion entre sesion, tiempo en app y website")

#renderizamos el grafico
plt.show()


