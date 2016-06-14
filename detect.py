 
from sys import argv
import zbar
from PIL import Image
import cv2
import picamera

#camera = picamera.PiCamera()
#camera.capture('image.jpg')
image = cv2.imread('/home/pi/images.png')

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY,dstCn=0)
pil = Image.fromarray(gray)
width, height = pil.size
raw = pil.tobytes()


# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    if symbol.data == "None":
        print "Drone bevindt zich buiten het raster"
    else:
        print symbol.data
