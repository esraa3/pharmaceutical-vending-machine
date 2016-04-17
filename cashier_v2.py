import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)

class cashier:
 
    #attributes of cashier object with inital value
    med_price= 0
    paid_coins= 0
    paid_paper= 0
    total_paid= 0

    #Not used until Now
    total_saving = 0
    total_spent = 0
    
    #Constructor
    def __init__(self,med_num):
        med = Medicine(med_num)
        self.start_new_process()
        

    def start_new_process(self):
        #set coins & paper & money to Zero again for new client
        self.med_price= med.price
        self.coins = 0
        self.paper = 0
        self.money = 0
    ##############################
    #first task receive money
    def accept_money(self):
        pull_motor = motor("MN")
        pull_motor.move_forward(5)
        #image object
        image=image()
        self.paid_paper+=image.get_paper_value()
        self.coin_acceptor()
        self.total_money()

    def coin_acceptor(self):
        if(GPIO.input(15)==True):
            # we deal for one type of coins for Now
            self.paid_coins+=1
            
    def total_money(self):
        self.total_paid = self.paid_coins + self.paid_paper

    def remain(self):
        return self.med_price - self.total_paid
    
    ################################







       
                
