import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class cashier:
 
    #attributes of cashier object with inital value
    med_price= 0
    coins= 0
    paper= 0
    money= 0

    #Not used until Now
    total_saving = 0
    total_spent = 0
    
    #Constructor
    def __init__(self):
        self.start_new_process()

    def start_new_process(self):
        #set coins & paper & money to Zero again for new client
        self.med_price= 0
        self.coins = 0
        self.paper = 0
        self.money = 0

    def count_coins(self):
        # pin from coin acceptor
        GPIO.setup(15,GPIO.IN)
        if(GPIO.input(15)==True):
            # we deal for one type of coins for Now
            self.coins+=1

    def count_paper(self):
        # from class ImageProcessing Get paper value
        image = image()
        if(image.get_value())>0 :
            self.paper += image.get_value()
            
    def money(self):
        self.money = self.coins + self.paper
        return self.money
    
            
     def is_paid_for_med(self,med_number):
         # take object form medicine class to get med price from
         med = medicine(med_number)
         self.med_price= med.price
         if(self.money >= self.med_price):
             return true
         else:
             return fasle

    def get_charge(self):
        #find the money that should back to client
        if(self.money > self.med_price):
             return self.money - self.med_price
         else:
             return fasle

        
