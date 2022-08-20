import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("files/lena.jpg",0)     

# img = np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,50),(50,100),(255),-1)
# cv2.rectangle(img,(0,100),(50,150),(127),-1)
# cv2.rectangle(img,(50,100),(100,150),(64),-1)
# cv2.rectangle(img,(50,150),(100,200),(180),-1)

# b, g, r = cv2.split(img)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)


cv2.imshow("image",img)
# cv2.imshow("b",b)
# cv2.imshow("g",g)
# cv2.imshow("r",r)

# plt.hist(img.ravel(),256,[0,256])
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
plt.show()



if cv2.waitKey(40) == 27:
    cv2.destroyAllWindows()

