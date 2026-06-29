import pandas as pd

titanic = pd.read_csv("Aula/titanic.csv")


x = titanic[titanic["Pclass"] == 1]
x = titanic[titanic["Survived"] == 1]
x = x.loc[:, ["Pclass", "Survived"]]

print(x)
