import numpy as np

python = np.array([101,102,103,104,105,106,107])
estatistica = np.array([103,104,108,109,110,105])
visualizacao = np.array([101,103,105,111,112])

py_est = np.union1d(python, estatistica)
todos = np.intersect1d(python, np.intersect1d(estatistica, visualizacao))
a = np.union1d(estatistica, visualizacao)
b = np.setdiff1d(a, python)



print("Python ou Estatística: ", py_est)
print("Os 3 cursos: ", todos)
print("Que estão em estatística e visualização mas não em python: ", b)
