import pandas as pd
import numpy as np

dados = pd.read_csv("../Pandas/CSV/tips.csv", sep=";")


gorjeta = dados['tip'].count()
total = dados['total_bill'].count()

dados['Porcentagem_Gorjeta (%)'] = dados['tip'] * 100 / dados['total_bill']

maior = dados['Porcentagem_Gorjeta (%)'].max()
linha_maior = (dados['Porcentagem_Gorjeta (%)'] == maior)

# print(dados[linha_maior])

media_genero = dados.groupby('sex')['tip'].mean()
# print(media_genero)

# print(dados.shape[0])

media_gorjeta = dados['tip'].mean()

dados['Pagador Ruim'] = np.where(dados['tip'] < media_gorjeta, 1, 0)

dia_gorjeta = (dados.groupby('day')['Pagador Ruim'].count()).idxmin()

# print(dia_gorjeta)

fumante_gorjeta = (dados.groupby('smoker')['Pagador Ruim'].count())
# print(fumante_gorjeta)

filtro = dados[(dados['servings'] > 3) & (dados['time'] == 'Dinner') & (dados['smoker'] == 'No') & (dados['day'] == 'Sat')].tip.mean()

print(dados[linha_maior])
print(media_genero)
print(dados.shape[0])
print(dia_gorjeta)
print(fumante_gorjeta)
print(filtro)












