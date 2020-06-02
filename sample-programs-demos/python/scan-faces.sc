#! /bin/bash

FILES=./img/faces/*
rm ./img/faces/scraped-faces/*.jpg
for f in $FILES
do
    python FaceDetect-master/face_detect.py $f
done