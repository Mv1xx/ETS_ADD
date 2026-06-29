import random
from datetime import datetime
import time

acertos = 0
lista = list()

play = input("Pressione ENTER para iniciar >> ")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1) 
print("Valendo!")

for i in range(3):
    sec = time.time()
    
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)

    calculo = n1 * n2

    print(f"\nQuanto é {n1} x {n2}?")
    resposta = int(input("Resposta: "))
    sec2 = time.time()

    total = round(sec2 - sec, 2)
    lista.append(total)

    if resposta == calculo:
        print("Correto! Tempo: ", total)
        acertos += 1
    else:
        print("Errado... Tempo: ", total)

media = round(sum(lista)/len(lista), 2)
if media < 3:
    classi = "Rápido"
elif media < 6:
    classi = "Médio"
else:
    classi = "Lento"

print("\n=== Resultado Final ===")
print("Acertos: ", acertos)
print("Tempo médio: ", media)
print("Classificação: ", classi)
