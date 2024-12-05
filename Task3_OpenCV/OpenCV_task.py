import cv2 as cv
import numpy as np

videoCap = cv.VideoCapture('Ball_Tracking.mp4')

while True:
    ret, frame = videoCap.read()
    if not ret:
        break 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    blur = cv.GaussianBlur(gray, (17,17), 0)
    cv.imshow('Frame', blur)

    blank = np.zeros(frame.shape, dtype='uint8')
    cv.imshow('Contours Drawn', blank)

    if cv.waitKey(15) & 0xFF == ord('q'):
        break
        
videoCap.release()
cv.destroyAllWindows()
