from lib import *

H = 20
W = 20
P = 20

fundo = get_map(W, H, P)

def quadrado(a1, a2, b1, b2):
    for i in range (a1, a2 + 1):
        fundo[a1][i] = (255,0,0)
        fundo[i][a1] = (255,0,0)
    
    for j in range(b1, b2 + 1):
        fundo[b2][j] = (255,0,0)
        fundo[j][b2] = (255,0,0)

quadrado(2, 10, 2, 10)
start(bg=(255,255,255), bg_map = fundo)
