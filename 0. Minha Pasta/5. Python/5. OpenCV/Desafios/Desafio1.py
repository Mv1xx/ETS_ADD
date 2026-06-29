import cv2 as cv
import numpy as np

def funcao(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEWHEEL:
        if x < 250:
            cv.circle(img, (x, y), 50, (0,0,255), -1)
    if event == cv.EVENT_LBUTTONDBLCLK:
        if x > 200:
            cv.ellipse(img, (x, y), (60,20), 0,0,360, (0, 100, 18), -1)
       

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('a')
cv.setMouseCallback('a', funcao)


while True:
    cv.imshow('a', img)
    if cv.waitKey(10) & 0xFF == 27:
        break

cv.destroyAllWindows()