#!/bin/bash
catDistro=$(sudo cat /etc/os-release | grep "ID" | awk -F= '{print $2}')
echo "Checking distro for auto install compatibility..."

function runDNFScript () {
	sudo dnf update
	sudo dnf install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python3-virtualenv python3-tkinter nmap
}

function runAPTScript () {
	sudo apt update
	sudo apt install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python3-virtualenv python3-tk nmap
}

function runYUMScript () {
	sudo yum update
	sudo yum install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python3-virtualenv python3-tk nmap
}

# Leaving OS's here for further testing.

#if [[ "$catDistro" == *"fedora"* ]]; then
#  runDNFScript

elif [[ "$catDistro" == *"kali"* ]]; then
  runAPTScript

elif [[ "$catDistro" == *"parrot"* ]]; then
  runAPTScript

elif [[ "$catDistro" == *"ubuntu"* ]]; then
  runAPTScript

else
  echo "Distro unrecognized, auto install failed. Please install these packages manually:"
  echo "python3-pip"
  echo "build-essential"
  echo "libssl-dev"
  echo "libffi-dev"
  echo "python3-dev"
  echo "python3-virtualenv"
  echo "python3-tkinter"
  echo "nmap"

fi

virtualenv .
source ./bin/activate
sudo pip3 install python-nmap
sudo pip3 install -r requirements.txt

