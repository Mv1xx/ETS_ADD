import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# plote um gráfico do tipo barras horizontais, em que apresente os meses (eixo Y) e a
# quantidade de passageiro em cada mês do ano de 1950 (eixo X). A paleta de cores é opcional.

# sns.catplot(x=dayWeek,data=tips, kind='count')

a = pd.read_csv("../CSV/flights.csv")

sns.catplot(x = 'passengers', y='month', data=a)


