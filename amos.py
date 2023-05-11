#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import MODULES.Scanning, MODULES.Enumeration, MODULES.revshell, MODULES.privEsc, MODULES.tools, MODULES.functions, MODULES.MultipleIPs, MODULES.HTTPtools
from tkinter import *
import re, os

skipVulners = False

class AmosApp:
    def __init__(self, master=None):

        # Assiging variables to path of amos and current user
        self.amosDir = os.getcwd()
        self.userName = os.getlogin()

        # Getting permission values of current user.  This is because we run amos as sudo, we then change the results permission to current user for easy viewing
        self.uid = os.stat(self.amosDir).st_uid
        self.gid = os.stat(self.amosDir).st_gid

        # build ui
        self.topLevelAmos = tk.Tk() if master is None else tk.Toplevel(master)
        self.topLevelAmos.title("Amos")
        self.topLevelAmos.configure(height=200, width=200)
        self.topLevelAmos.resizable(False, False)
        
        # Adding file menu sctructure
        self.menubar = Menu(master=self.topLevelAmos)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="About", command=lambda:aboutHeBi(self))
        filemenu.add_command(label="Donate", command=lambda:donate(self))
        
        self.menubar.add_cascade(label="File", menu=filemenu)
        self.topLevelAmos.config(menu=self.menubar)

        # build notebook
        self.notebookAmos = ttk.Notebook(self.topLevelAmos)
        self.notebookAmos.configure(height=600, width=900)
        self.notebookAmos.pack(side="top")

        # building frames
        self.frameScanner = MODULES.functions.frameMaker(self, text="Scanner")
        self.frameBrute = MODULES.functions.frameMaker(self, text="Brute")
        self.frameHTTP = MODULES.functions.frameMaker(self, text="HTTP")
        self.frameRevShell = MODULES.functions.frameMaker(self,text="Rev Shells")
        self.framePrivEsc = MODULES.functions.frameMaker(self, text="Priv Esc")    
        self.frameTools = MODULES.functions.frameMaker(self, text="Tools")
       
        ############# PRINTING TAB NAMES #################
        # print(self.notebookAmos.tab(self.frameScanner)['text'])
        # print(self.notebookAmos.tab(self.frameBrute)['text'])
        # print(self.notebookAmos.tab(self.frameRevShell)['text'])
        # print(self.notebookAmos.tab(self.framePrivEsc)['text'])
        # print(self.notebookAmos.tab(self.frameTools)['text'])
        ############# PRINTING TAB NAMES #################


        # Disabling the Brute tab until valid results are found from scanning
        self.notebookAmos.tab(self.frameBrute, state="disabled")

        # Applying the HexxedBitHeadz background wallpaper
        img_HeBi= tk.PhotoImage(file="./IMAGES/AmosBackgroundGreen.png")

        ttk.Label(self.frameScanner, image=img_HeBi).pack()
        ttk.Label(self.frameBrute, image=img_HeBi).pack()
        ttk.Label(self.frameHTTP, image=img_HeBi).pack()
        ttk.Label(self.frameRevShell, image=img_HeBi).pack()
        ttk.Label(self.framePrivEsc, image=img_HeBi).pack()
        ttk.Label(self.frameTools, image=img_HeBi).pack()

        # Begin running tabs UI
        MODULES.HTTPtools.threadingSetup(self)
        MODULES.revshell.threadingSetup(self)
        MODULES.privEsc.threadingSetup(self)
        MODULES.tools.threadingSetup(self)

        # Creating the entry box for target name
        self.entryTargetName = MODULES.functions.entryBoxes(frameName=self.topLevelAmos, _text_="")
        self.entryTargetName.place(anchor="nw", width=125, x=95, y=95)

        # Creating the entry box for target IP
        self.entryTargetIP = MODULES.functions.entryBoxes(frameName=self.topLevelAmos, _text_="")                                                          
        self.entryTargetIP.place(anchor="nw", width=125, x=240, y=95)

        # Making the scan button
        self.scanButton = MODULES.functions.buttonMaker(frameName=self.frameScanner, text="Scan")
        self.scanButton.place(anchor="nw", x=285, y=550)
        self.scanButton.configure(command=self.nmapScan, width=5)

        # Making the scanner top window
        self.scrollWindowScannerTop = MODULES.functions.windowMaker(frameName=self.frameScanner)
        self.scrollWindowScannerTop.place(anchor="nw", height=325, width=325, x=525, y=40)

        # Making the scanner bottom window
        self.scrollWindowScannerBottom = MODULES.functions.windowMaker(frameName=self.frameScanner)
        self.scrollWindowScannerBottom.place(anchor="nw", height=150, width=325, x=525, y=380)

        # Making progress bar
        self.progressBar = MODULES.functions.progressBarMaker(self) 
        self.progressBar.place(anchor="nw", x=20, y=585)

        # Making check box for UDP scan    ######################### Disabling this feature 
        # self.checkBoxUDP = MODULES.functions.checkBoxMaker(frameName=self.frameScanner, text="Disable UDP scan")
        # self.checkBoxUDP.place(anchor="nw", x=285, y=480)

        # Making check box for vuln scan
        self.checkBoxVulners = MODULES.functions.checkBoxMaker(frameName=self.frameScanner, text='Disable Vuln scan')      
        self.checkBoxVulners.place(anchor="nw", x=285, y=510)

        # Greetings banner
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Welcome to Amos!\n\nWARNING:  This tool is used for research purposes, and not intended to be used in any unauthorized way!  We do not recommend using this on exam environments to ensure authorized guidance and resources.\n\nTo get started, simply insert the target name (not required) & Target IP (required) and hit scan. Results can found in:\n\n/home/" + self.userName + "/Documents/\n\nIf no target name was provided, the IP address will be used in it's place.")

        # Making the brute top window
        self.scrollWindowbruteTop = MODULES.functions.windowMaker(frameName=self.frameBrute)
        self.scrollWindowbruteTop.place(anchor="nw", height=325, width=325, x=525, y=40)

        # Making the brute bottom window
        self.scrollWindowBruteBottom = MODULES.functions.windowMaker(frameName=self.frameBrute)
        self.scrollWindowBruteBottom.place(anchor="nw", height=150, width=325, x=525, y=380)

        # Main widget
        self.mainwindow = self.topLevelAmos

        self.topLevelAmos.mainloop()
        
    def run(self):
        self.mainwindow.mainloop()

    def nmapScan(self):

        # Input validation of IP addresses, multiple can be entered, comma seperator, NO SPACES:
        # 192.168.1.1,255.255.255.255,10.10.10.10,0.0.0.0
        ipv4_pattern = "^(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),)*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        

        # IF we get an IP match, check to see if only 1 IP, or multiple
        if re.match(ipv4_pattern, str(self.entryTargetIP.get())):

            mulipleIPs = []

            for ipAddr in self.entryTargetIP.get().split(","):
                mulipleIPs.append(ipAddr)

            #IF multiple IPs, run code specific for situation
            if len(mulipleIPs) > 1:
                MODULES.MultipleIPs.mulitpleIPFunction(self, mulipleIPs)
                self.scanButton.configure(state="disabled")  
                self.scrollWindowScannerTop.config(state="disabled")
                self.checkBoxVulners.config(state="disabled")
                #self.checkBoxUDP.config(state="disabled")
                self.topLevelAmos.mainloop()
            
            # IF NOT multiple IPs, pass and run code as normal
            if len(mulipleIPs) <= 1:
                pass
        
        # IF NO IPs are found, provide error message to user, run UI
        else:
            MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Invalid IP input!")
            self.topLevelAmos.mainloop()

        
        # Input validation of Target name, no more than 30 chars.
        if len(self.entryTargetName.get()) > 1:
            self.entryTargetName.delete(30, END)

        # Start progress bar, disable any modifiable options while running
        self.progressBar.start(15)
        self.scanButton.configure(state="disabled")  
        self.scrollWindowScannerTop.config(state="disabled")
        self.checkBoxVulners.config(state="disabled")
        # self.checkBoxUDP.config(state="disabled")

        # IF checkbox is ticked for vulners, include vulners scan
        if 'selected' in self.checkBoxVulners.state():
            self.skipVulners = True
        else:
            self.skipVulners = False
        
        
        MODULES.Scanning.preScan(self)
        

    # def disableUDP(self):   ########################## Disabled 
        
        # if 'selected' in self.checkBoxUDP.state():
        #     self.skipUDP = True
        # else:
        #     self.skipUDP = False


