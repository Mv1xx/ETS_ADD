import numpy as np
import pandas as pd

vendedores = np.array([1,2,1,3,2,1,3,2,3,1])
regiões = np.array(["Norte","Sul","Norte","Sul","Leste","Norte","Leste","Sul","Sul","Leste"])
vendas = np.array([120,200,150,300,180,90,250,210,310,160])

vendedor1 = (vendedores == 1)
vendedor1 = vendas[vendedor1].sum()

vendedor2 = (vendedores == 2)
vendedor2 = vendas[vendedor2].sum()

vendedor3 = (vendedores == 3)
vendedor3 = vendas[vendedor3].sum()

print("Total de vendas por vendedor: ")
print("Vendedor 1: ",vendedor1)
print("Vendedor 2: ", vendedor2)
print("Vendedor 3: ", vendedor3)

leste = (regiões == 'Leste')
leste = vendas[leste].sum()

sul = (regiões == 'Sul')
sul = vendas[sul].sum()

norte = (regiões ==' Norte')
norte = vendas[norte].sum()


print("\nTotal de vendas por região: ")
print("Região Leste: ", leste)
print("Região Sul: ", sul)
print("Região Norte: ", norte)

media = vendas.mean()
print("\nMédia geral de vendas: ", media)
print("Vendas acima da média: ", vendas[(vendas > media)])














