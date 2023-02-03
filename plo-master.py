import cv2
import time
import numpy as np
import math

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
        lines = cv2.HoughLinesP(img, rho=1, theta=np.pi/360, threshold=100, minLineLength=30, maxLineGap=10)
        if lines is not None:
            for line in lines:
                vec = np.array([line[0,0], line[0,1]]) - np.array([line[0,2], line[0,3]])
                vecAng = np.arctan2(vec[0], vec[1])
                vecAng = math.degrees(vecAng)
                if vecAng < -135 and vecAng > -180:
                    cv2.line(source,pt1=(line[0,0],line[0,1]),pt2=(line[0,2],line[0,3]),color=(0,0,255),thickness=1)
                    vecFlg = 1
    else:
        time.sleep(1)