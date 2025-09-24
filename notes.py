# OpenCV - Open Source Computer Vision Library
# OpenCV is a library of programming functions mainly aimed at real-time computer vision.    
'''
# Phase 0 - Getting Ready for OpenCV

# Issues before inventing OpenCV
1. Coding Difficulty
2. Performance Issues
3. Lack of Standardization


# OpenCV Features 
1. Easy to use functions
2. Lighting Fast Performance
3. Open Source Standard

# OpenCV invented by Gary Bradski at Intel Research Labs
# Released in Open Source in 2000

# in 2005 - used in research labs
# in 2010 - used in phones, factories
# in 2015 - added support in AI and DL
# in 2020+ - used in self-driving cars, face recognition, AR filters, drones

# more than 4000 functions

# Vision - Images, Videos, objects, faces, motion, documents, barcodes

# Phase 1 - Getting Started with OpenCV

Reading, Displaying and Saving Images.
Image Dimensions, Color Channels and Grayscale Conversion

Image :  A 2D array of pixels
Pixel :  Matrix of numbers representing color intensity. It is smallest   unit of an Image.

Image Resolution :  Number of pixels in an image (Width x Height)
Grayscale :  Single channel image (Black and White)

BGR :  OpenCV uses BGR format instead of RGB
Image File Formats :  JPEG, PNG, BMP, TIFF

JPG/JPEG - for small loose images
PNG - for high quality images
BMP - for Windows bitmaps
TIFF - for super high quality images


Width : Total no. of pixels horizontally
Height : Total no. of pixels vertically

Color Channel : It is a single layer of color information in an image.

Each pixel in a color image is represented by three values corresponding to the intensity of Red, Green, and Blue channels. so no of channel is 3

In a grayscale image, each pixel is represented by a single value indicating the intensity of light (brightness) at that pixel. so no of channel is 1

as cv2 is B G R so, 
255,0,0 -- pure blue
0,255,0 -- pure green
0,0,255 -- pure red
0,0,0  -- pure black
255,255,255 -- pure white 
128,128,128 -- pure gray


# read image
image = cv2.imread('image.jpg', flag)

# flag = 1 : for color image (default)
# flag = 0 : for grayscale image
# flag = -1 : for unchanged image (including alpha channel)

#displaying image
cv2.imshow("Window Title", image)  #open the window
    cv2.waitKey(0)   # wait for a key
    cv2.destroyAllWindows()  # close the window

0 - waits indefinitely until a key is pressed to close all windows

# Saving an image
cv2.imwrite("output.jpg", image)

# image dimensions
using shape attribute it tells height, width, color channel


# image greyscale conversion using cvtColor

-- processing time of greyscale images is less
-- complexity is also low
-- cv2.COLOR_BGR2GRAY converts color to gray

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Phase 2 - Image Transformations and Manipulation Techniques

1. Resizing & Scaling
2. Cropping
3. Rotation & Flipping
4. Adding Text
5. Drawing Shapes


1. Resizing & Scaling

cv2.resize()

resized = cv2.resize(src, dsize, fx, fy, interpolation)

# dsize - desired size (width, height)
# fx - scaling factor along x-axis
# fy - scaling factor along y-axis
# interpolation - interpolation method (default is cv2.INTER_LINEAR)

2. Cropping

cropped_image = image[startY:endY, startX:endX]

startY - starting y-coordinate (top)
endY - ending y-coordinate (bottom)
startX - starting x-coordinate (left)
endX - ending x-coordinate (right)

3. Image Rotation and Flipping

M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (width, height))

# center - center of rotation (x, y)

# angle - rotation angle in degrees (positive values mean counter-clockwise rotation)
+90 - rotates 90 degrees counter-clockwise
-90 - rotates 90 degrees clockwise

# scale - scaling factor (1.0 means no scaling)
0.5 - reduces size by half
2.0 - doubles the size

# width, height - dimensions of the output image

flipped_image = cv2.flip(image, flipCode)
# flipCode = 0 : flip vertically top to bottom
# flipCode > 0 : flip horizontally left to right
# flipCode < 0 : flip both vertically and horizontally 

/ division  - integer division
// floor division - float division means it gives decimal values

# center of a image : (width/2, height/2) or (image.shape[1]//2, image.shape[0]//2)

# Basic Image Drawing Techniques

Drawing Lines
Drawing Rectangeles
Drawing Circles
Adding Text

cv2.line(image, start_point, end_point, color, thickness)
cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.circle(image, center, radius, color, thickness)
cv2.putText(image, text, org, font, fontScale, color, thickness)

# start_point - starting point of the line (x1, y1)
# end_point - ending point of the line (x2, y2)
# top_left - top-left corner of the rectangle (x1, y1)
# bottom_right - bottom-right corner of the rectangle (x2, y2)
# center - center of the circle (x, y)
# radius - radius of the circle in pixels
# text - text string to be drawn
# org - bottom-left corner of the text string in the image (x, y)
# font - font type (e.g., cv2.FONT_HERSHEY_SIMPLEX)
# fontScale - font scale factor that is multiplied by the font-specific base size
# color - color of the shape or text (B, G, R)
# thickness - thickness of the shape or text (in pixels). If negative(-1), the shape is filled


# Phase 4: Working with Video & Webcam

1. Capturing video from webcam (cv2.VideoCapture)
2. Frame-by-frame processing, Real-time filters
3. Saving video (cv2.VideoWriter)

What is a Video ?
    A sequence of images (frames) displayed in quick succession to create the illusion of motion.

What is a Webcam ?
    A device that captures video in real-time, often used for video conferencing, streaming, and recording.

Frame-by-frame processing ?
    Analyzing and manipulating each individual frame of a video stream.

A normal video contains 30-60 frames per second (fps)

Frame - a single image in a sequence of images that make up a video

Frame Rate (fps) - number of frames displayed per second in a video

more fps means smoother video

# Capturing video from webcam

cap = cv2.VideoCapture(source)  # 0 is the default camera index of your webcam
# for external camera use 1,2,3...


    Hex digits: 0–9, A–F where A=10, …, F=15.

    0x71 = (7 × 16^1) + (1 × 16^0) = 7×16 + 1×1 = 112 + 1 = 113.

# Frame-by-frame video processing

a) draw shapes
b) detect objects
c) analyze motion, size, color
d) label frames with text, time,date
e) assign specific time 

# save webcam video to a file using openCV
cv2.VideoWriter(output_file, fourcc, fps, frame_size)

# fourcc is a 4-character code used to specify the video codec(compression format).
# Common codecs include:
# 'XVID' - widely supported codec for AVI files(audio video interleave)
# 'MJPG' - Motion JPEG codec
# 'X264' - H.264 codec for MP4 files(MPEG-4 Part 14)
# 'DIVX' - DivX codec   

# fps - frames per second (e.g., 20.0, 30.0)
# frame_size - size of the video frames (width, height)

# when we need to stop the video recording, we use release() method

things to do

1. read video from a file
2. find width, height, fps
3. start recording and save to a file
4. show the videos that it is getting saved
5. stop recording when 'q' is pressed


# Phase 5: Image Filtering & Blurring

1. Gaussian blur 
2. Median blur
3. Sharpening filters
4. Smoothing noisy images
5. Enhancing image clarity

# blurring - reduces sharpness and detail in an image

#1.  Gaussian Blur -  A technique that uses a Gaussian function to smooth an image by averaging pixel values with their neighbors, reducing noise and detail.

# noise - random variations in pixel values that can degrade image quality

# we use filters to reduce noise

# smoothing - increases resolution and reduces harshness from the image

# kernel - a small matrix used for image processing operations like blurring, sharpening, and edge detection.

blurred_image = cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y), sigma)

# kernel_size - size of the Gaussian window kernel (must be odd and positive, e.g., 3, 5, 7)

# kernel size :
(1,1)- no blur
(3,3)- mild blur
(5,5)- moderate blur
(7,7)- strong blur
(9,9)- very strong blur
(21,21)- extreme blur

# blending - combining two images using weighted averages to create a smooth transition between them.
                
# sigma - controls the amount of blurring; higher values result in more blur
sigma = 0 means it is calculated based on kernel size


# 2. Median Blur - A technique that replaces each pixel's value with the median value of its neighboring pixels, effectively reducing noise while preserving edges in the image.

median_blurred = cv2.medianBlur(image, kernel_size)

# kernel_size - size of the square kernel (must be odd and positive, e.g., 3, 5, 7)

median value means the middle value in a sorted list of numbers

difference between gaussian and median blur
- Gaussian Blur uses a weighted average of pixel values, while Median Blur uses the median value of neighboring pixels.
- Gaussian Blur is better for reducing Gaussian noise, while Median Blur is more effective for removing salt-and-pepper noise.

# Sharpening Filters - Techniques that enhance the edges and fine details in an image by emphasizing high-frequency components, making the image appear clearer and more defined.

cv2.filter2D(source, ddepth, kernel)

# ddepth - desired depth of the output image (use -1 to match the source image depth)

ddepth : 1 = 8-bit unsigned integers
         2 = 8-bit signed integers
         3 = 16-bit unsigned integers
         4 = 16-bit signed integers
         5 = 32-bit signed integers
         -1 = same as source image

# kernel - a matrix that defines the filter to be applied for sharpening

(3,3) - sharpening kernel
sharpening_kernel = np.array([
                              [-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]
                              ])


0 -1 0
-1 5 -1
0 -1 0        

# this will sharp the center pixel more than the surrounding pixels and its neighbors will be subtracted from it

# Phase 6: Edge Detection & Thresholding

Canny edge detection
Binary & adaptive thresholding
Bitwise operations (AND, OR, NOT)
Extracting outlines from images

# Canny Edge Detection - A multi-stage algorithm that detects edges in an image by identifying areas of rapid intensity change, using techniques like gradient calculation, non-maximum suppression, and hysteresis thresholding.

# extract key features from an image like outlines

# Thresholding - A technique that converts a grayscale image into a binary image by setting pixel values above a certain threshold to one value (e.g., white) and those below the threshold to another value (e.g., black), effectively segmenting the image.

# Bitwise Operations - Operations that manipulate individual bits of binary images, allowing for logical operations like AND, OR, and NOT to combine or modify images based on pixel values.


AND - Combines two binary images by performing a logical AND operation on corresponding pixels, resulting in a pixel being white (1) only if both input pixels are white (1).

OR - Combines two binary images by performing a logical OR operation on corresponding pixels, resulting in a pixel being white (1) if at least one of the input pixels is white (1).

NOT - Inverts a binary image by flipping the pixel values, turning white pixels (1) to black (0) and black pixels (0) to white (1).

# canny edge detection

-> to detect borders
-> seperate objects
-> feature extraction in face recognition

# Stages of Canny Edge Detection
1. Noise Reduction - Apply Gaussian blur to reduce noise and improve edge detection accuracy.
2. Gradient Calculation - Compute the intensity gradients of the image using Sobel operators to identify edge
3. Non-Maximum Suppression - Thin out the edges by suppressing non-maximum gradient values, retaining only the local maxima.
4. Double Thresholding - Apply two thresholds (high and low) to classify pixels as strong, weak, or non-edges.
5. Edge Tracking by Hysteresis - Finalize edges by connecting weak edges to strong edges if they are adjacent, discarding isolated weak edges.


edges = cv2.Canny(image, threshold1, threshold2)

#threshold1 - lower threshold for edge detection
#threshold2 - upper threshold for edge detection

# threshold syntax :
# binary thresholding
_, binary_image = cv2.threshold(image, thresh, maxval, type)

# thresh - threshold value (0-255)
# maxval - maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types
# type - thresholding type (e.g., cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV)

# Thresh_binary - pixel value is set to maxval if it is greater than thresh, otherwise it is set to 0

# Best value for thresh is 127 (midpoint of 0-255)


# Bitwise Operations
bitwise_and = cv2.bitwise_and(image1, image2) -> to cut out a shape from another image
bitwise_or = cv2.bitwise_or(image1, image2) -> to combine 2 images
bitwise_not = cv2.bitwise_not(image) -> to invert an image from black to white and white to black

# Phase 7: Contours & Shape Detection

Finding contours - cv2.findContours to locate object boundaries 
Drawing contours on images  - highlight detected objects by drawing around thier edges
Shape detection using approxPolyDP - approximate shapes using approxPolyDP for object recognition
Object recognition basics 

# finding and drawing contours 

# contours - curves joining all the continuous points along a boundary with same color or intensity

contours , hierarchy = cv2.findContours(binary_image, mode, method)

# mode - contour retrieval mode (e.g., cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_TREE)
-> it will tell how the contours are stored and organized

# method - contour approximation method (e.g., cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_NONE)

# it will tell how the contour points needs to be stored

contours = returns a list of contour points
hierarchy = contains information about the image topology


# draw contours
# -1 means draw all contours
contour_image = cv2.drawContours(image.copy(), contours, -1, (0,255,0), 2)

syntax of drawContours
cv2.drawContours(image, contours, contourIdx, color, thickness)
# contourIdx - index of the contour to draw (use -1 to draw all contours)
0 means first contour
-1 means second contour
1 means third contour and so on
# color - color of the contour (B, G, R)
# thickness - thickness of the contour line (in pixels). If negative(-1), the contour is filled

# Shape detection using approxPolyDP
-> by counting their vertices


approx = cv2.approxPolyDP(contour, epsilon, closed)

# contour - shape outline
# epsilon - maximum distance between the original contour and its approximation (a small percentage of the contour's perimeter, e.g., 0.02 * cv2.arcLength(contour, True))

smaller the epsilon value, closer the approximation to the original contour

# closed - boolean indicating whether the shape is closed (True) or open (False)


Phase 8: Face & Object Detection

# Haar Cascades for face detection: pre-trained classifiers to detect faces in images and videos
# Haar Cascade is a trained model that uses machine learning to detect objects in images based on features like edges, lines, and textures.

Face detection using Haar Cascades : 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Eye detection using Haar Cascades :
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

Smile detection using Haar Cascades :
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

Drawing boxes on detected faces and eyes
faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)


# scaleFactor - parameter specifying how much the image size is reduced at each image scale (e.g., 1.1 means reducing size by 10%)

# minNeighbors - parameter specifying how many neighbors each candidate rectangle should have to retain it (higher values result in fewer detections but with higher quality)
















'''