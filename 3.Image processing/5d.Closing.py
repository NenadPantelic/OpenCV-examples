import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('binary_noise.jpg')
img =  cv2.imread('closing.png')
kernel = np.ones((5,5),np.uint8)
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)



plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Closed')
plt.xticks([]), plt.yticks([])
plt.show()
