import cv2
import numpy as np



img = cv2.imread('messi5.jpg')
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
print(b,g,r)
b = img[:,:,0]
img[:,:,2] = 0
print(b)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
