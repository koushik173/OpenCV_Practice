import cv2
import datetime
camera = "http://192.168.0.104:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)

print("for width", cap.get(3))
print("for height", cap.get(4))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,400))
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height'+str(cap.get(4))+'width'+str(cap.get(3))
        date = "date"+str(datetime.datetime.now())
        frame = cv2.putText(frame, (text),(10,20), font,1,(0,0,255),1,cv2.LINE_AA)
        frame = cv2.putText(frame, (date),(10,40), font,1,(0,0,255),1,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

        
