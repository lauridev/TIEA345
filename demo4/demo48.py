#@author Lauri Poikolainen 27.2.2019
import numpy as np
import cv2 
from matplotlib import pyplot as plt
from picamera import PiCamera

#ottaa kuvan
camera=PiCamera()
camera.capture("kuva6.jpg")

#lukee kuvan ja tarkistaa kaikki henkilöt kuvasta
img=cv2.imread("kuva6.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray =gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh)in eyes:
        cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#print(faces)
#tallentaa tuloksen
plt.imsave('tuliko.png',img)

