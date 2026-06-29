import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

ecommerce = pd.read_csv("Arquivos/ecommerce.csv")
print(ecommerce)

sns.catplot(data=ecommerce, x='Metodo_Pagamento', kind='count')
plt.show()

#Responda: Qual método é mais utilizado?
#Pix