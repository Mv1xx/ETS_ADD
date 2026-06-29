import random
import math 

cont = 0
cont_vermelho = 0
cont_aVermelho = 0
n = 10000

def sorteio():
    a = random.choice(urna)
    urna.remove(a)
    return a

def combinacao(n, p):
    c = math.factorial(n) / (math.factorial(p) * math.factorial(n-p))
    return c


for i in range(n):
    urna = ['vermelho', 'vermelho', 'vermelho', 'vermelho', 'azul', 'azul', 'azul', 'verde', 'verde']
    a = sorteio()
    b = sorteio()
    
    if a == b:
        cont += 1
    if a == 'vermelho' and b == 'vermelho':
        cont_vermelho += 1
    if a == 'vermelho':
        cont_aVermelho += 1

prob_mesmaCor = round((cont / n) * 100, 2) 
prob_vermelho = round((cont_vermelho / cont_aVermelho) * 100, 2) 

print("Probabilidade de sair duas bolas com a mesma cor: ", prob_mesmaCor, "%")
print("Probabilidade de sair a segunda bola como vermelha, dado que a primeira é vermelha: ", prob_vermelho, "%")
resultado = combinacao(9,2)
print(resultado)
    
    
        

