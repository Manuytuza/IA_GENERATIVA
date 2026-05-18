import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("datos.csv") #cargar csv
print(df.info()) #columnas, non-null, type columns
print(df.isnull().sum()) #sum of nulls for columns
df["Edad"] = df["Edad"].fillna(0) #change nan for (x)
df["New"] = df["Edad"] / df["Ventas"] #new column of df
#df["New"] = df["New"].astype(float) #cambiar type de column
df["New"] = df["New"].round(2) #redondedar a 2 decuamles
print(df.head())

"""
df["New"] = np.where(
    df["Ventas"] != 0,
    df["Edad"] / df["Ventas"],
    0
)
np.where(condición, valor_si_true, valor_si_false)
"""
print(df.describe().round(2)) #summary of df to 2 decimals

mb = df[df["Ventas"] > 150]
print(mb) #boolean masc

group = df.groupby("Nombre")["Ventas"].agg(["sum","min","max","mean"])
print(group) #groupby plus .agg

fig,axs = plt.subplots(2,1)
df.plot(
    kind = "scatter",
    x= "Nombre",
    y="Ventas",
    xlabel="hola_horizontal",
    ylabel="vertical",
    title= "scatter grafic",
    ax=axs[0]
)

df.plot( #df["Ventas"].plot()
    kind = "hist",
    y="Ventas", #only need one column
    title="hist grafic",
    ax = axs[1]

)
plt.tight_layout()
fig.suptitle("fig , axs")
plt.show()

df_sort = df.sort_values("Ventas")
print(df_sort)
group1= df.groupby("Nombre")["Ventas"].sum()
print(group1)