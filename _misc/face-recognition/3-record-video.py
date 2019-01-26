# OpenCV (3)

# Imports
import numpy as np 
import cv2
import os

# Set output file
filename = 'openCV_test.mp4'

# Video encoding
VIDEO_TYPE = {
    "avi": cv2.VideoWriter_fourcc(*'XVID'),
    "mp4": cv2.VideoWriter_fourcc(*'H264')
    # "mp4": cv2.VideoWriter_fourcc(*'XVID')
}

# Parse extension from filename to set video encoding
def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE["avi"]


# Set standard video dimensions
STD_DIMENSIONS = {
    '480p': (640, 480),
    '720p': (1280, 720),
    '1080p': (1920, 1080)
}

# Standard movie features
fps = 24.0
my_res = '480p'

# Resolution adjuster
def change_res(cap, width, height):
    cap.set(3,width) # width
    cap.set(4,height) # height

# Video dimension getter and setter method
def get_dims(cap, res):
    width, height = STD_DIMENSIONS['480p'] # Set default
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height
        

# Create capture device object (default webcam)
cap = cv2.VideoCapture(0)

# Set up video recording
dims = get_dims(cap, my_res)
video_type_cv2 = get_video_type(filename)
out = cv2.VideoWriter(filename, video_type_cv2, fps, dims)

# Loop for continuous usage of video capture device
# Read frames from capture and display them
while True:
    ret, frame = cap.read() 

    # Main feed window
    cv2.imshow('Video Feed', frame)

    # Video recording window
    out.write(frame)

    # To prevent video feed hanging (Added functionality where hit 'q' to end feed)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

# Closing capture object and recording
cap.release()
out.release()
cv2.destroyAllWindows()