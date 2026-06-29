def qnt_soldados(*):
    if atacantes == 1:
        qnt_at = 1
    elif atacantes < 6:
        qnt_at = 6 - 1
    else:
        qnt_at = 6
    
    
    if defensores > 6:
        qnt_de = 6
    else:
        qnt_de = defensores
    
    return qnt_at, qnt_de

def sorteando_dano(l_atc, l_def):
    for i in range(qnt_atc):
        dano_atc = r.randint(1, 6)
        dano_def = r.randint(1, 6)
        l_atc.append(dano_atc)
        l_def.append(dano_def)
    
    return l_atc, l_def

atacantes = 50
defensores = 50

qnt_atq, qnt_def = qnt_soldados(atacantes, defensores)

for i in 