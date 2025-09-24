# Real time face detection

import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default camera (0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 1.1 - scaleFactor
    # 5 - minNeighbors
    # 1 - least safe checking
    # 5 - safer checking
    # 6 - very safe checking

    for(x,y,w,h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        # x - how far from left
        # y - how far from top
        # w - width of rectangle
        # h - height of rectangle

    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows() 
