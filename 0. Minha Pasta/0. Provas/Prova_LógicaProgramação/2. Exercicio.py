import random

num_sort = random.randint(1, 1000)
n = 0
conte = 0
print("Numero secreto: " num_sort)
while n != num_sort:
    n = int(input("Tente acertar o número sorteado: "))
    conte = conte + 1
    
    if num_sort - n in [1, 2, 3] or n - num_sort in [1, 2, 3]:
        print("Quase!")
    elif n > num_sort:
        print("Muito Alto")
    else:
        print("Muito Baixo")
print(f"Parabens!voce acertou. O número é {num_sort}\nForam necessárias {conte} tentativas")