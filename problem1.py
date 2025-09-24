# load image asking user the location in the input
# ask user whether show or save
# ask  file output name in form of input from user and then display log for saving the file 


import cv2, os

location_input = str(input("Please enter the image location:"))

image = cv2.imread(location_input)

if image is not None:
    print("Image is loaded")
    show_or_save_input = input("Show or Save ? ")
    if show_or_save_input == "show":
        cv2.imshow("Window Title", image)  
        cv2.waitKey(0)   
        cv2.destroyAllWindows()
        print("Image showed successfully")
    elif show_or_save_input == "save":

        saving_name = input("Enter the Saving name of th Image: ")

        out_dir = "Demo Images"
        os.makedirs(out_dir, exist_ok=True)

        out_path = os.path.join(out_dir, f"{saving_name}.jpg")
        ok = cv2.imwrite(out_path, image)
        print("Saved Successfully at ", out_path)
    else:
        print("Invalid Prompt")
else:
    print("Image is not loaded")


