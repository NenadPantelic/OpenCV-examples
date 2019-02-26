import cv2
import numpy as np

image = cv2.imread("messi5.jpg",0)
print(image)
cv2.imshow("Image_grayscale",image)


image2 = cv2.imread("messi5.jpg",1)
print(image)
cv2.imshow("Image_color",image2)

image3 = cv2.imread("messi5.jpg",-1)
print(image)
cv2.imshow("Image_original",image3)


cv2.waitKey(0)
cv2.destroyAllWindows()
