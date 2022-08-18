import numpy as np
import cv2

img1 = np.zeros((500,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)

img2 = cv2.imread("files/image_1.png",1)
img2 = cv2.resize(img2, (500,500))

bitAnd = cv2.bitwise_and(img2,img1)
bitOr = cv2.bitwise_or(img2,img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)
bitXor = cv2.bitwise_xor(img1,img2)

cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
# cv2.imshow("bitwise and", bitAnd)
# cv2.imshow("bitwise or", bitOr)
# cv2.imshow("bitwise not", bitNot1)
# cv2.imshow("bitwise not", bitNot2)
# cv2.imshow("bitwise xor", bitXor)


cv2.waitKey(0)
cv2.destroyAllWindows()