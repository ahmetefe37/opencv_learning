import cv2
import numpy as np

img = cv2.imread("files/sudoku.png",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detecting the edges
edges = cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow("edges",edges)
lines = cv2.HoughLines(edges,0.95,np.pi / 180, 130)

for line in lines:
    radius, angle = line[0]
    a = np.cos(angle)
    b = np.sin(angle)
    x0 = a * radius
    y0 = b * radius
    # new coords are stores the rounded of value of (radius * cos(angle) - 1000 * sin(angle))
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0  - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow("image",img)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()