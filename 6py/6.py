#Analitica 
#OPEN AI SE PAGARA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#gráficos básicos incorporados en PANDAS
df1 = pd.read_csv('df1', index_col=0)

df2 = pd.read_csv('df2')
#print(df2.info())

df3 = pd.read_csv('df3')
#print(df2.info())

#crear histograma a partir del df - si hay seaborn lo toma como base
#df1['A'].hist()
#plt.show()
#df1['A'].plot.hist()
#plt.show()
#manera alterna B
#df1['A'].plot(kind='hist',              bins=50 )
#plt.show()
#euristica no es exacto pero es desente 
##Tipos de plots sia born
tips = sns.load_dataset('tips')
print(tips.shape)
tips.head()
"""
# gráfico de líneas
tips['total_bill'].plot(kind="hist")
plt.title('Total de la Cuenta a lo Largo del Tiempo')
plt.show()

# área
df2.plot.area(alpha=0.6)
plt.show()
# área: manera alterna MEJOR FORMA
df2.plot(kind='area',
         alpha=0.6)
plt.show()
"""
# barras: en paralelo, con recorte de filas
df3_p10 = df3.iloc[:10] #iloc si excluye al ultimo 10 
#df3_p10.plot(kind='bar') # alternativa: df3_p10.plot.bar()

# barra apilada - haciendo recorte de filas
df3_p10.plot(kind='bar',
             stacked=True #apila
             )
    # alternativa: df3_p10.plot.bar(stacked=True)
plt.show()

# series de tiempo: alternativa
df1.plot(kind='line',
         y='C')
plt.show()

# scatter (nube de puntos)
df1.plot(kind='scatter',
         x='A', y='C')
# alternativa: df1.plot.scatter(x='A', y='C')

# boxplot (cajas y vigotes)
df3.plot(kind='box')

#####
#1. Crear un Dataframe de Pandas que contenga
#Columna NATURAL - Numeros naturales del 1 al 20
#Columna PRIMOS - Los primeros 20 números primos

import pandas as pd

a = [x for x in range(1,21)]
#print(a)
b = primos = [ #by chat-gpt
    x for x in range(2, 100)
    if all(x % y != 0 for y in range(2, x)) #devuelve True si todo es True
][:20]

df = pd.DataFrame({
    "naturales": a,
    "primos" : b
})
print(df)

#######MATPLOTLIB
# Crear datos para el gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear el gráfico
plt.plot(x, y)

