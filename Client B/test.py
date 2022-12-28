import cv2
import os
import base64
import requests

# import sqlite3
import numpy as np
from PIL import Image

detector = cv2.CascadeClassifier('home/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

def getModelFromServer():
    response = requests.get("http://localhost:8080/download/model",allow_redirects=True)
    open('home/trainer/trainer.yml','wb').write(response.content)
    print("~~~~ Model Downloaded From Server ~~~~~~~~")

def recognizeFace(): 
        getModelFromServer()
        recognizer.read('home/trainer/trainer.yml')
        cascadePath = 'home/haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(cascadePath)

        font = cv2.FONT_HERSHEY_SIMPLEX

        confidence = 100

        # Retriving names from database
        # data = conn.execute('''select * from facedata''')
        # for x in data:
        #     names.append(x[1]) 

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("preview", cv2.WINDOW_NORMAL)

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
                # print("confidence:: " , confidence)

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
        print("confidence:: " , confidence)
        cam.release()
        cv2.destroyAllWindows()
        if(confidence > 45):
            return -1

        return face_id

recognizeFace()