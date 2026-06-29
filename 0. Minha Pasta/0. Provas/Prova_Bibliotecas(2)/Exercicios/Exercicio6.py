import cv2
from matplotlib.pylab import rand
import numpy as np


def rodas(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (150, 450), 40, (0,0,0), -1)
        cv2.circle(img, (150, 450), 25, (60,60,60), -1)

        cv2.circle(img, (350, 450), 40, (0,0,0), -1)
        cv2.circle(img, (350, 450), 25, (60,60,60), -1)

    if event == cv2.EVENT_FLAG_RBUTTON:
        cv2.rectangle(img, (150,350), (200, 280), (300,300,300), -1)
        cv2.rectangle(img, (300,350), (250, 280), (300,300,300), -1)
        cv2.rectangle(img, (390,350), (350, 280), (300,300,300), -1)
    
    if event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img, (300, 100), 20, (300,200,0), -1)
        cv2.circle(img, (280, 80), 20, (300,200,0), -1)
        cv2.circle(img, (280, 70), 20, (300,200,0), -1)
        cv2.circle(img, (280, 80), 20, (300,200,0), -1)

        cv2.circle(img, (150, 100), 20, (300,200,0), -1)
        cv2.circle(img, (170, 75), 20, (300,200,0), -1)
        cv2.circle(img, (180, 70), 20, (300,200,0), -1)
        cv2.circle(img, (200, 80), 20, (300,200,0), -1)


back_color = (200, 100, 0)

img = np.full((500,500,3), back_color, dtype = np.uint8)
arbusto1 = cv2.circle(img, (400, 400), 50, (0,200,0), -1)
arbusto2 = cv2.circle(img, (100, 400), 50, (0,200,0), -1)
asfalto = cv2.rectangle(img, (0,500), (600, 400), (100, 100, 100), -1)
carro = cv2.rectangle(img, (100,430), (400, 250), (10, 10, 200), -1)
                        #(esquerda, baixo), (direita, cima)
cv2.namedWindow('img')
cv2.setMouseCallback('img', rodas)

while True:
    cv2.imshow('img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.imwrite('onibus_vermelho.jpg', img)
        break

cv2.destroyAllWindows()