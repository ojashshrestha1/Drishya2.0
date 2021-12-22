import numpy as np
import cv2

def detecthuman(imagefile):
    img = cv2.imread(imagefile,0)
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt_tree.xml')
    upperBody_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_upperbody.xml')
    arrFace = face_cascade.detectMultiScale(img)
    arrUpperBody = upperBody_cascade.detectMultiScale(img)
    if(arrFace != () or arrUpperBody != ()):
        return True
            #for (x,y,w,h) in arrUpperBody:
            #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            #print('body found')
    else:
        return False
#    cv2.imshow('image',img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
