import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("datos.csv")
print(df.info())
print(df.isnull().sum())
df["Edad"] = df["Edad"].fillna(0)
df["New"] = df["Edad"] / df["Ventas"]
#df["New"] = df["New"].astype(float)
df["New"] = df["New"].round(2)
print(df.head())

"""
df["New"] = np.where(
    df["Ventas"] != 0,
    df["Edad"] / df["Ventas"],
    0
)
"""
print(df.describe().round(2))

mb = df[df["Ventas"] > 150]
print(mb) 

group = df.groupby("Nombre")["Ventas"].agg(["sum","min","max","mean"])
print(group)