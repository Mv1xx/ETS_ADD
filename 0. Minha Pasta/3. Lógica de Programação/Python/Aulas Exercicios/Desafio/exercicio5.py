num = int(input("Digite um número: "))

for i in range(1, num+1):
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0) or (i == 2 or i == 3 or i == 5):
        print(i)