import pandas as pd

master = pd.read_csv('../Pandas/CSV/master.csv')

master.drop(columns=['country', 'year', 'HDI for year'], inplace=True)

master["Country"] = master['country-year'].str[:-4]
master["Year"] = master['country-year'].str[-4:]

filtro = master[(master['Country'] == 'Brazil') & (master['Year'] == '1987') & (master['sex'] == 'female') & (master['generation'] == 'Boomers')]

print(filtro)