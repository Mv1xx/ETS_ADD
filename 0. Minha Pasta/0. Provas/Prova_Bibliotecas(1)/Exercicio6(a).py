import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

consumo_cidades = pd.read_csv("consumo_de_energia_cidades.csv")
print(consumo_cidades)

total_cidade = consumo_cidades.groupby('Cidade')['Consumo_Residencial'].sum()

plt.bar(total_cidade.index, total_cidade.values, color = ['blue', 'orange', 'green'])
plt.title("Consumo Residencial Total Anual por Cidade")
plt.ylabel("Consumo Total Residencial")
plt.show()



