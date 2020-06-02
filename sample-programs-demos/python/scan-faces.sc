#! /bin/bash

FILES=./img/faces/*

for f in $FILES
do
    python FaceDetect-master/face_detect.py $f
done