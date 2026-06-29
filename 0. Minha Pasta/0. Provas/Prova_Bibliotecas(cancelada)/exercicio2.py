import pandas as pd

vendas = pd.read_csv("vendas.csv")

print(vendas)
print("5 primeiras linhas: \n", vendas.head())
print("\n Tipo de dados: \n", vendas.dtypes)

vendas['desconto'] = vendas['desconto'].fillna(0)
vendas['preco'] = vendas['preco'].fillna(vendas['preco'].mean())
print(vendas)

colunas = ['produto', 'categoria', 'preco', 'quantidade', 'desconto']

print(vendas[colunas].head(10))
print(vendas[colunas].tail(5))

vendas['valor_bruto'] = vendas['preco'] * vendas['quantidade']
vendas['valor_liquido'] = vendas['valor_bruto'] * ( 1 - vendas['desconto'])
vendas['ticket_medio_item'] = vendas['valor_liquido'] / vendas['quantidade']

print(vendas)

filtro = vendas[(vendas['categoria'] == 'Eletrônicos') & (vendas['valor_liquido'] > 1000) & (vendas['data'] > '01/01/2023')]
print(filtro)

print("Faturamento total: ", vendas['valor_liquido'].sum())
print("\nMédia de faturamento por venda: ", vendas['valor_liquido'].mean())
print("\nQuantidade total de itens vendidos: ", vendas['categoria'].count())

maisVendido = vendas.groupby('produto')['produto'].count().sort_values(ascending=False)
print(maisVendido)

maiorFaturamento = vendas.groupby('produto')['valor_liquido'].sum().sort_values(ascending=False)
print(maiorFaturamento)

categoriaFaturamento = vendas.groupby('categoria')['valor_liquido'].sum().sort_values(ascending = False)
print(categoriaFaturamento)


