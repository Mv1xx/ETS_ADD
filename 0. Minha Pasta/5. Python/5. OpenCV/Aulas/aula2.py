import cv2 as cv
import numpy as np
import time

#quadrado preto so de zeros
img = np.zeros((512, 512, 3), np.uint8)


#linhas horizontais (imagem, (xi, y1), (xf, yf), (color), thickness)
cv.line(img, (150, 0), (150, 512), (255,255,255), 5)
cv.line(img, (350, 0), (350, 512), (255,255,255), 5)

#linhas verticais
cv.line(img, (0, 150), (512, 150), (255, 255, 255), 5)
cv.line(img, (0, 350), (512, 350), (255, 255, 255), 5)

cv.rectangle(img, (200,200), (300, 300), (0,255,0), -1)
cv.circle(img, (75,75), 50,(0,0,255), -1)
cv.ellipse(img, (137, 420), (60,20), 0,0,360, (0, 100, 18), -1)


font = cv.FONT_HERSHEY_SIMPLEX
texto = 'tabuleiro top'

#escrevendo texto (imagem, texto, (xt, yt), tipodefonte, tamanho da fonte, color, thickness, line)
cv.putText(img, texto, (50,50), font, 1.5, (191, 191), 4, cv.LINE_AA)

cv.imshow('tic-tac-toe', img)
num = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
time.sleep(1)






