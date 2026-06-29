import matplotlib.pyplot as plt
import numpy as np
import math

fig, eixo = plt.subplots(ncols=1,nrows=2,figsize=(10,5))

a = np.arange(1, 7)
fa = a**2
ga = list()

for valor in a:
    ga.append(math.factorial(valor))
    
eixo[0].plot(a, ga)
eixo[1].plot(a, fa, color='red')

eixo[0].grid(linestyle='dashed')
eixo[1].grid(linestyle='dashed')

eixo[0].set_title("Função f(x) = x!")
eixo[1].set_title("Função g(x) = x**2")
plt.show()