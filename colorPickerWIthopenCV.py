import cv2
import numpy as np

def cross(x):
    pass
#create a black imgae
img = np.zeros((300,512,3),np.uint8) #empty image
cv2.namedWindow("Color Picker")

#Creating switch for on and of the trackbars
switch = '0:OFF&1:ON '
cv2.createTrackbar(switch, 'Color Picker',0,1,cross)

#creating trackbar for adjusting colors
cv2.createTrackbar("R", 'Color Picker',0,255,cross)
cv2.createTrackbar("G", 'Color Picker',0,255,cross)
cv2.createTrackbar("B", 'Color Picker',0,255,cross)

while True:
    cv2.imshow("Color Picker", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    s=cv2.getTrackbarPos(switch, 'Color Picker')
    r=cv2.getTrackbarPos("R", 'Color Picker')
    g=cv2.getTrackbarPos("G", 'Color Picker')
    b=cv2.getTrackbarPos("B", 'Color Picker')

    if s==0:
        img[:]=0
    else:
        img[:] = (b,g,r)

cv2.destroyAllWindows()