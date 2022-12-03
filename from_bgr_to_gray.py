import cv2 as cv
import numpy as np

img = cv.imread('images/adele.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blured_img = cv.GaussianBlur(gray_img, ksize=(5, 5), sigmaX=0)
img = cv.Canny(blured_img, 100, 140)  # if < 100 then make 0 , if  > 140 , then make 255

con, hir = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.drawContours(new_img, con, contourIdx=-1, color=(230, 111, 148), thickness=1)
cv.imshow("Result", new_img)
cv.waitKey(3000)
