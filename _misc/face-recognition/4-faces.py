# OpenCV (4)

# Imports
import numpy as np 
import cv2
import pickle

# Front of face classifier (functions on grayscale)
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

# Declare recognizer (model) and read trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Read labels for classification
labels = {}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()} # Reversing initial name:id dictionary to be able to print name instead of id

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

    # Convert frame to grayscale and initialize model
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    
    # Iterate through face position and save image
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w] # Region of interest (y-start:y-end, x-start:x-end )
        
        # Predict label id (classification) and confidence level
        id_, conf = recognizer.predict(roi_gray)

        # Write name of predicted face above rectangle
        if conf >=45:
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontsize = 1
            name = labels[id_]
            print(name + '\n' + str(id_))
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, fontsize, color, stroke, cv2.LINE_AA)

        # Save image
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        # Draw a rectangle over the region of interest
        color = (255, 0, 0) # BGR not RGB
        stroke = 2
        end_coord_x = x + w
        end_coord_y = y + h 
        cv2.rectangle(frame, (x,y), (end_coord_x, end_coord_y), color, stroke)

    # Main feed window
    cv2.imshow('Video Feed', frame)

    # To prevent video feed hanging (Added functionality where hit 'q' to end feed)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

# Closing capture object and recording
cap.release()
cv2.destroyAllWindows()