import os

import numpy as np

import cv2

from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

recognizer = cv2.face.LBPHFaceRecognizer_create();

path="C:/Your_face_dataset_path/face_dataset"

def getImagesWithID(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   

    faces = []

    IDs = []

    for imagePath in imagePaths:      

  #convert the images to grayscale

        facesImg = Image.open(imagePath).convert('L')

        face_NP = np.array(facesImg, 'uint8')

        #Extract the label of image

        ID= int(os.path.split(imagePath)[-1].split(".")[1])

        #Detect the face

        faces.append(face_NP)

        IDs.append(ID)

        cv2.imshow("Adding faces for traning",face_NP)

        cv2.waitKey(10)

    return np.array(IDs), faces

Ids,faces  = getImagesWithID(path)

recognizer.train(faces,Ids)

recognizer.save("C:/Required_Destination_Path/trainingdata.yml")

cv2.destroyAllWindows()
