import numpy as np
import cv2

capture = cv2.VideoCapture(0)
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)

while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything if job is finished
capture.release()
cv2.destroyAllWindows()
