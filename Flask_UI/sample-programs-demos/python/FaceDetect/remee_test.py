##! /bin/bash
#
#FILES=./img/faces/base-faces/*
#rm ./img/faces/scraped-faces/*.jpg
#for f in $FILES
#do
#    python3 FaceDetect/face_detect.py $f
#done

import os
from face_detect_remee import face_detect


dir = os.path.dirname(__file__)
img_dir = os.path.join(dir, '../img')

for root, dirs, files in os.walk(img_dir+"/"):
    for file in files:
        if file.endswith(".jpg"):
             print(os.path.join(root, file))
             face_detect(os.path.join(root, file))

