import cv2
import numpy as np
from matplotlib import pyplot as plt

apple = cv2.imread("files/apple.jpg",1)
orange = cv2.imread("files/orange.jpg",1)

blend = np.hstack((apple[:, :256],orange[:, 256:]))

print(apple.shape)
print(orange.shape)

# generate gaussian pyramids for apple 
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate gaussian pyramids for orange 
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


# generate Laplacian pyramids for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)

# generate Laplacian pyramids for orange
orange_copy = gp_apple[5]
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)

# add left and right half of images in each levels
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n +=1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[: ,0:int(cols/2)], orange_lap[: ,int(cols/2): ]))
    apple_orange_pyramid.append(laplacian)

# reconstruction
reconsturction_result = apple_orange_pyramid[0]
for i in range(1,6):
    reconsturction_result = cv2.pyrUp(reconsturction_result)
    reconsturction_result = cv2.add(apple_orange_pyramid[i],reconsturction_result)


cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("blend",blend)
cv2.imshow("reconsturction",reconsturction_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
