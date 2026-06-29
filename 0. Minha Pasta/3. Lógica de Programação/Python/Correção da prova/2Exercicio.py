import random

num_sorteado = random.randint(1, 1000)
num = conte = 0


while num != num_sorteado:
    num = int(input("Digite um palpite: "))
    conte = conte + 1
    if num_sorteado + 3 == num or num_sorteado - 3 == num:
        print("Quase!!")
    elif num > num_sorteado:
        print("Muito Alto!")
    else:
        print("Muito baixo")

print('-=' * 20)
print(f"Parabens, você acertou, o número era {num_sorteado}\nfora necessárias {conte} tentativas")
        