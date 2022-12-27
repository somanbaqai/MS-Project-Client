import cv2
import os
import base64
import requests
# import threading
# import matplotlib.pyplot as plt
# from threading import Thread, Lock
# plt.switch_backend('Agg') 
from multiprocessing import Process, Manager, Pool
from datetime import datetime

# import sqlite3
import numpy as np
from PIL import Image
from website.settings import BASE_DIR
from datetime import date

import django
django.setup()
from home.models import  ModelConfiguration


detector = cv2.CascadeClassifier(BASE_DIR+'/home/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


# # Create a connection witn databse
# conn = sqlite3.connect('db.sqlite3')
# if conn != 0:
#     print("Connection Successful")
# else:
#     print('Connection Failed')
#     exit()

# Creating table if it doesn't already exists
# conn.execute('''create table if not exists facedata ( id int primary key, name char(20) not null)''')

def getModelFromServer():
    t1 = datetime.now()
    # config = ModelConfiguration.objects.last()
    config = ModelConfiguration.objects.filter(startingDate__lte = date.today()).filter(endDate__gte = date.today()).last()
    print("config for fetching model from server :: " , config.endpointForFetching)
    response = requests.get(config.endpointForFetching,allow_redirects=True)
    open(BASE_DIR+'/home/trainer/trainer.yml','wb').write(response.content)
    print("~~~~ Model Downloaded From Server ~~~~~~~~")
    t2 = datetime.now()
    delta = t2 - t1
    # time difference in seconds
    print(f"Get Model: Time difference is {delta.total_seconds()} seconds")
    # time difference in milliseconds
    ms = delta.total_seconds() * 1000
    print(f"get Model: Time difference is {ms} milliseconds")


def sendModelToServer():
    t1 = datetime.now()
    # config = ModelConfiguration.objects.last()
    config = ModelConfiguration.objects.filter(startingDate__lte = date.today()).filter(endDate__gte = date.today()).last()
    print("config for posting model to server :: " , config.endpointForPosting)
    files = {"file" : open(BASE_DIR+'/home/trainer/trainer.yml','rb')}
    response = requests.post(config.endpointForPosting, files=files)
    # open(BASE_DIR+'/home/trainer/trainer.yml','wb').write(response.content)
    print("~~~~ Model Uploaded To Server~~~~~~~~")
    print(" Uplaod API Response :: " , response)
    t2 = datetime.now()
    delta = t2 - t1
    # time difference in seconds
    print(f"Send Model: Time difference is {delta.total_seconds()} seconds")
    # time difference in milliseconds
    ms = delta.total_seconds() * 1000
    print(f"Send Model: Time difference is {ms} milliseconds")



class FaceRecognition: 

    def getModelFromServer(self):
        config = ModelConfiguration.objects.last()
        print("config for fetching model from server :: " , config.endpointForFetching)
        response = requests.get(config.endpointForFetching,allow_redirects=True)
        open(BASE_DIR+'/home/trainer/trainer.yml','wb').write(response.content)
    def sendModelToServer(self):
        config = ModelConfiguration.objects.last()
        print("config for posting model to server :: " , config.endpointForPosting)
        files = {"file" : open(BASE_DIR+'/home/trainer/trainer.yml','rb')}
        response = requests.post(config.endpointForPosting, files=files)
        # open(BASE_DIR+'/home/trainer/trainer.yml','wb').write(response.content)
        print("~~~~ Model Uploaded To Server~~~~~~~~")
        print(" Uplaod API Response :: " , response)
   

    def faceDetect(self, Entry1):
       
        face_id = Entry1
        # pool = Pool(processes = 1)
        # pool.
        # print(pool.map(self.getDetectedFaceForRegistration, range(1),str(face_id)))
        # proc = Process(target=self.getDetectedFaceForRegistration, args=(face_id))
        p = Process(target=self.getDetectedFaceForRegistration, args=(face_id,))
        p.start()
        p.join()
        # proc.start()
        # proc.join()
        # print(pool.map(self.getDetectedFaceForRegistration, face_id))
        # face_name = Entry2
        # try:
        #     conn.execute('''insert into facedata values ( ?, ?)''', (face_id, face_name))
        #     conn.commit()
        # except sqlite3.IntegrityError:
        #     print("\n ERROR! This id alreeady exists in database!")
        #     print("\n Try agian with new id\n")
        #     exit()
    def getDetectedFaceForRegistration(self,face_id):

        print("received face id :: ")
        print(face_id)
        cam = cv2.VideoCapture(0)
            
        count = 0

        while(True):

            ret, img = cam.read()
            # img = cv2.flip(img, -1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite(BASE_DIR+'/home/dataset/User.' + face_id + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('Register Face', img)

            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                break
    
    
        cam.release()
        cv2.destroyAllWindows()

    
    def trainFace(self):
        # Path for face image database
        path = BASE_DIR+'/home/dataset'
        def getImagesAndLabels(path):

            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
            faceSamples=[]
            ids = []

            for imagePath in imagePaths:

                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                img_numpy = np.array(PIL_img,'uint8')

                face_id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = detector.detectMultiScale(img_numpy)

                for (x,y,w,h) in faces:
                    faceSamples.append(img_numpy[y:y+h,x:x+w])
                    ids.append(face_id)

            return faceSamples,ids

        print ("\n Training faces. It will take a few seconds. Wait ...")
        faces,ids = getImagesAndLabels(path)
        getModelFromServer()
        recognizer.read(BASE_DIR+'/home/trainer/trainer.yml')
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.save(BASE_DIR+'/home/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
        sendModelToServer()
        print("\n {0} faces trained. Exiting Program".format(len(np.unique(ids))))


    def recognizeFace(self): 

        pool = Pool(processes = 1)
        # print(pool.map(self.test, range(1)))
        confidence , face_id= pool.map(self.getFaceForRecognizer, range(1))[0]
        print("confidence recevied :: " , confidence)
        print("face id recevied :: " , face_id)
        
        if(confidence > 45):
            return -1

        return face_id

    def getFaceForRecognizer(self, id):
        getModelFromServer()
        recognizer.read(BASE_DIR+'/home/trainer/trainer.yml')
        cascadePath = BASE_DIR+'/home/haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(cascadePath)

        font = cv2.FONT_HERSHEY_SIMPLEX

        confidence = 100

        # Retriving names from database
        # data = conn.execute('''select * from facedata''')
        # for x in data:
        #     names.append(x[1]) 

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:
            face_id = -1
            ret, img =cam.read()

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                face_id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                print("confidence:: " , confidence)

                # Check if confidence is less then 100 ==> "0" is perfect match 
                if (confidence < 100):
                    name = 'Detected'
                else:
                    name = "Unknown"
                
                cv2.putText(img, str(name), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('Detect Face',img) 


            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            # print("exit key pressed :: " , k)
            if k == 27:
                break
            if confidence < 45:
                break

        print("\n Exiting Program")
        cam.release()
        cv2.destroyAllWindows()
        return confidence, face_id
        # globalConfidence = confidence
        # return_dict[confidence] = confidence
    
     