import math
def intevalo_confianca(z, dv, n, media):
    e = z * (dv / math.sqrt(n))
    return round(media - e, 2), round(media + e, 2)

def Z(media, afirmacao, n, dv):
    z = (media - afirmacao) /(dv / math.sqrt(n))
    return round(z, 2)

def proporcao(y, ps, pf, n):
    p = y / n
    z = (p - ps) / (math.sqrt(ps * pf/n)) 
    return round(z, 2)