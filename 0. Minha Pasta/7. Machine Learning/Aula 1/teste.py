import pandas
import random

plano_saude = pandas.read_csv("../Aula 1/plano_saude.csv")
qnt_elementos = plano_saude['idade'].count()

def covariancia(v):
    mediax = round(plano_saude["idade"].mean(), 2)
    mediay = round(plano_saude["custo"].mean(), 2)
    soma = 0
    stdX = plano_saude['idade'].std()
    stdY = plano_saude['custo'].std()
    
    for i in range(qnt_elementos):
        x = plano_saude["idade"][i] - mediax
        y = plano_saude["custo"][i] - mediay

        soma += (x * y) 

    cv = soma / (qnt_elementos - 1)
    cr = cv / (stdX * stdY)
    m = cr * (stdY / stdX)

    b = mediay - (m * mediax)

    p = b + m * v
    return round(p, 2)

a = int(input("Digite uma idade para descobrir o valor do plano de saúde: "))
print(f"Com a idade {a} o preço de plano de saúde é aproximadamente {covariancia(a)}")
