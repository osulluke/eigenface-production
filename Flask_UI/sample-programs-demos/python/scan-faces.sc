#! /bin/bash

FILES=./img/faces/base-faces/*
rm ./img/faces/scraped-faces/*.jpg
for f in $FILES
do
    python3 FaceDetect-master/face_detect.py $f
done