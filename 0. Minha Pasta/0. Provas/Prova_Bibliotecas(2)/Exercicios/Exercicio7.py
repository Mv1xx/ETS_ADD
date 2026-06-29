import cv2
import random

cap = cv2.VideoCapture('babydance.mp4')
ret, frame = cap.read()
font = cv2.FONT_HERSHEY_COMPLEX
texto = "Dance baby, dance!"

while True:
    ret, frame = cap.read()
    x = random.randint(0,640)
    y = random.randint(0,480)

    cv2.putText(frame, texto, (x, y), font, 1.5, (191,0,191), 4, cv2.LINE_AA)
    if ret == False:
        break

    cv2.imshow('bebe dancando', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()