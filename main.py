import RPi.GPIO as GPIO
from time import sleep
from SeleniumMasterCompareImage import ImageCompare
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from control import *
GPIO.setmode(GPIO.BCM)
def main():
        lcd = Adafruit_CharLCD()
        lcd.clear()
        lcd.message("Hello\nEnter Medicine number")
        #wecome message
        
        #input medicine number
        
        #show price on LCD
        
        #confirm order
        
        #Request the money(paper&coins)
        
        #check money
        imageCompare=ImageCompare()
        a=imageCompare.compare('1.jpg','2.jpg')
        print 'Images Equal?',a
        #output the medicine
        med=input("Enter med num : ")
        chemist1.get_medicine(med)
        #output the reminder in terms of 5s and 10s

        
        chemist1=chemist()
##        try:
##            while(1):
                med=input("Enter med num : ")
                chemist1.get_medicine(med)
##        except:
##            print(" Error ")
            
if __name__ == "__main__":main()

