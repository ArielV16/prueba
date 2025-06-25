#🧠 Desafío Final: Exploración Visual de Datos de E-Commerce
#Ahora que ya sabes cómo utilizar matplotlib y seaborn para visualizar datos y explorar relaciones entre variables, te proponemos este desafío.

#📦 Dataset
#Trabajaremos con un conjunto de datos real sobre clientes de comercio electrónico y su comportamiento en diferentes plataformas (sitio web, app móvil, etc.).

#Acceso al dataset:
#https://www.kaggle.com/datasets/iyadavvaibhav/ecommerce-customer-device-usage

#🎯 Objetivo
#Explora visualmente este conjunto de datos y responde las siguientes preguntas usando gráficos con matplotlib y seaborn:

#¿Qué variables podrían estar más relacionadas con el gasto anual de los clientes (Yearly Amount Spent)?

#time on app y time on app 

#¿Existen diferencias visibles entre los usuarios que usan más la App vs. el Website?



#¿Qué tipo de gráfico resulta más útil para observar correlaciones entre tiempo de uso y gasto?



#¿Cómo se distribuyen los datos para cada variable numérica? ¿Existen valores extremos?



#¿Puedes identificar visualmente una posible relación lineal entre alguna variable y el gasto anual?



#🧰 Instrucciones
#Carga los datos y explora su estructura.
#Selecciona un subconjunto de variables que te parezcan relevantes.
#Aplica gráficos de dispersión, diagramas de caja, mapas de calor, etc.
#Comenta cada paso que realices como lo hemos hecho en este notebook.




# Importamos las librerías necesarias:
# - pandas: para cargar y manipular datos
# - matplotlib.pyplot: para crear visualizaciones básicas
# - seaborn: para visualizaciones estadísticas más avanzadas
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


# 

sns.boxplot(
    x='Avatar',
    y='Yearly_Amount_Spent',
    hue='Avatar',
    data=df,
    palette="muted",
    legend=False
)

plt.title("Tiempo de los Usuarios en la website")

plt.xlabel("promedio de sesion")
plt.ylabel("tiempo de los usuarios")

plt.show()