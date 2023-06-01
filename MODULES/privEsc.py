#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import threading
import MODULES.functions, MODULES.codeVault
from functools import partial


def threadingSetup(self):
    THREADdrawUI = threading.Thread(target=privEsc, args=(self, ), daemon=True)
    THREADdrawUI.start()

def privEsc(self):

    # Placing window
    privEscWindow = MODULES.functions.windowMaker(frameName=self.framePrivEsc)
    privEscWindow.place(anchor="nw", height=260, width=325, x=525, y=300)

    # Placing labels
    labelTargetType = tk.Label(self.framePrivEsc, text="OS", background="black", foreground="#64d86b")
    labelTargetType.place(anchor="nw", x=520, y=25)

    variableOS = StringVar(self.framePrivEsc)
    dropDownOS = OptionMenu(self.framePrivEsc, variableOS, "Windows", "Unix", command=lambda x:myCallback())  #######
    dropDownOS.place(anchor="nw", x=520, y=50)

    labelTargetType = tk.Label(self.framePrivEsc, text="Section", background="black", foreground="#64d86b")
    labelTargetType.place(anchor="nw", x=650, y=25)

    variableSection = StringVar(self.framePrivEsc)
    dropDownSection = OptionMenu(self.framePrivEsc, variableSection, "User", "Network", "System", command=lambda x:myCallback())  #######
    dropDownSection.place(anchor="nw", x=650, y=50)

    def myCallback():

        # Attempt to remove any content in Window if any exists
        try:
            privEscWindow.configure(state="normal")
            privEscWindow.delete(1.0,END)                       
        except UnboundLocalError:
            pass

        match variableOS.get():
 
            # If Windows is selected, get Arch value, then ......
            case 'Windows':
                OS = "Windows"               
                
            # If Unix is selected, get Arch value, then ......
            case 'Unix':
                OS = "Unix"
            

        match variableSection.get():

            # user drop down selected, checking for OS
            case 'User':
                if OS == "Windows":   
                    
                    # Windows user privesc commands displayed as buttons capable of copying to clipboard 
                    command = MODULES.codeVault.windowsUser()
                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")
                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)

                if OS == "Unix":
                    # Unix user privesc commands displayed as buttons capable of copying to clipboard
                    command = MODULES.codeVault.linuxUser()

                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")

                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)
                else:
                    pass

            case 'Network':
                if OS == 'Windows':

                    # Windows network privesc commands displayed as buttons capable of copying to clipboard
                    command = MODULES.codeVault.windowsNetwork()
                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")

                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)
        

                if OS == "Unix":

                    # Unix network privesc commands displayed as buttons capable of copying to clipboard
                    command = MODULES.codeVault.linuxNetwork()

                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")

                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)


            case 'System':
                if OS == 'Windows':

                    # Windows system privesc commands displayed as buttons capable of copying to clipboard
                    command = MODULES.codeVault.windowsSystem()
                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")

                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)


                if OS == "Unix":

                    # Unix system privesc commands displayed as buttons capable of copying to clipboard
                    command = MODULES.codeVault.linuxSystem()

                    for item in command:

                        privEscButtons = MODULES.functions.buttonMaker(frameName=privEscWindow, text=item)

                        privEscWindow.window_create("end", window=privEscButtons)
                        privEscWindow.insert("end", "\n")

                        privEscButtons.configure(command=partial(gtc,item), width=25, wraplength=200)

    def gtc(dtxt):
        # Function that copies text to clipbord
        MODULES.functions.statusUpdate(self, statusText="Text copied to clipboard")
        self.framePrivEsc.clipboard_clear()
        self.framePrivEsc.clipboard_append(dtxt)   
