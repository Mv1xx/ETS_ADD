import cv2 as cv
import numpy as np

def funcao(event, x, y, flags, param):
    global r, g, b
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 50, (b, g, r), -1)

r = g = b = 0
img = np.zeros((512,512, 3), np.uint8)
cv.namedWindow('imagem')
cv.setMouseCallback('imagem', funcao)
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    cv.putText(img, 'red ='+ str(r), (10,30), font,1, (255,255,255), 2)
    cv.putText(img, 'green ='+ str(g), (10,80), font, 1, (255,255,255), 2)
    cv.putText(img, 'blue ='+ str(b), (10,130), font, 1, (255,255,255), 2)
    cv.imshow('imagem', img)
    key = cv.waitKey(1) & 0xFF

    if key == ord('r'):
        r += 10
    elif key == ord('g'):
        g += 10
    elif key == ord('b'):
        b += 10
    if key == 27:    
        break

cv.destroyAllWindows()
