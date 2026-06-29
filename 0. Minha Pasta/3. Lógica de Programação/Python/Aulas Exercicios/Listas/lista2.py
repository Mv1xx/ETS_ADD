import random

linha = 10
coluna = 10
elementos = 3

matriz = []

def aleatorio():
    return random.randint(1, 100)

for i in range(linha):
    linhas = list()
    for j in range(coluna):
        colunas = list()
        for k in range(3):
            colunas.append(aleatorio())
        linhas.append(colunas)
    matriz.append(linhas)

for q in matriz:
    print(q)
        

