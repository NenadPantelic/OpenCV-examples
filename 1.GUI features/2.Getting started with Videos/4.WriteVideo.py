import cv2
import numpy as np



cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc,20,(int(cap.get(3)),int(cap.get(4))))

while (cap.isOpened()):
    try:
        ret,frame = cap.read()
        out.write(frame)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
