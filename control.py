class motor:
    pin1 = None
    pin2 = None
    def __init__(self,type):   
        #make pins output
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        #set pins
        self.set_pins(type);
    def set_pins(self , type):
        type=type.lower()
        if (type=="x"):
            #motor X Config pins
            self.pin1 = 23
            self.pin2 = 24
        elif(type=="y"):
            #motor Y  Config pins
            self.pin1 = 17
            self.pin2 = 27
        elif (type=="z"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        elif (type=="coin_ret"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        elif (type=="paper_in"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        elif (type=="10_ret"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        elif (type=="20_ret"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        elif (type=="paper_to_box"):
            #motor Z Config pins
            #pins are not set
            self.pin1 = 11  
            self.pin2 = 8
        else:
            print("This Type of motor not available")
    #you can combine these in one function (Move) with arg Direction   
    def move_forward(self , time):
          #S=GPIO.PWM(self.pin1,50) #50 is frquency
          #S.start(10) #10 is start duty
          print ("Going forwards on pin {}".format(self.pin1))
          GPIO.output(self.pin1,GPIO.HIGH)
          GPIO.output(self.pin2,GPIO.LOW)
          sleep(time)
          GPIO.output(self.pin1,GPIO.LOW)
          
    def move_Backward(self , time ):
          #Normal code Without PWM
          print ("Going Backword on pin {}".format(self.pin2))
          GPIO.output(self.pin1,GPIO.LOW)
          GPIO.output(self.pin2,GPIO.HIGH)
          sleep(time)
          GPIO.output(self.pin2,GPIO.LOW)
#######################################################################################
class medicine:
    #attributes of medicine object with inital value
    med_x = 0
    med_y = 0    
    width = 0
    push_time = 0
    count = 0
    price = 0
    name =""
    
    #Constructor
    def __init__(self, med_number):
        # Leave object Blank unless i set number make arg (med_number = None)
        #if(med_number != None ):
        self.set_medicine(med_number)
    # Set Medicine to Object    
    def set_medicine(self , med_number):
        #Dictionary contain info about all medicine (As DataBase)
        Medicine_Base = {
                          1:[0,0,12,0.6,5,3],
                          2:[1,0,4,0.3,3,3],
                          3:[2,0,4,0.3,3,],
                          4:[3,0,4,0.3,3,],
                          5:[0,1,4,0.3,3,],
                          6:[1,1,4,0.3,3,],
                          7:[2,1,4,0.3,3,],
                          8:[3,1,4,0.3,3,],
                          9:[0,2,4,0.3,3,],
                          10:[1,2,4,0.3,3,],
                          11:[2,2,4,0.3,3,],
                          12:[3,2,4,0.3,3,]
                        }
        try:
            med_info = Medicine_Base[med_number]         
            self.med_x = med_info[0]
            self.med_y = med_info[1]
            self.width = med_info[2]
            self.push_time = med_info[3]
            self.count = med_info[4]
            self.price=med_info[5]
            self.name=med_info[6]
        except:
            # Restore To Default
            self.unset_medicine()
    def unset_medicine(self):
            self.med_x = 0
            self.med_y = 0
            self.width = 0
            self.push_time = 0
            self.count = 0          
    def get_location(self):
        return [self.med_x , self.med_y]   
    def is_found(self,med_number):
        self.set_medicine(med_number)
        if(self.count == 0):
            return False
        else:
            return True
#################################################################################
class chemist:
    #Attributes needed
    med_wanted = 0 #i think this should deleted as attribute
    arrived = 0  # this also the same   
    current_x = 0
    current_y = 0
    delta_x = 0
    delta_y = 0    
    #initial objects from other classes 
    med_box = object
    motor_x = object
    motor_y = object
    motor_z = object
    # constructor Empty now
    # def __init__(self):   
    def set_target_location(self , med_number) :
        #take object from class medicine to grap all medicine info
        med_box = medicine(med_number)
        #save med number Temp
        self.med_wanted = med_number
        #Determine target
        self.delta_x = med_box.med_x - self.current_x
        self.delta_y = med_box.med_y - self.current_y      
    def get_medicine(self , med_number) :       
        med_box = medicine(med_number)
        #check medicine exist
        if(med_box.is_found(med_number)):
            self.set_target_location(med_number)         
            #inital motors objects
            motor_x = motor("x")
            motor_y = motor("y")
            motor_z = motor("z")
            #move in x direction
            if(self.delta_x > 0):
                motor_x.move_forward(self.delta_x*1.2)
            else:
                motor_x.move_Backward(-1*self.delta_x*1.2)
            #move in y direction
            if(self.delta_y > 0):
                motor_y.move_forward(self.delta_y*0.79)
            else:
                motor_y.move_Backward(-1*self.delta_y*1.5)
            
            #push medicine box , and back after that  #commented for test
            #motor_z.move_forward(med_box.push_time)
            #motor_z.move_Backward(med_box.push_time)
            #sleep 1 sleep before check arraival
            #sleep(1)
            #temp set for current location
            self.current_x = self.delta_x + self.current_x
            self.current_y = self.delta_y + self.current_y
            #check arrived of medicine
            #commented for test
            #self.check_arrived()
    def check_arrived(self):
        arrived_signal= GPIO.input(17)
        # if signal form push button at output hole set to 1
        if(arrived_signal == 1):
            print("Medicine arrived");
            #set new location (as far away from original (0,0))
            self.current_x = self.current_x + self.delta_x
            self.current_y= self.current_y + self.delta_y 
            # set arrived = 1
            self.arrived = 1
        else:
            # back system to original point and try to get medicine again
            self.reset()
            self.get_medicine(med_number)
            ####### set arrived = 0
            self.arrived = 0   
    def Reset(self):
        #set current and target attributes to 0
        current_x = 0
        current_y = 0
        delta_x = 0
        delta_y = 0
        ###move all x and y backward till origin switch give a signal 
        #motor_z.mov       
        # try to get medicine again
        self.get_medicine(self.med_wanted)
##################################################################################
