import numpy as np
import cv2



#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3],np.uint8)

# img = cv2.line(img,(0,0),(100,100),(0,255,0), 5)
# img = cv2.arrowedLine(img,(0,100),(200,100),(0,255,0), 5) 
# img = cv2.rectangle(img,(150,150),(300,300),(0,0,255),5)
# img = cv2.rectangle(img,(150,150),(300,300),(0,0,255),-1)
img = cv2.circle(img,(150,150),40,(0,255,0),5)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"OpenCV",(150,150),font,2,(255,0,0),5,cv2.LINE_AA)

cv2.imshow("resim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()