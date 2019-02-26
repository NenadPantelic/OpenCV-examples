import cv2
import numpy as np


lista = [[[185, 128, 41] for i in range(512)] for j in range(512)]
img = np.asarray(lista,dtype=np.uint8)
pts = np.array([[200,300],[300,300],[250,86]])
#pts = pts.reshape((-1,2,2))
#pts = pts.reshape((-1,3,2))

#cv2.polylines(img,[pts],True,(255,255,255))
#cv2.fillPoly(img,pts,(185,128,41))
#zeleni
cv2.ellipse(img,(150,300),(65,65),0,-60,-360,(0,255,0),-1)
cv2.circle(img,(150,300),25,(185,128,41),-1)

#plavi
cv2.ellipse(img,(300,300),(65,65),0,240,-60,(255,0,0),-1)
cv2.circle(img,(300,300),25,(185,128,41),-1)

#crveni
cv2.ellipse(img,(225,170),(65,65),0,60,-240,(0,0,255),-1)
cv2.circle(img,(225,170),25,(185,128,41),-1)


cv2.imshow("OpenCV logo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
