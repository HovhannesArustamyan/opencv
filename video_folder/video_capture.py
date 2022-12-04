import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

colors = [[5, 107, 0, 19, 255, 255],
          [133, 56, 0, 59, 156, 255],
          [57, 76, 0, 100, 255, 255]]


def find_color(img, colors):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        cv2.imshow(str(color[0]), mask)


while True:
    success, img = cap.read()
    find_color(img, colors)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


img = cv2.imread('/opencv_proj/images/lopez.png')
cv2.imshow('img', img)
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow('imgCanny', imgCanny)

cv2.waitKey(7000)
