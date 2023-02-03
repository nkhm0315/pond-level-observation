import cv2
import time

timer = time.time()
stopSec = 10

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if timer + stopSec < time.time():
        timer = time.time()
        cap = cv2.VideoCapture(0)
        ret, source = cap.read()
        cap.release()
        cv2.imshow('Frame', source)
        #cv2.imwrite('./data/' + str(time.time) + 'jpg', source)
        img = cv2.Canny(source, 50, 200)
    else:
        time.sleep(1)