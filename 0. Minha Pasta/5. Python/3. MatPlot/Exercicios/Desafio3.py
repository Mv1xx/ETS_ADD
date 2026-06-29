import pandas as pd
import matplotlib.pyplot as plt

passageiros = pd.read_csv("../CSVs/flights.csv")
colunas = ['passengers', 'year']
filtro = passageiros[colunas][passageiros['month'] == 'May']

print(passageiros)
print(filtro['year'], filtro['passengers'])

plt.plot(filtro['year'], filtro['passengers'], marker='o')
plt.grid()
plt.show()