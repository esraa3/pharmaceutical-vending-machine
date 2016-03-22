import RPi.GPIO as GPIO
from time import sleep
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from control import *
GPIO.setmode(GPIO.BCM)
def main():
        lcd = Adafruit_CharLCD()
        lcd.clear()

        
        chemist1=chemist()
        try:
            while(1):
                med=input("Enter med num : ")
                chemist1.get_medicine(med)
        except:
            print(" Error ")
            
if __name__ == "__main__":main()

