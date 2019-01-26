# OpenCV (1)

# Imports
import numpy as np 
import cv2

# Capture device (default webcam)
cap = cv2.VideoCapture(0)

# Loop for continuous usage of video capture device
# Read frames from capture and display them
while True:
    ret, frame = cap.read() 

    # Main feed window
    cv2.imshow('Video Feed', frame)

    # Greyscale window
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Greyscale Feed', grey)

    # To prevent video feed hanging (Added functionality where hit 'q' to end feed)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

# Closing capture object
cap.release()
cv2.destroyAllWindows()