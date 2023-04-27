#!/usr/bin/python3
import MODULES.Scanning, MODULES.Enumeration, MODULES.revshell, MODULES.privEsc, MODULES.tools, MODULES.functions, MODULES.write2report
from tkinter import *
from nmap import PortScanner
import threading

nm = PortScanner()

def mulitpleIPFunction(self, multipleIPs):
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Congrats!  You found the flag!\n\nThis Feature is not yet working, but supporting multiple IP scans is in the works!\n\nFl@g{ItsNottaBugItsaFeature}")

        # self.progressBar.start(15)

#         # Delete top window
#         MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=" ")
        
#         for IP in range(len(multipleIPs)):
#                 self.TargetIP = multipleIPs[IP]
#                 TargetName = self.TargetIP
#                 threadingSetup(self)


# def threadingSetup(self):
#     THREADdrawUI = threading.Thread(target=functionScan, args=(self, ), daemon=True)
#     THREADdrawUI.start()

# def functionScan(self):
#         print(self.TargetIP)

#         # Break line
#         MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerTop, updateText="----------"  + str(self.TargetIP) + "-----------\n")

# #####################################################################

#         MODULES.functions.fullPortScan(self)
#         print(self.serviceScan)

#         HTMLheader = "Full port scan results"

#         # Function that is needed in order to create multiple labels as open ports are found.
#         def applytoLabel():


#                 ### REWRITE SCANSUMMARY VARIABLE AS A LIST INSTEAD OF A STRING.  THEN WHEN WE WRITE TO REPORT, WE CAN TREAT IT AS 3 ELEMENTS IN THE TABLE
#                 # REFERNCE:     view-source:file:///C:/Users/devin/Downloads/index.html

#                 scanSummary = []      

#                 for port,service in self.dicAllOpenPorts.items():

#                         serviceProduct = self.fullPortScan['scan'][self.self.TargetIP]['tcp'][port]['product']
#                         serviceVersion = self.fullPortScan['scan'][self.self.TargetIP]['tcp'][port]['version']

#                         scanSummary.extend([[str(port), str(service), serviceProduct + serviceVersion],])


#                 ############################################################
                        
#                 MODULES.write2report.serviceScan2html(HTMLheader, scanSummary)

#         applytoLabel()


# #####################################################################

#         fullOpenPortList = ','.join(map(str, self.fullOpenPortList))

#         # Vulners nmap scan
#         MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerTop, updateText="Running vulners scan: " + str(self.TargetIP) + "\n\n")

#         self.vulnersScan = nm.scan(self.TargetIP, arguments='-sV --script vulners -p ' + fullOpenPortList)   ######################

#         for port in self.fullOpenPortList:

#                     HTMLheader = "Vulners scan results for port: " + str(port)

#                     try:
#                         script_list = self.vulnersScan['scan'][self.self.TargetIP]["tcp"][port]["script"]["vulners"] + '\n'

#                         element = script_list

#                         MODULES.write2report.append2html(HTMLheader, element)

#                     except KeyError:
#                         pass


# #####################################################################


#         # All scans complete
#         MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerTop, updateText="All targets complete!")

#         # Stop the progress bar
#         self.progressBar.stop()

