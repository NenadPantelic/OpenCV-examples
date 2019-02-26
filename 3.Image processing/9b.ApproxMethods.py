import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('rectangle.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, 0, (0,255,0), 3)
#cv2.drawContours(img2,contours2,-1,(0,255,0),3)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

