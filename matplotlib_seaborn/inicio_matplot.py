# Importamos las librerías necesarias:
# - pandas: para cargar y manipular datos
# - matplotlib.pyplot: para crear visualizaciones básicas
# - seaborn: para visualizaciones estadísticas más avanzadas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Esta línea mágica permite que los gráficos de Matplotlib se muestren directamente dentro del notebook.
# Aunque en Google Colab suele estar activada por defecto, es buena práctica incluirla.
#usar solo en colab o jupyter
#%matplotlib inline

# Cargamos el conjunto de datos desde una URL pública.
# Este dataset contiene información sobre consumo de combustible y emisiones de CO2
# para vehículos ligeros vendidos en Canadá.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"


# Usamos pandas para leer el archivo CSV y almacenarlo en un DataFrame llamado df
df = pd.read_csv(url)

# Mostramos las primeras 5 filas del DataFrame para tener una idea general del contenido
df.head()

# Mostramos un resumen estadístico de las variables numéricas del DataFrame
df.describe()
# El método describe() genera un resumen estadístico de las columnas numéricas del conjunto de datos. Esto incluye:
# count: cuántos valores no nulos hay por columna.
# mean: el promedio de los valores.
# std: la desviación estándar (mide cuán dispersos están los datos respecto del promedio).
# min y max: el valor mínimo y máximo encontrados.
# 25%, 50%, 75%: los percentiles (cuartiles), útiles para entender la distribución de los datos.
# Es muy útil para tener una primera visión general del conjunto de datos,
# identificar posibles valores extremos y entender la escala de las variables antes de analizarlas más a fondo.


# Creamos un histograma de la variable CO2EMISSIONS, que muestra la distribución de las emisiones de CO2
plt.hist(df['CO2EMISSIONS'], bins=30, color='steelblue', edgecolor='black')

# Título del gráfico
plt.title("Histograma de Emisiones de CO2")

# Etiqueta del eje X (valores de emisiones en gramos por kilómetro)
plt.xlabel("CO2 (g/km)")

# Etiqueta del eje Y (cantidad de vehículos con ese rango de emisiones)
plt.ylabel("Cantidad de vehículos")

# Mostramos el gráfico
plt.show()

# Este histograma nos permite ver cómo se distribuyen las emisiones de CO₂ en el conjunto de datos.
# El parámetro bins=30 divide el rango de valores en 30 grupos (o barras).
# Los ejes indican cuántos vehículos caen en cada rango de emisiones.
# Nos ayuda a identificar si la mayoría de los vehículos emiten poco, mucho o están distribuidos uniformemente.

# Seleccionamos solo algunas columnas del DataFrame original para enfocarnos en las variables que más nos interesan
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

# Mostramos una muestra aleatoria de 9 filas del nuevo DataFrame cdf
cdf.sample(9)

# La variable cdf contiene un subconjunto del DataFrame original df,
# en el que seleccionamos solo las columnas que podrían tener una relación directa con las emisiones de CO2:
# ENGINESIZE: tamaño del motor (en litros).
# CYLINDERS: número de cilindros del motor.
# FUELCONSUMPTION_COMB: consumo de combustible combinado (ciudad y carretera).
# CO2EMISSIONS: emisiones de dióxido de carbono (g/km).
# sample(9) permite ver una selección aleatoria de 9 registros del DataFrame cdf.
# Esto es útil para explorar diferentes casos del conjunto de datos sin mostrarlo todo.

# Crear histogramas de algunas variables para observar su distribución
# Esto nos permite conocer la forma de los datos antes de aplicar modelos
features = ['CYLINDERS','ENGINESIZE','FUELCONSUMPTION_COMB','CO2EMISSIONS']
df[features].hist(figsize=(10,8))
plt.suptitle('Distribución de Variables Numéricas')
plt.show()



# Creamos un gráfico de dispersión (scatter plot) con las siguientes configuraciones:
# - df.FUELCONSUMPTION_COMB: valores del eje X (consumo combinado de combustible)
# - df.CO2EMISSIONS: valores del eje Y (emisiones de CO2)
# - color='blue': define el color de los puntos en el gráfico
# - alpha=0.5: define la opacidad de los puntos (0 totalmente transparente, 1 totalmente opaco)
#   Usar una alpha más baja permite ver mejor la concentración de puntos cuando hay muchos datos.
plt.scatter(df.FUELCONSUMPTION_COMB, df.CO2EMISSIONS, color='blue', alpha=0.5)

