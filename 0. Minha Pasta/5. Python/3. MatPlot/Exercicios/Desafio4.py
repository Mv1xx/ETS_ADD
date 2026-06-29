import matplotlib.pyplot as plt
import pandas as pd

filmes = pd.read_csv("../CSVs/netflix_titles.csv").dropna()

eua = filmes[(filmes['type'] == "Movie") & (filmes['country'] == "United States") & (filmes['release_year'] >= 2015) & (filmes['release_year'] <= 2020)]
a = eua.groupby("release_year")['title'].count()

brazil = filmes[(filmes['type'] == 'Movie') & (filmes['country'] == 'Brazil') & (filmes['release_year'] >= 2015) & (filmes['release_year'] <= 2020)]
brazil['duration'] = brazil['duration'].str[:-3].astype(int)

colunas = ['duration', 'title']
c = brazil[colunas].sort_values(by="duration", ascending=False).head(5)

print(c)

fig, eixo = plt.subplots(nrows = 1, ncols=2, figsize=(10,5))

eixo[0].bar(a.index, a.values)
eixo[1].bar(c['title'], c['duration'])
plt.xticks(rotation= 45)

plt.show()