import cv2 as cv

cap = cv.VideoCapture('video_car.mp4')
ret, frame = cap.read()

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv.imshow('corrida', frame)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()