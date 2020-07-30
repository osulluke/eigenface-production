#! /bin/bash

sudo apt install python3-pip
sudo apt install --yes ubuntu-restricted-extras
pip3 install --user -r requirements.txt ;
python3 Flask_UI/main.py 