import cv2

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
writer = cv2.VideoWriter('video1.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                         (frame_width, frame_height))
while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    print(frame.shape)
    cv2.imshow("frame", frame)
    writer.write(frame)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
