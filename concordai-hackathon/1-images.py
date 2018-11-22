# Artificial Intelligence Concordia Hackathon, November 2018
# Arthur Intelligence - Computer Vision Challenge (1/2)
# Team 1: PyTry
# Matteo Esposito, Sashank Subba, Sonam Tamang

import numpy as np 
import cv2

FACE_CASCADE = cv2.CascadeClassifier('./data/cascades/haarcascade_frontalface_alt2.xml')
# Set in webpage ('upload file button')
IMG_PATH = './images/'
IMAGES = []

for i in range(1,9):
    IMAGES.append(str(i) + '.jpg')

for pic in IMAGES:
    # Convert .jpg to a numpy array
    img_reg = cv2.imread('./images/' + pic)
    img_resized = cv2.resize(img_reg, (600, 600), cv2.INTER_AREA) # Reg
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY) # Grayscale

    # Detect faces in the image
    faces = FACE_CASCADE.detectMultiScale(
        img_resized,
        scaleFactor=1.2,
        minNeighbors=5
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img_resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Output picture with identified faces
    cv2.imshow("Picture output", img_resized)

    # End run with 'q' press
    while True:    
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break;
