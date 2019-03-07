import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/New folder (2)/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/New folder (2)/opencv/sources/data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:

    ret, img = cap.read()

    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:

        break

cap.release()

cv2.destroyAllWindows()
