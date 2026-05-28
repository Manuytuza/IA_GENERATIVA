import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("iadata.csv")

df1 = df[df["Domain"]== "Language"]
print(df1.describe())

df1= df1[df1["Training computation (petaFLOP)"]>3.75e+09]

df1 = df1.sort_values(
    by = "Training computation (petaFLOP)",
    ascending = True
)
print(df1.shape) 

df1.plot(
    kind = "barh",
    x="Entity", 
    y ="Training computation (petaFLOP)",
    #figsize=(12, 10)
    )

plt.xlabel("Training computation")
plt.ylabel("Entity")
plt.title("Language Models")
plt.tight_layout()
plt.show()

df1.iloc("")