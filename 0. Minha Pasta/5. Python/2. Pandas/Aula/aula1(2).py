import pandas as pd

titanic = pd.read_csv("Aula/titanic.csv")

y = titanic["Age"].fillna(titanic["Age"].mean()) #preenche os valores nulos de uma colunas com a média da coluna
print(y.head(15))
z = titanic.fillna(200)