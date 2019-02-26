import cv2
import numpy as np

image = cv2.imread("messi5.jpg",0)
#print(image)
cv2.imshow("Messi image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.destroyWindow("Messi image")
