import cv2
import numpy as np

# img = cv2.imread("files/sudoku.png",1)
img = cv2.imread("files/road.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((2,2),np.uint8)
closing =  cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)

_, thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
_, thresh2 = cv2.threshold(thresh1,127,255,cv2.THRESH_TOZERO)

cv2.imshow("closing",closing)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh2)

# detecting the edges
edges = cv2.Canny(thresh2,50,150,apertureSize=3)
cv2.imshow("edges",edges)
lines = cv2.HoughLinesP(edges,2,np.pi / 180, 100, minLineLength=50,maxLineGap=2)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow("image",img)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()