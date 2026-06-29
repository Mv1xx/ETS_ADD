import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

estudantes = pd.read_csv("desempenho_estudantes.csv")
print(estudantes)

a = estudantes.groupby('Participacao')['Nota_Estatistica'].mean().sort_values(ascending=False)
print(a)

plt.bar(a.index, a.values)
plt.xlabel("Participação")
plt.ylabel("Média Nota Estatística")
plt.title("Média da Nota de Estatística por Participação")
plt.show()