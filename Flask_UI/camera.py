##################################################
## FileName: camera.py
##################################################
## Author: RDinmore, XWu
## Date: 2020.06.27
## Purpose: capture screen
## Libs: cv2, math
## Path: Flask_UI/camera.py
##################################################

import cv2
from math import fmod
from facedetect import *
from db_functions import *
import cv2 as cv
import time
import subprocess as sp
import multiprocessing as mp
from os import remove
from moviepy.editor import *
from functools import partial

def clean_output_files(path):
    for root,dirs,files in os.walk(path):
        for name in files:
            if '.mp4' in name:
                os.remove(os.path.join(root,name))
                print('Delete files:',os.path.join(root,name))   

def process_video_multiprocessing(group_number, file_name):
    cap = cv.VideoCapture(file_name)

    frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    num_processes = mp.cpu_count()
    frame_jump_unit =  frame_count// num_processes
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_jump_unit * group_number)

    # get height, width and frame count of the video
    width, height = (
            int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        )
    no_of_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    proc_frames = 0

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv.VideoWriter()
    out.open("output_{}.mp4".format(group_number), fourcc, fps, (width, height), True)
    try:
        while proc_frames < frame_jump_unit:
            ret, frame = cap.read()
            if not ret:
                break
            #time_start= lambda: int(round(time.time() * 1000))
            im = facesquare(frame)
            out.write(frame)
            #time_end=lambda: int(round(time.time() * 1000))
            #print('face detection time cost',time_end-time_start,'ms')
            proc_frames += 1
    except:
        # Release resources
        cap.release()
        out.release()

    # Release resources
    cap.release()
    out.release()


def combine_output_files(num_processes):
    L = []
    for root, dirs, files in os.walk("./"):
        files.sort()
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                L.append(video)

    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile("./static/target.mp4", fps=24, remove_temp=True)

def multi_process(file_name):
    num_processes = mp.cpu_count()
    print("Video processing using {} processes...".format(num_processes))
    p = mp.Pool(num_processes)
    partial_func = partial(process_video_multiprocessing, file_name=file_name)
    p.map(partial_func, range(num_processes))

    combine_output_files(num_processes)

def video_process(file_name):
    clean_output_files(".")
    time_start=time.time()
    cap = cv.VideoCapture(file_name)
    frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    num_processes = mp.cpu_count()
    print("Number of CPU: " + str(num_processes))
    frame_jump_unit =  frame_count// num_processes
    multi_process(file_name)
    time_end=time.time()
    print('time cost',time_end-time_start,'s')