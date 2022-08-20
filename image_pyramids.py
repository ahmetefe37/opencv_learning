from email.mime import image
import cv2
import numpy as np


img = cv2.imread("files/lena.jpg",1)

# lower1 = cv2.pyrDown(img)
# lower2 = cv2.pyrDown(lower1)

# higher1 = cv2.pyrUp(lower2)

layer = img.copy()
gp = [layer]

#smalling the image
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow("upper level Gaussian pyramids",layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)




cv2.imshow("original image",img)
# cv2.imshow("lower 1",lower1)
# cv2.imshow("lower 2",lower2)

cv2.waitKey(0)
cv2.destroyAllWindows()
