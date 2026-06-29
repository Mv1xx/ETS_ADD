import random

num = random.randint(0, 11)
conte = 1

while True:
    advinha = int(input("Tente advinha qual número é: "))
    
    while advinha != num:
        print("\nAHHH errou, tente novamente")
        advinha = int(input("Tente advinha qual número é: "))
        conte = conte + 1
    
    break

print('\n-='*30)
print(f"Você acertou! o número era {num}, Você precisou de {conte} tentativas para acertar")