import numpy as np
import cv2
from matplotlib import pyplot as plt

norm_img = cv2.imread("files/smarties.png",1)
img = cv2.imread("files/smarties.png",cv2.IMREAD_GRAYSCALE)

# img = cv2.imread("files/j.png",cv2.IMREAD_GRAYSCALE)

# _,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

# kernel = np.ones((5,5),np.uint8)

# dilation = cv2.dilate(mask,kernel,iterations=2)
# erosion = cv2.erode(mask,kernel,iterations=1)
# opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
# closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
# gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
# tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

kernel = np.ones((2,2),np.uint8)

dilation = cv2.dilate(img,kernel,iterations=4)
erosion = cv2.erode(img,kernel,iterations=4)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)


titles = ["image","normal img","dilation","erosion","opening","closing","gradient","tophat"]

images = [img,norm_img,dilation,erosion,opening,closing,gradient,tophat]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()