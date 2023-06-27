# AMOS (Automated Methodology for Offensive Security)

Description: AMOS refers to an automated methodology used in the field of offensive security, specifically in the context of penetration testing. It encompasses a systematic and automated approach to identifying vulnerabilities, exploiting weaknesses, and evaluating the security posture of target systems. AMOS helps security professionals streamline the process of conducting comprehensive and efficient penetration tests to uncover potential security flaws and provide recommendations for mitigation.

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
