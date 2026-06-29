import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

estudantes = pd.read_csv("desempenho_estudantes.csv")
print(estudantes)

#relação entre Horas_Estudo, Nota_Estatistica

plt.scatter(estudantes['Horas_Estudo'], estudantes['Nota_Estatistica'])
plt.legend()
plt.show()
