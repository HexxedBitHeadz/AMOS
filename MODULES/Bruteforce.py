#!/usr/bin/python3
from nmap import PortScanner
import tkinter as tk
from tkinter import *
import MODULES.functions
import threading

nm = PortScanner()


def bruteforce(self, port, service):

    # Here in this tab, we will test and display findings for: 1. Anonymous access 2. nmap credfile.txt attack.
    var = tk.IntVar()

    # Creating checkboxes
    checkboxes = MODULES.functions.checkBoxMaker(frameName=self.scrollWindowBruteBottom, text=str(port) + " - " + str(service))
    checkboxes.configure(variable=var, command=lambda:myCallback(self, var, port, service))

    # Adding checkboxes to bottom window
    self.scrollWindowBruteBottom.window_create("end", window=checkboxes)
    checkboxes.pack(anchor=W)

    # Making the brute button
    self.bruteButton = MODULES.functions.buttonMaker(frameName=self.frameBrute, text="brute em!")
    self.bruteButton.place(anchor="nw", x=525, y=550)

    try:
        self.bruteButton.configure(command=lambda:attackCreds(self), width=10)
    
    except TypeError:
        pass

    # Making the creds button
    self.credsButton = MODULES.functions.buttonMaker(frameName=self.frameBrute, text="Update creds")
    self.credsButton.place(anchor="nw", x=700, y=550)
    self.credsButton.configure(command=lambda:updateCreds(self), width=10)
    self.credsButton.configure(state="normal")
    

dicEnabled = {}

def myCallback(self, var, port, service):

    # This function is for the purpose of activating / deactivating the value of check boxes
    var = var.get()
 
    if var == 1:
        dicEnabled.update({service:port})

    if var == 0:
        dicEnabled.pop(service,port)

    # When pressed, go to threadSetup function
    self.bruteButton.configure(command=lambda:threadingSetup(self, dicEnabled, port, service))


def threadingSetup(self, dicEnabled, port, service):
    
    # Setting up thread for attackCreds function
    THREADbruteNmap = threading.Thread(target=attackCreds, args=(self, dicEnabled, port, service), daemon=True)
    THREADbruteNmap.start()

def attackCreds(self, dicEnabled, port, service):

    # Disable entry boxes while scans are running
    self.entryTargetName.config(state='disabled')
    self.entryTargetIP.config(state='disabled')

    # Deleting top window text.
    self.scrollWindowbruteTop.configure(state="normal")
    self.scrollWindowbruteTop.delete("1.0", END)
    self.scrollWindowbruteTop.configure(state="disabled")

    # Start the progress bar
    self.progressBar.start(15)

    self.bruteButton.configure(state="disabled")
    self.credsButton.configure(state="disabled")

    ##### https://nmap.org/nsedoc/categories/brute.html

    updateText = ""

    # Assigning nmap args
    for service,port in dicEnabled.items():        
        nmapArguments = ' -Pn --script ' + service + '-brute --script-args "brute.credfile=creds.txt" -p '

        # Updating status label.
        MODULES.functions.statusUpdate(self, statusText= service + " Brute attack in progress...")
    
        # Attacking every eligible service with creds.txt file
        bruteScan = nm.scan(self.TargetIP + nmapArguments + str(port))

        ### try to have updateText reflect results live, instead of all at one at the end.
        try:
            updateText += "====" + service + " on port: " + str(port) + "\n" + bruteScan["scan"][self.TargetIP]["tcp"][port]["script"][service + "-brute"] + "\n\n"

        except KeyError:
            updateText += "====" + service + " on port: " + str(port) + ": No valid accounts found.\n\n"
        MODULES.functions.topWindowUpdate(window=self.scrollWindowbruteTop, updateText=updateText)
    
    # Updating status, stopping progress bar and re-enable button
    MODULES.functions.statusUpdate(self, statusText="Brute attack finished")
    self.progressBar.stop()
    self.bruteButton.configure(state="normal")
    self.credsButton.configure(state="normal")
    self.entryTargetName.config(state='normal')
    self.entryTargetIP.config(state='normal')


    # Writing updateText to html report.
    Header = "BRUTE USERNAMES"

    updateText = updateText.split("====")

    # Remove any leading or trailing whitespace from each line
    updateText = [s.strip() for s in updateText]
    MODULES.write2report.auth2html(self, Header, updateText)

# This code is a work around to implement wildcard in service bove when found.
class MyStr(str):
    def __eq__(self, other: object):
        return self.__contains__(other)

# Function to allow tab button to move between windows
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")

def updateCreds(self):
    self.credsButton.configure(state="disabled")

    # Taking creds file and assigning user / password variables
    user = []
    password = []
    with open('creds.txt', 'r') as f:
        for line in f:
            user += line.strip().split("/")[:1]
            password += line.strip().split("/")[1::2]
        
    # making new window to pop out
    credsWindow = MODULES.functions.popOutWindow(frameName=self.frameBrute, text="Cred List")

    # Making the users window
    credsUserScrollWindow = MODULES.functions.windowMaker(frameName=credsWindow)
    credsUserScrollWindow.place(anchor="nw", height=500, width=200, x=10, y=10)
    credsUserScrollWindow.configure(state="normal", insertbackground='#64d86b')
    credsUserScrollWindow.insert("1.0", "\n".join(user))
    credsUserScrollWindow.bind("<Tab>", focus_next_window)

    # Making the passwords window
    credsPasswordScrollWindow = MODULES.functions.windowMaker(frameName=credsWindow)
    credsPasswordScrollWindow.place(anchor="nw", height=500, width=200, x=290, y=10)
    credsPasswordScrollWindow.configure(state="normal", insertbackground='#64d86b')
    credsPasswordScrollWindow.insert("1.0", "\n".join(password))
    credsPasswordScrollWindow.bind("<Tab>", focus_next_window)

    # Making the save button
    self.saveButton = MODULES.functions.buttonMaker(frameName=credsWindow, text="Save")
    self.saveButton.place(anchor="nw", x=215, y=525)
    self.saveButton.configure(command=lambda:saveCreds(), width=5)

    # When closing the credsWindow, enable the update button again
    credsWindow.protocol("WM_DELETE_WINDOW", lambda: onclose(self, credsWindow))

    def onclose(self, credsWindow):
        credsWindow.destroy()
        self.credsButton.configure(state="normal")

    def saveCreds():

        # This function is to work with the crendentials usernames and password windows.  Here we read from the creds.txt file, display the context, and add any new entries from the user
        resultUser = []
        resultPassword = []

        credsUsers = credsUserScrollWindow.get("1.0", END)
        for line in credsUsers.rsplit():
            resultUser.append(line)
        
        credsPasswords = credsPasswordScrollWindow.get("1.0", END)
        for line in credsPasswords.rsplit():
            resultPassword.append(line)
        
        def join_by_index(*lists, delimiter=""):
            return [delimiter.join(items) for items in zip(*lists)]

        concatCreds = join_by_index(resultUser, resultPassword, delimiter="/")

        text_file = open("creds.txt", "w")
        for entry in concatCreds:
            text_file.write(entry + "\n")
        text_file.close()

        # Status update new creds saved!
        statusLabel = MODULES.functions.labelMaker(frameName=credsWindow, text="Creds saved!")
        statusLabel.place(anchor="nw", x=20, y=550)
        statusLabel.after(3000, lambda:statusLabel.destroy())
