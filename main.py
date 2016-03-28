import RPi.GPIO as GPIO
from time import sleep
from SeleniumMasterCompareImage import ImageCompare
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from keypad import keypad
from control import *
GPIO.setmode(GPIO.BCM)
def main():
        while(1):
                #wecome message
                lcd = Adafruit_CharLCD()
                lcd.clear()
                lcd.message("Hello\nEnter Medicine number")
                #input medicine number
                keypressed =keypad()
                #show price on LCD and confirm order 
                lcd.clear()
                lcd.message(Medicine_Base[med_number][6],"\n",Medicine_Base[med_number][7])
                #confirm order
                keypressed =keypad()
                if keypressed != "C":
                        pass
                #Request the money(paper&coins)
                lcd.clear()
                lcd.message("Enter ",Medicine_Base[med_number][7]," LE")        
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
##                med=input("Enter med num : ")
                chemist1.get_medicine(med)
##        except:
##            print(" Error ")
            
if __name__ == "__main__":main()

