import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# mouse event list

# 'EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 
# 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
# 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 
# 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
# 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
# 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP'

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x," - ",y)
    #     font = cv2.FONT_HERSHEY_COMPLEX
    #     XYstring = str(x) +" - "+ str(y)
    #     cv2.putText(img,XYstring,(x,y),font,1,(0,0,255),4)
    #     cv2.imshow("image",img)

    # if event == cv2.EVENT_RBUTTONDOWN:
    #     font = cv2.FONT_HERSHEY_COMPLEX
    #     XYstring = str(x) +" - "+ str(y)
    #     cv2.putText(img,XYstring,(x,y),font,1,(0,255,0),4)
    #     cv2.imshow("image",img)

        cv2.circle(img, (x,y),3,(0,255,0),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img,points[-1],points[-2],(0,255,0),3)
        cv2.imshow("image",img)


img = np.zeros([512,512,3],np.uint8)
# img = cv2.imread("lena.jpg",1)
cv2.imshow("image",img)
points = []

cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()