import pandas as pd

titanic = pd.read_csv("../Pandas/CSV/train.csv")

homens_coluna = (titanic["Sex"] == 'male')
mulheres_coluna = (titanic['Sex'] == 'female')

qnt_homens = titanic[homens_coluna].shape[0] * 100 / titanic.shape[0]
qnt_mulheres = titanic[mulheres_coluna].shape[0] * 100 / titanic.shape[0] 

print(f"Homens no titanic: {qnt_homens} %")
print(f"Mulheres no titanic: {qnt_mulheres} %")