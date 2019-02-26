import numpy as np
import cv2

img = cv2.imread('bolt.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
M = cv2.moments(cnt)
print M
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)
area = cv2.contourArea(cnt)
print(area)
perimeter = cv2.arcLength(cnt,True)
print(perimeter)
epsilon = 0.5*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print(approx)
hull = cv2.convexHull(cnt)
k = cv2.isContourConvex(cnt)
print(k)
x,y,w,h = cv2.boundingRect(cnt)

cv2.drawContours(img,hull,0,(255,0,0),3)
cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
cv2.drawContours(img,approx,-1,(255,0,0),3)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,2550),2)
'''
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
'''
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(0,255,0),2)
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,255),2)
'''
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(255,255,0),2)
'''
cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
img = cv2.imread('hand.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
hull = cv2.convexHull(cnt)
cv2.drawContours(img,hull,0,(255,0,0),3)
cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
