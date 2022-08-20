import cv2
import numpy as np

img = cv2.imread("files/shapes.jpg",1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_img,240,255,cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for c in contours:
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c,True), True)

    cv2.drawContours(img, [approx], 0, (0,0,0),3)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        asp_ratio = float(w)/h
        print(asp_ratio)
        if asp_ratio > 0.95 and asp_ratio < 1.05:
            cv2.putText(img,"Square",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,"Rectangle",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 10:
        cv2.putText(img,"star",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    
    else:
        cv2.putText(img,"circle",(x+15,y+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()







