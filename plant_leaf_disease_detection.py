#import libraries
import cv2
import numpy as np
#upload image
l1=cv2.imread('l1.jpeg')
#resize
resize=cv2.resize(l1,(200,200))
#convert image to hsv
hsv=cv2.cvtColor(resize,cv2.COLOR_BGR2HSV)
#set boundaries
lower=np.array([10,50,50])
upper=np.array([35,255,255])

mask=cv2.inRange(hsv,lower,upper)
disease_area=cv2.bitwise_and(resize,resize,mask=mask)
contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
output=resize.copy()
cv2.drawContours(output,contours,-1,(0,255,0),2)

#to display the output
cv2.imshow('l1',resize)
cv2.imshow('mask',mask)
cv2.imshow('disease_area',disease_area)
cv2.imshow('output',output)
#to hold the image
cv2.waitKey(0)