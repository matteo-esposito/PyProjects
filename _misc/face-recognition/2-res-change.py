# OpenCV (2)

# Imports
import numpy as np 
import cv2

# Create capture device object (default webcam)
cap = cv2.VideoCapture(0)

# Resolution adjusters
def make_480p():
    cap.set(3,640) # width
    cap.set(4,480) # height

def make_720p():
    cap.set(3,1280) # width
    cap.set(4,720) # height

def make_1080p():
    cap.set(3,1920) # width
    cap.set(4,1080) # height

def change_res(width, height):
    cap.set(3,width) # width
    cap.set(4,height) # height

# Frame rescaling
def rescale_frame(frame, percent=75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

# Change resolution to 480p to speed up execution
make_480p()

# Loop for continuous usage of video capture device
# Read frames from capture and display them
while True:
    ret, frame = cap.read() 

    # Rescale frame
    frame = rescale_frame(frame, percent=30)

    # Main feed window
    cv2.imshow('Video Feed', frame)    
    
    # Rescale frame
    frame2 = rescale_frame(frame, percent=100)

    # Main feed window
    cv2.imshow('Video Feed 2', frame2)

    # To prevent video feed hanging (Added functionality where hit 'q' to end feed)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

# Closing capture object
cap.release()
cv2.destroyAllWindows()