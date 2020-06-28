#! /bin/bash

pip3 install --user -r requirements.txt ;
cd Flask_UI &&
python3 main.py && sleep 1 &&
chromium-browser --new-window http://localhost:5000/ &