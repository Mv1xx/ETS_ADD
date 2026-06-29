import random

linha = int(input("Digite o número de linha: "))
coluna = int(input("Digite o número de colunas: "))
soma = 0

for i in range(linha):
    for j in range(coluna):
        n = random.randint(0, 9)
        print(n, end=" ")
        
        if n % 2 == 0:
            soma = soma + n
    print("\n")
print("A soma dos números pares é: ", soma)


