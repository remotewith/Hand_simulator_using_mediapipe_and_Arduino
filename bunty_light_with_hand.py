from turtle import width
import cv2
import mediapipe as mp
import thesius_module as the
from pyfirmata import Arduino,SERVO

from time import sleep
import numpy as np


port ='COM6'
pin=10
p=9
pon=6
#led_pin=13

board=Arduino(port)
board.digital[pin].mode=SERVO
board.digital[p].mode=SERVO
board.digital[pon].mode=SERVO

def nothing(x):
          pass

def rotate(q,angle):
          board.digital[q].write(angle)
          #sleep(.15)


cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture('http://[2409:4031:4e8c:7ce6::f248:9204]:8080/video')
detector=the.handDetector()


while True:
    t,a=False,False
    _,img=cap.read()


    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:
        w=np.interp(lmList[9][1],[-80,460],[0,180])
        h=np.interp(lmList[9][2]+20,[100,560],[0,180])  
        
        t=True

        if lmList[8][2] < lmList[7][2]:
            a=True

    while a:

        #board.digital[led_pin].write(1)
        #break
        rotate(pon,110)
        break
        
    while not a:

        #board.digital[led_pin].write(0)
        #break
        rotate(pon,0)
        break
        
    while t:
        rotate(pin,h)
        rotate(p,w)
        break
              
            
    while not t:
        rotate(pin,0)
        rotate(p,0)
        break


    cv2.imshow('Image',img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows
cap.release()
