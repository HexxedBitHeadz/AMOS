#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import threading, subprocess
import MODULES.functions, os
from tkinter.filedialog import askdirectory

def threadingSetup(self):
    # Setting up thread for tools function
    THREADTools = threading.Thread(target=tools, args=(self, ), daemon=True)
    THREADTools.start()

def tools(self):

    # #Placing window
    toolsWindow = MODULES.functions.windowMaker(frameName=self.frameTools)
    toolsWindow.place(anchor="nw", height=150, width=325, x=525, y=380)

    # Labels
    # HTTP server label
    HTTPServer = MODULES.functions.labelMaker(frameName=self.frameTools, text="HTTP Server")
    HTTPServer.place(anchor="nw", x=520, y=25)

    # Mail Server label
    mailServer = MODULES.functions.labelMaker(frameName=self.frameTools, text="Mail Server")
    mailServer.place(anchor="nw", x=720, y=25)

    # FTP Server label
    FTPServer = MODULES.functions.labelMaker(frameName=self.frameTools, text="FTP Server")
    FTPServer.place(anchor="nw", x=520, y=125)

    # Buttons
    # HTTP start and stop buttons
    HTTPStartButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Start")
    HTTPStartButton.config(width=1, command=lambda:enableService(self, HTTPStartButton, HTTPStopButton, toolsWindow, service="HTTP"))
    HTTPStartButton.place(anchor="nw", x=520, y=50)

    HTTPStopButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Stop")
    HTTPStopButton.config(width=1, command=lambda:disableService(HTTPStartButton, HTTPStopButton, toolsWindow, service="HTTP"))
    HTTPStopButton.config(state="disabled")
    HTTPStopButton.place(anchor="nw", x=570, y=50)

    # Mail start and stop buttons
    MailStartButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Start")
    MailStartButton.config(width=1, command=lambda:enableService(self, MailStartButton, MailStopButton, toolsWindow, service="Mail"))
    MailStartButton.place(anchor="nw", x=720, y=50)

    MailStopButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Stop")
    MailStopButton.config(width=1, command=lambda:disableService(MailStartButton, MailStopButton, toolsWindow, service="Mail"))
    MailStopButton.config(state="disabled")
    MailStopButton.place(anchor="nw", x=770, y=50)

    # FTP start and stop buttons
    FTPStartButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Start")
    FTPStartButton.config(width=1, command=lambda:enableService(self, FTPStartButton, FTPStopButton, toolsWindow, service="FTP"))
    FTPStartButton.place(anchor="nw", x=520, y=150)

    FTPStopButton = MODULES.functions.buttonMaker(frameName=self.frameTools, text="Stop")    
    FTPStopButton.config(width=1, command=lambda:disableService(FTPStartButton, FTPStopButton, toolsWindow, service="FTP"))
    FTPStopButton.config(state="disabled")
    FTPStopButton.place(anchor="nw", x=570, y=150)

def enableService(self, startButton, stopButton, toolsWindow, service):
    # Matching service name user selection, kicking off desired service
    match service:
        case "HTTP":
            startButton.config(state="disabled")
            stopButton.config(state="normal")
            try:
                MODULES.functions.statusUpdate(self, statusText="Selecting server directory...")
                foldername = askdirectory()
                os.chdir(foldername + "/")
            except TypeError:
                pass             

            bashCommand = "sudo python3 -m http.server 80"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True)
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="HTTP server started. \n")

        case "Mail":
            startButton.config(state="disabled")
            stopButton.config(state="normal")
            bashCommand = "sudo python3 -m smtpd -n -c DebuggingServer localhost:25"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True)
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="Mail server started. \n")

        case "FTP":
            startButton.config(state="disabled")
            stopButton.config(state="normal")

            try:
                MODULES.functions.statusUpdate(self, statusText="Selecting server directory...")
                foldername = askdirectory()
                os.chdir(foldername + "/")
            except TypeError:
                pass   

            bashCommand = "sudo python3 -m pyftpdlib -p 21 --write"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True) 
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="FTP server started. \n")

def disableService(startButton, stopButton, toolsWindow, service):
    
    # Matching service name user selection, killing off desired service
    match service:
        case "HTTP":
            startButton.config(state="normal")
            stopButton.config(state="disabled")        
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":80"])
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="HTTP server stopped. \n")

        case "Mail":
            startButton.config(state="normal")
            stopButton.config(state="disabled")
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":25"])
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="Mail server stopped. \n")
        
        case "FTP":
            startButton.config(state="normal")
            stopButton.config(state="disabled")
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":21"])
            MODULES.functions.bottomWindowUpdate(window=toolsWindow, updateText="FTP server stopped. \n")
