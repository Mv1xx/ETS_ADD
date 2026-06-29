import json

with open ('data.json','r') as data:
    data_dict = json.load(data)

lista_produtos = list()
lista_vendas = list()

#lista dos produtos
for produtos in data_dict['vendas']:
    lista_produtos.append(produtos['produto'])

set_produtos = set(lista_produtos)
print(set_produtos)

#soma das vendas
for vendas in data_dict['vendas']:
    lista_vendas.append(vendas['valor'])

soma_vendas = sum(lista_vendas)
print(soma_vendas)

#produtos mais vendido

   
    
    



        