# Etiquetamos el eje X para indicar que representa el consumo de combustible en condiciones combinadas.
plt.xlabel('Consumo combinado (L/100 km)')

# Etiquetamos el eje Y para indicar que representa las emisiones de dióxido de carbono por kilómetro.
plt.ylabel('Emisiones de CO2 (g/km)')

# Agregamos un título descriptivo para que el gráfico tenga contexto sin necesidad de explicación adicional.
plt.title('Relación entre Consumo y Emisiones')

# Agregamos una cuadrícula de fondo para facilitar la lectura de los valores de los ejes y mejorar la interpretación.
plt.grid(True)

# Finalmente, renderizamos y mostramos el gráfico en pantalla.
plt.show()

# Usamos seaborn para crear un gráfico de pares (pairplot), que genera una matriz de gráficos
# donde cada celda representa una comparación entre dos variables numéricas.

# Este tipo de visualización es útil para:
# - Detectar relaciones lineales o no lineales entre variables.
# - Identificar posibles correlaciones visuales.
# - Observar patrones, agrupamientos o valores atípicos.
# - Tener una visión general del comportamiento conjunto de todas las variables numéricas seleccionadas.

# df[features] contiene las columnas que seleccionamos previamente como relevantes.
# kind='scatter' indica que queremos usar diagramas de dispersión en cada celda de comparación.
# plot_kws={'alpha': 0.4} configura la transparencia de los puntos para que, cuando hay muchos puntos superpuestos,
# sea más fácil distinguir las áreas de mayor densidad (zonas con más datos agrupados).

sns.pairplot(df[features], kind='scatter', plot_kws={'alpha': 0.4})

# Agregamos un título general al conjunto de gráficos con plt.suptitle().
# El argumento y=1.02 eleva un poco el título por encima de la figura para que no se sobreponga con los gráficos.
plt.suptitle('Relaciones entre Variables', y=1.02)

# Finalmente, mostramos en pantalla la matriz de gráficos generada.
plt.show()

# Si vemos una tendencia clara (por ejemplo, una nube de puntos con pendiente ascendente),
# eso sugiere una posible correlación positiva entre esas variables. E
# Esto es muy útil antes de aplicar modelos como la regresión.


# Usamos seaborn para crear un gráfico de dispersión con una línea de regresión lineal ajustada automáticamente.
# Este tipo de gráfico es útil para identificar relaciones lineales entre dos variables numéricas.
# En el eje x colocamos el tamaño del motor (ENGINESIZE) y en el eje y las emisiones de CO2.
# 'scatter_kws' permite ajustar detalles del gráfico de dispersión, en este caso la transparencia de los puntos.
sns.lmplot(x='ENGINESIZE', y='CO2EMISSIONS', data=df, scatter_kws={'alpha': 0.3})

# Agregamos un título descriptivo al gráfico
plt.title('Regresión Lineal entre Tamaño del Motor y Emisiones')

# Mostramos el gráfico
plt.show()

# Creamos un gráfico de dispersión (scatter plot) para visualizar la relación entre el consumo de combustible en ciudad
# y las emisiones de CO2. Cada punto representa un vehículo.
plt.scatter(df['FUELCONSUMPTION_CITY'], df['CO2EMISSIONS'], alpha=0.5)

# Establecemos el título del gráfico
plt.title("Consumo en ciudad vs Emisiones de CO2")

# Etiquetamos el eje X con la variable de consumo de combustible en ciudad (litros cada 100 km)
plt.xlabel("Consumo (L/100km) en ciudad")

# Etiquetamos el eje Y con la variable de emisiones de CO2 en gramos por kilómetro
plt.ylabel("CO2 (g/km)")

# Activamos la cuadrícula para facilitar la lectura visual de las relaciones entre los valores
plt.grid(True)

# Mostramos el gráfico en pantalla
plt.show()


# Utilizamos Seaborn para crear un gráfico de caja (boxplot), una herramienta muy útil para analizar
# la distribución de una variable numérica (en este caso, CO2EMISSIONS) agrupada por una variable categórica (número de cilindros).

# ¿Qué nos muestra este gráfico?
# - La línea dentro de cada caja representa la mediana de las emisiones para ese número de cilindros.
# - Los bordes de la caja muestran el primer y tercer cuartil (Q1 y Q3), es decir, donde se concentra el 50% central de los datos.
# - Las "bigotes" (líneas que salen de la caja) representan la extensión de los datos sin considerar los valores atípicos.
# - Los puntos que aparecen fuera de los bigotes se consideran outliers o valores atípicos.

