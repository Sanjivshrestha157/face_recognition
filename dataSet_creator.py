import cv2
import numpy as np
import trainer
def main():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    id=input("Enter user id:")
    
    sampleNum=0
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.5,2)
        for(x,y,w,h) in faces:
            sampleNum+=1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            
            cv2.waitKey(100)
        cv2.imshow("Face",img)
        cv2.waitKey(1)
        if(sampleNum>20):
            break
        
    cam.release()
    cv2.destroyAllWindows()
    trainer.main()