import pandas as pd

# faixa-etaria:
# < 12 -> criança
# >= 12 = & > 18 -> adolescente
# >=18  & < 65 -> adulto
# >= 65 -> idoso

dataframe = pd.read_csv("Aula/titanic.csv", sep=",")

def idade(linha):
    if linha["Age"] < 12:
        return " Criança"
    elif linha["Age"] >= 12 and linha["Age"] < 18:
        return "Adolescente"
    elif linha["Age"] >=18 and linha["Age"] < 65:
        return "Adulto"
    elif linha["Age"] >= 65:
        return "Idoso"

nova_coluna = dataframe.apply(idade, axis = 1)
dataframe["Faixa-Etária"] = nova_coluna
print(dataframe)

