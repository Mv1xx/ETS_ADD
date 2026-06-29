import random as r

def soldados(at, de):
    
    if at == 1:
        qnt_at = 1
    elif at < 6:
        qnt_at = 6 - 1
    else:
        qnt_at = 6
    
    
    if de > 6:
        qnt_de = 6
    else:
        qnt_de = de
    
    return qnt_de, qnt_at

defensores = 50
atacantes = 50
lista_atc = list()
lista_def = list()

qnt_atc, qnt_def = soldados(atacantes, defensores)

def sorteando_dano(l_atc, l_def):
    for i in range(qnt_atc):
        dano_atc = r.randint(1, 6)
        dano_def = r.randint(1, 6)
        l_atc.append(dano_atc)
        l_def.append(dano_def)
    
    return l_atc, l_def


danos_atq, danos_def = sorteando_dano(lista_atc, lista_def)

maior = max(len(danos_atq), len(danos_def))

print(f"Atacantes: {danos_atq}")
print(f"Defensores: {danos_def}")

while atacantes > 1 or defensores > 0:
    while len(danos_atq) > 0 or len(danos_def) > 0:
        for i in range(0, maior):
            if lista_atc[i] > lista_def[i]:
                defensores -= 1
            elif lista_def[i] > lista_atc[i]:
                atacantes -= 1
            else:
                atacantes -= 1
                
    danos_atq, danos_def = sorteando_dano(lista_atc, lista_def)
        
    







    


    
    
        
    
    
        
        