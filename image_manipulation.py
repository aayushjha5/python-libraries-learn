import cv2

# loading an image
# image = cv2.imread("Demo Images/image1.jpg")
'''
if image is None:
    print("Error: Image not found")
else:
    print("Image loaded Successfully")
'''

#displaying an image
'''
if image is not None:
    cv2.imshow("Window Title", image)  
    cv2.waitKey(0)   
    cv2.destroyAllWindows()  
else:
    print("Error: Image can not be loaded")
'''
    
# saving an image
'''
if image is not None:
    success = cv2.imwrite("Demo Images/output1.jpg", image)
    if success:
        print("Image saved successfully as output1.jpg")
    else:
        print("Failed to save the image")
else:
    print("Image not found")

'''

# image dimensions
'''
if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else: 
    print("Could not load image")
'''

'''
Image Loaded:
Height: 700
Width: 1050
Channels: 3
'''

# grey conversion

'''

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("Demo Images/greyscaled1.jpg", gray)

else:
    print("Image not loaded")

'''

# image resizing and scaling

# resized = cv2.resize(image, dsize, fx, fy, interpolation)
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")

    resized_image = cv2.resize(image,(300,300))    # width, height : 300,300

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized_image)

    cv2.imwrite("Demo images/resized_output.jpg", resized_image)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
    
# cropping using slicing
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")

    cropped_image = image[100:200, 50:150]

    cv2.imshow("Original Image",image)
    cv2.imshow("Cropped Image",cropped_image)

    cv2.imwrite("Demo images/cropped_output.jpg", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

# image rotation 
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    (h,w) = image.shape[:2]    # (700, 1050)

    # create rotational matrix for counter-clockwise 90'
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)

    rotated_image = cv2.warpAffine(image, M, (w,h))

    cv2.imshow("Original Image",image)
    cv2.imshow("Rotated Image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''

# image flipping
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")

    flipped_H = cv2.flip(image, 1)
    flipped_V = cv2.flip(image, 0)
    flipped_B = cv2.flip(image, -1)

    cv2.imshow("Original Image",image)
    cv2.imshow("flipped_H Image",flipped_H)
    cv2.imshow("flipped_V Image",flipped_V)
    cv2.imshow("flipped_B Image",flipped_B)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''

# draw a line on image

'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    line_on_image = cv2.line(image, (50,100), (300,100), (255,0,0), 4)

    cv2.imshow("Line on Image",line_on_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
# draw a rectangle on image
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    rectangle_on_image = cv2.rectangle(image, (50,50), (250,200), (0,0,255), 4)

    cv2.imshow("Rectangle on Image",rectangle_on_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

# draw a circle
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    circle_on_image = cv2.circle(image, (250,150), 50, (255,255,0), 2)

    cv2.imshow("Circle on Image",circle_on_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''

# add label/text on image
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    text_on_image = cv2.putText(image, 'MacBook M1 Air ', (580,650), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)

    cv2.imshow("Text on Image",text_on_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

# Gaussian Blur

image = cv2.imread("Demo Images/tree.jpg")
'''
if image is None:
    print("Image not found")
else:
    print("Image loaded")
    blurred = cv2.GaussianBlur(image, (3,3), 3)
    blurred_1 = cv2.GaussianBlur(image, (21,21), 3)

    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image 0", blurred)
    cv2.imshow("Blurred Image 1", blurred_1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''

# median blur

'''
if image is None:
    print("Image not found")
else:   
    print("Image loaded")

    median_blurred = cv2.medianBlur(image, 21)

    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blurred Image", median_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

# image sharpening
import numpy as np
'''

image = cv2.imread("Demo Images/low_res.png")

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])



if image is None:
    print("Image not found")
else:
    print("Image loaded")

    sharpened_image = cv2.filter2D(image, -1 , sharpen_kernel)

    cv2.imshow("Original Image" , image)
    cv2.imshow("Sharpened Image" , sharpened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''


# canny edge detection

'''
#importing the image in black and white format
image = cv2.imread("Demo Images/flower.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50,150)

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    cv2.imshow("Original Image" , image)
    cv2.imshow("Edges" , edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
# thresholding
'''
image = cv2.imread("Demo Images/man.png", cv2.IMREAD_GRAYSCALE)

ret , thresh_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    cv2.imshow("Original Image" , image)
    cv2.imshow("Thresholded image" , thresh_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
# bitwise operations
'''
# size of image1 and image2 should be same
# we have to use only greyscale images or binary mask for bitwise operations
# apple portrait mode use bitwise not operation

image1 = np.zeros((300,300), dtype="uint8")
image2 = np.zeros((300,300), dtype="uint8")

cv2.circle(image1, (150,150), 100, 255, -1)
cv2.rectangle(image2, (100,100), (250,250), 255, -1)

bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_not = cv2.bitwise_not(image1)
bitwise_xor = cv2.bitwise_xor(image1, image2)


cv2.imshow("Circle", image1)
cv2.imshow("Rectangle", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)
cv2.imshow("Bitwise XOR", bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

#contour detection

'''

image = cv2.imread("Demo Images/shape.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# _ is placeholder for ret value which is not used right now

# find contours

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours
# -1 means draw all contours
contour_image = cv2.drawContours(gray, contours, -1, (0,255,0), 3)

cv2.imshow("Contour Image", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

'''
# detect shapes using apprxPolyDP() function

image = cv2.imread("Demo Images/shape.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# _ is placeholder for ret value which is not used right now

# find contours

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours
# -1 means draw all contours
contour_image = cv2.drawContours(gray, contours, -1, (0,255,0), 3)

for contour in contours:

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    # draw contour

    cv2.drawContours(image, [approx], 0, (0,0,255), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)

cv2.imshow("Contour Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''




