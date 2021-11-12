!#/bin/bash

echo "What is the box's name? "
read boxName
mkdir $boxName
cd $boxName
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
sudo apt update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python2 get-pip.py
