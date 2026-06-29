p = input("Digite p: ") #palavra
n = int(input("Digite n: ")) #quantidade de casas que irá variar cada letra da palavra

def funcao(p, n):
    lista = list()
    for c in p:
        f = chr((ord(c) - ord('a') + n ) % 26 + ord('a')) # add (n) na quantidade de casas de cada letra
        lista.append(f) #add toda letra convertida em uma lista - palavra inteira
    print(''.join(lista)) #mostra a lista
    
funcao(p, n)
