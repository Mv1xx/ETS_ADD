import cv2 as cv
import numpy as np

cap = cv.VideoCapture('video_car.avi')
fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('novo_video.avi', fourcc, 30.0, (300,300))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.flip(frame, 0)
        output.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:
            break

        
cap.release()
output.release()
cv.destroyAllWindows()