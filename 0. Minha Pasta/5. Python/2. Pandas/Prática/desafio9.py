import pandas as pd

titanic = pd.read_csv("Aula/titanic.csv")

def idade(linha):
    if linha["Age"] < 12:
        return " Criança"
    elif linha["Age"] >= 12 and linha["Age"] < 18:
        return "Adolescente"
    elif linha["Age"] >=18 and linha["Age"] < 65:
        return "Adulto"
    elif linha["Age"] >= 65:
        return "Idoso"
    else:
        return "Nada"

nova_coluna = titanic.apply(idade, axis = 1)
titanic["Faixa-Etária"] = nova_coluna
print(titanic)

total = titanic["Faixa-Etária"].count()
print(total)