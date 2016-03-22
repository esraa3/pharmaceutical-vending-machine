from PIL import Image
from pytesseract import image_to_string
import pytesseract
img = Image.open('C:\Users\esraa\Desktop\image ook\img.jpg')
img.load()
i = pytesseract.image_to_string(img)
print i
