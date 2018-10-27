import cv2

ant_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('sample.jpeg')
cv2.imshow("undetected", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ants = ant_cascade.detectMultiScale(img,1.1,1)

for (x,y,w,h) in ants:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)

cv2.imshow('detected',img)
cv2.waitKey()
