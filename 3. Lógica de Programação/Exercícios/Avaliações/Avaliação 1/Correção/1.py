a = int(input('lado a:\n>>'))
b = int(input('lado b:\n>>'))
c = int(input('lado c:\n>>'))

nao_triangulo = False
if not (abs(b-c)<a<b+c):
    nao_triangulo = True
if not (abs(a-c)<b<a+c):
    nao_triangulo = True
if not (abs(a-b)<c<a+b):
    nao_triangulo = True
if nao_triangulo:
    print('não é um triângulo!')
    exit()

    

if a == b and b == c:
    print('equilatero!')
elif a != b and b != c and a != c:
    print('escaleno!')
elif a == b or b == c or a == c:
    print('isóceles!') 