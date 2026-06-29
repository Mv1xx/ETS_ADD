import pandas as pd

# Ela embarcou em Southampton (Inglaterra)
# Ela era da segunda classe
# Ela tinha 29.0 anos
# E no nome completo dela tinha Anne, mas ele não sabe se era nome ou sobrenome.
# Lembre sempre de retirar os valores NaN das colunas (aplique outro valor no lugar deles)

dataframe = pd.read_csv("Aula/titanic.csv")

dataframe = dataframe[dataframe["Embarked"] == 'S']
dataframe = dataframe[dataframe["Pclass"] == 2]
dataframe = dataframe[dataframe["Age"] == 29.0]
dataframe = dataframe[dataframe["Sex"] == "female"]
dataframe = dataframe.loc[:, ["Name"]].dropna()

lista = list()

for i in dataframe.index:
    if "Anne" in dataframe.loc[i, "Name"]:
        lista.append(dataframe.loc[i, "Name"])
        print(lista)

