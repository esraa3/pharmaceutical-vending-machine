##import RPi.GPIO as GPIO
####from Adafruit_CharLCD import Adafruit_CharLCD
##import time
##GPIO.setmode(GPIO.BCM)
### Initialise and clear LCD
##lcd = Adafruit_CharLCD()
##lcd.clear()
##time.sleep(0.5)
class keypad:
    def __init__(self):    
        MATRIX = [ [1,2,3,'A'],
                   [4,5,6,'B'],
                   [7,8,9,'C'],
                   ['*',0,'#','D']]
        ROW = [14,18,23,24]
        COL = [17,27,22,10]
        for j in range(4):
            GPIO.setup(COL[j],GPIO.OUT)
            GPIO.output(COL[j],1)   
        for i in range(4):
            GPIO.setup(ROW[i],GPIO.IN , pull_up_down = GPIO.PUD_UP)
        try:
            while(True):   
                ##CODE
                for j in range(4):
                    GPIO.output(COL[j],0)#LOW
                    for i in range(4):
                        if GPIO.input(ROW[i]) == 0:
                            key_pressed = MATRIX[i][j]
                            return key_pessed
        ##                    lcd.clear()
        ##                    lcd.message("{} was pressed".format(key_pressed))
        ##                    time.sleep(0.2)
        ##                    while (GPIO.input (ROW[i]) ==0):
        ##                           pass
        ##            GPIO.output(COL[j],1)#HIGH
        except KeyboardInterrupt:
            GPIO.cleanup()
