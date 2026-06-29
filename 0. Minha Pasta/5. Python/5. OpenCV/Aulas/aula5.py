import cv2 as cv
import random
import numpy as np

def funcao(event, x, y, flags, param):
    global a, b, c 
    if event == cv.EVENT_LBUTTONDOWN:
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)

a = b = c = 0
cv.namedWindow('janela')
cv.setMouseCallback('janela', funcao)

while True:
    img = np.full((215, 215, 3), (a, b, c), np.uint8)
    cv.imshow('janela', img)
    if cv.waitKey(10) & 0xFF == 27:
        break