def aboutHeBi(self):
    # Disable file menu
    self.menubar.entryconfig(1, state="disabled")

    # Runs the about window code
    aboutWindow = MODULES.functions.popOutWindow(frameName=None, text="About Hexxed BitHeadz")
    aboutWindow.geometry("500x500")

    # Contents of about window
    aboutLabel = MODULES.functions.labelMaker(frameName=aboutWindow, text="AMOS is developed and maintained by Hexxed BitHeadz, just a few cyber fanatics exploring the digital world in our own creative ways.  Feel free to reach out to us at HexxedBitHeadz@gmail.com")

    aboutLabel.place(x=30, y=10)
    aboutLabel.configure(wraplength=450, justify="left")

    # Setting the about page image
    img_HeBiWallpaper = tk.PhotoImage(file=self.amosDir + "/IMAGES/HeBiWallpaper.png")
    panel = Label(aboutWindow, image=img_HeBiWallpaper)
    panel.photo = img_HeBiWallpaper
    panel.place(x=50, y=75)

    # When closing the aboutWindow, enable the update button again
    aboutWindow.protocol("WM_DELETE_WINDOW", lambda: onclose(self, aboutWindow))

    def onclose(self, credsWindow):
        aboutWindow.destroy()
        self.menubar.entryconfig(1, state="normal")


