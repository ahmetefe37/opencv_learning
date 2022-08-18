import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("files/messi5.jpg",0)

canny = cv2.Canny(img,100,200)

images = [img,canny]
titles = ["image","canny"]

for i in range(2):
    plt.subplot(2,1,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])



plt.show()