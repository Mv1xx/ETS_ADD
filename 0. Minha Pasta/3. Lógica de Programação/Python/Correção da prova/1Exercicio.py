a = float(input("digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a == b == c:
    print("Equilatero") 
elif a == b or a == c or b == c:
    print("Isoceles")
else:
    print("Escaleno")   