import numpy as np

import cv2

haar_cascade_face = cv2.CascadeClassifier('C:/Your_Path_of_Opencv_file/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

id = input('Enter user id : ')

photos=0;

while 1:

    ret, img = camera.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade_face.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        photos=photos+1;

        cv2.imwrite("C:/Users/User/Desktop/New folder (2)/face_dataset/User."+str(id)+ "." +str(photos)+ ".jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.waitKey(100)

    cv2.imshow('img',img)

    cv2.waitKey(1)

    if photos >= 10:        #i.e. if no. of photos clicked by computer is more than 10, then terminate clicking photos

        break

camera.release()

cv2.destroyAllWindows()
