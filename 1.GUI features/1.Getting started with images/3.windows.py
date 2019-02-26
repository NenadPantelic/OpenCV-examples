import cv2
import numpy as np


image = cv2.imread("messi5.jpg",0)
cv2.namedWindow("Image window",cv2.WINDOW_NORMAL)
#cv2.namedWindow("Image window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Image window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
