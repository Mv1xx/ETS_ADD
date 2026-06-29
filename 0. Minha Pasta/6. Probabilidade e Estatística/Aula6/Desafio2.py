import random
lista = []
n_simulacoes = 1000
for x in range(n_simulacoes):
    n = 10
    infectado = 1
    alunos = 100
    for i in range(10):
        for j in range(infectado):
            chance = random.randint(1, 100)
            if chance < 30:
                infectado += 1
                alunos -= 1
    lista.append(infectado)
        
media = round(sum(lista) / n_simulacoes, 2)
print("Média: ", media)
