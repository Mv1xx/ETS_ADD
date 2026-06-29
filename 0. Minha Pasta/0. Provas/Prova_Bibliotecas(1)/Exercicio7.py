import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

consumo_cidades = pd.read_csv("consumo_de_energia_cidades.csv")
print(consumo_cidades)

plt.hist(consumo_cidades['Temperatura_Media'], ec='black')
plt.title("Distribuição de Temperatura Média nas Cidades")
plt.xlabel("Temperatura Média")
plt.ylabel("Frequência")
plt.show()
