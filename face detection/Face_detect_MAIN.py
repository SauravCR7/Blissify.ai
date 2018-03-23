import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(1)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
 
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        print("x")
        print(x)
        print("y")
        print(y)
        print("x+w")
        print(x+w)
        print("y+h")
        print(y+h)

        image=frame[y:y+h,x:x+w]
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('detection',image)
        image = cv2.resize(image,(200,200), interpolation = cv2.INTER_CUBIC)
        
        
        #roi_gray=gray[y:y+h,x:x+h]
        #roi_color=frame[y:y+h,x:x+h]
        '''
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        '''
    
    cv2.imshow('face',frame)
    if cv2.waitKey(1) & 0xff==ord('v'):
            cv2.imwrite("face.jpeg",image)
            break       
    

   

cap.release()
cv2.destroyAllWindows()
