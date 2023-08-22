import cv2
import numpy as np

vid = cv2.VideoCapture("cars.mp4")

if vid.isOpened()==False:
    print("Video not found")


while vid.isOpened():
    ret,frame = vid.read()
    if ret==True:
        height,width = frame.shape[:2]
        height = int(height/3)
        width = int(width/3)
        frame = cv2.resize(frame,(width,height),interpolation=cv2.INTER_LINEAR)
        cv2.imshow("Footage",frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

vid.release()

cv2.destroyAllWindows()