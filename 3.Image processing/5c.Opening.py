import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('binary_noise.jpg')
img = cv2.imread('opening.png')

kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)



plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('Opened')
plt.xticks([]), plt.yticks([])
plt.show()
