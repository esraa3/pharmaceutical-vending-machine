 
from sys import argv
import zbar
from PIL import Image
import cv2
import picamera

camera = picamera.PiCamera()
camera.vflip=True
camera.hflip=True
camera.capture('image.jpg')
sleep (5)
camera.capture('image1.jpg')
sleep (5)
camera.capture('image2.jpg')
sleep (5)
camera.capture('image3.jpg')

image = cv2.imread('/home/pi/image.jpg')
image1 = cv2.imread('/home/pi/image1.jpg')
image2 = cv2.imread('/home/pi/image2.jpg')
image3 = cv2.imread('/home/pi/image3.jpg')
count=0
imageList=[image,image1,image2,image3]
for image in imageList:
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
    #if symbol.data == "None":
        #print "Drone bevindt zich buiten het raster"
    #else:
        return symbol.data
        count+=1
if (count >=1):
         return True
else:
         return False 
    

