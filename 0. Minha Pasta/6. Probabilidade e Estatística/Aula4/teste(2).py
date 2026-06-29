import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = pd.read_csv("transacoes_fraude.csv")

a["Suspeita"] = np.where(a["tentativas_login"] > 3, 1, np.where(a["falha_login"] == 1, 1, 0))

b = a.groupby("Suspeita")["fraude"].count()

fig, eixo = plt.subplot(1, 1, figsize = [20, 20])

print(fig)

# fig, axis = plt.subplot(2, 2, figsize=(10,8))

# axis[0] = plt.bar(a['Suspeita'])

