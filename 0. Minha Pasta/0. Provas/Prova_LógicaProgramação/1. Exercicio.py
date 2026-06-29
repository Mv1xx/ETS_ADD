a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if abs( b - c ) < a < b+c:
    print("é um triângulo isóceles")
elif abs(a - c) < b < a + c:
    print("é um triângulo equilátero")
elif abs(a - b) < c < a+ b:
    print("é um triângulo escaleno")

