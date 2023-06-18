from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os, re, psutil

import MODULES.HTTPtools

# Import all modules from MODULES folder
for module in os.listdir("./MODULES"):
    if module.endswith(".py"):
        exec("import MODULES." + module[:-3])


root = Tk()
root.title("Amos v1.1.1")
root.geometry("900x600")
root.configure(background="black")
root.resizable(False, False)


class Amos(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        # Get current working directory
        self.amosDir = os.getcwd()
        # get current user name
        self.userName = os.getlogin()

        # Getting permission values of current user.  This is because we run amos as sudo, we then change the results permission to current user for easy viewing
        self.uid = os.stat(self.amosDir).st_uid
        self.gid = os.stat(self.amosDir).st_gid

        # Create the menu bar
        self.menu_bar = Menu(root)
        root.config(menu=self.menu_bar)

        # Create the file menu
        file_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Add options to the file menu
        file_menu.add_command(label="About", command=lambda:aboutHeBi(self))
        file_menu.add_command(label="Donate", command=lambda:donate(self))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=exit_program)



        self.image = Image.open(self.amosDir + "/IMAGES/AmosBackgroundGreen.png")  # Updated image file name
        self.background_image = ImageTk.PhotoImage(self.image)

        self.notebookAmos = ttk.Notebook(self, width=900, height=100)
        self.notebookAmos.pack(expand=1, fill="both")

        # Create the first tab
        self.frameScanner = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.frameScanner, text="Scanner")

        # Create the second tab
        self.frameBrute = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.frameBrute, text="Brute")

        self.frameHTTP = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.frameHTTP, text="HTTP")

        self.frameRevShell = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.frameRevShell, text="RevShell")

        self.framePrivEsc = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.framePrivEsc, text="PrivEsc")

        self.frameTools = Frame(self.notebookAmos, bg="")
        self.notebookAmos.add(self.frameTools, text="Tools")

        # Create canvas for the background image
        self.canvas = Canvas(root, highlightthickness=0, background="black")
        self.canvas.place(x=0, y=25, relwidth=1, relheight=1)
        self.canvas.bind('<Configure>', self._resize_image)

        self.entries = {
            self.frameScanner: [],
            self.frameBrute: [],
            self.frameHTTP: [],
            self.frameRevShell: [],
            self.framePrivEsc: [],
            self.frameTools: []
        }

        self.notebookAmos.tab(self.frameBrute, state="disabled")

        self.notebookAmos.bind("<<NotebookTabChanged>>", self.update_entries)

        self.create_disable_checkboxs()
        self.create_scan_button()
        self.create_progress_bar()

        self.entry_values = {}  # Dictionary to store entry values

        self.entryTargetName = Entry(self.canvas, bg="white", fg="black")
        self.entryTargetName.place(x=95, y=75, width=125, height=25)

        self.entryTargetIP = Entry(self.canvas, bg="white", fg="black")
        self.entryTargetIP.place(x=240, y=75, width=125, height=25)

        self.scrolled_textScannerTop = ScrolledText(self.canvas, background="#000008", foreground="#64d86b",
                                        state="disabled", wrap="word")

        self.scrolled_textScannerBottom = ScrolledText(self.canvas, background="#000008", foreground="#64d86b",
                                        state="disabled", wrap="word")

        self.scrolled_textBruteTop = ScrolledText(self.canvas, background="#000008", foreground="#64d86b",
                                        state="disabled", wrap="word")
  
        self.scrolled_textBruteBottom = ScrolledText(self.canvas, background="#000008", foreground="#64d86b",
                                        state="disabled", wrap="word")

        self.entryWebPort = MODULES.functions.entryBoxes(frameName=self.canvas, _text_="80")

        self.httpWindow = MODULES.functions.windowMaker(frameName=self.canvas)

        self.linkExtractPort = MODULES.functions.labelMaker(frameName=self.canvas, text="Enter port #:")

        self.linkExtract = MODULES.functions.labelMaker(frameName=self.canvas, text="Web Extractor")

        self.linkDirBust = MODULES.functions.labelMaker(frameName=self.canvas, text="Directory Buster")

        self.linkExtractButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Start")

        self.dirBustButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Start")

        self.enumButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Enumeration")

        self.bruteButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="brute em!")

        self.credsButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Update creds")

        self.revShellGenerateButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Generate!")     

        self.revShellGenerateButton.configure(command=lambda:MODULES.revshell.generate(self))        

        
        self.labelLocalDetails = MODULES.functions.labelMaker(frameName=self.canvas, text="LOCAL DETAILS")       

        self.labelMyIP = MODULES.functions.labelMaker(frameName=self.canvas, text="My IP:") 
        
        self.labelMyPort = MODULES.functions.labelMaker(frameName=self.canvas, text="Local port:")

        self.labelTargetDetails = MODULES.functions.labelMaker(frameName=self.canvas, text="TARGET DETAILS")
    
        self.labelTargetType = MODULES.functions.labelMaker(frameName=self.canvas, text="OS / Web")

        self.labelTargetArch = MODULES.functions.labelMaker(frameName=self.canvas, text="Arch:")

        self.entryLocalPort = MODULES.functions.entryBoxes(frameName=self.canvas, _text_="")

        self.revShellBottomWindow = MODULES.functions.windowMaker(frameName=self.canvas)

     



        # Drop down boxes
        dicInterfaces = psutil.net_if_addrs()

        listInterfaces = []
        for interface,IPaddress in dicInterfaces.items():
            listInterfaces.append([interface + "-" + IPaddress[0][1]])

        self.variableMyIP = StringVar(self.canvas)

        self.dropDownMyIP = OptionMenu(self.canvas, self.variableMyIP, *listInterfaces, command=lambda x:MODULES.revshell.myCallback(self))


        self.variableOSWeb = StringVar(self.canvas)

        self.dropDownOSWeb = OptionMenu(self.canvas, self.variableOSWeb, "Windows", "Unix", "Web", command=lambda x:MODULES.revshell.myCallback(self))

        self.variableLanguage = StringVar(self.canvas)
    
        self.variableArch = StringVar(self.canvas)

        self.dropDownArch = OptionMenu(self.canvas, self.variableArch, "x86", "x64", command=lambda x:MODULES.revshell.myCallback(self))
       
        self.dropDownArch.config(state=DISABLED)     
        
        self.privEscWindow = MODULES.functions.windowMaker(frameName=self.canvas)

        self.labelTargetTypeOS = tk.Label(self.canvas, text="OS", background="black", foreground="#64d86b")

        self.variableOS = StringVar(self.canvas)
        self.dropDownOS = OptionMenu(self.canvas, self.variableOS, "Windows", "Unix", command=lambda x:MODULES.privEsc.myCallback(self))

        self.labelTargetTypeSection = tk.Label(self.canvas, text="Section", background="black", foreground="#64d86b")

        self.variableSection = StringVar(self.canvas)
        self.dropDownSection = OptionMenu(self.canvas, self.variableSection, "User", "Network", "System", command=lambda x:MODULES.privEsc.myCallback(self))

