import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

estudantes = pd.read_csv("desempenho_estudantes.csv")
print(estudantes)

sns.displot(estudantes['Nota_Matematica'], kde=True)
plt.show()