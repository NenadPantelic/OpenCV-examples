import cv2
import numpy


img = cv2.imread('messi5.jpg')
print img.shape
ball = img[80:140,130:190]
img[73:133,100:160] = ball


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
