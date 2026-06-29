import cv2 as cv
import numpy as np
import time

img = np.zeros((512, 512, 3), np.uint8)

cv.rectangle(img, (200,200), (300, 300), (0,255,0), -1)
cv.circle(img, (75,75), 50,(0,0,255), -1)
cv.ellipse(img, (137, 420), (60,20), 0,0,360, (0, 100, 18), -1)

cv.imshow('a', img)
num = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
time.sleep(1)

imgaa = np.zeros((512, 512), np.uint8)

fontaa = cv.FONT_HERSHEY_SIMPLEX
cv.putText(imgaa, str(num), (200,250), fontaa, 1.5, (191,191), 4, cv.LINE_AA)

cv.imshow('104', imgaa)
cv.waitKey(1000) & 0xFF
cv.destroyAllWindows()