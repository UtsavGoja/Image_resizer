import cv2

# formula = scale_percent_widht/height = widht/height of the img -/+  new width/height of the img 
# for eg ; if you have an img of size 600 x 400 and you want to make it 500 x 200 you have to 
# set the value of "scale_percent_widht & scale_percent_height", 100 and 200 respectively 

# you can also change file format (for eg: jpg to png , etc)

source = "Image_resizer/qrcover.png" # your image path
destination = "Image_resizer/resized_qrcover.png" # your resized img path
scale_percent_widht = 55
scale_percent_height = 88

img  = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_width = int(img.shape[1] - scale_percent_widht)
# new_width = int(img.shape[1] + scale_percent_widht)  # if you want to add widht to the current width

new_height = int(img.shape[0] - scale_percent_height)
# new_height = int(img.shape[0] + scale_percent_height)  # if you want to add height to the current height

output = cv2.resize(img, (new_width, new_height))

cv2.imwrite(destination, output)