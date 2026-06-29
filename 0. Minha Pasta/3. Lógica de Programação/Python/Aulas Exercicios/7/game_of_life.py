from lib import *
import random 

w = 100
h = 100
p = 7

def posicao_e_valida(x, y):
    if x < 0:
        return False
    if x >= w:
        return False

    if y < 0:
        return False
    if y >= h:
        return False
    
    return True

def conta_vizinhos_vivos(map, x, y):
    quantidade= 0

    if posicao_e_valida(y-1, x-1) and map[y-1][x-1]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y-1,x) and map[y-1][x]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y-1,x+1) and map[y-1][x+1]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y,x+1) and map[y][x+1]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y+1,x+1) and map[y+1][x+1]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y+1,x) and map[y+1][x]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y+1,x-1) and map[y+1][x-1]['color'] == (0,0,0):
        quantidade += 1
    if posicao_e_valida(y,x-1) and map[y][x-1]['color'] == (0,0,0):
        quantidade += 1
    
    return quantidade

def comportamento (e, e_map):
    vizinho = conta_vizinhos_vivos(e_map, e['x'], e['y'])

    vivo = e['color'] == (0,0,0)

    if vivo:
        if vizinho < 2 or vizinho > 4:
            if random.randint(1, 25) != 1:
                e['color'] = (255, 255, 255)
    else:
        if vizinho == 3:
            e['color'] = (0,0,0)

celula_morta = {
    'func' : comportamento, 
    'color' : (255, 255, 255),
    'z' : 1,
    'label' : 'celula morta'
}

celula_viva = {
    'func' : comportamento, 
    'color' : (0,0,0),
    'z' : 1,
    'label' : 'celula viva'
}

mapa_de_entidade = get_map(w, h, p)

for i in range(h):
    for j in range(w):
        mapa_de_entidade[i][j] = celula_morta.copy()

mapa_de_entidade [49][50] = celula_viva.copy()
mapa_de_entidade [50][50] = celula_viva.copy()
mapa_de_entidade [51][50] = celula_viva.copy()

start(e_map=mapa_de_entidade)