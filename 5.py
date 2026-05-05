# EMPEZAMO EL DIA 04/05 import requests
import requests #permite conectar con servidores

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()

with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

#recordar parsing en fechas para pasar de str a fecha 
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")
print("shape: ", nba.shape)
print(nba.head(10))

print('temporadas: ', nba['year_id'].unique())
print('posibles resultados: ', nba['game_result'].unique())
print('ligas: ', nba['lg_id'].unique())

print(nba[nba['lg_id'] == 'ABA'] )#mascara booleana al todo el dataset

print(nba['year_id'][nba['lg_id']=='ABA'])#mascara bolleana a una sola columna

##IMPORTANTE siempre se usa nba.info() y d

#tipos de datos por columnas
# lo más común a fijarse: fechas, índices
nba.info()
# stats
print("viene describe")
print(nba.describe())#.T
print(nba.describe().T) #se cambia filas por columnas (visualizacion)

# Exploración de datos
print(nba["team_id"].value_counts()) #cuantas veces aparece y ordenado de + a -
print(nba["fran_id"].value_counts()) #pero al pedir como franquisea selen mas ya que se pasaron de un ciudad a otra

print("filtro")
# Caso: ¿Hay dos Lakers?
#.loc permite filtrar filas(que cumplan la mascara), columnas 
#value dice el total ordenado
print(nba.loc[nba["fran_id"] == "Lakers", ["team_id"] ].value_counts())
print("")

#agg solo funciona con una columna
# Cuándo jugó partidos MNL - equipo antiguo
print(nba.loc[nba["team_id"] == "MNL", ["date_game"] ].agg(["min", "max"]))
    # NOTA: arroja un algo equivocado por asumirlo como str (ver los datos completos)
# se necesita convertir a formato de fecha
print("parsing, pd.to_datetime")
##parsing
# convertir a formato estándar de fecha
nba['date_game_std'] = pd.to_datetime(nba['date_game']) #si existe chanco y si no creo, ahora crea
print(nba.loc[nba["team_id"] == "MNL", "date_game_std"].agg( ["min", "max"] ))

#df["nueva_fecha"] = df["fecha"].dt.strftime("%d/%m/%Y") , permite editar 

#cuantos puntos hicieron los Boston Celtics
nba.loc[nba["team_id"] == "BOS", ["pts"] ].sum()

#ejes del dataframe
print(nba.axes[1]) #== nba.columns
print(nba.axes) #== nba.index
# probar con axes[0] u axes[1]

#revisar presencia de una columna
print("pts" in nba.columns)
# alternativa (no exactamente igual, pero muy cercana): in nba.columns

#Repaso rápido de .loc == lo que yo le puse como index e .iloc == indice original
# .loc e .iloc
colors = pd.Series(
    ["red", "purple", "blue", "green", "yellow"],
    index=[1, 2, 3, 5, 8]
    )
colors
print(colors.loc[3])
print(colors.iloc[3])

# explicar la diferencia

##FILATRADO
#tail es cola o ultimo registros
print(nba.tail(3))
#aplicado a NBA
print(nba.iloc[-2]) #penultima fila (verificar con nba.tail)

#combinar filas y columnas en el filtrado
#con loc puede recurrer a indices y nombres, mas felxible
#inprime un rango con ciertas columnas incluye el ultimo 5559 y iloc si menos -1
print(nba.loc[5556:5559 , ["fran_id", "opp_fran", "pts", "opp_pts"]])

#FILTROS  2000 =< nba["year_id"] < 2010
the_2000s = nba[(nba["year_id"] >= 2000) & (nba["year_id"] < 2010)]
print(the_2000s.shape)
print(len(the_2000s))

##Filtrados de datos en dataframe

# Evitar NULL
# elegir datos según estos sean NOT NULL en una columna elegida
# analizar por snipets

#variable con notes
games_with_notes = nba[nba["notes"].notnull()] #NOT NULL no es vacio, is null es vacio
print(games_with_notes.shape)
print(games_with_notes['notes'])

# Filtro por caracteres
ers = nba[nba["fran_id"].str.endswith("ers")]
print(ers.shape)
print(ers["fran_id"].unique()) #sin reptetiones == .unique()

#filtro multiple, evitar copia
# notar indentación (en este caso sí es para ayudar a la lectura, no es obligatoria)
nba[(nba["pts"] > 100) &
    (nba["opp_pts"] > 100) &
    (nba["team_id"] == "BLB")
    ]

#otro ejemplo (indentar)
nba[(nba["_iscopy"] == 0) &
    (nba["team_id"].str.startswith("LA")) &
    (nba["year_id"]==1992) &
    (nba["notes"].notnull())
    ]


##Estadísticas
#estadisticas
nba["pts"].sum()

#agrupar y sumar
#sort = orden del corchete
nba.groupby("fran_id", sort=False)["pts"].agg(['count','sum','mean','min','max'])  

#filtro, multi columna y contar
nba[
    (nba["fran_id"] == "Spurs") &
    (nba["year_id"] > 2010)
    ].groupby(["year_id", "game_result"])["game_id"].count() # el orden importa

##Manipulación

df = nba.copy() # ¿por qué no simplemente df = nba?
df.shape

df["difference"] = df.pts - df.opp_pts
df.difference.head(10)

#cambian nombres de columnas
renamed_df = df.rename(
    columns={"game_result": "result", "game_location": "location"}
    )
renamed_df.info()

##Drop
# notar el uso de "inplace"
print(df.shape)
elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]
df.drop(elo_columns, inplace=True, axis=1)
#con implace True si elimino 
#se define axis 
print(df.shape)

#define un lista
df["game_location"] = pd.Categorical(df["game_location"])
print(df["game_location"].dtype)
print(df["game_location"])

##Limpieza
# Eliminar registros vacios
rows_without_missing_data = nba.dropna()
print(rows_without_missing_data.shape)  # recordar: nba tiene 126314 filas

# Reemplazar datos vacios
data_with_default_notes = nba.copy()
data_with_default_notes["notes"].fillna(
    value="no notes at all",
    inplace=True)
#llena los vacios y confirma con implace =True
data_with_default_notes["notes"].describe()

### ver::[:,"xxx"]
# # Extra (más avanzado): evitar los objetos intermedios
# # Reemplazar datos vacios
# # reemplazo directo de los NaN values en 'notes'
# data_with_default_notes.loc[:, "notes"] = data_with_default_notes["notes"].fillna("no notes at all")
# data_with_default_notes["notes"].describe()

##Visualización
#%matplotlib inline
import matplotlib.pyplot as plt
# magic command de jupyter: aquí no hace mucha diferencia
 # (solo es necesario llamarla una vez por sesión)
nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot() ##por defecto es plot("line")
plt.show()

#bar plot
nba["fran_id"].value_counts().head(10).plot(kind="bar") #head(10) es top 10 y kind= "bar"
plt.show()

#pie
nba[
    (nba["fran_id"] == "Heat") &
    (nba["year_id"] == 2013)
    ]["game_result"].value_counts().plot(kind="pie")
plt.show()