                                             Face-Detection-and-Identification

This is a Python Program which detects, registers, and recognize faces that are displayed in camera.
For successful implementation of this program, Opencv library and haar cascades xml files are used.

To execute this project successfully, follow the steps below :

1) Install python in PC.

2) Install opencv using command prompt/terminal box :

      "pip install opencv-python"
      
      "pip install opencv-contrib-python"
      
3) Download Opencv for haar cascade xml files.

4) Run "camera_program.py" and "face_detection.py" to check if the opencv modules are working properly. If not, 
   then there is an installation problem.
   
   NOTE => MAKE SURE TO SET APPROPRIATE PATH FOR HAAR CASCADE AND OTHER REQUIRED PATHS
   
5) Now for face identification, there are 3 steps :
     
     i) Registration of person's face
     
     ii) Train PC to recognize faces
     
     iii) Identify faces
     
6) Registration of person's face :- Run "face_dataset_collection_live.py" and register your face by giving a user ID(say 1 or 2).
                                    The PC will take about 10 photos in one run, for the given ID.

7) Train PC to recognize faces :- Run "face_recognition_train_and_create_object_file.py" and create a ".yml" object file that will
                                  read all the faces in the existing dataset, and the file can be useful to identify faces.Then, edit
                                  "face_identification.py" and provide details to the corresponding ID of person.
                                  
8) Identify faces :- Run "face_identification.py", and this project will run successfully.
