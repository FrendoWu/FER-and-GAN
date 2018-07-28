import numpy as np
import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	print(x,y,w,h)
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	crop_gray = gray[y:y+h, x:x+w]
	crop_color = img[y:y+h, x:x+w]

	cv2.imwrite("croppedface_gray.jpg", crop_gray)
    # eyes = eye_cascade.detectMultiScale(crop_color)
    # for (ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(crop_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('img.png',img)