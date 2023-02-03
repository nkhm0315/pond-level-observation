import cv2
import time

cap = cv2.VideoCapture(0)
timer = time.time()
stopSec = 10

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if timer + stopSec < time.time():
        timer = time.time()
        ret, source = cap.read()
        cv2.imshow('Frame', source)
        #cv2.imwrite('./data/' + str(time.time) + 'jpg', source)
    else:
        time.sleep(1)