from lib import *

H = 20
W = 20
P = 20

fundo = get_map(W, H, P)

def quadrado(a1, a2, b1, b2):
    for i in range (a1, a2 + 1):
        for j in range(b1, b2 + 1):
            fundo[i][j] = (255,0,0)


quadrado(2, 10, 2, 10)
start(bg=(255,255,255), bg_map = fundo)
