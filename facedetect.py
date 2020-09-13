import numpy as np
import cv2
import random

##------------------------ multiple face detection-----------------------###

cas_path =r"C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
face = cv2.CascadeClassifier(cas_path)
v = cv2.VideoCapture(0)
while(1):
    rate,frame = v.read()
    frame = cv2.flip(frame,1)
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face.detectMultiScale(frame1,1.3,5)    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.imshow("Roll ON Baby",frame)
    if(cv2.waitKey(1) == 27):
        break        
v.release()
cv2.destroyAllWindows()


