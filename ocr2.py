from PIL import Image
from pytesseract import image_to_string
import pytesseract
#take image by camera and read it
#img = Image.open('C:\Users\esraa\Desktop\image ook\ocr.jpg')
import picamera
camera = picamera.PiCamera()
camera.capture('image.jpg')

#load image and convert it to string 
img.load()
i = pytesseract.image_to_string(img)

#print the string 
print i
