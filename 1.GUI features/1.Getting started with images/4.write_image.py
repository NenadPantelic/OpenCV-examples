import cv2
import numpy as np

image = cv2.imread("messi5.jpg",0)
cv2.imshow("Image",image)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_grayscale.png",image)
    cv2.destroyAllWindows()
print(k)
