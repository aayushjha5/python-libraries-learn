import cv2

# Capturing video from webcam
cap = cv2.VideoCapture(0)

'''

while True:
    # reading one frame from the camera using read function
    ret, frame = cap.read()    #ret is a boolean variable that returns true if the frame is available, frame = image array of captured frame

    if not ret:
        print("Could not read frame ")
        break

    # if returns true show the  image 
    cv2.imshow("Webcam Feed", frame)

    # wait for 'q' key to stop showing the video

    if cv2.waitKey(1) & 0xFF == ord('q'):   #wait for 1 ms, if 'q' is pressed break the loop
        print("Quitting...")
        break

cap.release()   #release the webcam
cv2.destroyAllWindows()  #close all windows

'''

# frame by frame video processing

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # can also write 3 ; the property id for width
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # can also write 4 ; the property id for height
# fps = int(cap.get(cv2.CAP_PROP_FPS))          # can also write 5 ; the property id for fps

codec = cv2.VideoWriter_fourcc(*'H264')  # using XVID codec
recorder = cv2.VideoWriter("Demo videos/my_video.mp4", codec, 60, (frame_width, frame_height))
# print(fps)
while True:
    success, image = cap.read()

    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recording LIVE", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()


'''
ignore the warning 
OpenCV: FFMPEG: tag 0x34363248/'H264' is not supported with codec id 27 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x31637661/'avc1'
'''