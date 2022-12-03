import cv2


img = cv2.imread('images/adele.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp = sift.detect(gray, None)
kp1, des = sift.detectAndCompute(gray, None)
img = cv2.drawKeypoints(gray, kp1, img, flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints.jpg', img)
