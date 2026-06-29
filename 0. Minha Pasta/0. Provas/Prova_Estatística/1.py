import random

simulacao = 10000
semana = 7
cont = 0
chuvas_semanas = list()

for i in range(simulacao):
    chuva = 0
    for j in range(semana):
        chance = random.randint(0, 100)
        if chance <= 30:
            chuva += 1
    chuvas_semanas.append(chuva)
    if chuva >= 3:
        cont += 1 #qnt de vezes que choveu pelo menos 3 vezes na semana

resultado = round(cont / simulacao * 100, 2)
print(f"{resultado}%")