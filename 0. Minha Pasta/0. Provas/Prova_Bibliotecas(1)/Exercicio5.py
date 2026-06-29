import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

consumo_cidades = pd.read_csv("consumo_de_energia_cidades.csv")

campinas = consumo_cidades[(consumo_cidades['Cidade'] == 'Campinas')]

print(campinas)

plt.plot(campinas["Mes"], campinas['Consumo_Residencial'], marker='o', label = "Consumo Residencial")
plt.plot(campinas['Mes'], campinas['Consumo_Comercial'], marker='o', label = 'Consumo Comercial')
plt.title("Consumo de Energia em Campinas por Mês")
plt.xlabel("Mês")
plt.ylabel("Consumo de Energia")
plt.legend()
plt.show()