#####################################

        self.labelLanguage = MODULES.functions.labelMaker(frameName=self.canvas, text="Language:")
        self.dropDownLanguage = OptionMenu(self.canvas, self.variableLanguage, "", command=lambda x:MODULES.revshell.myCallback(self))
        

#####################################


        self.toolsWindow = MODULES.functions.windowMaker(frameName=self.canvas)
        
        self.HTTPServer = MODULES.functions.labelMaker(frameName=self.canvas, text="HTTP Server")
        
        self.mailServer = MODULES.functions.labelMaker(frameName=self.canvas, text="Mail Server")
        
        self.FTPServer = MODULES.functions.labelMaker(frameName=self.canvas, text="FTP Server")
        
        self.HTTPStartButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Start")

        self.HTTPStartButton.config(width=1, command=lambda:MODULES.tools.enableService(self, service="HTTP"))
        
        self.HTTPStopButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Stop")

        self.HTTPStopButton.config(width=1, command=lambda:MODULES.tools.disableService(self, service="HTTP"))
        self.HTTPStopButton.config(state="disabled")

        self.MailStartButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Start")
        self.MailStartButton.config(width=1, command=lambda:MODULES.tools.enableService(self, service="Mail"))

        self.MailStopButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Stop")
        
        self.MailStopButton.config(width=1, command=lambda:MODULES.tools.disableService(self, service="Mail"))
        self.MailStopButton.config(state="disabled")

        self.FTPStartButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Start")
        self.FTPStartButton.config(width=1, command=lambda:MODULES.tools.enableService(self, service="FTP"))

        self.FTPStopButton = MODULES.functions.buttonMaker(frameName=self.canvas, text="Stop")    
        self.FTPStopButton.config(width=1, command=lambda:MODULES.tools.disableService(self, service="FTP"))
        self.FTPStopButton.config(state="disabled")

        self.enumButton.configure(state="disabled")

        self.linkExtractButton.config(width=1, command=lambda:MODULES.HTTPtools.functionlinkExtract(self))

        self.dirBustButton.config(width=1, command=lambda:MODULES.HTTPtools.fileSelect(self))
        
        
        # Greetings banner
        MODULES.functions.topWindowUpdate(window=self.scrolled_textScannerTop, updateText="Welcome to Amos!\n\nWARNING:  This tool is used for research purposes, and not intended to be used in any unauthorized way!  We do not recommend using this on exam environments to ensure authorized guidance and resources.\n\nTo get started, simply insert the target name (not required) & Target IP (required) and hit scan. Results can found in:\n\n/home/" + self.userName + "/Documents/\n\nIf no target name was provided, the IP address will be used in it's place.")
        
        # Begin running tabs UI
        MODULES.HTTPtools.threadingSetup(self)
        MODULES.revshell.threadingSetup(self)
        MODULES.privEsc.threadingSetup(self)
        MODULES.tools.threadingSetup(self)

    def create_disable_checkboxs(self):
        self.checkbox_var = BooleanVar()
        self.checkbox = Checkbutton(self.canvas, text="Disable Vulners scan", variable=self.checkbox_var, bg="black", fg="red")
        self.checkbox.place(x=280, y=450)

    def create_scan_button(self):
        self.scan_button = Button(self.canvas, text="Scan", bg="#008f11", fg="black", command=self.perform_scan)
        self.scan_button.place(x=280, y=500, width=100, height=50)

    def create_progress_bar(self):
        self.progress_bar = ttk.Progressbar(self.canvas, orient="horizontal", length=100, mode="indeterminate")
        self.progress_bar.place(x=20, y=530)

    def update_entries(self, event):
        selected_tab = self.notebookAmos.select()
        self.current_frame = self.notebookAmos.tab(self.notebookAmos.select(), "text")



        # If scanner is the current tab, show the ScrolledText widgets
        if str(self.current_frame) == "Scanner":
            self.scrolled_textScannerTop.place(x=525, y=10, width=325, height=325)
            self.scrolled_textScannerBottom.place(x=525, y=350, width=325, height=150)
            self.enumButton.place(anchor="nw", x=525, y=510)
        else:
            self.scrolled_textScannerTop.place_forget()
            self.scrolled_textScannerBottom.place_forget()
            self.enumButton.place_forget()

        # If scanner is the current tab, show the ScrolledText widgets
        if str(self.current_frame) == "Brute":
            self.scrolled_textBruteTop.place(x=525, y=10, width=325, height=325)
            self.scrolled_textBruteBottom.place(x=525, y=350, width=325, height=150)
            self.bruteButton.place(anchor="nw", x=525, y=530)
            self.credsButton.place(anchor="nw", x=700, y=530)
        else:
            self.scrolled_textBruteTop.place_forget()
            self.scrolled_textBruteBottom.place_forget()
            self.bruteButton.place_forget()
            self.credsButton.place_forget()


        if str(self.current_frame) == "HTTP":
            self.entryWebPort.place(anchor="nw", width=75, x=625, y=10)
            self.httpWindow.place(anchor="nw", height=150, width=325, x=525, y=380)
            self.linkExtractPort.place(anchor="nw", x=520, y=10)
            self.linkExtract.place(anchor="nw", x=520, y=50)
            self.linkDirBust.place(anchor="nw", x=680, y=50)
            self.linkExtractButton.place(anchor="nw", x=520, y=100, width=100, height=50)
            self.dirBustButton.place(anchor="nw", x=680, y=100, width=100, height=50)
        else:
            self.entryWebPort.place_forget()
            self.httpWindow.place_forget()
            self.linkExtractPort.place_forget()
            self.linkExtract.place_forget()
            self.linkDirBust.place_forget()
            self.linkExtractButton.place_forget()
            self.dirBustButton.place_forget()


        if str(self.current_frame) == "RevShell":
            self.revShellGenerateButton.place(anchor="nw", x=725, y=220, width=100, height=50)
            self.labelLocalDetails.place(anchor="nw", x=520, y=25)
            self.labelMyIP.place(anchor="nw", x=520, y=50)
            self.labelMyPort.place(anchor="nw", x=520, y=125)
            self.labelTargetDetails.place(anchor="nw", x=725, y=25)
            self.labelTargetType.place(anchor="nw", x=725, y=50)
            self.labelTargetArch.place(anchor="nw", x=725, y=125)
            self.entryLocalPort.place(anchor="nw", width=75, x=520, y=150)
            self.dropDownMyIP.place(anchor="nw", x=520, y=75)
            self.dropDownOSWeb.place(anchor="nw", x=725, y=75)
            self.dropDownArch.place(anchor="nw", x=725, y=150)
            self.revShellBottomWindow.place(anchor="nw", height=260, width=325, x=525, y=300)

            self.labelLanguage.place(anchor="nw", x=520, y=200)
            self.dropDownLanguage.place(anchor="nw", x=525, y=225)


        else:
            self.revShellGenerateButton.place_forget()
            self.labelLocalDetails.place_forget()
            self.labelMyIP.place_forget()
            self.labelMyPort.place_forget()
            self.labelTargetDetails.place_forget()
            self.labelTargetType.place_forget()
            self.labelTargetArch.place_forget()
            self.entryLocalPort.place_forget()
            self.dropDownMyIP.place_forget()
            self.dropDownOSWeb.place_forget()
            self.dropDownArch.place_forget()
            self.revShellBottomWindow.place_forget()
            self.labelLanguage.place_forget()
            self.dropDownLanguage.place_forget()

        if str(self.current_frame) == "PrivEsc":
            self.privEscWindow.place(anchor="nw", height=260, width=325, x=525, y=300)
            self.labelTargetTypeOS.place(anchor="nw", x=520, y=25)
            self.dropDownOS.place(anchor="nw", x=520, y=50)
            self.labelTargetTypeSection.place(anchor="nw", x=650, y=25)
            self.dropDownSection.place(anchor="nw", x=650, y=50)
        else:
            self.privEscWindow.place_forget()
            self.labelTargetTypeOS.place_forget()
            self.dropDownOS.place_forget()
            self.labelTargetTypeSection.place_forget()
            self.dropDownSection.place_forget()

        if str(self.current_frame) == "Tools":
            self.toolsWindow.place(anchor="nw", height=150, width=325, x=525, y=380)
            self.HTTPServer.place(anchor="nw", x=520, y=25)
            self.mailServer.place(anchor="nw", x=720, y=25)
            self.FTPServer.place(anchor="nw", x=520, y=125)
            self.HTTPStartButton.place(anchor="nw", x=520, y=50)
            self.HTTPStopButton.place(anchor="nw", x=570, y=50)
            self.MailStartButton.place(anchor="nw", x=720, y=50)
            self.MailStopButton.place(anchor="nw", x=770, y=50)
            self.FTPStartButton.place(anchor="nw", x=520, y=150)    
            self.FTPStopButton.place(anchor="nw", x=570, y=150)
        else:
            self.toolsWindow.place_forget()
            self.HTTPServer.place_forget()
            self.mailServer.place_forget()
            self.FTPServer.place_forget()
            self.HTTPStartButton.place_forget()
            self.HTTPStopButton.place_forget()
            self.MailStartButton.place_forget()
            self.MailStopButton.place_forget()
            self.FTPStartButton.place_forget()
            self.FTPStopButton.place_forget()




    def perform_scan(self):

        def validate_ip_address(ip_address):
            pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
            return re.match(pattern, ip_address) is not None

        def validate_multiple_ip_addresses(ip_addresses):
            for ip_address in ip_addresses:
                if not validate_ip_address(ip_address):
                    return False
            return True

        def validate_input(input_text):
            if len(input_text) <= 30:
                return True
            return False



        # Example usage:
        ip_input = self.entryTargetIP.get()  # Assuming 'self' refers to the current object

        ip_list = ip_input.split()  # Split the input string by whitespace

        if validate_multiple_ip_addresses(ip_list):
            pass
        else:
            MODULES.functions.topWindowUpdate(window=self.scrolled_textScannerTop, updateText="Invalid IP address")
            return

        target_name = self.entryTargetName.get()  # Assuming 'self' refers to the current object

        if validate_input(target_name):
            pass
        else:
            MODULES.functions.topWindowUpdate(window=self.scrolled_textScannerTop, updateText="Target name is too long!")
            root.mainloop()

        self.progress_bar.start(15)
        self.scan_button.config(state=DISABLED)
        self.scrolled_textScannerTop.config(state=DISABLED)
        self.checkbox.config(state=DISABLED)

        # IF checkbox is ticked for vulners, include vulners scan
        if self.checkbox_var.get() == 1:
            self.skipVulners = True

        else:
            self.skipVulners = False

        MODULES.Scanning.preScan(self)














    def _resize_image(self, event=None):
        new_width = root.winfo_width()
        new_height = root.winfo_height() - 50  # Subtract the height of the tab bar

        if new_width > 0 and new_height > 0:
            resized_image = self.image.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(resized_image)
            self.canvas.delete("background")
            self.canvas.create_image(0, 0, anchor=NW, image=self.background_image, tags="background")




def aboutHeBi(self):
    # Disable file menu
    self.menu_bar.entryconfig(1, state="disabled")

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
        self.menu_bar.entryconfig(1, state="normal")



def donate(self):

    # Disable file menu
    self.menu_bar.entryconfig(1, state="disabled")

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
        donateSummary.clipboard_clear()
        donateSummary.clipboard_append(dtxt)

        # Copy to clipboard label confirmation
        labelCopyUpdate=tk.Label(donationWindow, text="Link copied to clipboard!", background="black", foreground="#64d86b")
        labelCopyUpdate.place(anchor="nw", x=10, y=325)


    # When closing the donationWindow, enable the update button again
    donationWindow.protocol("WM_DELETE_WINDOW", lambda: onclose(self, donationWindow))

    def onclose(self, credsWindow):
        donationWindow.destroy()
        self.menu_bar.entryconfig(1, state="normal")







def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()



e = Amos(root)
e.pack(fill=BOTH, expand=YES)

e.current_tab = e.frameScanner


root.after(0, e._resize_image)  # Call _resize_image after the window is displayed

root.mainloop()
