import pandas as pd

dataframe = pd.read_csv("Aula/BostonHousing.csv")

coluna = ['crim','medv']
print(dataframe[coluna].head(14))