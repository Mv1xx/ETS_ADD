import random

lista = [[[], [], [],
          [], [], [],
          [], [], []
        ]]

for i in lista:
    for j in i:
        elemento = 0
        for k in range(3):
            elemento = random.randint(1, 30)
            j.append(elemento)

print(lista)