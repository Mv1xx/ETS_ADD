num = int(input("Digite um número: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j % i != 0:
            print(i)