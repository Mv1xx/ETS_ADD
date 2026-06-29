import random
import math
import formulas

afirmacao = 75
amostra = 120
aprovados = 81
a = 5

resultado = formulas.proporcao(aprovados, 0.75, 0.25, amostra)
print(resultado)

tabela = 0.0287
print("OIO")

if tabela <= a:
    print("Rejeita!")
else:
    print("Não rejeita!")


n = 10000
proporcoes = []
for i in range(n):
    aprovados = 0
    for j in range(120):
        chance = random.randint(0, 100)
        if chance <= 75:
            aprovados += 1

    proporcao = aprovados / 120
    proporcoes.append(proporcao)

cont = 0
for i in proporcoes:
    if i <= 81/120:
        cont += 1
    
prob = cont / 10000
print("Probabilidade estimada: ", prob)
 
# media = round(sum(lista) / len(lista), 2)
# print(media)
# proporcao = formulas.proporcao(media, 0.75, 0.25, 120)
# print(proporcao)

