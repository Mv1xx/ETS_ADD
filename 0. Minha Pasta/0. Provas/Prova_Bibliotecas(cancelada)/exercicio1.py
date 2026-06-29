import numpy as np

a = np.random.randint(1,50, 20).reshape((4,5))

b = np.random.randint(1,50, 20).reshape((4,5))

print("Shape A: ", a.shape)
print("Shape B: ", b.shape)

print(" ")
print("ndim A: ", a.ndim)
print("ndim B: ", b.ndim)

print(" ")
print("Size A: ", a.size)
print("Size B: ", b.size)

print(" ")
print("União AB: ", np.union1d(a, b))
print("Interseção AB: ", np.intersect1d(a, b))
print("Diferença AB: ", np.setdiff1d(a, b))

print(" ")
print(a.reshape((2, 10)))

print(" ")
c = (a**2) + (2 * b)

print(c)
print(" ")
print("Soma c: ", c.sum())
print("Média c: ", c.mean())


print(a)
print(" ")
print(b)
print(" ")
print("Segunda linha de A: ", a[1])
print("Duas ultimas colunas de B: \n", b[: , -2:])
print("Subarray A: ", a[0:4, 2:5])

print("\n elementos de A > 25: ")
filtro = (a > 25)
print(a[filtro])

print("\n Substuir elementos pares por zero: ")
b = np.where(b % 2 == 0, 0, b)
print(b)

print("\n Média por linha A: ")
print(a.mean(axis=1))
print("\n Soma por coluna B: ")
print(b.sum(axis=0))
print("\n Desvio padrão A: ")
print(a.std())
