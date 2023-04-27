# AMOS
Welcome to Amos! Put together by myself, Aromak of Hexxed BitHeadz.  After obtainig my OSCP certification, I wanted a project that would build some coding skills, and reflect on what I have learned on this path.

Amos is a python3 tkinter frame GUI pentesting tool.  It utilizes the power of nmap, then looks to purge the juicy details right on to the GUI.  First, Amos does a quick nmap scan. giving you results of the top 1000 port scan.  Next, a full port scan is performed, and whatever open ports are found, are fed into a service scan, getting as much details possible about the found services.  If any services are brutable for creds, the Brute tab will enable, and you are able to update you wordlists, and brute speficic services of your choice.  The HTTP tab assists with web extraction, looking for links, emails and phone numbers.  Directory buster will of course assist in finding those not so obvious urls with a wordlist of your choice.  Rev shells tab can assit in providing quick code to genereate reverse shells.  Priv Esc tab is there for those manual enumeration moments.  Finally, the tools tab can stand up a HTTP, FTP, or mail server with just a click of a button.  Be sure to check your Documents folder as html reports to get compiled throughout.

Amos will not find and auto exploit any machine for you.  It is more of an enumeration companion, aimed to script out the first few steps of an engagement, and assit throughout the session.  It is not recommended to use this tool on any exam, or as a replacement for any vulnerability scanner.  This tool is barely out in it's first release and results may vary.

Due to use of match case scripting, only >= python 3.10 is supported.

## First time intallation
INSERT GIT CLONE COMMAND HERE

source ./install.sh

sudo python3 amos.py

## Running from virtual environment

From the Amos folder:

source ./bin/activate

sudo amos.py

