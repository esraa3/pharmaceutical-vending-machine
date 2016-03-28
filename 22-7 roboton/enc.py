#!/usr/bin/env python
# encoding: utf-8

__title__ = "Encoder"
__author__ = "Roboton Programing Team"
__version__ = ""

"""
    Encoder
    ~~~~~~~~~~~~~
    A program that read left, right encoder tick and metal detector
    state, proccess data and output x, y plot state on the map .
    x, y between 0 and 19
    state = 0 : no mine
    state = 1 : mine above                                                       
    state = 2 : mine below
    require:
        *python 2.7
        *pyserial 2.7 library
    :copyright: (c) 2015 by Roboton Programing Team <e-mail>
    Dalia Diab
    Mohab Adel
    Walid Yasir
    Yasmin Elnezamy
"""

# importing libraries
import serial
from math import pi,sin,cos,atan2

class Encoder(object):
    # Encoder Attributes
    R = 6     #radius of the robot free wheel
    L = 47   #the distance between the two free wheel
    N = 16    #encoders' ticks per revolution

    theta = 0      #angle of robot
    x = 0          #x position of robot
    y = 0          #y position of robot
    ticks_l_old = 0    # old ticks of left encoder
    ticks_r_old = 0    # old ticks of right encoder

    def __init__(self, app, ser):
        self.app = app

        #serial init
        self.ser = ser

    def get_xy(self, ticks_l, ticks_r):
        """
        this method apply these equations to return x and y
            * find delta ticks
            * find distance : 2 pi R delta_ticks / N
            * find Dc -distance center- : (distance_right + distance_left) / 2
            * find x_new : x_old + Dc cos(theta)
            * find y_new : y_old + Dc sin(theta)
            * find theta_new : theta_old + (Dr - Dl) / l
            * correct theta: atan2(sin(theta), cos(theta))
        """
        # find delta ticks
        delta_ticks_l = ticks_l - self.ticks_l_old
        delta_ticks_r = ticks_r - self.ticks_r_old

        # ubdate old ticks
        self.ticks_l_old = ticks_l
        self.ticks_r_old = ticks_r

        # find distance
        dl = 2 * pi * self.R * delta_ticks_l / self.N
        dr = 2 * pi * self.R * delta_ticks_r / self.N
        dc = (dr + dl) / 2

        # find x, y
        self.x = round(self.x + dc * cos(self.theta), 3)
        self.y = round(self.y + dc * sin(self.theta), 3)


        # find theta
        self.theta += (dr - dl) / self.L
        self.theta = atan2(sin(self.theta), cos(self.theta))

        # return
        return self.x, self.y, round(self.theta * 180 / pi, 3)
    
    def read_serial(self):
        """
            while loop to read serial data from arduino
            data in the form "left tick:right tick:state"
            analyse data and plot mines
        """
        while True:
            # read serial
            mes = self.ser.readline()
            print mes
            # split data
            mes = mes.split(":")
            left = int(mes[0])
            right = int(mes[1])
            state = int(mes[2])
            
            # get x and y
            x_y =  self.get_xy(left, right)
            
            # plot 
            x = int(x_y[0] / 100)   # x square's number
            y = int(x_y[1] / 100)   # y square's number
            self.app.draw_mine(x, y, state)  # draw
	    self.app.ticks.set(str(left)+" : "+str(right))
            self.app.distance.set(str(x_y[1])+" : "+str(x_y[0]))  
            self.app.current_square.set(str(x)+" : "+str(y))
