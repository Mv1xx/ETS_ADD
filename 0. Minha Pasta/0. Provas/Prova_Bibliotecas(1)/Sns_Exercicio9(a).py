import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

estudantes = pd.read_csv("desempenho_estudantes.csv")
print(estudantes)

#relação entre Horas_Estudo, Nota_Estatistica

sns.relplot(data = estudantes, x = 'Horas_Estudo', y='Nota_Estatistica', hue='Curso')
plt.show()
