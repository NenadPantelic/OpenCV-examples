import numpy as np
import cv2

img = cv2.imread('conv.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(img,[cnt],0,(0,255,0),-1)

x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
#solidity = float(area)/hull_area
equi_diameter = np.sqrt(4*area/np.pi)
print(aspect_ratio)
print(extent)
#print(solidity)
print(equi_diameter)
#(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
#print(angle)
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
print(pixelpoints)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)
mean_val = cv2.mean(img,mask = mask)
print(min_val,max_val,mean_val)

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print(leftmost)
print(rightmost)
cv2.circle(img, (leftmost[0], leftmost[1]), 3, (0, 255, 255), -1)
cv2.circle(img, (rightmost[0], rightmost[1]), 3, (0, 255, 255), -1)
cv2.circle(img, (topmost[0], topmost[1]), 3, (0, 255, 255), -1)
cv2.circle(img, (bottommost[0], bottommost[1]), 3, (0, 255, 255), -1)

cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
