import random

linha = 3
coluna = 3
elementos = 3

matriz = []

def aleatorio():
    return random.randint(1, 10)

for i in range(linha):
    linhas = list()
    for j in range(coluna):
        colunas = list()
        for k in range(3):
            colunas.append(aleatorio())
        linhas.append(colunas)
    matriz.append(linhas)
         

print(quantidade)
#for q in matriz:
#    print(q)
        