# Para evitar advertencias de futuras versiones de Seaborn, especificamos explícitamente la variable que define el color (hue).
# En este caso, usamos la misma variable categórica 'CYLINDERS_CAT' tanto en 'x' como en 'hue'.
# Además, desactivamos la leyenda ya que el eje X ya indica las categorías.

sns.boxplot(
    x='CYLINDERS_CAT',           # Variable categórica en el eje X (convertida a string)
    y='CO2EMISSIONS',            # Variable numérica en el eje Y
    hue='CYLINDERS_CAT',         # Indicamos que la coloración se basa también en los cilindros
    data=df,                     # Dataset que contiene los datos
    palette="Set2",              # Paleta de colores amigable
    legend=False                 # Desactivamos la leyenda para evitar redundancia
)

# Título del gráfico para indicar claramente lo que se está visualizando
plt.title("Distribución de Emisiones por Nº de Cilindros")

# Etiqueta del eje X que representa las categorías de cilindros
plt.xlabel("Nº de cilindros")

# Etiqueta del eje Y que indica el valor numérico de las emisiones
plt.ylabel("CO2 (g/km)")

# Mostrar el gráfico en pantalla
plt.show()



## Reflexión: ¿Qué tipo de gráfico usar?

#| Tipo de gráfico | ¿Cuándo usarlo? |
#|-----------------|-----------------|
#| Histograma | Para ver cómo se distribuye una variable numérica |
#| Barras | Para comparar categorías |
#| Dispersión | Para analizar relaciones entre dos variables numéricas |
#| Boxplot | Para ver rangos, medianas y valores extremos en una variable |

#Ahora que sabes qué tipos de gráficos existen, tiene sentido aprender **cómo generarlos usando librerías específicas**.




# Creamos un histograma para ver cómo se distribuyen las emisiones de CO2 entre los vehículos

# Usamos la función hist() de matplotlib para graficar los datos de la columna 'CO2EMISSIONS'
# 'bins=30' divide los valores en 30 rangos o intervalos
# 'color' define el color de las barras y 'edgecolor' el color del borde de cada barra
plt.hist(df['CO2EMISSIONS'], bins=30, color='teal', edgecolor='black')

# Título del gráfico
plt.title("Distribución de Emisiones de CO2")

# Etiqueta del eje X: muestra los valores de CO2 emitido
plt.xlabel("CO2 emitido (g/km)")

# Etiqueta del eje Y: muestra la cantidad de vehículos que tienen ese nivel de emisión
plt.ylabel("Cantidad de vehículos")

# Agrega una cuadrícula para facilitar la lectura del gráfico
plt.grid(True)

# Muestra el gráfico en pantalla
plt.show()

# Este gráfico es útil para ver si las emisiones de CO₂ están concentradas en un rango específico
# o si están muy dispersas.
# Nos da una primera idea del comportamiento general de los datos antes de aplicar modelos más complejos.


# Creamos un diagrama de dispersión (scatter plot) para analizar la relación entre el tamaño del motor y las emisiones de CO2

# Usamos 'ENGINESIZE' como eje X (tamaño del motor en litros)
# Usamos 'CO2EMISSIONS' como eje Y (emisiones de CO2 en gramos por kilómetro)
# 'alpha=0.5' hace los puntos semi-transparentes para facilitar la visualización cuando hay muchos datos
# 'color' define el color de los puntos en el gráfico
plt.scatter(df['ENGINESIZE'], df['CO2EMISSIONS'], alpha=0.5, color='darkorange')

# Título del gráfico
plt.title("Relación entre tamaño del motor y emisiones de CO2")

# Etiqueta del eje X
plt.xlabel("Tamaño del motor (L)")

# Etiqueta del eje Y
plt.ylabel("Emisiones de CO2 (g/km)")

# Mostrar una cuadrícula para facilitar la lectura del gráfico
plt.grid(True)

# Mostrar el gráfico en pantalla
plt.show()

# Este gráfico nos ayuda a ver si existe una relación lineal entre el tamaño del motor y las emisiones.
# A simple vista, si los puntos siguen una línea ascendente, podríamos inferir que
# motores más grandes tienden a emitir más CO₂. Esta visualización es muy útil
# como paso previo a aplicar un modelo de regresión.


