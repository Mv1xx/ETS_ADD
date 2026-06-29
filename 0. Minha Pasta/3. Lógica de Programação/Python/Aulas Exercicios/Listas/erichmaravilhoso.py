import random

linhas = 10
elementos = 3
matriz = []
maior = 0

for i in range(linhas):
    linha = list()
    for k in range(elementos):
        elemento = random.randint(1, 9)
        linha.append(elemento)
    matriz.append(linha)
    
for i in matriz:
    for j in i:
        if j > maior:
            maior = i
            i[0] = maior
        
    print(linha)


#for linha in matriz:
    #print(linha)