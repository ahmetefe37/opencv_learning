import imp
import cv2
import numpy as np
from matplotlib import pyplot as plt




# img = cv2.imread("files/opencv-logo.png",1)
# img = cv2.imread("files/gaussian_blur.png",1)
# img = cv2.imread("files/water.png",1)
img = cv2.imread("files/lena.jpg",1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# homojenik filtre 1/(yükseklik * genişlik)
kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
mblur = cv2.medianBlur(img,5)
biliteralFilter = cv2.bilateralFilter(img,9,75,75)

titles = ["image","2D Convolution","blur","Gaussian Blur","Median Blur","biliteral Filter"]
img = [img,dst,blur,gblur,mblur,biliteralFilter]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(img[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()