import RPi.GPIO as GPIO
from time import sleep
from SeleniumMasterCompareImage import ImageCompare
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from keypad import keypad
from control import *
from my_keypad import *
GPIO.setmode(GPIO.BCM)

def main():
        while(1):
                #wecome message
                lcd = Adafruit_CharLCD()                        
                lcd.clear()
                lcd.message("Hello\nEnter Medicine number")
                #input medicine number
                ret= new my_keypad()
                if ret == 0:
                        lcd.message("Error")
                        sleep (2)
                        continue
                med_num = ret
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
                        lcd.message("Error")
                        sleep (2)
                        continue
                #take money
                motor("paper_in").move_forward(5)
                #match code here
                #case matched
                entered = matched 
                #case no match
                entered =0
                #take coins
                while(1):
                        lcd.message("Enter {0} LE \n Remaing :{1} LE ".Format(med.price,med.price - entered)
                        #if gpio goes low
                                entered+=1
                                #if entered = price break loop
                                    
                #output the medicine
                chemist().get_medicine(med_num)
                #output the reminder in terms of 1s and 10s and 20s
                while (reminder>0):
                        if reminder>=20:
                                    #output 1*20
                                    reminder -=20
                                    continue
                        elif reminder >=10:
                                    #output 1*10
                                    reminder -=10
                                    continue
                       else:
                                    #output ones
                                    reminder--
                                    continue             
if __name__ == "__main__":main()

