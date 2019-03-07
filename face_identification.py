import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('C:/Users/User/Desktop/New folder (2)/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("C:/Users/User/Desktop/New folder (2)/training_data_set/trainingdata.yml")
id=0
font=cv2.FONT_HERSHEY_SIMPLEX
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="Vishal Gupta Reg. no. 012"
        if(id==2):
            id="Siddharth reg. no. 007"
        if id==3:
            id="Sanjeev Mudaliar reg. no. 011"
        if id==4:
            id="Gaurav"
        if id==5:
            id='rahul'
        if id==6:
            id="akshay"
        cv2.putText(img,str(id),(x,y+h),font,0.55,(0,255,156),2)
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

