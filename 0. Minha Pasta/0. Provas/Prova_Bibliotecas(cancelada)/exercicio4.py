import matplotlib.pyplot as plt
import numpy as np
import math 

x = np.arange(-2, 2.5, 0.5)
cos = list()
sen = list()

# z = np.array(math.cos(x * 2 * math.pi))

# print(z)
for i in x:
   cos.append(math.cos(i * 2 * math.pi))
   sen.append(math.sin(i * 2 * math.pi))

print(math.sin())
fig, eixo = plt.subplots(2, 1)
eixo[0].plot(x, cos)
eixo[1].plot(x, sen)
plt.grid()
plt.show()




