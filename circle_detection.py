import cv2
import numpy as np

img = cv2.imread("files/smarties.png")
output = img.copy()
gray_img = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img,5)
circles = cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    cv2.circle(output,(x,y),r, (255,255,0),3)


cv2.imshow("image",output)

cv2.waitKey(0)
cv2.destroyAllWindows()