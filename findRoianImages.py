#In this Video, we talk about ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.

import cv2
import numpy as np


def mouse_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        textt= '. '+str(x)+', '+str(y)
        font= cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img,textt, (x,y), font,1,(133,145,0),1)

#read image
img = cv2.imread("ironman.jpg")
img = cv2.resize(img,(900,600))
# cv2.namedWindow("enets")
# cv2.setMouseCallback("enets", mouse_event)

#now pass like [y1:y2,x1:x2]
#y1=9, y2=162, x1=533, x2=689
roi = img[0:180,545:670]
# roi = img[0:180,420:545]
# roi = img[0:180,295:420]


#putting roi into any pixel values
img[0:180, 671:796] = roi
img[0:180,420:545] = roi
img[0:180,295:420] = roi


cv2.imshow("enets",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# while True:
#     cv2.imshow("enets",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()