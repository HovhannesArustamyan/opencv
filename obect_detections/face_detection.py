import cv2 as cv
img = cv.imread('../images/adele.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cv.CascadeClassifier('../xml/haarcascade_face.xml')
results = faces.detectMultiScale(gray, scaleFactor=1.9, minNeighbors=2)
for (x, y, w, h) in results:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 155), thickness=2)
    cv.imshow('Detected faces', img)
    cv.waitKey()
cv.destroyAllWindows()
