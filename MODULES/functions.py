#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from nmap import PortScanner
import os
import MODULES.Enumeration, MODULES.write2report, MODULES.functions


def frameMaker(self, text):
    # Code to genreate frames    
    frameName = Frame(self.notebookAmos, bg="black")
    self.notebookAmos.add(frameName, text=text)
    return frameName

def entryBoxes(frameName, _text_):
    # Code to genreate entry boxes
    boxName = ttk.Entry(frameName)
    boxName.delete("0", "end")
    boxName.insert("0", _text_)
    return boxName

def windowMaker(frameName):
    # Code to genreate windows
    topWindowName = ScrolledText(frameName)
    topWindowName.configure(background="#000008", foreground="#64d86b", state="disabled", wrap="word")
    return topWindowName

def labelMaker(frameName, text):
    # Code to genreate lables
    labelName = tk.Label(frameName, text=text, background="black", foreground="#64d86b")
    return labelName
    
def buttonMaker(frameName, text):
    # Code to genreate buttons
    buttonName = tk.Button(frameName)
    buttonName.configure(bg="#008f11", relief="flat", width=20, default="normal", text=text)
    return buttonName

def progressBarMaker(self, frameName):
    # Code to genreate progress bars
    progressBarName  = ttk.Progressbar(frameName, orient="horizontal", length=100, mode="indeterminate")
    progressBarName .place(anchor="nw", x=20, y=560)
    return progressBarName

def checkBoxMaker(frameName, text):
    # Code to genreate check boxes
    s = ttk.Style()
    s.configure('Red.TCheckbutton', background='black', foreground='red')
    checkBoxName = ttk.Checkbutton(frameName, style='Red.TCheckbutton')
    checkBoxName.configure(text=text)
    return checkBoxName

def popOutWindow(frameName, text):
    # Code to genreate pop out windows
    windowName=Toplevel(frameName)
    windowName.geometry("500x600")
    windowName.title(text)
    windowName.configure(background="#000008")
    windowName.resizable(False, False)
    return windowName

###########################

def documentsFolderPathCheck(self):
    # Getting the user path, checking for the Documents folder existance.  If it does not exist, create it
    DocumentsFolder = ("/home/" + self.userName + "/Documents/")



    # Checking if path already exists
    str(os.path.exists(DocumentsFolder))

    # If not, create it
    if not os.path.exists(DocumentsFolder):
        os.mkdir(DocumentsFolder)
    os.chdir(DocumentsFolder)

    # Checking for the Documents/TargetName folder.  If it does not exist, create it
    str(os.path.exists(self.entryTargetName.get()))
    
    if not os.path.exists(self.entryTargetName.get()):
        os.mkdir(self.entryTargetName.get())
        os.chown(self.entryTargetName.get(), self.uid, self.gid)
    else:
        pass
    os.chdir(self.entryTargetName.get())




def statusUpdate(self, statusText):
    # If previous status update exists, try destroying it before new update
    try:
        self.statusLabel.destroy()
    except AttributeError:
        pass

    #Updating status label (BOTTOM LEFT UNDER PROGRESS BAR)
    self.statusLabel = tk.Label(text=statusText, background="black", foreground="#64d86b")
    self.statusLabel.place(anchor="nw", x=12, y=577)

def topWindowUpdate(window, updateText):
    # Updating top window
    window.configure(state="normal")
    window.delete(1.0,END)
    window.insert('end', updateText)
    window.configure(state="disabled")

def bottomWindowUpdate(window, updateText):
    # Updating bottom window
    window.configure(state="normal")
    window.insert('end', updateText)
    window.configure(state="disabled")

def topWindowDelete(window):
    # Delete contents in top window
    window.configure(state="normal")
    window.delete("1.0",END)
    window.configure(state="disabled")

def bottomWindowDelete(window):
    # Delete contents in bottom window
    window.configure(state="normal")
    window.delete(1.0,END)
    window.configure(state="disabled")

##########################################

def quickPortScan(self):
    nm = PortScanner()

    # nmap quick scan
    self.quickPortScan = nm.scan(self.targetIP, arguments='-sS -T4 -Pn')   ######################

    # Finding open ports
    quickOpenPortList = list(self.quickPortScan['scan'][self.targetIP]['tcp'].keys())
    
    # Prepping service variable for assignment
    quickOpenServiceList = []

    # Assigning quick list of open services to variable
    for n in range(len(quickOpenPortList)):        
        quickOpenServiceList += list(self.quickPortScan['scan'][self.targetIP]['tcp'][quickOpenPortList[n]]['name'].split())

    # Writing quick open ports and service name results to Amos top screen
    n = len(quickOpenPortList)
    updateText = ''
    for i in range(n):

        updateText = updateText + "port: " + str(quickOpenPortList[i]) + "\t" + "\t" + str(quickOpenServiceList[i]) + "\n"
    MODULES.functions.topWindowUpdate(window=self.scrolled_textScannerTop, updateText="Here are quick hits: \n\n" + updateText)

    # Writing the quick scan done update at bottom window.
    MODULES.functions.bottomWindowUpdate(window=self.scrolled_textScannerBottom, updateText="nmap quick port scan done!\n")

    return self.quickPortScan

def fullPortScan(self):
    nm = PortScanner()

    # Assign variable for full list of open ports
    self.fullOpenPortList = []

    # nmap full scanning for open ports
    self.fullPortScan = nm.scan(self.targetIP, arguments='--defeat-rst-ratelimit --max-rtt-timeout 900ms --initial-rtt-timeout 750ms --max-retries 3 -sS -T4 -Pn -p-') ##################

    try:
        self.fullOpenPortList = list(self.fullPortScan['scan'][self.targetIP]['tcp'].keys())

    # Error message in case scan goes wrong
    except KeyError:
        MODULES.functions.topWindowUpdate(window=self.scrolled_textScannerTop, updateText="Error!  No ports found...\n\nPlease check target details and try again.")

    # Assign variable for full list of banners tied to open ports
    self.fullOpenServiceList = []

    # Assigning FULL list of open banners to variables tied to open ports
    try:
        for n in range(len(self.fullOpenPortList)):        
            self.fullOpenServiceList += list(self.fullPortScan['scan'][self.targetIP]['tcp'][self.fullOpenPortList[n]]['name'].split())

    except AttributeError:
        pass

    # Combining ports and banners to a dictionary.
    self.dicAllOpenPorts = dict(zip(self.fullOpenPortList, self.fullOpenServiceList))

    return self.dicAllOpenPorts


def serviceScan(self, fullOpenPortList):
    nm = PortScanner()

    # nmap scan of services (-A) scanning of ONLY the ports found in previous full scan
    self.serviceScan = nm.scan(self.targetIP, arguments='--max-rtt-timeout 900ms --initial-rtt-timeout 750ms --max-retries 5 --script-timeout 30s -sS -A -T4 -Pn -p' + fullOpenPortList)   ######################

    return self.serviceScan


def vulnersScan(self, fullOpenPortList):
    nm = PortScanner()

    # nmap vulners scan of ONLY the ports found in previous full scan
    self.vulnersScan = nm.scan(self.targetIP, arguments='-sV --script vulners -p ' + fullOpenPortList)   ######################  

    return self.vulnersScan