# Usamos Seaborn para crear un histograma con una curva de densidad (kde=True)
# Esto permite visualizar la distribución de las emisiones de CO2 de forma más suave y detallada

# 'df['CO2EMISSIONS']' es la serie de datos a graficar
# 'kde=True' agrega la curva de densidad que ayuda a ver la forma de la distribución
# 'color' define el color de las barras, y 'edgecolor' agrega bordes a cada barra para mejor visibilidad
sns.histplot(df['CO2EMISSIONS'], kde=True, color='red', edgecolor='black')

# Título del gráfico
plt.title("Distribución de emisiones de CO2 (Seaborn)")

# Etiqueta del eje X
plt.xlabel("CO2 Emissions (g/km)")

# Etiqueta del eje Y
plt.ylabel("Frecuencia")

# Mostrar el gráfico
plt.show()

# A diferencia de matplotlib, seaborn.histplot() incluye de forma opcional la estimación de densidad (kde),
# lo que permite una interpretación más detallada de la forma de la distribución, ideal para análisis exploratorios.






# Analizamos ahora si hay relación entre el consumo en ciudad y las emisiones

sns.jointplot(x="FUELCONSUMPTION_CITY", y="CO2EMISSIONS", data=df, alpha=0.5, color="purple")

# Este gráfico combina:
# - Un scatter plot (diagrama de dispersión)
# - Un histograma para cada variable en los márgenes
# Esto nos ayuda a ver tanto la distribución de cada variable como su relación.




# Paso 1: Seleccionamos algunas variables numéricas relevantes para el análisis.
# Estas variables tienen sentido porque están relacionadas entre sí desde una perspectiva de consumo y emisiones.
variables = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']

# Paso 2: Usamos la función pairplot de Seaborn para crear un gráfico de pares (pairplot).
# ¿Qué hace este gráfico?
# - Genera una matriz de gráficos de dispersión (scatterplots) que compara cada variable con todas las otras.
# - Por ejemplo: crea un gráfico entre ENGINE SIZE y CYLINDERS, otro entre ENGINE SIZE y CO2EMISSIONS, y así sucesivamente.
# - Además, en la diagonal muestra un histograma de cada variable, para entender su distribución individual.
# El parámetro 'alpha=0.4' hace que los puntos sean parcialmente transparentes,
# lo cual facilita la visualización cuando hay muchos datos sobrepuestos.

sns.pairplot(df[variables], kind='scatter', plot_kws={'alpha': 0.4})

# Paso 3: Agregamos un título general para todo el conjunto de gráficos.
# El parámetro 'y' ajusta la posición vertical del título para que no tape ningún gráfico.
plt.suptitle("Relación entre variables", y=1.02)

# Paso 4: Mostramos el gráfico completo
plt.show()





# Paso 1: Calculamos y visualizamos la matriz de correlación.
# ¿Qué es una correlación?
# Es una medida estadística que indica la fuerza y la dirección de la relación lineal entre dos variables numéricas.

# - El valor de la correlación varía entre -1 y 1:
#   + 1   → correlación positiva perfecta: cuando una variable sube, la otra también sube en la misma proporción.
#   - 1   → correlación negativa perfecta: cuando una variable sube, la otra baja en la misma proporción.
#     0   → no hay correlación lineal entre las variables.

# Paso 2: Establecemos el tamaño de la figura para que se vea bien
plt.figure(figsize=(8, 6))

# Paso 3: Usamos un mapa de calor (heatmap) de Seaborn para representar la matriz de correlación.
# - `annot=True` muestra los valores numéricos dentro de cada celda.
# - `cmap='coolwarm'` es una paleta de colores que va del azul (negativo) al rojo (positivo).
# - `fmt=".2f"` limita los números a dos decimales.
sns.heatmap(df[variables].corr(), annot=True, cmap='coolwarm', fmt=".2f")

# Paso 4: Agregamos un título al gráfico
plt.title("Matriz de correlación entre variables")

# Paso 5: Mostramos el gráfico
plt.show()

# Por qué es importante analizar la matriz de correlación?
# Permite identificar relaciones fuertes entre variables, lo cual es muy útil en machine learning para:
# Seleccionar variables que tienen mayor poder predictivo (por ejemplo, ENGINESIZE está muy correlacionada con CO2EMISSIONS).
# Detectar variables redundantes (por ejemplo, si dos variables están muy correlacionadas, podrían aportar información similar).
# Es una excelente herramienta de análisis exploratorio de datos (EDA) antes de construir cualquier modelo.






