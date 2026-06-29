import cv2 as cv

dog = cv.imread('dog.jpg', cv.IMREAD_ANYCOLOR)
dog_cinza = cv.imread('dog.jpg', cv.IMREAD_GRAYSCALE)
dog_transp = cv.imread('dog.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('dog', dog)
x = cv.waitKey(0)
print('TECLA APERTADA', x)
cv.destroyAllWindows()

cv.imwrite('dig_cinza.jpg', dog_cinza)