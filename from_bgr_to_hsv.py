import cv2 as cv

img = cv.imread('images/adele.jpg')
img_ = cv.cvtColor(img, cv.COLOR_BGR2HSV)
r, g, b = cv.split(img)

img__ = cv.merge([b, g])
cv.imshow("Result", img__)
cv.waitKey(6000)
