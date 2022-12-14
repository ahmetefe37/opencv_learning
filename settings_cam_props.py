import cv2

capture = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter("output_video.avi",fourcc,20.0,(640,480))

width, height = capture.get(cv2.CAP_PROP_FRAME_WIDTH) , capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width,height)

capture.set(3,245)
capture.set(4,122)

while capture.isOpened():
    ret, frame = capture.read()

    if ret == True:
        # out.write(frame)

        gray_cap = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow("camera",gray_cap)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

print(width,height)
capture.release()
# out.release()
cv2.destroyAllWindows()