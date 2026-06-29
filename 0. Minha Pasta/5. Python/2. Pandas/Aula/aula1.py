import pandas as pd

titanic = pd.read_csv("titanic.csv", sep=",")

titanic.head() #cabeçalho - primeiras 5 linhas

titanic.tail() #ultimas 5 linhas

titanic['Survived'].head() #informações da coluna com os primeiros 5 dados - head()
titanic.Survival.head()

titanic.shape #qntd de linhas e colunas

titanic.index #inclui uma coluna index (ID) 

titanic.columns #quantidade de colunas

titanic.dtypes #tipo de dados de cada coluna

filtro_tipo_numerico = (titanic.dtypes == "object") #procura colunas com o tipo de dados igual a objeto e guarda na variável

titanic.iloc[:, :-1] #seleciona linhas e colunas - POR ÍNDICE
titanic.iloc[15:, :3]

titanic.loc[:,["Survived"]].head() #seleciona colunas - POR NOME

titanic.describe() #dados estatísticos de todas as colunas (media, quantidade, minuto etc)
titanic.Age.describe() #dados estatísticos de uma coluna específica


titanic['Embarked'].unique()#valores únicos de uma coluna específica

x= titanic.dropna() #excluir todas as linhas nulas
print(x.isna().head(15)) #verifica se existem valores nulos





