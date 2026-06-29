import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

consumo_cidades = pd.read_csv("consumo_de_energia_cidades.csv")
print(consumo_cidades)

total_cidade = consumo_cidades.groupby('Cidade')['Consumo_Residencial'].sum()

plt.pie(total_cidade, labels=['Campinas', 'Sorocaba', 'Ribeirao'])
plt.show()



