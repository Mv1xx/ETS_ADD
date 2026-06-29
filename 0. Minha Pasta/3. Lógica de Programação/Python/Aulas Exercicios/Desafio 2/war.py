import random

def soldados (at, de):
    if at == 1:
        return
    elif at < 6:
        qnt_at = at - 1
    else:
        qnt_at = 6
    
    if de > 6:
        qnt_de = 6
    else:
        qnt_de = de
    
    return qnt_at, qnt_de

def dano():
    lista_at = list()
    lista_de = list()
    
    for i in range(qnt_at):
        dano_at = random.randint(1, 6)
        lista_at.append(dano_at)
    
    for j in range(qnt_de):
        dano_de = random.randint(1, 6)
        lista_de.append(dano_de)
    
    lista_at.sort(reverse = True)
    lista_de.sort(reverse = True)
    return lista_at, lista_de
        

atacantes = 4
defensores = 5

lista_at = list()
lista_de = list()

qnt_at, qnt_de = soldados(atacantes, defensores)

dano_at, dano_de = dano()

print(f"Atacantes: {dano_at}\nDefensores: {dano_de}")

menor = min(len(dano_at), len(dano_de))

# while True:
#     while qnt_at > 0 or qnt_de > 0:
#         dano_at, dano_de = dano()
        
#         for i in range(menor):
#             if dano_at[i] > dano_de[i]:
#                 defensores = defensores - 1
                
#             elif dano_at[i] < dano_de[i]:
#                 atacantes = atacantes - 1
                
#             else:
#                 atacantes = atacantes - 1

    
    
#     print(f"Atacantes: {dano_at}\nDefensores: {dano_de}")
    
#     if atacantes == 0 or defensores == 0:
#         break

while qnt_at > 0 or qnt_de > 0:
    dano_at, dano_de = dano()
    for i in range(menor):
        if dano_at[i] > dano_de[i]:
            defensores = defensores - 1
            
        elif dano_at[i] < dano_de[i]:
            atacantes = atacantes - 1
            
        else:
            atacantes = atacantes - 1
    






    