def donate(self):

    # Disable file menu
    self.menubar.entryconfig(1, state="disabled")

    # Runs the donate window code
    donationWindow = MODULES.functions.popOutWindow(frameName=None, text="Donations")
    donationWindow.geometry("500x600")
    
    # QR code image
    img_QRCode = tk.PhotoImage(file=self.amosDir + "/IMAGES/QRCode.png")
    panel = Label(donationWindow, image=img_QRCode)
    panel.photo = img_QRCode
    panel.place(x=10, y=10)


    # tee 1 image
    tee_1 = tk.PhotoImage(file=self.amosDir + "/IMAGES/tee_1.png")
    panel = Label(donationWindow, image=tee_1)
    panel.photo = tee_1
    panel.place(x=20, y=375)

    # # tee 2 image
    tee_2 = tk.PhotoImage(file=self.amosDir + "/IMAGES/tee_2.png")
    panel = Label(donationWindow, image=tee_2)
    panel.photo = tee_2
    panel.place(x=275, y=375)

    # Payplay donate link and button
    donateLink = '''https://www.paypal.com/donate/?business=5MX6P8YU3CNBY&no_recurring=0&item_name=This+donation+goes+to+furthering+cyber+research+and+tools+provided+by+Hexxed+BitHeadz.&currency_code=USD'''

    donateButton = MODULES.functions.buttonMaker(frameName=donationWindow, text="Copy link to clipboard")
    donateButton.configure(command=lambda: gtc(self, donateLink))
    donateButton.place(x=10, y=275)

    # Donate summary 
    donateSummary = MODULES.functions.labelMaker(frameName=donationWindow, text="Your donation contributes to the research and development projects from Hexxed BitHeadz.  \n\nWith this, we keep our coffee cups full, the monitors running, and the developoment going!\n\nThank you for checking out Amos, our introductory contribution to Cyber.\n\nIn the US?  Donate $30 or more and receive a Hexxed BitHeadz tee!  We'll contact you after payment to discuss request size and name to be printed.")
    donateSummary.place(x=275, y=10)
    donateSummary.configure(wraplength=220, justify="left")

    def gtc(self, dtxt):
        # This code is needed to properly copy to clipboard
        self.topLevelAmos.clipboard_clear()
        self.topLevelAmos.clipboard_append(dtxt)

        # Copy to clipboard label confirmation
        labelCopyUpdate=tk.Label(donationWindow, text="Link copied to clipboard!", background="black", foreground="#64d86b")
        labelCopyUpdate.place(anchor="nw", x=10, y=325)


    # When closing the donationWindow, enable the update button again
    donationWindow.protocol("WM_DELETE_WINDOW", lambda: onclose(self, donationWindow))

    def onclose(self, credsWindow):
        donationWindow.destroy()
        self.menubar.entryconfig(1, state="normal")

if __name__ == "__main__":
    app = AmosApp()
    app.run()

