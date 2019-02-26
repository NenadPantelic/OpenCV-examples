import cv2
import numpy as np



cap = cv2.VideoCapture(0)
while(True):
    if not cap.isOpened():
        cap.open()
    else:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame",gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

for i in range(19):
    print(cap.get(i))

cap.set(3,320)
cap.set(4,800)

cap.release()
cv2.destroyAllWindows()
