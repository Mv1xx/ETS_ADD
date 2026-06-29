import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

vendas = pd.read_csv('vendas.csv').dropna()

vendas['valor_total'] = vendas['preco'] * vendas['quantidade']
vendas['data'] = vendas['data'].astype('datetime64[us]')

sns.barplot(data=vendas, x=vendas['valor_total'], y = vendas['valor_total'].sum())
plt.show()