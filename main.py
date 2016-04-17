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
                med_num = keypressed
                #show price on LCD and confirm order 
                lcd.clear()
                med = Medicine(med_num);
                lcd.message(med.name,"\n",med.price)
                delay(5)
                #confirm order
                lcd.clear()
                lcd.message("To Confirm Order \nEnter C")
                keypressed =keypad()
                if keypressed != "C":
                        continue
                #Request the money(paper&coins)
                lcd.clear()
                cashier = cashier(med_num)
                lcd.message("Enter {0} LE \n Remaing :{1} LE ".Format(med.price,cashier.remain())
                            
                #check money
                imageCompare=ImageCompare()
                a=imageCompare.compare('1.jpg','2.jpg')
                print 'Images Equal?',a
                #output the medicine
                chemist1=chemist()
                chemist1.get_medicine(med_num)
                #output the reminder in terms of 5s and 10s

        
        
##        try:
##            while(1):
##                med=input("Enter med num : ")
                ##chemist1.get_medicine(med)
##        except:
##            print(" Error ")
            
if __name__ == "__main__":main()

