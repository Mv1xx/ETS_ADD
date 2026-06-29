import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

ecommerce = pd.read_csv("Arquivos/ecommerce.csv")
print(ecommerce)

sns.catplot(x='Quantidade_Itens', y='Valor_Compra', data=ecommerce, hue='Categoria_Produto')
plt.show()

#Responda: Existe relação entre quantidade comprada e valor gasto?
#Com esses dados, não é possível identificar uma relação direta entre quantidade de itens e valor gasto na compra, tendo em vista que todas as quantidades de itens estão aproximadamente como mesmo tamanho e espessura