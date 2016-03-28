#!/usr/bin/env python
# encoding: utf-8

__title__ = "Main Gui"
__author__ = "Roboton Programing Team"
__version__ = ""

"""
    Main Gui
    ~~~~~~~~~~~~~
    A program that create our Gui and map.
    require:
        *python 2.7

    :copyright: (c) 2015 by Roboton Programing Team <e-mail>
    Dalia Diab
    Mohab Adel
    Walid Yasir
    Yasmin Ali
"""

# importing libraries
from Tkinter import *
import serial
import thread

from Joystick import JoystickControl
from enc import Encoder

from tkFileDialog import askopenfilename

class GUI(object, Frame):
    
    # check mines variables
    x_old = 0
    y_old = 0
    flag = True
    
    def __init__(self, parent):
        # init frame
        Frame.__init__(self, parent)

        self.parent = parent

        self.buildGui()

    def buildGui(self):
        """
            build components of gui and show it
        """
        
        # set title and make frame fill window
        self.parent.title("where 's my mine")
        self.pack(fill = BOTH, expand = 1)

        # init grids
        for i in range(0,30):
           self.columnconfigure(i, pad = 3)
           self.rowconfigure(i, pad = 3)
          
        self.buttons = []       # buttons array for map
	        
        # fill array with 19 column and 19 row
        for i in range(19):
            self.buttons.append([])
            for j in range(19):
                t = "(" , i, ",", j, ")"
                self.buttons[i].append(Button(self, text = t))
                self.buttons[i][j].grid(row = i, column = j)
                self.buttons[i][j]["bg"] = "#ffc7b9" # color light pink
        
        #label 1 print ticks
        self.ticks = StringVar()
        self.ticks.set("ticks here!")
        Label(self, textvariable = self.ticks).grid(row = 0, column = 29)

        #design Gui (fixed labels)
        Label(self, text="********************",fg="Red").grid(row=9, column=29)
        Label(self, text="********************",fg="Red").grid(row=14, column=29)
              
       
        #label 2 x,y as distance
        self.distance = StringVar()
        self.distance.set("x : y")
        Label(self, textvariable = self.distance).grid(row = 1, column = 29)
       
        
        #label 3 where's my robot (squares!)
        self.current_square = StringVar()
        self.current_square.set("(x,y)")
        Label(self, textvariable = self.current_square).grid(row = 2, column = 29)
        
        # entry comm_num
        self.e1=Entry(self)
        self.e1.grid(row=5,column=29)
        
        # entry manual draw
        self.e2=Entry(self)
        self.e2.grid(row=10,column=29)
        
        # connect serial button
        Button(self,text='connect serial',command=self.connect_serial).grid(row=7,column=29)
        Button(self,text='connect joystick',command=self.connect_joystick).grid(row=16,column=29)
        Button(self,text='connect Arduino',command=self.connect_arduino).grid(row=18,column=29)        
        Button(self,text='Manual Draw',command=self.manual_draw).grid(row=12,column=29)
        #Import Button:
        Button(self,text="Import",bg="purple",command=self.import_file).grid(row=28,column=28)
        


        self.pack()

    #function to import file
    def import_file(self):
        f = askopenfilename()
        my_file=open(f,"r")
        
        for i in my_file:
           self.get_position(i) 
            

    def get_position(self,line):
        
        read_line=line.split(":")
        x=int(read_line[0])
        y=int(read_line[1])
        m=int(read_line[2])
        self.draw_mine(x,y,m)

    # connect serial button handler
    def connect_arduino(self):
        self.enc = Encoder(self, self.arduino)
        thread.start_new_thread(self.enc.read_serial, ()) 
      
      
    def connect_joystick(self):
      
        self.joy = JoystickControl(self.arduino)
        thread.start_new_thread(self.joy.joystick_read, ())
      
    def manual_draw(self):
        map=self.e2.get().split(":")
        x=int(map[0])
        y=int(map[1])
        mine_state=int(map[2])
        self.draw_mine(x,y,mine_state)
        
    def connect_serial(self):
       
      	"""
      			connect serial 	
        """
        
        # handle serial connection error
        try:
        	
            com_num=self.e1.get()
            self.arduino=serial.Serial(com_num,9600)
        except IOError as e : 
            print "Serial Communication Cannot Establish (Please Check your Comnum) ",e  
    def draw_mine(self, x, y, m):
        """
            plot mines on map grid
        """

        # check state 
        x_change = (x != self.x_old)
        y_change = (y != self.y_old)
        if x_change or y_change:
            self.flag= True

        # plot state
        if m == 2:
            self.buttons[x][y]["bg"] = "red"
            self.update()

        elif m == 1:
            self.buttons[x][y]["bg"] = "green"
            self.update()

        elif m == 0 and self.flag:
            self.flag = False
            self.buttons[x][y]["bg"] = "blue"
            self.update()
    
        self.x_old = x
        self.y_old = y

  
