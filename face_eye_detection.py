import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        # creating region of interest for face
        roi_gray = gray[y:y+h, x:x+w]    # will cut the face part from the whole image
        roi_color = frame[y:y+h, x:x+w]  # will cut the colored version of face part from the whole image

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, 'Eyes Open', (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv2.putText(frame, 'Smiling', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow('Smart Face Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break   

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows() 