import cv2
import numpy as np


x = np.uint8([250])
y = np.uint8([10])



print (cv2.add(x,y))
print(x + y)




img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

img = cv2.add(img1,img2)
img_ = img1 + img2


cv2.imshow('Addition 1',img)
cv2.imshow('Addition 2',img_)

cv2.waitKey(0)
cv2.destroyAllWindows()
