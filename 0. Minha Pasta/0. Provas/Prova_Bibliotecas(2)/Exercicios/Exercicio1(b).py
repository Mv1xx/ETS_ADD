import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

ecommerce = pd.read_csv("Arquivos/ecommerce.csv")
print(ecommerce)

sns.catplot(data=ecommerce, kind='box', x="Categoria_Produto", y="Valor_Compra")
plt.show()

#Responda: Qual categoria possui maior variação de valores?
#Roupas