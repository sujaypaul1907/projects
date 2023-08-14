#firstly - pip install opencv-python

import cv2

#Configure parameters
img_source = "python_3.png"
new_image_name = "new_python.png"
src = cv2.imread(img_source)

#Percent of original image
scale_percent = int(input("What percent of original image you want to resize? Enter percent : "))


new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#Resizing command
output = cv2.resize(src, (new_width, new_height))

#saving the file
cv2.imwrite(new_image_name, output)