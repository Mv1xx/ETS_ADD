import random 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

tempo_atendimento = []
s = s1 = 0
n = 10000
medias = []

def X():
    for i in range(n):
        chance = random.randint(5,100)

        if chance < 85:
            leve = random.randint(5,20)
            tempo_atendimento.append(leve)
        else:
            complexo = random.randint(40,60)
            tempo_atendimento.append(complexo)
    
    return tempo_atendimento

def Y(n):
    soma = 0
    for i in range(n):
        soma += X()
    return soma/n

valores = X()

df = pd.DataFrame(valores, columns=["tempo_atendimento"])

media = df["tempo_atendimento"].mean()
desvio_padrao = round(df["tempo_atendimento"].std(), 2)

for i in valores:
    s+= ((i - media)**2)

variancia = round(s/n, 2)

print("--" * 30)
print("media: ", media)
print("Desvio padrão: ", desvio_padrao)
print("variancia: ", variancia)

for i in range(n):
    medias.append(Y(100))

plt.hist(medias, bins = 30)
plt.show()

x = 22
z = ( x - media)/desvio_padrao
prob = 1 - norm.cdf(z)
print("A probabilidade de ser maior que 22 minutos é ", prob)




    


