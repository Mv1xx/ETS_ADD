import cv2 as cv

dog = cv.imread('dog.jpg', cv.IMREAD_ANYCOLOR)
img = cv.cvtColor(dog, cv.COLOR_BGR2HSV)

# cv.imshow('dog', dog)
cv.imshow('a', img)

cv.waitKey(0)
cv.destroyAllWindows()
