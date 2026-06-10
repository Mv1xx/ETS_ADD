import os
import time
 
 
#===============================================
#   Crie uma funçao que move a imagem
#   em X como se fosse uma esteira, portanto
#   o que está na ultima coluna case ande 1
#   para o lado a coluna vai para a primeira
#   coluna
#===============================================
 
scene = [
    '    X                         X               X   ',
    '    X                        XX  X           XX   ',
    '   XX       X               XXXX XX          XXX  ',
    '   XXX      XX       X      XXXXXXXX         XXXX ',
    '  XXXXX    XXXX     XX     XXXXXXXXX        XXXXX ',
    ' XXXXXX   XXXXX    XXX    XXXXXXXXXXX       XXXXXX',
    ' XXXXXX  XXXXXXX   XXX    XXXXXXXXXXX      XXXXXXX',
    ' XXXXXXX XXXXXXX  XXXXX   XXXXXXXXXXXX     XXXXXXX',
    ' XXXXXXX XXXXXXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXX',
]
 
def moveX(step):
    scene_copy = scene.copy()

    for col in range(len(scene[0])):
        for lin in range(len(scene)):
            aux = list(scene_copy[lin]) 
            aux[(col+step)%(len(scene[0]))] = scene[lin][col]
            scene_copy[lin] = ''.join(aux)
    
    return scene_copy



 
for i in range(1000000):
    scene = moveX(1)
 
    for s in scene:
        print(s)
 
    time.sleep(0.01)
    os.system('cls')
 
 