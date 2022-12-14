import numpy as np
import cv2

img = cv2.imread("files/messi5.jpg",1)
img2 = cv2.imread("files/opencv-logo.png",1)

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333,100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#img_result = cv2.add(img,img2)
img_result = cv2.addWeighted(img,0.8,img2,0.2,0)


cv2.imshow("image",img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

