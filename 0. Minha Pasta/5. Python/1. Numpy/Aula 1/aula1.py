import numpy

my_array = numpy.array(['0, 1, 2, 3, 4, 5, 6, 7, 8, 9'])

array_range = numpy.arange(0, 100, 10)

# print(array_range)

array_bolean = numpy.full((10,10), True)

# print(array_bolean)

array_matriz = numpy.array(numpy.random.randint(0,10,10)).reshape((3,3))
numimpar = (array_matriz % 2 != 0)
array_matriz[numimpar] = 0

print(array_matriz)