import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

ecommerce = pd.read_csv("Arquivos/ecommerce.csv")
print(ecommerce)

sns.displot(ecommerce['Valor_Compra'], kde = True)
plt.show()

#Responda: A maioria das compras é de baixo, médio ou alto valor?
#Entre médio e alto, entretanto, predominantemente médio