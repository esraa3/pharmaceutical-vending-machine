import cv2
import numpy as np
import PIL
from PIL import Image
import picamera

true=0
false=0

#take photo by camera
camera = picamera.PiCamera()
camera.capture('image.jpg')

#define the list of boundaries
boundaries = [
        ([153, 0, 153], [255, 102, 255]),
        ([51,102,0], [204,255,153]),
        ([0,102,0], [153,255,153])

         ]
# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    kernel = np.ones((5,5),np.float32)/25
    image = cv2.filter2D(image,-1,kernel)
 
# find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image,image, mask = mask)
    arr = np.array(output)
    if arr.any():
         true+=1
    else:
         false+=1
                
    if true<=1:
         print 'true'


