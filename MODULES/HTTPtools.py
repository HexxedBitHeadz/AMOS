#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import queue, threading, requests, lxml, os, urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import MODULES.functions, MODULES.write2report
from threading import Thread

# Custom class created to properly identify results from multithreaded dirb buster code
class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def threadingSetup(self):
    pass



def functionlinkExtract(self):

    # Disable entry boxes while scans are running
    self.entryTargetName.config(state='disabled')
    self.entryTargetIP.config(state='disabled')

    # Status update 
    MODULES.functions.bottomWindowUpdate(window=self.httpWindow, updateText="Extracting " + str(self.entryTargetIP.get()) + ":" + str(self.entryWebPort.get()) + "\n")

    # Assigning url to extract details form
    url = "http://" + str(self.entryTargetIP.get()) + ":" + str(self.entryWebPort.get())

    # Code that analyzes page and extracts details
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    links = soup.findAll('a',href=True)
    extractResults = []

    for link in links:
        link=link['href']
        if link and link!='#':
            extractResults.extend([[url,link]])

    # Removing any duplicate findings from results list
    res = []
    [res.append(x) for x in extractResults if x not in res]

    # checking folder path
    MODULES.functions.documentsFolderPathCheck(self)

    # Writing results to html report
    HTMLheader="Web extract"
    MODULES.write2report.webExtract2html(self, HTMLheader, res)

    # Changing permission to regular user from sudo, making report and creds files easier to access
    os.chown("/home/" + self.userName + "/Documents/" + self.targetName + "/HTML_report-Extraction-" + self.entryWebPort.get() + ".html", self.uid, self.gid)

    # Updating bottom window to show extraction done and where to find
    MODULES.functions.bottomWindowUpdate(window=self.httpWindow, updateText="Extraction done " + str(self.entryTargetIP.get()) + ":" + str(self.entryWebPort.get()) + "\n\n")

    # Enalbe entry boxes while scans are running
    self.entryTargetName.config(state='normal')
    self.entryTargetIP.config(state='normal')

    MODULES.functions.bottomWindowUpdate(window=self.httpWindow, updateText="Results found in:\n ~/Documents/" + self.targetName + "/HTML_report-Extraction- " + self.entryWebPort.get() + ".html\n\n")

def check_url(full_url):
    # Function to check urls for 200 response
    response = requests.get(full_url)
    if response.status_code == 200:
        return full_url

    else:
        #print(url, 'is not valid.')
        pass

    
def functionDirBust(self, dirBustButton, httpWindow, target_url, filename):

    # Disable entry boxes while scans are running
    self.entryTargetName.config(state='disabled')
    self.entryTargetIP.config(state='disabled')

    # Try deleting any contents in the bottom window if there are any
    try:
        MODULES.functions.bottomWindowDelete(window=self.httpWindow)
        
    except:
        pass

    # Reading wordlist file, appending to url, updating status label and checking for 200s
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            element = []
    
        # Start the progress bar
        self.progress_bar.start(15)

        for line in lines:
            full_url = target_url + line.strip()
            MODULES.functions.statusUpdate(self, statusText="checking: " + full_url)
            thread = CustomThread(target=check_url, args=(full_url,))
            thread.start()

            # If 200 found, display to bottom window
            if thread.join() is not None:
                MODULES.functions.bottomWindowUpdate(window=self.httpWindow, updateText=thread.join() + "\n")

                element += thread.join().split("\n")

        # Sending details to html report, re-enable start button and stoping progress bar                 
        HTMLheader = "Directory Buster : " + str(self.entryWebPort.get())
        MODULES.write2report.dirBust2html(self, HTMLheader, element)
        self.dirBustButton.configure(state="normal")
        MODULES.functions.statusUpdate(self, statusText="Finished directory buster.")

        os.chown("/home/" + self.userName + "/Documents/" + self.targetName + "/HTML_report-DirBust-" + self.entryWebPort.get() + ".html", self.uid, self.gid)

        self.progress_bar.stop()

        # Enalbe entry boxes while scans are running
        self.entryTargetName.config(state='normal')
        self.entryTargetIP.config(state='normal')


    # If no file is found or user cancels file selection, update status label
    except TypeError:
        MODULES.functions.statusUpdate(self, statusText="NO FILE SELECTED!")
        threadingSetup(self)

def fileSelect(self):
    # Prep steps for dirBust func, wordlist file selection
    self.dirBustButton.configure(state="disabled")
    MODULES.functions.statusUpdate(self, statusText="Selecting wordlist file...")
    target_url = "http://" + self.entryTargetIP.get() + "/"
    filename = askopenfilename()
    MODULES.functions.statusUpdate(self, statusText="Running directory buster...")
    THREADdirBurst = threading.Thread(target=functionDirBust, args=(self, self.dirBustButton, self.httpWindow, target_url, filename), daemon=True)
    THREADdirBurst.start()

