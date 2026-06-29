import matplotlib.pylab as plt
import pandas as pd
import numpy as np

x = np.arange(-20,21,1)

y1 = x **2
y2 = x **3

fig, eixo = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5))
print(fig)

eixo[0].plot(x,y1)
eixo[1].plot(x,y2)

plt.show()