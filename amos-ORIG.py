#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

from PIL import Image, ImageTk

import re, os

# Import all modules from MODULES folder
for module in os.listdir("./MODULES"):
    if module.endswith(".py"):
        exec("import MODULES." + module[:-3])

topLevelAmos = Tk()
topLevelAmos.title("Amos v1.0")
topLevelAmos.geometry("900x600")
topLevelAmos.configure(background="black")
topLevelAmos.resizable(False, False)

class AmosApp(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        # Get current working directory
        self.amosDir = os.getcwd()
        # get current user name
        self.userName = os.getlogin()

        # Getting permission values of current user.  This is because we run amos as sudo, we then change the results permission to current user for easy viewing
        self.uid = os.stat(self.amosDir).st_uid
        self.gid = os.stat(self.amosDir).st_gid


        # Adding file menu sctructure
        self.menubar = Menu(master=topLevelAmos)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="About", command=lambda:aboutHeBi(self))
        filemenu.add_command(label="Donate", command=lambda:donate(self))

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda:exit())
        
        self.menubar.add_cascade(label="File", menu=filemenu)
        topLevelAmos.config(menu=self.menubar)


        # build notebook
        self.notebookAmos = ttk.Notebook(topLevelAmos)
        self.notebookAmos.pack(fill=BOTH, expand=YES)

        
        # Generate frames for each tab
        self.frameScanner = MODULES.functions.frameMaker(self, text="Scanner")
        self.frameBrute = MODULES.functions.frameMaker(self, text="Brute")
        self.frameHTTP = MODULES.functions.frameMaker(self, text="HTTP")
        self.frameRevShell = MODULES.functions.frameMaker(self, text="RevShell")
        self.framePrivEsc = MODULES.functions.frameMaker(self, text="PrivEsc")
        self.frameTools = MODULES.functions.frameMaker(self, text="Tools")


        # Generate background image
        self.image = Image.open(self.amosDir + "/IMAGES/AmosBackgroundGreen.png")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)



        # Generate background image container for every self.frame
        self.backgroundScanner = Label(self.frameScanner, image=self.background_image)
        self.backgroundScanner.pack(fill=BOTH, expand=YES)
        self.backgroundScanner.bind('<Configure>', self._resize_image)

        self.backgroundBrute = Label(self.frameBrute, image=self.background_image)
        self.backgroundBrute.pack(fill=BOTH, expand=YES)
        self.backgroundBrute.bind('<Configure>', self._resize_image)

        self.backgroundHTTP = Label(self.frameHTTP, image=self.background_image)
        self.backgroundHTTP.pack(fill=BOTH, expand=YES)
        self.backgroundHTTP.bind('<Configure>', self._resize_image)

        self.backgroundRevShell = Label(self.frameRevShell, image=self.background_image)
        self.backgroundRevShell.pack(fill=BOTH, expand=YES)
        self.backgroundRevShell.bind('<Configure>', self._resize_image)

        self.backgroundPrivEsc = Label(self.framePrivEsc, image=self.background_image)
        self.backgroundPrivEsc.pack(fill=BOTH, expand=YES)
        self.backgroundPrivEsc.bind('<Configure>', self._resize_image)

        self.backgroundPrivTools = Label(self.frameTools, image=self.background_image)
        self.backgroundPrivTools.pack(fill=BOTH, expand=YES)
        self.backgroundPrivTools.bind('<Configure>', self._resize_image)



        # Begin running tabs UI
        MODULES.HTTPtools.threadingSetup(self)
        MODULES.revshell.threadingSetup(self)
        MODULES.privEsc.threadingSetup(self)
        MODULES.tools.threadingSetup(self)

        # Genreate an entrybox for the user to enter a target
        self.entryTargetName = MODULES.functions.entryBoxes(frameName=topLevelAmos, _text_="")
        self.entryTargetName.place(x=95, y=95, width=125, height=25)

        # Generate an entrybox for the user to enter a target IP
        self.entryTargetIP = MODULES.functions.entryBoxes(frameName=topLevelAmos, _text_="")
        self.entryTargetIP.place(x=240, y=95, width=125, height=25)

        # Generate the scan button
        self.scanButton = MODULES.functions.buttonMaker(frameName=topLevelAmos, text="Scan")
        self.scanButton.place(x=285, y=535, width=100)
        self.scanButton.configure(command=self.nmapScan)

        # Making the scanner top window
        self.scrollWindowScannerTop = MODULES.functions.windowMaker(frameName=self.frameScanner)
        self.scrollWindowScannerTop.place(x=525, y=40, width=325, height=325)

        # Making the scanner bottom window
        self.scrollWindowScannerBottom = MODULES.functions.windowMaker(frameName=self.frameScanner)
        self.scrollWindowScannerBottom.place(x=525, y=380, width=325, height=150)

        # Making progress bar, pass self.topLevelAmos so we can place it
        self.progressBar = MODULES.functions.progressBarMaker(self, frameName=topLevelAmos)

        # Making check box for vuln scan
        self.checkBoxVulners = MODULES.functions.checkBoxMaker(frameName=topLevelAmos, text='Disable Vuln scan')
        self.checkBoxVulners.place(x=285, y=510)


        # Greetings banner
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Welcome to Amos!\n\nWARNING:  This tool is used for research purposes, and not intended to be used in any unauthorized way!  We do not recommend using this on exam environments to ensure authorized guidance and resources.\n\nTo get started, simply insert the target name (not required) & Target IP (required) and hit scan. Results can found in:\n\n/home/" + self.userName + "/Documents/\n\nIf no target name was provided, the IP address will be used in it's place.")


        # Making the brute top window
        self.scrollWindowbruteTop = MODULES.functions.windowMaker(frameName=self.frameBrute)
        self.scrollWindowbruteTop.place(x=525, y=40, width=325, height=325)


        # Making the brute bottom window
        self.scrollWindowBruteBottom = MODULES.functions.windowMaker(frameName=self.frameBrute)
        self.scrollWindowBruteBottom.place(x=525, y=380, width=325, height=150)

        self.mainwindow = topLevelAmos

        # Run topLevelAmos in mainloop
        # Continue to show img_HeBi until topLevelAmos is closed

        self.mainwindow.mainloop()
