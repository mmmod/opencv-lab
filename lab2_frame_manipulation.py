import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    #
    # frame is a matrix that can be manipulated freely. Ideas:
    # * NumPy - https://het.as.utexas.edu/HET/Software/Numpy/reference/routines.array-manipulation.html
    #   * rearranging elements
    #   * scaling, tiling
    # * OpenCV - image processing https://docs.opencv.org/master/d7/dbd/group__imgproc.html
    #   * medianBlur(frame, 13)
    #   * cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything if job is finished
capture.release()
cv2.destroyAllWindows()
