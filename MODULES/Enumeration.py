#!/usr/bin/python3
import threading
import MODULES.Bruteforce, MODULES.functions, MODULES.HTTPtools
from tkinter import *


def enumeration(self):
    
    # Creating flag system to know when to stop progress bar.
    self.totalFlags = len(self.dicAllOpenPorts.keys())
    self.flag = 0
    
    # Deleting bottom window text.
    MODULES.functions.bottomWindowDelete(window=self.scrollWindowScannerBottom)

    # Disabling enumeration button.
    self.enumButton.configure(state="disabled")

    # Start the progress bar and provide status update
    self.progressBar.start(15)
    MODULES.functions.statusUpdate(self, statusText="Enumeration scans in progress...")

    # Creating the buttons with service names and putting them on the screen.
    for port,service in self.dicAllOpenPorts.items():
        serviceButtons = MODULES.functions.buttonMaker(frameName=self.scrollWindowScannerBottom, text=service)
        self.scrollWindowScannerBottom.window_create("end", window=serviceButtons)
        self.scrollWindowScannerBottom.insert("end", "\n")
        THREADscirptEnumLoop = threading.Thread(target=scriptEnumLoop, args=(self, port, service, serviceButtons), daemon=True)
        THREADscirptEnumLoop.start()


###########################################################

def scriptEnumLoop(self, port, service, serviceButtons):

    scriptList = []

    # Begin extracting data from nmap dictionaries, put into labels on screen
    try:
        productList = self.serviceScan["scan"][self.targetIP]["tcp"][port]["product"]
        versionList = self.serviceScan["scan"][self.targetIP]["tcp"][port]["version"]

        if productList != "":
            scriptList.extend([[str(productList)]])
        elif productList == "":
            productList = "NONE"
            scriptList.extend([[str(productList)]])

        if versionList != "":
            scriptList.extend([[str(versionList)]])
        elif versionList == "":
            versionList = "NONE"
            scriptList.extend([[str(versionList)]])

        updateText = "====port: " + str(port) + " - " + service + "\n" + productList + " " + versionList

    except KeyError:
        updateText = "" 

    try:
            
        for scriptHeadersList, scriptDetailsList in self.serviceScan["scan"][self.targetIP]["tcp"][port]["script"].items():
                   
            if scriptHeadersList != "":
                scriptList.extend([[str(scriptHeadersList)]])
            elif scriptHeadersList == "":
                scriptHeadersList = "NONE"
                scriptList.extend([[str(scriptHeadersList)]])

            if scriptDetailsList != "":
                scriptList.extend([[str(scriptDetailsList)]])
            elif scriptDetailsList == "":
                scriptDetailsList = "NONE"
                scriptList.extend([[str(scriptDetailsList)]])

            updateText += "\n\n" + "==" + str(scriptHeadersList) + ":\n" + str(scriptDetailsList) + "\n"
        
    except KeyError:
        pass
 
    try:
        extraInfoList = self.serviceScan["scan"][self.targetIP]["tcp"][port]["extrainfo"]

        if extraInfoList != "":
            scriptList.extend([str(extraInfoList)])
        elif extraInfoList == "":
            extraInfoList = "NONE"
            scriptList.extend([str(extraInfoList)])

        updateText += "\n\n====Additional notes:\n" + extraInfoList

    except KeyError:
        updateText += ""

    serviceButtons.configure(state="normal")
    serviceButtons.bind("<Button-1>", lambda e:MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=updateText))

    # Writing updateText to html report.
    Header = service +  ":" + str(port)
    MODULES.write2report.enum2html(self, Header, scriptList)

    # Increasing flag variable by 1 everytime a port is enuemrated.
    self.flag += 1

    if self.flag == self.totalFlags:
        wrapUp(self)

def wrapUp(self):
    MODULES.functions.statusUpdate(self, statusText="Enumeration scans completed")
    self.progressBar.stop()

    # Reinstate the text boxes and button.
    self.scanButton.config(state='normal')
    self.entryTargetName.config(state='normal')
    # self.entryTargetName.delete(0, 'end')
    self.entryTargetIP.config(state='normal')
    # self.entrytargetIP.delete(0,'end')
    self.checkBoxVulners.config(state='normal')
    # self.checkBoxUDP.config(state='normal')

    # Counter keeping track of how many bruatable services are found
    self.numberOfBrutableService = 0    
    
    # Begin matching service names from results segragating for further enumeration
    for port,service in self.dicAllOpenPorts.items():
        match MyStr(service):
            
            case 'ftp':
                makeCheckBox(self, port, service)
                            
            case 'http':
                makeCheckBox(self, port, service)
                #MODULES.HTTPtools.threadingSetup(self)  ######## No longer needed here?  Needs review
                
            case 'imap':
                makeCheckBox(self, port, service)
                            
            case 'microsoft-ds':
                makeCheckBox(self, port, service)
                            
            # case 'mongo':
            #     makeCheckBox(self, port, service)  ####### Disabling, did not work properly during testing
                                
            case 'mssql':
                makeCheckBox(self, port, service)
                            
            case 'mysql':
                makeCheckBox(self, port, service)
                            
            case 'netbios-ssn':
                makeCheckBox(self, port, service)
                            
            case 'postgres':
                makeCheckBox(self, port, service)
                           
            case 'pop3':
                makeCheckBox(self, port, service)
                            
            case 'redis':
                makeCheckBox(self, port, service)
                            
            case 'smb':
                makeCheckBox(self, port, service)
                            
            case 'smtp':
                makeCheckBox(self, port, service)

            case 'snmp':
                makeCheckBox(self, port, service)
                            
            case 'ssh':
                makeCheckBox(self, port, service)
                            
            case 'telnet':
                makeCheckBox(self, port, service)
                            
            case 'vnc':
                makeCheckBox(self, port, service)
                            
            case _:
                pass
                

# This code is a work around to implement wildcard in service bove when found.  For example ZeusFTP will still be found as FTP, etc.
class MyStr(str):
    def __eq__(self, other: object):
        return self.__contains__(other)


def makeCheckBox(self, port, service):
    # Making check boxes servies that are able to be cred - bruteforced
    try:
        self.notebookAmos.tab(self.frameBrute, state="normal")
        self.numberOfBrutableService += 1
        
    except:
        pass

    MODULES.Bruteforce.bruteforce(self, port, service)

