# import cv2
# import numpy as np

# def draw(event,x,y, flags,param):
#     if event== cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),10,(0,0,255),-1)
#     if event== cv2.EVENT_RBUTTONDBLCLK:
#         cv2.rectangle(img,(x,y),(x+140,y+100),(122,0,133),2)

# cv2.namedWindow(winname="ress")

# #creating a black images 
# img = np.zeros((255,255,3), np.uint8)
# cv2.setMouseCallback("ress", draw)

# while True:
#     cv2.imshow("ress",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()


## create a function which helep to find cordinates of any rpixel and its colors

import cv2
import numpy as np

def mouse_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        textt= '. '+str(x)+', '+str(y)
        font= cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img,textt, (x,y), font,1,(133,145,0),1)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        font= cv2.FONT_HERSHEY_PLAIN
        b= img[y,x,0]
        g= img[y,x,1]
        r= img[y,x,2]
        textt = '. '+str(b)+', '+str(g)+', '+str(r)
        cv2.putText(img,textt, (x,y), font,1,(133,145,0),1)


#creating blank images
# img = np.zeros((500,500,3), np.uint8)
img = cv2.imread("ironman.jpg")
img = cv2.resize(img,(900,600))
cv2.namedWindow("enets")
cv2.setMouseCallback("enets", mouse_event)

while True:
    cv2.imshow("enets",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()