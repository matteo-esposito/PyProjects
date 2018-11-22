# Artificial Intelligence Concordia Hackathon, November 2018
# Arthur Intelligence - Computer Vision Challenge (2/2)
# Team 1: PyTry
# Matteo Esposito, Sashank Subba, Sonam Tamang

import numpy as np 
import cv2

# Cascades
FACE_CASCADE = cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_alt2.xml')
FB_CASCADE = cv2.CascadeClassifier('./data/cascades/haarcascade_fullbody.xml')

# Create capture device object (default webcam)
cap = cv2.VideoCapture(0)

# Resolution adjusters
def make_480p():
    cap.set(3,640) # width
    cap.set(4,480) # height

make_480p()

# Loop for continuous usage of video capture device
# Read frames from capture and display them
while True:
    ret, frame = cap.read() 

    # Convert feed to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face and body cascade
    faces = FACE_CASCADE.detectMultiScale(
        gray, 
        scaleFactor = 1.1, 
        minNeighbors = 5
    )
    bodies = FB_CASCADE.detectMultiScale(
        gray, 
        scaleFactor = 1.05, 
        minNeighbors = 3
    )

    # Face detection and counter
    for (x,y,w,h) in faces:
        # Rectangle around the recognised face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1) 
        # Rectangle around the face counter output + face counter output
        cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
        cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_DUPLEX, 0.5,  (0,0,0), 1)

    # Body detection
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1) 

    # Main feed window
    cv2.imshow('Video Feed', frame)

    # To prevent video feed hanging (Added functionality where hit 'q' to end feed)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Closing capture object and recording
cap.release()
cv2.destroyAllWindows()