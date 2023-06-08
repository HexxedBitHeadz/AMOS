#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import threading
import MODULES.functions, MODULES.codeVault
from functools import partial


def threadingSetup(self):
    pass

def privEsc(self):
    pass



def myCallback(self):

    def gtc(dtxt):
        # Function that copies text to clipbord
        MODULES.functions.statusUpdate(self, statusText="Text copied to clipboard")
        self.framePrivEsc.clipboard_clear()
        self.framePrivEsc.clipboard_append(dtxt)   



    # Attempt to remove any content in Window if any exists
    try:
        self.privEscWindow.configure(state="normal")
        self.privEscWindow.delete(1.0,END)                       
    except UnboundLocalError:
        pass

    match self.variableOS.get():

        # If Windows is selected, get Arch value, then ......
        case 'Windows':
            OS = "Windows"               
            
        # If Unix is selected, get Arch value, then ......
        case 'Unix':
            OS = "Unix"
        

    match self.variableSection.get():

        # user drop down selected, checking for OS
        case 'User':
            if OS == "Windows":   
                
                # Windows user privesc commands displayed as buttons capable of copying to clipboard 
                command = MODULES.codeVault.windowsUser()
                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")
                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)

            if OS == "Unix":
                # Unix user privesc commands displayed as buttons capable of copying to clipboard
                command = MODULES.codeVault.linuxUser()

                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")

                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)
            else:
                pass

        case 'Network':
            if OS == 'Windows':

                # Windows network privesc commands displayed as buttons capable of copying to clipboard
                command = MODULES.codeVault.windowsNetwork()
                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")

                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)
    

            if OS == "Unix":

                # Unix network privesc commands displayed as buttons capable of copying to clipboard
                command = MODULES.codeVault.linuxNetwork()

                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")

                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)


        case 'System':
            if OS == 'Windows':

                # Windows system privesc commands displayed as buttons capable of copying to clipboard
                command = MODULES.codeVault.windowsSystem()
                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")

                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)


            if OS == "Unix":

                # Unix system privesc commands displayed as buttons capable of copying to clipboard
                command = MODULES.codeVault.linuxSystem()

                for item in command:

                    privEscButtons = MODULES.functions.buttonMaker(frameName=self.privEscWindow, text=item)

                    self.privEscWindow.window_create("end", window=privEscButtons)
                    self.privEscWindow.insert("end", "\n")

                    privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)


