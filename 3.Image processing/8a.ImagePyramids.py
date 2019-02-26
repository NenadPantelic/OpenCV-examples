import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
lower_reso = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso)
lower_reso3 = cv2.pyrDown(lower_reso2)


plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(lower_reso,cmap = 'gray')
plt.title('Lower resolution'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(lower_reso2,cmap = 'gray')
plt.title('Lower resolution2'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(lower_reso3,cmap = 'gray')
plt.title('Lower resolution3'), plt.xticks([]), plt.yticks([])
plt.show()


higher_reso = cv2.pyrUp(lower_reso)

plt.subplot(131),plt.imshow(lower_reso,cmap = 'gray')
plt.title('Lower resolution image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(higher_reso,cmap = 'gray')
plt.title('Higher resolution image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img,cmap = 'gray')
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.show()
