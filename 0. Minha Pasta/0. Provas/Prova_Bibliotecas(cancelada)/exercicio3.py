import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_csv('vendas.csv').dropna()

vendas['valor_total'] = vendas['preco'] * vendas['quantidade']
vendas['data'] = vendas['data'].astype('datetime64[us]')

print(vendas)

a = vendas.groupby('produto')['quantidade'].sum().sort_index()

plt.bar(list(a.index), a.values)
plt.show()


