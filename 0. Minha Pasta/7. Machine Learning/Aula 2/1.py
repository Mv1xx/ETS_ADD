from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("house_prices.csv")
x_casas = casas.iloc[:, 2:18]
y_casas = casas.iloc[:, 1].values
casas.drop('date', axis = 1, inplace = True) #dificil basear outras caracteristicas na data
#casas.describe() ->> caracteristicas do dataset

casas.isnull().sum() #qnt de valores nulos em cada coluna

figura = plt.figure(figsize=(20,20)) #tamanho da figura
sns.heatmap(casas.corr(), annot=True) #corr >> correlação; annot >> legenda 
plt.show()