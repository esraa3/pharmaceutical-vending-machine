from sys import argv
import zbar
import Image
import cv2

#take image by camera and read it 
#image = cv2.imread('C:\Users\esraa\Desktop\image ook\dow.jpg')
import picamera
camera = picamera.PiCamera()
camera.capture('image.jpg')

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY,dstCn=0)
pil = Image.fromarray(gray)
width, height = pil.size
raw = pil.tostring()


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
