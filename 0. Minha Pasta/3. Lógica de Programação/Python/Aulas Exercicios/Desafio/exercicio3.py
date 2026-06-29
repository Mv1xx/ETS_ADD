seq = int(input("Digite um número para a sequência: "))
fibonacci = armaz2 = 1
print(f"{fibonacci} {fibonacci}", end= " ")

for i in range(seq - 2):
    armaz = fibonacci
    fibonacci = fibonacci + armaz2
    print(fibonacci, end=" ")
    armaz2 = armaz
    
   
    
    
    