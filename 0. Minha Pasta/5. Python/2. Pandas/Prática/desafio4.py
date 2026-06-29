import pandas as pd

# Deve ser um carro com 5 lugares; (Passengers)
# Selecione os 10 carros com maior MPG(Miles Per Gallon) na cidade;
# Dos 10 mais econômicos, mostre os 5 modelos mais baratos; (Price)
# Mostre somente as colunas 'Manufacturer','Make','Price','MPG.city','Type','Passengers'

dataframe= pd.read_csv("Aula/Cars93_miss.csv")

x = dataframe[dataframe["Passengers"] == 5]
x = x.loc[:, ["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]].dropna()
x = x.sort_values(by = "MPG.city").tail(10)
x = x.sort_values(by = "Price").head(5)

print(x)