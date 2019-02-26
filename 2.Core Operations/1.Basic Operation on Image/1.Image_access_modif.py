import cv2,numpy as np

img = cv2.imread('messi5.jpg')


#citanje piksela

pixel = img[100,100]
pixel_red = img[100,100,2]

print(pixel)
print(pixel_red)
#izmena piksela
img[100,100] = [0,0,0]


#numpy access i izmena

pixel = img.item(100,100,2)
print(pixel)
img.itemset((100,100,0),255)
img.itemset((100,100,1),255)
img.itemset((100,100,2),255)



print(pixel)
#print(pixel2)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
