import numpy as np

import cv2

haar_cascade_face = cv2.CascadeClassifier('C:/Your_Opencv_file_path/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

haar_cascade_eye = cv2.CascadeClassifier('C:/Your_Opencv_file_path/opencv/sources/data/haarcascades/haarcascade_eye.xml')

camera = cv2.VideoCapture(0)

while 1:

    ret, img = camera.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade_face.detectMultiScale(gray, 1.5, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]

        eyes = haar_cascade_eye.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:

            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        print("found " +str(len(eyes)) +" eye(s)")

    print("found " +str(len(faces)) +" face(s)")

    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:             #i.e. if pressed Esc button, then close

        break

camera.release()

cv2.destroyAllWindows()
