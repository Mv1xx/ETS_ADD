import numpy as np


my_array = np.array(np.random.randint(0, 6, 6)).reshape((3, 2))
print(my_array)
print(" ")
print(my_array[0][0:] + 5)
print(my_array[1][0:] * 3)
print(my_array[2][0:] / 2)