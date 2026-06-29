import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("../Pandas/CSV/titanic.csv")


media_idade = titanic.groupby('Sex')['Age'].mean().to_frame(name="Media Idade")

vivos = titanic[titanic["Survived"] == 1].groupby("Sex").count()
mortos = titanic[titanic["Survived"] ==0].groupby("Sex").count()

media_idade['vivos'] = vivos['PassengerId']
media_idade['mortos'] = mortos['PassengerId']

print(media_idade)






