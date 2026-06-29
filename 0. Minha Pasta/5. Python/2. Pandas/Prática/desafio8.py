import pandas as pd

# homens
# homens mortos
# mulheres
# mulheres mortas
# crianças
# adulto 
# adolescente
# idoso
# 1 classe 
# 2 classe 
# 3 classe 
# mortos 1
# mortos 2
# mortos 3

titanic = pd.read_csv("Aula/titanic.csv", sep=",")

def soma_sibsp_parch(linha):
    if linha["Age"] < 12:
        return  "Criança"
    
    elif linha["Age"] >= 12 and linha["Age"] < 18:
        return  "Adolescente"
    
    elif linha["Age"] >= 18 and linha["Age"] < 65:
        return  "Adulto"
    
    elif linha["Age"] >= 65:
        return "Idoso"
    else:
        return "Nada"
nova_coluna = titanic.apply(soma_sibsp_parch, axis=1)
titanic["Faixa Etária"] = nova_coluna

titanic["Relatives"] = nova_coluna
#--------------------------------------------------------------------------------------------------------------
def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""
    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

def soma_sibsp_parch(linha):
    return linha["SibSp"] + linha["Parch"] 

nova_coluna = titanic.apply(soma_sibsp_parch, axis=1)

mortos = titanic[titanic["Survived"] == 0]
vivo = titanic[titanic["Survived"] == 1]
total = titanic.Survived.count()


# mortos_com_familia = titanic.Survived[titanic["Relatives"] == 1].count()
# mortos_sem_familia = titanic.Survived[titanic["Relatives"] == 0].count()

homens = titanic.Survived[titanic["Sex"] == "male"].count()
mulheres = titanic.Survived[titanic["Sex"] == "female"].count()


homens_mortos = titanic.Sex[(titanic["Sex"] == "male") & (titanic["Survived"] == 0)].count()
mulheres_mortos = titanic.Sex[(titanic["Sex"] == "female") & (titanic["Survived"] == 0)].count()

crianca = titanic.Survived[titanic["Faixa Etária"] == "Criança"].count()
adolescente = titanic.Survived[titanic["Faixa Etária"] == "Adolescente"].count()
adulto = titanic.Survived[titanic["Faixa Etária"] == "Adulto"].count()

clase1 = titanic.Survived[titanic["Pclass"] == 1].count()
clase2 = titanic.Survived[titanic["Pclass"] == 2].count()
clase3 = titanic.Survived[titanic["Pclass"] == 3].count()


clase1Morto = mortos.Survived[mortos["Pclass"] == 1].count()
clase2Morto = mortos.Survived[mortos["Pclass"] == 2].count()
clase3Morto = mortos.Survived[mortos["Pclass"] == 3].count()




# print(mortos_com_familia)
# print(mortos_sem_familia)
print(homens)
print(mulheres)
print(calculate_percentage(crianca,total))
print(calculate_percentage(adolescente,total))
print(calculate_percentage(adulto,total))
print(clase1)
print(clase2)
print(clase3)
print(clase1Morto)
print(clase2Morto)
print(clase3)
print(homens_mortos)
print(mulheres_mortos)