#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import threading, subprocess
import MODULES.functions, os
from tkinter.filedialog import askdirectory

def threadingSetup(self):
    pass


def tools(self):
    pass
    # #Placing window usign frameTools from amos.py
    



def enableService(self, service):
    # Matching service name user selection, kicking off desired service
    match service:
        case "HTTP":
            self.HTTPStartButton.config(state="disabled")
            self.HTTPStopButton.config(state="normal")
            try:
                MODULES.functions.statusUpdate(self, statusText="Selecting server directory...")
                foldername = askdirectory()
                os.chdir(foldername + "/")
            except TypeError:
                pass             

            bashCommand = "sudo python3 -m http.server 80"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True)
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="HTTP server started. \n")

        case "Mail":
            self.MailStartButton.config(state="disabled")
            self.MailStopButton.config(state="normal")
            bashCommand = "sudo python3 -m smtpd -n -c DebuggingServer localhost:25"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True)
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="Mail server started. \n")

        case "FTP":
            self.FTPStartButton.config(state="disabled")
            self.FTPStopButton.config(state="normal")

            try:
                MODULES.functions.statusUpdate(self, statusText="Selecting server directory...")
                foldername = askdirectory()
                os.chdir(foldername + "/")
            except TypeError:
                pass   

            bashCommand = "sudo python3 -m pyftpdlib -p 21 --write"
            threading.Thread(target=subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE), args=(), daemon=True) 
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="FTP server started. \n")

def disableService(self, service):
    
    # Matching service name user selection, killing off desired service
    match service:
        case "HTTP":
            self.startButton.config(state="normal")
            self.stopButton.config(state="disabled")        
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":80"])
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="HTTP server stopped. \n")

        case "Mail":
            self.startButton.config(state="normal")
            self.stopButton.config(state="disabled")
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":25"])
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="Mail server stopped. \n")
        
        case "FTP":
            self.startButton.config(state="normal")
            self.stopButton.config(state="disabled")
            subprocess.call(["sudo", "ss", "--kill", "state", "listening", "src", ":21"])
            MODULES.functions.bottomWindowUpdate(window=self.toolsWindow, updateText="FTP server stopped. \n")
