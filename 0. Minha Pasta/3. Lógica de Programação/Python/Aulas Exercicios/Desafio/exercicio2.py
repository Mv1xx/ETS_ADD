num = int(input("Digite um número: "))
fatorial = 1

for i in range(num, 0, -1):
    fatorial = fatorial * (num)
    num = num - 1
    print(f"{i} X", end=" ")

print(f"= {fatorial}")
    
    
    