import cv2 as cv

img = cv.imread('images/adele.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
r, g, b = cv.split(img)

img_ = cv.merge([b, g])
cv.imshow("Result", img_)
cv.waitKey(3000)
