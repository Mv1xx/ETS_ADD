import numpy as np

n = int(input("Digite um número: "))
matriz = np.full((n,n), 0)

for i in range(len(matriz)):
    matriz[i, i] = 1
    matriz[i, n-1-i] += 2

print(matriz)
    


