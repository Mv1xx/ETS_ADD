
def toLow(frase):
    frase_minu = list()
    for i in frase:
        if 64 < ord(i) < 91:
            minu = ord(i) + 32
            letra_minu = chr(minu)
            frase_minu.append(letra_minu)
        else:
            frase_minu.append(i)
    return ''.join(frase_minu)
            
        

a = toLow('HaHA PaPOi? HAHA PAPOI! UaaaaA')
print(a)


