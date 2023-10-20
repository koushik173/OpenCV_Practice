import cv2
import numpy as np

img = cv2.imread("ironman.jpg")
img = cv2.resize(img,(900,600))

#creating image border
border =cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("border",border)
cv2.waitKey(0)
cv2.destroyAllWindows()