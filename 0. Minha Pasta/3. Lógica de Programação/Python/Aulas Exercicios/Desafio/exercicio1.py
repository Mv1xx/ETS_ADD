lista = list()
for i in range(10):
    num = int(input("Add um número na lista: "))
    lista.append(num)

num2 = int(input("Digite outro número: "))

conte = 0
for i in lista:
    if i < num2:
        conte+= 1

print(f"Existem {conte} número menores que {num2} na lista")
        