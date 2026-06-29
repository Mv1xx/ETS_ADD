import numpy as np

n = int(input("Digite um número: "))

matriz = np.array(np.random.randint(1, 9, (n*n))).reshape((n, n))
s = 0



somavizinho =np.empty_like(matriz)

for i in range(n):
    for j in range(n):
        s = 0
        if n<n-1:
            s+=matriz[i+1, j]
        if i>0:
            s+=matriz[i-1,j]
        if j<n-1:
            s+=matriz[i, j+1]
        if j>0:
            s+=matriz[i,j-1]
        somavizinho [i, j] = s

print(matriz)
print(somavizinho)