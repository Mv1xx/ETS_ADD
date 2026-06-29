
def bissexto(a):
    if a % 100 == 0:
        if a % 400 == 0:
            return True
        else:
            return False
    else:
        if a % 4 == 0:
            return True
        else:
            return False
    
    
ano = int(input("Digite um ano: "))
eh_bissexto = bissexto(ano)

print(eh_bissexto)