import cv2 as cv

img = cv.imread('../images/adele.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cv.CascadeClassifier('xml/haarcascade_face.xml')
eyes = cv.CascadeClassifier('xml/haarcascade_eye.xml')
result = faces.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=3)
for (x, y, w, h) in result:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 187), thickness=8)
    cv.imshow('gray', img)
    cv.waitKey(2000)
    roi = img[y:y + h, x:x + w]
    roi_gray = gray_img[y:y + h, x:x + w]
    eye_result = eyes.detectMultiScale(roi_gray, scaleFactor=1.2)
    for (x_eye, y_eye, w_eye, h_eye) in eye_result:
        cv.rectangle(roi, (x_eye, y_eye), (x_eye + w_eye, y_eye + h_eye), (0, 0, 187), thickness=4)
        cv.imshow('gray', img)
        cv.waitKey(0)
cv.destroyAllWindows()
