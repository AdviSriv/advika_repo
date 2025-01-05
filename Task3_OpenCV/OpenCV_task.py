import cv2 as cv
import numpy as np

videoCap = cv.VideoCapture('Ball_Tracking.mp4')

while True:
    ret, frame = videoCap.read()
    if not ret:
        break 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_green = np.array([38, 60, 20])
    upper_green = np.array([100, 255, 255])

    mask = cv.inRange(hsv, lower_green, upper_green)
    contours,_ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area > 200:  
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, "Ball", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv.imshow('frame', frame)
   
    if cv.waitKey(15) & 0xFF == ord('q'):
        break
        
videoCap.release()
cv.destroyAllWindows()
