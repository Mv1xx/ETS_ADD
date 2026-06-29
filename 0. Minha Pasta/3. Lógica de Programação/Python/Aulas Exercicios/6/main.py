import random as rd
from lib import get_map, start
 
W = 50
H = 50
P = 10
 
bg_map = get_map(W, H, P)
 
 
def desenha_quadrado(x1,y1,x2,y2,color):
    for i in  range(y1,y2):
        for j in range(x1,x2):
            bg_map [i][j] = color
 
 
 
desenha_quadrado(24,24,26,26,(255,255,0))
 
start(
    bg_map=bg_map
)