#        self.mainwindow.after(1000, self.mainwindow.destroy)
        
           

    # def run(self):
    #     self.mainwindow.mainloop()


    def _resize_image(self,event):

        # Resize the image to fit the window

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.backgroundScanner.configure(image =  self.background_image)
        self.backgroundBrute.configure(image =  self.background_image)
        self.backgroundHTTP.configure(image =  self.background_image)
        self.backgroundRevShell.configure(image =  self.background_image)
        self.backgroundPrivEsc.configure(image =  self.background_image)
        self.backgroundPrivTools.configure(image =  self.background_image)


    def nmapScan(self):
        # Check to see if self.entryTargetIP is a single or multiple valid ip address
        if re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", self.entryTargetIP.get()):    
            pass
        else:
            MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Invalid IP address")
            return
        
        # Verify that entryTargetName is 30 characters or less
        if len(self.entryTargetName.get()) > 30:
            MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Target name is too long!")
            self.topLevelAmos.mainloop()
        else:
            pass

         # start progress bar
        self.progressBar.start(15)
        self.scanButton.config(state=DISABLED)
        self.scrollWindowScannerTop.config(state=DISABLED)
        self.checkBoxVulners.config(state=DISABLED)


        # IF checkbox is ticked for vulners, include vulners scan
        if 'selected' in self.checkBoxVulners.state():
            self.skipVulners = True
        else:
            self.skipVulners = False
        
        
        MODULES.Scanning.preScan(self)


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



app = AmosApp(topLevelAmos)
app.pack(fill=BOTH, expand=YES)




