#!/usr/bin/python3
from tkinter import *
import threading, psutil
import MODULES.functions, MODULES.codeVault


def threadingSetup(self):
    # Setting up thread for revshell function
    THREADdrawUI = threading.Thread(target=revshell, args=(self, ), daemon=True)
    THREADdrawUI.start()

def revshell(self):

    #Making the genreate button
    self.revShellGenerateButton = MODULES.functions.buttonMaker(frameName=self.frameRevShell, text="Generate!")
    self.revShellGenerateButton.place(anchor="nw", x=725, y=220, width=100, height=50)
    self.revShellGenerateButton.configure(command=lambda:generate(), state="disabled")

    # Left columns labels.
    labelLocalDetails = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="LOCAL DETAILS")
    labelLocalDetails.place(anchor="nw", x=520, y=25)

    labelMyIP = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="My IP:")
    labelMyIP.place(anchor="nw", x=520, y=50)

    labelMyPort = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="Local port:")
    labelMyPort.place(anchor="nw", x=520, y=125)

    # Right columns labels.
    labelTargetDetails = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="TARGET DETAILS")
    labelTargetDetails.place(anchor="nw", x=725, y=25)

    labelTargetType = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="OS / Web")
    labelTargetType.place(anchor="nw", x=725, y=50)
    labelTargetArch = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="Arch:")
    labelTargetArch.place(anchor="nw", x=725, y=125)

    # Entry text box for port number
    entryLocalPort = MODULES.functions.entryBoxes(frameName=self.frameRevShell, _text_="")
    entryLocalPort.place(anchor="nw", width=75, x=520, y=150)

    # Drop down boxes
    dicInterfaces = psutil.net_if_addrs()

    listInterfaces = []
    for interface,IPaddress in dicInterfaces.items():
        listInterfaces.append([interface + "-" + IPaddress[0][1]])

    variableMyIP = StringVar(self.frameRevShell)
    dropDownMyIP = OptionMenu(self.frameRevShell, variableMyIP, *listInterfaces, command=lambda x:myCallback())
    dropDownMyIP.place(anchor="nw", x=520, y=75)

    variableOSWeb = StringVar(self.frameRevShell)
    dropDownOSWeb = OptionMenu(self.frameRevShell, variableOSWeb, "Windows", "Unix", "Web", command=lambda x:myCallback())  #######
    dropDownOSWeb.place(anchor="nw", x=725, y=75)

    variableLanguage = StringVar(self.frameRevShell)
   
    variableArch = StringVar(self.frameRevShell)
    dropDownArch = OptionMenu(self.frameRevShell, variableArch, "x86", "x64", command=lambda x:myCallback())
    dropDownArch.place(anchor="nw", x=725, y=150)
    dropDownArch.config(state=DISABLED)


    def myCallback():

        match variableOSWeb.get():
 
            ######## HOW TO CLEAR / RESET DROP DOWN LANGUAGE WHEN SWITCHING OS'S?????????????

            # If Windows is selected, get Arch value, then create language drop down menu
            case 'Windows':
                dropDownArch.config(state=NORMAL)

                if variableArch.get() == "x86" or variableArch.get() == "x64":
                    
                    labelLanguage = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="Language:")
                    labelLanguage.place(anchor="nw", x=520, y=200)

                    dropDownLanguage = OptionMenu(self.frameRevShell, variableLanguage, "C", "C#", "nc", "PowerShell", "Python", command=lambda x:myCallback())
                    dropDownLanguage.place(anchor="nw", x=525, y=225)
 

            # If Unix is selected, get Arch value, then create language drop down menu
            case 'Unix':
                dropDownArch.config(state=NORMAL)

                if variableArch.get() == "x86" or variableArch.get() == "x64":
                    
                    labelLanguage = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="Language:")
                    labelLanguage.place(anchor="nw", x=520, y=200)

                    dropDownLanguage = OptionMenu(self.frameRevShell, variableLanguage, "Awk", "Bash", "nc", "Perl", "Python", "Ruby", command=lambda x:myCallback())
                    dropDownLanguage.place(anchor="nw", x=525, y=225)


            # If Web is selected, set Arch to blank, then disable, then create language drop down menu        
            case 'Web':

                try:
                    variableArch.set("")
                except SyntaxError:
                    pass

                dropDownArch.config(state=DISABLED)

                labelLanguage = MODULES.functions.labelMaker(frameName=self.frameRevShell, text="Language:")
                labelLanguage.place(anchor="nw", x=520, y=200)

                dropDownLanguage = OptionMenu(self.frameRevShell, variableLanguage, "asp", "aspx", "java", "JavaScript", "jsp", "war", "NodeJS", "php", command=lambda x:myCallback())
                dropDownLanguage.place(anchor="nw", x=525, y=225)

        # List with all user selected options is created
        optionsList = [variableMyIP.get(), entryLocalPort.get(), variableOSWeb.get(), variableArch.get(), variableLanguage.get()]
        
        # Verifying that all 5 options (4 if Web) have been entered, then enabling the generate button
        if variableOSWeb.get() == 'Windows' and len(list(filter(None, optionsList))) == 5:
            self.revShellGenerateButton.configure(state="normal")

        if variableOSWeb.get() == 'Unix' and len(list(filter(None, optionsList))) == 5:
            self.revShellGenerateButton.configure(state="normal")  

        if variableOSWeb.get() == 'Web' and len(list(filter(None, optionsList))) == 4:
            self.revShellGenerateButton.configure(state="normal")

    # Placing window
    self.revShellBottomWindow = MODULES.functions.windowMaker(frameName=self.frameRevShell)
    self.revShellBottomWindow.place(anchor="nw", height=260, width=325, x=525, y=300)

    def generate():
    

        # Input validation of local, no more than 5 chars.
        if len(entryLocalPort.get()) > 1:
            entryLocalPort.delete(5, END)

        # Try eliminating the other characters around the IP address
        try:
            listIPs = list(eval(variableMyIP.get()))
            listIPs = listIPs[0]

            # Create dictionary of user selected inputs
            dicRevShellVars = {"MyIP": listIPs.split("-")[1], "Local Port": entryLocalPort.get(), "OSWeb": variableOSWeb.get(), "Arch": variableArch.get(), "Language": variableLanguage.get()}

            #print(dicRevShellVars)

        except SyntaxError:
            pass


        # Match code to take the user inputs and display the correct results
        match dicRevShellVars['OSWeb']:
            case 'Windows':
                match dicRevShellVars['Arch']:
                    case 'x86':
                        pass
                    case 'x64':
                        pass
                match dicRevShellVars['Language']:
                    case 'C':
                        printCode(MODULES.codeVault.windowsC(dicRevShellVars))
                    case 'C#':
                        printCode(MODULES.codeVault.windowsCSharp(dicRevShellVars))
                    case 'nc':
                        printCode(MODULES.codeVault.windowsnc(dicRevShellVars))
                    case 'PowerShell':
                        printCode(MODULES.codeVault.windowsPS_1(dicRevShellVars))
                    case 'Python':
                        printCode(MODULES.codeVault.windowsPython(dicRevShellVars))
            
            case 'Unix':
                match dicRevShellVars['Arch']:
                    case 'x86':
                        pass
                    case 'x64':
                        pass
                match dicRevShellVars['Language']:
                    case 'Awk':
                        printCode(MODULES.codeVault.unixAwk(dicRevShellVars))
                    case 'Bash':
                        printCode(MODULES.codeVault.unixBash(dicRevShellVars))
                    case 'nc':
                        printCode(MODULES.codeVault.unixnc(dicRevShellVars))
                    case 'Perl':
                        printCode(MODULES.codeVault.unixPerl(dicRevShellVars))
                    case 'Python':
                        printCode(MODULES.codeVault.unixPython(dicRevShellVars))
                    case 'Ruby':
                        printCode(MODULES.codeVault.unixRuby(dicRevShellVars))

            case 'Web':

                match dicRevShellVars['Language']:
                    case 'asp':
                        printCode(MODULES.codeVault.webASP(dicRevShellVars))
                    case 'aspx':
                        printCode(MODULES.codeVault.webASPX(dicRevShellVars))
                    case 'java':
                        printCode(MODULES.codeVault.webJava(dicRevShellVars))
                    case 'JavaScript':
                        printCode(MODULES.codeVault.webJavaScript(dicRevShellVars))
                    case 'jsp':
                        printCode(MODULES.codeVault.webJSP(dicRevShellVars))
                    case 'war':
                        printCode(MODULES.codeVault.webWar(dicRevShellVars))
                    case 'NodeJS':
                        printCode(MODULES.codeVault.webNodeJS(dicRevShellVars))
                    case 'php':
                        printCode(MODULES.codeVault.webPHP(dicRevShellVars))

    def gtc(dtxt):
        # Function that allows copy to clip board
        MODULES.functions.statusUpdate(self, statusText="Text copied to clipboard")
        self.frameRevShell.clipboard_clear()
        self.frameRevShell.clipboard_append(dtxt)
       
                    
    def printCode(revShellCode):

        # Delete content in Window if any exists before populating new data
        self.revShellBottomWindow.configure(state="normal")
        self.revShellBottomWindow.delete(1.0,END)

        # Make the copy button
        revShellButtons = MODULES.functions.buttonMaker(frameName=self.revShellBottomWindow, text="Click Me to copy!")
        revShellButtons.configure(width=33, command=lambda: gtc(revShellCode))

        # Creating the window and placing in the desired revshell code
        self.revShellBottomWindow.window_create("end", window=revShellButtons)
        self.revShellBottomWindow.insert("end", "\n")
        self.revShellBottomWindow.insert("end", revShellCode)
        self.revShellBottomWindow.configure(state="disabled")

