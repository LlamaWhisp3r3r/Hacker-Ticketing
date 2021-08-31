!#/bin/bash

cd ~
mkdir Documentation
mkdir Documentation/AttackTree
mkdir Documentation/Boxes
mkdir Documentation/General
mkdir Enumeration
mkdir Enumeration/Ports
mkdir Enumeration/Websites
mkdir Enumeration/IPs
mkdir Hashes
mkdir Hashes/Cracked
mkdir Hashes/Hashes
mkdir Exploits
mkdir Exploits/Website
mkdir Exploits/Kernal
mkdir Exploits/Service
mkdir VPN
sudo apt update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python2 get-pip.py
