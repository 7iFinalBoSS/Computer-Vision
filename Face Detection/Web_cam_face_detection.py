import cv2

face_detector = cv2.CascadeClassifier("C:\\Users\\Lenovo\\Desktop\\450 in 62\\haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while(True):
    
    ret, frame = video_capture.read()
    
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    detections = face_detector.detectMultiScale(image_gray, scaleFactor = 1.3)
    
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
video_capture.release()
cv2.destroyAllWindows()