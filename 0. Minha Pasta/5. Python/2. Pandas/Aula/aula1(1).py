import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(round(titanic.groupby("Embarked").mean()["Age"].sort_values()["s"], 5))