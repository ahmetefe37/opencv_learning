from cgitb import grey
from turtle import width
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread("files/road.jpg",1)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def func_region(img,verticles):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    # matched_mask_color = (255,) * channel_count
    matched_mask_color = 255
    cv2.fillPoly(mask,verticles,matched_mask_color)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img

def draw_line(img,lines):
    img = img.copy()
    blank_img = np.zeros((img.shape[0], img.shape[1],3), dtype = np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_img,(x1,y1),(x2,y2),(0,0,255),5)

        img = cv2.addWeighted(img,0.8,blank_img,1,0.0)
        return img

def process(img):
    width = img.shape[1]
    height = img.shape[0]

    print(width ," - " , height)

    region = [(0,height),(width/2,height/2),(width,height)]

    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_img,100,200)
    cropped_img = func_region(canny_img,np.array([region],np.int32))

    lines = cv2.HoughLinesP(cropped_img,2, np.pi / 180, 120, lines=np.array([]), minLineLength=40,maxLineGap=100)

    line_image = draw_line(img,lines)
    return line_image

cap = cv2.VideoCapture("files/road_line.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("road video",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# titles = ["image", "cropped","canny","line_img"]

# images = [img,cropped_img,canny_img,line_image]

# for i in range(4):
#     plt.subplot(2,2,i+1), plt.imshow(images[i],"gray")
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

cap.release()
cv2.destroyAllWindows()
