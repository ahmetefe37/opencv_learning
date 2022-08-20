import cv2
import numpy as np

# img = cv2.imread("files/opencv-logo.png",1)
img = cv2.imread("files/lena.jpg",1)
# img_grey = cv2.imread("files/opencv-logo.png",0)
img_grey = cv2.imread("files/lena.jpg",0)

ret , thresh = cv2.threshold(img_grey, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("number of contours: "+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow("image",img)
cv2.imshow("grey image",img_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()