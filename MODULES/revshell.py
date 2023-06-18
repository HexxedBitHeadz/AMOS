#!/usr/bin/python3
from tkinter import *
import threading, psutil
import MODULES.functions, MODULES.codeVault


def threadingSetup(self):
    pass


def myCallback(self):

    match self.variableOSWeb.get():


        # If Windows is selected, get Arch value, then create language drop down menu
        case 'Windows':

            self.dropDownArch.config(state=NORMAL)

            if self.variableArch.get() == "x86" or self.variableArch.get() == "x64":
 

                self.dropDownLanguage = OptionMenu(self.canvas, self.variableLanguage, "C", "C#", "nc", "PowerShell", "Python", command=lambda x:myCallback(self))
                self.dropDownLanguage.place(anchor="nw", x=525, y=225)

        # If Unix is selected, get Arch value, then create language drop down menu
        case 'Unix':
            self.dropDownArch.config(state=NORMAL)

            self.dropDownLanguage = OptionMenu(self.canvas, self.variableLanguage, "Awk", "Bash", "nc", "Perl", "Python", "Ruby", command=lambda x:myCallback(self))
            self.dropDownLanguage.place(anchor="nw", x=525, y=225)


        # If Web is selected, set Arch to blank, then disable, then create language drop down menu        
        case 'Web':

            try:
                self.variableArch.set("")
            except SyntaxError:
                pass

            self.dropDownArch.config(state=DISABLED)

            dropDownLanguage = OptionMenu(self.canvas, self.variableLanguage, "asp", "aspx", "java", "JavaScript", "jsp", "war", "NodeJS", "php", command=lambda x:myCallback(self))
            dropDownLanguage.place(anchor="nw", x=525, y=225)

    # List with all user selected options is created
    optionsList = [self.variableMyIP.get(), self.entryLocalPort.get(), self.variableOSWeb.get(), self.variableArch.get(), self.variableLanguage.get()]
    
    # Verifying that all 5 options (4 if Web) have been entered, then enabling the generate button
    if self.variableOSWeb.get() == 'Windows' and len(list(filter(None, optionsList))) == 5:
        self.revShellGenerateButton.configure(state="normal")

    if self.variableOSWeb.get() == 'Unix' and len(list(filter(None, optionsList))) == 5:
        self.revShellGenerateButton.configure(state="normal")  

    if self.variableOSWeb.get() == 'Web' and len(list(filter(None, optionsList))) == 4:
        self.revShellGenerateButton.configure(state="normal")


def generate(self):


    def gtc(dtxt):
        # Function that allows copy to clip board
        MODULES.functions.statusUpdate(self, statusText="Text copied to clipboard")
        self.frameRevShell.clipboard_clear()
        self.frameRevShell.clipboard_append(dtxt)


    def printCode(revshellcode):
        # Delete content in Window if any exists before populating new data
        self.revShellBottomWindow.configure(state="normal")
        self.revShellBottomWindow.delete("1.0", "end") 

        # Make the copy button
        revShellButtons = MODULES.functions.buttonMaker(frameName=self.revShellBottomWindow, text="Click Me to copy!")
        revShellButtons.configure(width=33, command=lambda: gtc(revshellcode))

        # Creating the window and placing in the desired revshell code
        self.revShellBottomWindow.window_create("end", window=revShellButtons)
        self.revShellBottomWindow.insert("end", "\n")
        self.revShellBottomWindow.insert("end", revshellcode)
        self.revShellBottomWindow.configure(state="disabled")




    # Input validation of local, no more than 5 chars.
    if len(self.entryLocalPort.get()) > 1:
        self.entryLocalPort.delete(5, END)

    # Try eliminating the other characters around the IP address
    try:
        listIPs = list(eval(self.variableMyIP.get()))
        listIPs = listIPs[0]

        # Create dictionary of user selected inputs
        dicRevShellVars = {"MyIP": listIPs.split("-")[1], "Local Port": self.entryLocalPort.get(), "OSWeb": self.variableOSWeb.get(), "Arch": self.variableArch.get(), "Language": self.variableLanguage.get()}



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
