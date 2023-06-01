#!/usr/bin/python3
import time, threading, os
from nmap import PortScanner
from tkinter import *
import MODULES.Enumeration, MODULES.write2report, MODULES.functions



nm = PortScanner()

def preScan(self):


    # Clearing out top and bottom window in case user clicks scan agin after enumeration.  This deletes the service buttons and re-disables the brute tab.
    try:
        # Clear scanning tab windows
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=" ")
        MODULES.functions.bottomWindowDelete(window=self.scrollWindowScannerBottom)
        
        
        # Clear brute tab top window
        MODULES.functions.topWindowUpdate(window=self.scrollWindowbruteTop, updateText=" ")
     
        # Disabling the Brute tab until valid results are found from scanning
        self.notebookAmos.tab(self.frameBrute, state="disabled")
    except:
        pass

    # Disable entry boxes while scans are running
    self.entryTargetName.config(state='disabled')
    self.entryTargetIP.config(state='disabled')

    # Getting values from text boxes
    self.targetName = self.entryTargetName.get()
    self.targetIP = self.entryTargetIP.get()

    # Leaving TargetName blank to give it name of IP.  Thinking about x.x.x.x/24 scans
    if self.targetName == "":
        self.targetName = self.entryTargetIP.get()
    
    # Setting up treaded function
    THREADsetThreads = threading.Thread(target=setThreads, args=(self, ), daemon=True)
    THREADsetThreads.start()
    
    
def setThreads(self):

    # Checking for documents directory
    MODULES.functions.documentsFolderPathCheck(self)

    # Creatng template creds file
    MODULES.write2report.write2Creds(self)

    # Displaying that the target folder has been created. 
    MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=self.targetName + " created\n\n")

    # Begin report header
    MODULES.write2report.header2html(self)
    MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Running quick nmap scan...\n\n")

    # Kicking off quick and full nmap scans
    THREADquickNmap = threading.Thread(target=quickNmap, args=(self, ), daemon=True)
    THREADquickNmap.start()
    THREADfullNmap = threading.Thread(target=fullNmap, args=(self, ), daemon=True)
    THREADfullNmap.start()


##################### quickNmap #####################

def quickNmap(self):

    try:

        # Running namp command
        MODULES.functions.quickPortScan(self)
        
    except KeyError:
        # If error occurs, update top window
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Error!  No ports found...\n\nPlease check details and try again.")
        self.progressBar.stop()
        

##################### fullNmap #####################

def fullNmap(self):

    #time.sleep(1) # Used for testing

    # Updating status label.
    MODULES.functions.statusUpdate(self, statusText="Full port scan in progress...")
    
    # Performing nmap full port scan
    MODULES.functions.fullPortScan(self)
    MODULES.functions.statusUpdate(self, statusText="Full port scan completed...")

    # Writing the full port scan done update at bottom window.
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap full port scan done!\n")

    # Making list of all open ports found
    fullOpenPortList = ','.join(map(str, self.fullOpenPortList))

    MODULES.functions.statusUpdate(self, statusText="Service scan in progress...")
    
    # Running namp service scan
    MODULES.functions.serviceScan(self, fullOpenPortList)
    MODULES.functions.statusUpdate(self, statusText="Service scan complete...")

    # Writing the service scan done update at bottom window.
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap service scan done!\n")

    HTMLheader = "Full service scan results"

    # Function that is needed in order to create multiple labels as open ports are found.
    def applytoLabel():
        # This function is used to write results to html report
        scanSummary = []      

        for port,service in self.dicAllOpenPorts.items():

            serviceProduct = self.serviceScan['scan'][self.targetIP]['tcp'][port]['product']
            serviceVersion = self.serviceScan['scan'][self.targetIP]['tcp'][port]['version']

            scanSummary.extend([[str(port), str(service), serviceProduct + " " + serviceVersion],])
           
        MODULES.write2report.serviceScan2html(self, HTMLheader, scanSummary)

    applytoLabel()

    # Check box for enabling / disabling vulners scan
    if self.skipVulners == False:
        vulnersNmap(self)

    # if self.skipUDP == False:
    #     scanUDP(self)
  
    else:
        wrapUp(self)


# ##################### vulnersNmap #####################

def vulnersNmap(self):

    #time.sleep(1) # Used for testing

    # Updating status label.
    MODULES.functions.statusUpdate(self, statusText="Vulners scan in progress...")

    # Local list variable of open ports 
    fullOpenPortList = ','.join(map(str, self.fullOpenPortList))
   
    # Running the nmap vulners scan
    MODULES.functions.vulnersScan(self, fullOpenPortList)

    def applytoLabel():

        # This function is used to write results to html report
        for port in self.fullOpenPortList:
            HTMLheader = "Vulners scan results for port: " + str(port)
            vulnList = []

            try:
                vulnSummary = self.vulnersScan['scan'][self.targetIP]["tcp"][port]["script"]["vulners"] + '\n'
                
                # Removing empty strings
                vulnSummary = "".join([s for s in vulnSummary.splitlines(True) if s.strip("\r\n")])

                ### PRINTING FIRST LINE:
                vulnSummaryHeader = vulnSummary.partition('\n')[0]
                
                ### PRINTING RESULT LINES:
                vulnSummary = vulnSummary.partition("\n")[-1]

                ### SPLITTING LINES TO INDIVIDUAL LINES
                vulnList = vulnSummary.split("\n")

                vulnList2 = []
                for line in vulnList:
                    if line != "":
                        vulnList2.append(line.split())

                HTMLheader = "Vulners scan results for port: " + str(port) + vulnSummaryHeader
                MODULES.write2report.vulnScan2html(self, HTMLheader, vulnList2)

            except KeyError:
                pass
            
    applytoLabel()
   
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap vulners scan done!\n")
    wrapUp(self)



def scanUDP(self):
    pass

    # time.sleep(1) # Used for testing

    # # Updating status label.
    # MODULES.functions.statusUpdate(self, statusText="UDP port scan in progress...")

    # # Running namp command
    # #self.fullPortScan = nm.scan(self.targetIP, arguments='-Su -T4 -Pn -p')   
    # MODULES.functions.statusUpdate(self, statusText="UDP port scan completed...")

    # # Writing the full port scan done update at bottom window.
    # MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap UDP port scan done!\n")


def wrapUp(self):

    # Changing permission to regular user from sudo, making report and creds files easier to access
    os.chown("/home/" + self.userName + "/Documents/" + self.targetName + "/creds.txt", self.uid, self.gid)
    os.chown("/home/" + self.userName + "/Documents/" + self.targetName + "/report.html", self.uid, self.gid)
    
    MODULES.functions.statusUpdate(self, statusText="All scans complete!")

    # Stop the progress bar
    self.progressBar.stop()

    # Make the enumeration button
    self.enumButton = MODULES.functions.buttonMaker(frameName=self.frameScanner, text="Enumeration")
    self.enumButton.place(anchor="nw", x=525, y=530)
    self.enumButton.configure(command=lambda:MODULES.Enumeration.enumeration(self), width=10)
