#!/usr/bin/env python
# encoding: utf-8

__title__ = "Main code"
__author__ = "Roboton Programing Team"
__version__ = ""

"""
    Main code
    ~~~~~~~~~~~~~
    the main code of our software ...
    require:
        *python 2.7
        *pyserial 2.7 library
        *pygame 1.9.1 library
        *joystick.py
        *encoder.py
        *gui.py
    :copyright: (c) 2015 by Roboton Programing Team <e-mail>
    Dalia Diab
    Mohab Adel
    Walid Yasir
    Yasmin Elnezamy
"""

# importing libraries
from Gui import GUI
from Tkinter import Tk




# main function
def main():
    # root window
    root = Tk()
    
    # object of GUI class
    app = GUI(root)
    
    
    # main loop for gui
    root.mainloop()
    

if __name__ == "__main__":
    main()
