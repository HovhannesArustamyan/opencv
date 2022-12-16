import numpy as np
import cv2 as cv

photo = cv.imread('images/adele.jpg')
img = np.zeros(photo.shape[:2], dtype='uint8')
circle = cv.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv.rectangle(img.copy(), (25, 25), (250, 150), 255, -1)
img = cv.bitwise_and(photo, photo, mask=square)
img_or = cv.bitwise_or(circle, square)
img_xor = cv.bitwise_xor(circle, square)
img_not = cv.bitwise_not(square)

cv.imshow("Result", img_not)
cv.waitKey(4000)
