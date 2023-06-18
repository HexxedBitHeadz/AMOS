# AMOS
Amos is a python3 tkinter frame GUI pentesting tool.  It utilizes the power of nmap, then looks to purge the juicy details right on to the GUI.  First, Amos does a quick nmap scan. giving you results of the top 1000 port scan.  Next, a full port scan is performed, and whatever open ports are found, are fed into a service scan, getting as much details possible about the found services.  If any services are brutable for creds, the Brute tab will enable, and you are able to update you wordlists, and brute speficic services of your choice.  The HTTP tab assists with web extraction, looking for links, emails and phone numbers.  Directory buster will of course assist in finding those not so obvious urls with a wordlist of your choice.  Rev shells tab can assit in providing quick code to genereate reverse shells.  Priv Esc tab is there for those manual enumeration moments.  Finally, the tools tab can stand up a HTTP, FTP, or mail server with just a click of a button.  Be sure to check your Documents folder as html reports to get compiled throughout.

It is not recommended to use this tool on any exam, or as a replacement for any vulnerability scanner.  Results may vary.

Due to use of match case scripting, only >= python 3.10 is supported.

Install / Demo videos: https://drive.google.com/drive/folders/1Tn00ee7CddQfj0PuZQNreZh44mjv_Gne?usp=sharing

## First time installation
```
git clone https://github.com/HexxedBitHeadz/AMOS && cd AMOS
```

```
source ./install.sh
```

```
sudo python3 amos.py
```

## Running from virtual environment
Amos is ready for virutal deployment, simply acivate as you would any other venv:

From the Amos folder:
```
source ./bin/activate
```

```
sudo python3 amos.py
```

## Roadmap
- Continue to improve code form "proof of concept" to better written format.
- Expand Reverse Shell tab
- Expand Privelege Escalation tab

## Whats new in v1.1.1?
- fixed issue if target name is blank, target ip would not assign correctly.
- fixed issue in revshell tab language selection drop down would remain on screen in other tabs.

## Whats new in v1.1?
- Fixed the flashing issue when switching between tabs.
- Readjusted code to work with newly implimeted background canvas.
