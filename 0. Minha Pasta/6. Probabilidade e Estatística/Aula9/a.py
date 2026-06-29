import random 

n= 10000
a = 80

satisfeitos = []
proporcao_lista = []
for i in range(n): #simulacoes
    s = 0
    for j in range(a): #valores
        if random.random() <= 0.6:
            s += 1
    proporcao = s /a
    satisfeitos.append(s)
    proporcao_lista.append(proporcao)

soma = 0
cont =0

for i in range(n):
    soma += satisfeitos[i]
    if proporcao_lista[i] <= 44/80:
        cont += 1

media = soma/n
prob = cont/n
prob_satisfeitos = media/a

print("Média de satisfeitos: ", round(media, 2))
print("Probabilidade de satisfação: ", round(prob_satisfeitos, 2))
print("A probabilidade da proporção de satisfação ser igual a 44/80 ", round(prob, 2))