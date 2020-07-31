import time
from PIL import ImageGrab
import numpy as np
import cv2
from .eigen_screener import eigen_screener
from .data_connector import get_name_string
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import random
from collections import deque

def run_face_screener():
    DELAY = 0.40
    NORMALIZER = 255.0
    global eigen_screener 
    eigen_screener = eigen_screener()
    video_player = ""
    state = "SHOW"
    face_que = deque()
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())#, firefoxOtions=firefox_options)
    firefox_driver.get('http://127.0.0.1:5000/')

    while True:
        time.sleep(DELAY)
        try:
            video_player = firefox_driver.find_element_by_id('video_player') # Access video player element
        except:
            print("\n***VIDEO PLAYER NOT FOUND***\n") # print message if no video play is present

        # Get the current screen shot and capture faces
        im = ImageGrab.grab()
        im = np.array(im)
        eigen_screener.tv_watcher.scanForFaces(im)

        # Identify faces that have been captured; place them in que
        print('*****************************')
        for face in eigen_screener.tv_watcher.detected_faces:
            prediction = eigen_screener.face_space.aggregate_prediction(face)
            print(prediction)
            if prediction != "UNKNOWN" and len(face_que) > 0:
                try:
                    face_que.remove("UNKNOWN")
                except:
                    pass
            add_to_queue(prediction, face_que)

        eigen_screener.tv_watcher.detected_faces.clear()

        # Determine the state of the show
        state = check_commercial(face_que)

        # Mute the show based 'state' of the show (COMMERCIAL or SHOW)
        if video_player != "":
            control_video(state, firefox_driver, video_player)

def check_commercial(face_deque):
    num = face_deque.count("UNKNOWN")
    print("# of UNKNOWN =", num)
    if num > 4:
        return "COMMERCIAL"
    else:
        return "SHOW"

def add_to_queue(face, deque):
    if len(deque) >= 10:
        deque.pop()
    else:
        deque.appendleft(face)
    
    print("len(face_que) =", len(deque))

    return

def control_video(state, firefox_driver, video_player):
    if state == "SHOW":
        try:
            firefox_driver.execute_script("arguments[0].muted = false;", video_player) # Unmute the player
        except:
            pass
    elif state == "COMMERCIAL":
        try:
            firefox_driver.execute_script("arguments[0].muted = true;", video_player) # Mute the player
        except:
            pass

    return

if __name__ == "__main__":
    run_face_screener()