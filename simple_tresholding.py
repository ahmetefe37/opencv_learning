import numpy as np
import cv2

img = cv2.imread("files/gradient.png",1)

_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("images",img)
cv2.imshow("th1 image",th4)

cv2.waitKey(0)
cv2.destroyAllWindows()