import cv2
cam_ip = '192.168.1.225'
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.225:554/CH001.sdp')
count = 1

while True:
    _, frame = cap.read()
    cv2.imwrite("frame%d.jpg" % count, frame)
    count += 1
    if count == 5:
        break
    #cv2.imshow('Camera', frame)
    
    #k = cv2.waitKey(0) & 0xFF
    #if k == 27: #esc key ends process
       #cap.release()
       #break
cv2.destroyAllWindows()
