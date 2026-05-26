import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("iadata.csv")
print(df.tail(5))
print(df.columns)
print(df.info())
print("\n")

df1 = df.groupby("Domain")["Training computation (petaFLOP)"].mean().sort_values(ascending=False)

print(df1.columns)
print(df1.iloc[df["Training computation (petaFLOP)"]>10000, "Domain"].men())

