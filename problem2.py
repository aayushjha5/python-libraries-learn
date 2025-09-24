# take file location in input
# after that ask user whether to draw a line, circle, rectangle or draw a text
# line - takes value from user (x1y1 and x2y2)
# generate output and ask user to save or not ?
# similarly for rest options
# 



import cv2, webcolors, os

location_input = str(input("Please enter the image location: "))

image = cv2.imread(location_input)

if image is None:
    print("Image is not loaded")
else:
    print("Image is loaded")
    choice = int(input("Choose option to draw: \nLine : 1\nRectangle: 2\nCircle: 3\nText: 4\n"))

    if choice == 1:

        x1 = int(input("Enter x-coordinate of point where line should start: "))
        y1 = int(input("Enter y-coordinate of point where line should start: "))
        x2 = int(input("Enter x-coordinate of point where line should end: "))
        y2 = int(input("Enter y-coordinate of point where line should end: "))

        color_input = input("Enter Color of the line: ").strip().lower()
        rgb = webcolors.name_to_rgb(color_input)
        color_entry = (rgb.blue, rgb.green, rgb.red)

        thickness = int(input("Enter thickness of the line(ex: 2): "))

        line_image = cv2.line(image,(x1,y1),(x2,y2),color_entry,thickness)

        cv2.imshow("Line on Image",line_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        save_or_not = input("Save or not ? ")
        if save_or_not == "yes":
            saving_name = input("Enter the Saving name of Output: ")

            out_dir = "Demo images"
            os.makedirs(out_dir, exist_ok=True)

            out_path = os.path.join(out_dir, f"{saving_name}.jpg")
            ok = cv2.imwrite(out_path, line_image)
            print("Saved Successfully at ", out_path)
        else:
            print("Program is finished")

    elif choice == 2:

        x1 = int(input("Enter x-coordinate of top left point of rectangle: "))
        y1 = int(input("Enter y-coordinate of top left point of rectangle: "))
        x2 = int(input("Enter x-coordinate of bottom right point of rectangle: "))
        y2 = int(input("Enter y-coordinate of top bottom right of rectangle: "))

        color_input = input("Enter Color of the Rectangle: ").strip().lower()
        rgb = webcolors.name_to_rgb(color_input)
        color_entry = (rgb.blue, rgb.green, rgb.red)

        thickness = int(input("Enter thickness of the Rectangle(ex: 2): "))

        rectangle_image = cv2.rectangle(image,(x1,y1),(x2,y2),color_entry,thickness)

        cv2.imshow("Rectangle on Image",rectangle_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        save_or_not = input("Save or not ? ")
        if save_or_not == "yes":
            saving_name = input("Enter the Saving name of Output: ")

            out_dir = "Demo images"
            os.makedirs(out_dir, exist_ok=True)

            out_path = os.path.join(out_dir, f"{saving_name}.jpg")
            ok = cv2.imwrite(out_path, rectangle_image)
            print("Saved Successfully at ", out_path)
        else:
            print("Program is finished")

    elif choice == 3:
        x = int(input("Enter x-coordinate of center of circle: "))
        y = int(input("Enter y-coordinate of center of circle: "))
        r = int(input("Enter Radius of the circle (in Pixels): "))

        color_input = input("Enter Color of the Circle: ").strip().lower()
        rgb = webcolors.name_to_rgb(color_input)
        color_entry = (rgb.blue, rgb.green, rgb.red)

        thickness = int(input("Enter thickness of the Circle (ex: 2): "))

        circle_image = cv2.circle(image,(x,y),r, color_entry,thickness)

        cv2.imshow("Circle on Image",circle_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        save_or_not = input("Save or not ? ")
        if save_or_not == "yes":
            saving_name = input("Enter the Saving name of Output: ")

            out_dir = "Demo images"
            os.makedirs(out_dir, exist_ok=True)

            out_path = os.path.join(out_dir, f"{saving_name}.jpg")
            ok = cv2.imwrite(out_path, circle_image)
            print("Saved Successfully at ", out_path)
        else:
            print("Program is finished")

    elif choice == 4:

        x = int(input("Enter x-coordinate of Starting point of Text: "))
        y = int(input("Enter y-coordinate of Starting point of Text: "))
        input_text = str(input("Enter text to be inserted: "))


        color_input = input("Enter Color of the Text: ").strip().lower()
        rgb = webcolors.name_to_rgb(color_input)
        color_entry = (rgb.blue, rgb.green, rgb.red)

        thickness = int(input("Enter thickness of the Text(ex: 2): "))

        text_image = cv2.putText(image,input_text,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.2, color_entry, thickness)

        cv2.imshow("Text on Image",text_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        save_or_not = input("Save or not ? ")
        if save_or_not == "yes":
            saving_name = input("Enter the Saving name of Output: ")

            out_dir = "Demo images"
            os.makedirs(out_dir, exist_ok=True)

            out_path = os.path.join(out_dir, f"{saving_name}.jpg")
            ok = cv2.imwrite(out_path, text_image)
            print("Saved Successfully at ", out_path)
        else:
            print("Program is finished")

    else:
        print("Please enter a valid number")



'''

refactored result

import os, cv2, webcolors

def ask_str(msg): return input(msg).strip()
def ask_int(msg): return int(ask_str(msg))                     
def parse_color(name):
    rgb = webcolors.name_to_rgb(name.lower())                  
    return (rgb.blue, rgb.green, rgb.red)                      

def maybe_save(img, win="Output"):
    cv2.imshow(win, img); cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
    if ask_str("Save or not ? ").lower() == "yes":
        out_dir = "Demo images"; os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{ask_str('Enter the Saving name of Output: ')}.jpg")
        cv2.imwrite(out_path, img); print("Saved Successfully at", out_path)

path = ask_str("Please enter the image location: ")
image = cv2.imread(path)
if image is None:
    print("Image is not loaded")
else:
    print("Image is loaded")
    choice = ask_int("Choose option to draw: \nLine : 1\nRectangle: 2\nCircle: 3\nText: 4\n")

    if choice == 1:
        x1, y1 = ask_int("x1: "), ask_int("y1: ")
        x2, y2 = ask_int("x2: "), ask_int("y2: ")
        color = parse_color(ask_str("Enter Color of the line: "))
        th = ask_int("Enter thickness of the line(ex: 2): ")
        out = cv2.line(image.copy(), (x1,y1), (x2,y2), color, th)     
        maybe_save(out, "Line on Image")

    elif choice == 2:
        x1, y1 = ask_int("x1 (top-left): "), ask_int("y1 (top-left): ")
        x2, y2 = ask_int("x2 (bottom-right): "), ask_int("y2 (bottom-right): ")
        color = parse_color(ask_str("Enter Color of the Rectangle: "))
        th = ask_int("Enter thickness of the Rectangle(ex: 2): ")
        out = cv2.rectangle(image.copy(), (x1,y1), (x2,y2), color, th) 
        maybe_save(out, "Rectangle on Image")

    elif choice == 3:
        x, y, r = ask_int("center x: "), ask_int("center y: "), ask_int("radius: ")
        color = parse_color(ask_str("Enter Color of the Circle: "))
        th = ask_int("Enter thickness of the Circle (ex: 2): ")
        out = cv2.circle(image.copy(), (x,y), r, color, th)            
        maybe_save(out, "Circle on Image")

    elif choice == 4:
        x, y = ask_int("start x: "), ask_int("start y: ")
        txt = ask_str("Enter text to be inserted: ")
        color = parse_color(ask_str("Enter Color of the Text: "))
        th = ask_int("Enter thickness of the Text(ex: 2): ")
        out = cv2.putText(image.copy(), txt, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, th)  
        maybe_save(out, "Text on Image")

    else:
        print("Please enter a valid number")


'''