num = str(input("Digite um número: "))

print("O tipo de entrada é ", type(num))

def funcao(num):
    
    lista = list()
    
    for i in num:
        a = ord(i)
        b = chr(a)
        lista.append(b)
        
    return lista

print(funcao(num))
print("O tipo de entrada é ", type(funcao(num)))

    
    
