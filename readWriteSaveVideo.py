import cv2
# cap = cv2.VideoCapture("sample.mp4") 

# while True:
#     ret, frame = cap.read()
#     # print("width==>", cv2.CAP_PROP_FRAME_WIDTH)
#     # print("height==>", cv2.CAP_PROP_FRAME_HEIGHT)

#     frame = cv2.resize(frame,(700,450))
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('ColorFrame', frame)
#     cv2.imshow('grayFrame', gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# #release
# cap.release()
# cv2.destroyAllWindows()

#carture from web ipcamera

camera = "http://192.168.0.104:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)

#it is 4 byte code which is use to specify the video codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
# #It contain 4 parameter , name, codec,fps,resolution
# output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700,450))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
