import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

estudantes = pd.read_csv("desempenho_estudantes.csv")
print(estudantes)

a = estudantes.groupby('Participacao')['Nota_Estatistica'].mean().sort_values(ascending=False)
print(a)

sns.catplot(data=estudantes, x='Participacao', y='Nota_Estatistica', kind= 'bar')
plt.show()