plt.title('Gráfico de Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.show()

#Barra Vertical
# Crear datos para el gráfico
frutas = ['Manzanas', 'Plátanos', 'Naranjas', 'Peras']
cantidad = [20, 25, 15, 30]
# Crear el gráfico de barras verticales
plt.bar(frutas, cantidad)
plt.title('Cantidad de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Cantidad')
plt.show()

#Barra Horizontal
# Crear el gráfico de barras horizontales
plt.barh(frutas, cantidad)
plt.title('Cantidad de Frutas')
plt.xlabel('Cantidad')
plt.ylabel('Frutas')
plt.show()

#Pie
# Crear el gráfico de torta
plt.pie(cantidad, labels=frutas, autopct='%1.1f%%') #porcentaje dentro de pie
plt.title('Proporción de Frutas')
plt.show()

#Histograma
# Crear datos para el histograma
datos = np.random.normal(0, 1, 1000) #siempre es causiana normal 

# Crear el histograma
plt.hist(datos, bins=20)

plt.title('Histograma de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()
#Nube de puntos (scatter plot)

# Crear datos para el gráfico de dispersión
x = np.random.rand(50)
y = np.random.rand(50)

# Crear el gráfico de dispersión
plt.scatter(x, y)

plt.title('Gráfico de Dispersión')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#####SEABORN

# algunos datasets están pre-cargados en Seaborn (ej 'tips')
tips = sns.load_dataset('tips')
tips.head()

#scatterplot (nube de puntos)
sns.scatterplot(data=tips,
                x='total_bill', y='tip')

plt.title('Propina vs Total de la Cuenta')

plt.show()
#Histplot
# Crear un gráfico displot
sns.histplot(data=tips, x='total_bill',
             kde=True, #grafico de curva sobre
             bins='auto'
             )
plt.title('Distribución del Total de la Cuenta')
plt.show()

##Displot
"""
para distribución de datos numéricos
principales: histograma, kde, ecdf
alternativa (pronto será inválida): sns.distplot()"""
# Crear un gráfico displot
sns.displot(data=tips,
            x='total_bill',
            kind='hist', # hist (defeault), ecdf, kde
            kde=True #solo se usa en hist, los demas False o no corren
            )
plt.title('Distribución del Total de la Cuenta')
plt.show()

## clase 08/05

#Plots de distribución multivariable
sns.scatterplot(data=tips,
                x='total_bill'
                , y='tip'
                )
plt.title('Propina vs Total de la Cuenta')
plt.show()

#Jointplot
# Crear un gráfico jointplot
sns.jointplot(data=tips,
              x='total_bill', y='tip')
plt.show()

#Relplot: para scatter y line
sns.relplot(data=tips,
            x='total_bill', y='tip',
            kind='scatter', # opciones: scatter (default) y line
            style='time',
            size='size',
            hue='smoker'
            )
plt.show()

sns.relplot(data=tips,
            x='day', y='total_bill',
            kind = 'line',
            errorbar=(None) # probar con 'ci' y None
            )
plt.show()

#Regplot para regresión, incluye línea de ajuste por defecto

# Crear un gráfico de regresión
sns.regplot(data=tips,
            x='total_bill',
            y='tip'
            )

plt.title('Propina vs Total de la Cuenta') #permite ver como van los puntos 
plt.show()

##Pairplot
#matriz de gráficos entre varias variables

# Crear un gráfico pairplot, varios graficos int y float columns se consideran
sns.pairplot(tips)
plt.show()

# Usar parámetro hue (usa var categórica)
sns.pairplot(tips,
             hue='sex')
plt.show()

##Heatmap, primero se optime correlaciones

# Requiere seleccionar solo columnas numéricas
numeric_tips = tips.select_dtypes(include='number') #solo "number"

corr = numeric_tips.corr() # Crear la matriz de correlación

# Crear un gráfico heatmap
sns.heatmap(corr, cmap='coolwarm', annot=True) #revisar esto
plt.title('Matriz de Correlación')
plt.show()

##Plots de categorización

# Crear un gráfico barplot
sns.barplot(data=tips,
            x='day', y='total_bill')

plt.title('Total de la Cuenta por Día')

plt.show()

##Countplot, una sola variable

# Crear un gráfico countplot
sns.countplot(data=tips,
              x='day')
plt.title('Conteo de Observaciones por Día')
plt.show()

##Boxplot, Para la distribución de una variable numérica a través de cuartiles.

# Crear un gráfico boxplot
sns.boxplot(data=tips,
            x='day', y='total_bill')

plt.title('Distribución del Total de la Cuenta por Día')
plt.show()

#Swarmplot similar al violinplot, pero, en lugar de la distribución, muestra los puntos de datos individuales

# Crear un gráfico swarmplot
sns.swarmplot(data=tips,
              x='day', y='total_bill')
plt.title('Distribución del Total de la Cuenta por Día')
plt.show()
#Catplot: generaliza para varios tipos de gráficos categóricos
#incluye: 'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'

sns.catplot(data=tips,
            kind='count',
            x='day')
plt.show()

#Estilos  opciones: dark, darkgrid, ticks, whitegrid,

sns.set_style("ticks") #se guarda pára tod lo que sigue
sns.countplot(data=tips, x='smoker')
plt.show()
sns.set_context("talk") # paper, notebook, talk, poster
sns.countplot(data=tips, x='day')
plt.show()