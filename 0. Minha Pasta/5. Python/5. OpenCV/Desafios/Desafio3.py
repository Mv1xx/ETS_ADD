import cv2
cap = cv2.VideoCapture('video_car.mp4') # Armazenar o vídeo
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('carro_psicodélico.avi', fourcc, 30.0, (300,300))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame2 = cv2.resize(frame, (300,300))
        output.write(frame2)
        cv2.imshow('frame', frame2)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
output.release()
cv2.destroyAllWindows()