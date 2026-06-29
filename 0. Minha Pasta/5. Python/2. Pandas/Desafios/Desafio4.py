import pandas as pd

dados = pd.read_csv("../Pandas/CSV/dados.csv", encoding="latin1")

filtro = dados[(dados['bairro'] == 'Tijuca') & (dados['area'] > 130) & (dados['quartos'] == 3)].sort_values(by="preco", ascending=True)

print(filtro.head(5))